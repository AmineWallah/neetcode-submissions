class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join([char for char in s if char.isalnum()])
        clean_text = clean_text.lower()

        reversed_text = clean_text[::-1]
        if reversed_text == clean_text:
            return True
        else:
            return False
        