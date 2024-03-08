class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        # return cleaned == cleaned[::-1]
        return all(cleaned[i] == cleaned[~i] for i in range(len(cleaned) // 2))