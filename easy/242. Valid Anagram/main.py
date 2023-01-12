def is_anagram(s, t):
    if len(s) != len(t):
        return False
    hash_s = {}
    hash_t = {}
    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    return hash_s == hash_t


if __name__ == '__main__':
    print(is_anagram(s="anagram", t="nagaram"))  # True
    print(is_anagram(s="rat", t="car"))  # False
    print(is_anagram(s="aacc", t="ccac"))  # False
