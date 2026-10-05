"""Contains Duplicate (NeetCode: arrays & hashing).

Pattern:
Time: O(n)  Space:
Trick:
"""


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears at least twice."""
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
 


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    assert contains_duplicate([7]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("contains_duplicate: all tests passed")
