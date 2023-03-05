class Solution:
  def findValidSplit(self, nums: List[int]) -> int:
    leftFactors = collections.Counter()
    rightFactors = collections.Counter()

    # Gets prime factors under sqrt(10^6).
    def getFactors(num: int) -> List[int]:
      factors = []
      for divisor in range(2, min(1000, num) + 1):
        if num % divisor == 0:
          factors.append(divisor)
          while num % divisor == 0:
            num //= divisor
      # Handle the case that `num` contains a prime factor > 1000.
      if num > 1:
        factors.append(num)
      return factors

    for num in nums:
      for factor in getFactors(num):
        rightFactors[factor] += 1

    for i in range(len(nums) - 1):
      for factor in getFactors(nums[i]):
        rightFactors[factor] -= 1
        if rightFactors[factor] == 0:
          # rightFactors[factor] == 0, so no need to track leftFactors[factor].
          del rightFactors[factor]
          del leftFactors[factor]
        else:
          # Otherwise, need to track leftFactors[factor].
          leftFactors[factor] += 1
        if not leftFactors:
          return i

    return -1
