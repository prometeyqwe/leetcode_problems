from collections import defaultdict, Counter


def group_anagrams(strs):
    result_hash = defaultdict(list)
    for _str in strs:
        result_hash[frozenset(Counter(_str).items())].append(_str)

    return list(result_hash.values())


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
