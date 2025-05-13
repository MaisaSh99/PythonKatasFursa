from typing import List


def max_storage_area(containers: List[int]) -> int:
    """
    Imagine a series of storage containers placed side by side, where the height of each container
    is given by an integer in the array. Your task is to find the largest rectangular area that
    can be formed using one or more of these containers.

    For example:
    Input: containers = [2, 1, 5, 6, 2, 3]
    Output: 10
    Explanation: The largest rectangle is formed between containers at indices 2 and 3
    with height 5 and width 2.

    Hint for efficient implementation: stack

    Args:
        containers: a list of integers representing the heights of containers

    Returns:
        The area of the largest rectangle formed between containers
    """
    stack = []
    max_area = 0
    containers.append(0)  

    for i, height in enumerate(containers):
        while stack and containers[stack[-1]] > height:
            h = containers[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area


if __name__ == "__main__":
    containers = [2, 1, 5, 6, 2, 3]
    result = max_storage_area(containers)
    print("Max storage area:", result)  # Expected output: 10
