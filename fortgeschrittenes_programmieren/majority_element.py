def majority_element_fast(nums):
    """
    This function finds the majority element in a list of numbers.
    A majority element is an element that appears more than n/2 times in the list.
    :param nums: List[int] - List of integers
    :return: int - The majority element
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


def majority_element(nums):
    """
    This function uses the .count function of arrays in python
    """
    count = len(nums) // 2
    for num in nums:
        if nums.count(num) > count:
            return num
    return None


def main():
    """
    Main function to test the majority element functions.
    This should measure the time it costs for the different functions to run with up to 10**6 elements.
    """
    import time
    import random

    # Generate a list of random integers
    nums = [random.randint(1, 8) for _ in range(10**6)]
    # Introduce a majority element by changing every second element to 9
    for i in range(1, len(nums), 2):
        nums[i] = 9

    # Measure time for the fast function
    start_time = time.time()
    result_fast = majority_element_fast(nums)
    end_time = time.time()
    print(
        f"Majority element (fast): {result_fast}, Time taken: {end_time - start_time:.6f} seconds"
    )

    # Measure time for the slow function
    start_time = time.time()
    result_slow = majority_element(nums)
    end_time = time.time()
    print(
        f"Majority element (slow): {result_slow}, Time taken: {end_time - start_time:.6f} seconds"
    )


if __name__ == "__main__":
    main()
