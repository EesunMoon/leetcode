class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # +: right, -: left
        res =[] # stack

        for a in asteroids:
            # collide case) + then -
            while res and (a < 0 < res[-1]):
                # explode
                if a+res[-1] == 0:
                    res.pop()
                    break
                # collide
                if abs(a) > abs(res[-1]):
                    res.pop()
                else:
                    break
            else:
                res.append(a)
        return res