from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]: 
        fizz = 'Fizz'
        buzz = 'Buzz'
        fizzbuzz = 'FizzBuzz'
        result = []
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append(fizzbuzz)
            else:
                if i % 3 == 0:
                    result.append(fizz)
                elif i % 5 == 0:
                    result.append(buzz)
                else:
                    result.append(str(i))
        return result
    
if __name__ == "__main__":
    solution = Solution()
    res = solution.fizzBuzz(15)
    pass