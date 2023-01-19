def group_anagrams(strs):
    result = []
    result_hash = []
    for _str in strs:
        str_hash = dict()
        for _char in _str:
            str_hash[_char] = 1 + str_hash.get(_char, 0)
        for i in range(len(result_hash)):
            if str_hash == result_hash[i]:
                result[i].append(_str)
                break
        else:
            result_hash.append(str_hash)
            result.append([_str])

    return result


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
