"""Valid Palindrome (NeetCode: two pointers).

Pattern:
Time:    Space:
Trick:
"""


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same both ways, ignoring case and non-alphanumeric characters.

    Aim for O(1) extra space: don't build a cleaned copy of the string.
    """
    ...


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("ab_a") is True
    print("is_palindrome: all tests passed")
