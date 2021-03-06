# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Solution 1 O(n^2) time
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        chars_used = []
        count_result = 0
        for c in s:
            if c in chars_used:
                index = chars_used.index(c)
                if index+1==len(chars_used):
                    chars_used = []
                else:
                    chars_used = chars_used[index+1:]             
            chars_used.append(c)
            size = len(chars_used)
            if size > count_result:
                count_result = size
        return count_result

# Solution 2, O(n) time
    def lengthOfLongestSubstring2(self, s: str) -> int:
        chars_used = {}
        count_result = 0        
        i = 0
        for j in range(0,len(s)):
            if s[j] in chars_used:
                prev_i = i
                i = chars_used[s[j]] + 1
                for k in range(prev_i,i):
                    del chars_used[s[k]]
            chars_used[s[j]] = j
            size = j -i + 1
            if size > count_result:
                count_result = size
        return count_result

def main():
    res = Solution().lengthOfLongestSubstring("aabaab!bb")
    print(res)

if __name__ == "__main__":
    main()