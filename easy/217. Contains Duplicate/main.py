def contains_duplicate(nums):
    unique_list = set()
    for num in nums:
        if num not in unique_list:
            unique_list.add(num)
        else:
            break
    else:
        return "false"
    return "true"


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
