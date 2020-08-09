from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result_of_each_round = []
        for idx, item in enumerate(ops):

            if item == '+':
                result_of_each_round.append(
                    result_of_each_round[-2] + result_of_each_round[-1])

            elif item == 'D':
                result_of_each_round.append(result_of_each_round[-1] * 2)

            elif item == 'C':
                result_of_each_round.pop()

            else:
                result_of_each_round.append(int(item))

        return sum(result_of_each_round)


ops = ["5", "2", "C", "D", "+"]

assert Solution().calPoints(ops=ops) == 30
