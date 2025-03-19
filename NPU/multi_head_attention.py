import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class Multiheadattention(nn.Module):
    def __init__(self, model_dim = 768, num_heads = 12):
        ## 768: num_head * model_dim = 12 * 64
        super().__init__()
        assert model_dim % num_heads == 0, "model_dim must be divisible by num_heads"

        self.num_heads = num_heads              # 12
        self.model_dim = model_dim              # 768
        self.head_dim = model_dim // num_heads  # 64

        # Linear Transformation: Query, Key, Value
        self.weight_q = nn.Linear(self.model_dim, self.model_dim) # (768, 768)
        self.weight_k = nn.Linear(self.model_dim, self.model_dim) # (768, 768)
        self.weight_v = nn.Linear(self.model_dim, self.model_dim) # (768, 768)

        # final output projection
        self.fc_out = nn.Linear(self.model_dim, self.model_dim)   # (768, 768)

    def forward(self, x):
        """ compute attention value
            Attention score: softmax(QV^T / sqrt(dim_v)) V

            [ Optimization Process ] 
            - FLOPs
                1. Linear Projection (Q, K, V) - GEMM
                    (batch, seq_len, model_dim)
                    FLOPs = 3 * batch * seq_len * model_dim * model_dim
                    => compute-bound: systolic array (tensor parallel)

                2. Compute Attention Score (QK^T / sqrt(d_k))
                    Q (batch, num_heads, seq_len, head_dim)
                    K^T (batch, num_heads, head_dim, seq_len)
                    FLOPs = batch * num_heads * seq_len * seq_len * head_dim
                    => compute-bound: parallelization (Flash Attention)

                3. Softmax normalization
                    (batch, num_head, seq_len, seq_len)
                    FLOPs = batch * num_heas * seq_len * (2*seq_len-1)
                    => memory-bound (exp, sum(exp), division): approximation, LUT, turbo attention
                                                                KV caching (prior result save), INT8 Quantization

                4. Attention output (softmax(attention_score)*V)
                    (batch, num_head, seq_len, seq_len) * (batch, num_heads, seq_len, head_dim)
                    FLOPs = batch * num_heads * seq_len * seq_len * head_dim
                    => Compute-bound: Parallelization

                5. Linear output (fc_out)
                    FLOPs = batch * seq_len * model_dim * model_dim
                    => compute-bound: systolic array (tensor parallel)

        """
        batch, seq_len, model_dim = x.shape    # (batch, seq_len, model_dim)

        # 1) derive query, key, value
        query = self.weight_q(x)    # (batch, seq_len, model_dim) = (1, 128, 768)
        key = self.weight_k(x)      # (batch, seq_len, model_dim) = (1, 128, 768)
        value = self.weight_v(x)    # (batch, seq_len, model_dim) = (1, 128, 768)

        # 2) reshape: (batch, seq_len, num_heads, head_dim) = (1, 128, 12, 68)
        query = query.view(batch, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        key = key.view(batch, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        value = value.view(batch, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        ## => (batch, num_heads, seq_len, head_dim) = (1, 12, 128, 68)
        ## => easier to compute attention score for each head

        # 3) compute attention score
        # (batch, num_head, seq_len, head_dim) * (batch, num_head, head_dim, seq_len)
        # = (batch, num_head, seq_len, seq_len) = (1, 12, 128, 128)
        attention_scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        # 4) normalization: (1, 12, 128, 128)
        ## dim =-1 :: sequence view (row-wise)
        attention_probability = F.softmax(attention_scores, dim=-1)

        # 5) attention output -> (batch, seq_len, num_head * model_dim)
        # (batch, num_head, seq_len, seq_len) * (batch, num_head, seq_len, head_dim)
        # => (batch, num_head, seq_len, head_dim)
        attention_output = torch.matmul(attention_probability, value)


        # make (batch, seq_len, model_dim)
        attention_output = attention_output.transpose(1,2).contiguous().view(batch, seq_len, self.model_dim)
        attention_output = self.fc_out(attention_output) # (model_dim, model_dim)
        return attention_output
