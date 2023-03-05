class Solution {
  public int findValidSplit(int[] nums) {
    Map<Integer, Integer> leftFactors = new HashMap<>();
    Map<Integer, Integer> rightFactors = new HashMap<>();

    for (final int num : nums)
      for (final int factor : getFactors(num))
        rightFactors.merge(factor, 1, Integer::sum);

    for (int i = 0; i < nums.length - 1; ++i)
      for (final int factor : getFactors(nums[i])) {
        rightFactors.merge(factor, -1, Integer::sum);
        if (rightFactors.get(factor) == 0) {
          // rightFactors[factor] == 0, so no need to track leftFactors[factor].
          rightFactors.remove(factor);
          leftFactors.remove(factor);
        } else {
          // Otherwise, need to track leftFactors[factor].
          leftFactors.merge(factor, 1, Integer::sum);
        }
        if (leftFactors.isEmpty())
          return i;
      }

    return -1;
  }

  // Gets prime factors under sqrt(10^6).
  private List<Integer> getFactors(int num) {
    List<Integer> factors = new ArrayList<>();
    for (int divisor = 2; divisor <= Math.min(1000, num); ++divisor)
      if (num % divisor == 0) {
        factors.add(divisor);
        while (num % divisor == 0)
          num /= divisor;
      }
    // Handle the case that `num` contains a prime factor > 1000.
    if (num > 1)
      factors.add(num);
    return factors;
  }
}
