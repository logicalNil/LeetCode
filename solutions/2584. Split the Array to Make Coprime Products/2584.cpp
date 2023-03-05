class Solution {
 public:
  int findValidSplit(vector<int>& nums) {
    unordered_map<int, int> leftFactors;
    unordered_map<int, int> rightFactors;

    for (const int num : nums)
      for (const int factor : getFactors(num))
        ++rightFactors[factor];

    for (int i = 0; i < nums.size() - 1; ++i)
      for (const int factor : getFactors(nums[i])) {
        if (--rightFactors[factor] == 0) {
          // rightFactors[factor] == 0, so no need to track leftFactors[factor].
          rightFactors.erase(factor);
          leftFactors.erase(factor);
        } else {
          // Otherwise, need to track leftFactors[factor].
          ++leftFactors[factor];
        }
        if (leftFactors.empty())
          return i;
      }

    return -1;
  }

 private:
  // Gets prime factors under sqrt(10^6).
  vector<int> getFactors(int num) {
    vector<int> factors;
    for (int divisor = 2; divisor <= min(1000, num); ++divisor)
      if (num % divisor == 0) {
        factors.push_back(divisor);
        while (num % divisor == 0)
          num /= divisor;
      }
    // Handle the case that `num` contains a prime factor > 1000.
    if (num > 1)
      factors.push_back(num);
    return factors;
  }
};
