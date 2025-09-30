class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        money -= children
        get8 = money//7
        remain = children-get8
        money %= 7
        if remain < 0: # only one child get more money(>8)
            return children - 1
        if (remain ==1 and money==3) or (remain == 0 and money):
            # case 1) all children except for one child get 8, and only one child gets 4
            # case 2) all children can get 8, but money is left 
            get8 -= 1
        
        return get8