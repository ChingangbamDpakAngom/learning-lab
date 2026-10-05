"""Valid Anagram (NeetCode: arrays & hashing).

Pattern:
Time:    Space:
Trick:
"""


def is_anagram(s: str, t: str) -> bool:
    """Return True if t uses exactly the same letters as s, the same number of times."""
    ...
    if len(s) == len(t):
        s = set(sorted(s))
        t = set(sorted(t))
        if s == t:
            print("its anagram")

    else:
        print("not anagram")


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    assert is_anagram("aacc", "ccac") is False
    print("is_anagram: all tests passed")
