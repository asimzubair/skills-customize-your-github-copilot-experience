def is_palindrome(text):
    """Return True if text is a palindrome (ignoring spaces and case)."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def calculate_average(numbers):
    """Return the average of a list of numbers, or 0 for an empty list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def run_tests():
    """Run assertion tests for the assignment functions."""
    assert is_palindrome("Racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True

    assert calculate_average([]) == 0
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([5, 5, 5, 5]) == 5

    print("All tests passed!")


if __name__ == "__main__":
    run_tests();
