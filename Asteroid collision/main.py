"""
We are given an array asteroids of integers representing asteroids in a row.
The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:
- Input: asteroids = [5,10,-5]
- Output: [5,10]
- Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
- Input: asteroids = [8,-8]
- Output: []
- Explanation: The 8 and -8 collide exploding each other.

Example 3:
- Input: asteroids = [10,2,-5]
- Output: [10]
- Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
- Input: asteroids = [3,5,-6,2,-1,4]
- Output: [-6,2,4]
- Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left.
On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right,
without reaching asteroid 4.

Constraints:
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0
"""


class Solution:
    # stack
    # both time and complexity are O(n)
    def asteroid_collision(self, asteroids: list[int]) -> list[int]:
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
                continue
            # collide
            previous = None
            while res and asteroid < 0 < res[-1] <= asteroid * -1:
                previous = res.pop()
                if previous == asteroid * -1:
                    break
            # after collide, we are ensure that absolute value of the current asteroid:
            # |asteroid| < res[-1], there for:
            if res and res[-1] > 0:
                continue
            # collide has happened
            if previous:
                if (previous == asteroid * -1) or (res and res[-1] > 0):
                    continue
            res.append(asteroid)
        return res

    def asteroid_collision_simplify(self, asteroids: list[int]) -> list[int]:
        res = []
        for asteroid in asteroids:
            while res and res[-1] > 0 > asteroid:
                # 10, -5
                if -asteroid < res[-1]:
                    break
                # 8, -8
                elif -asteroid == res[-1]:
                    res.pop()
                    break
                res.pop()
            else:
                res.append(asteroid)
        return res
