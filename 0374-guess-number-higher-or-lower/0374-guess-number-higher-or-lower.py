# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # pick 맞추기
        # num > pick -> -1
        # num < pick -> 1
        # num == pick return
        low, high = 1, n

        # 1 10
        #     1 < 10
        #     mid = 5
        #     pick = 6
        # 5 10
        #     5 < 10
        #     mid = 7
        #     pick = 6
        # 5 7
        #     5 < 7
        #     mid = 6
        #     pick = 6


        while low <= high:
            mid = (low+high) //2
            guessed_num = guess(mid)
            if guessed_num == 1:
                low = mid + 1 
            elif guessed_num == -1:
                high = mid - 1
            else:
                return mid
