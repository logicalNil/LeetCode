class Solution:
  # Very simliar to 3. Longest SubWithout Repeating Characters
  def numberOfSubstrings(self, s: str) -> int:
    ans = 0
    # lastSeen[c] := index of last c appeared.
    lastSeen = {c: -1 for c in 'abc'}

    for i, c in enumerate(s):
      lastSeen[c] = i
      # s[0..i], s[1..i], s[min(lastSeen)..i] are satisfied strings.
      ans += 1 + min(lastSeen.values())

    return ans
