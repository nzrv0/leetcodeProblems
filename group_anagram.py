def group_anagram(strs):
    resoult = []
    example = []
    saved = ""
    for str in strs:
        sorted_el = "".join(sorted(str))
        if sorted_el in example:
            resoult.append([*example, str])
        else:
            example.append([sorted_el])

        # example.append(str)
    return example


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
resoult = group_anagram(strs)
print(resoult)
