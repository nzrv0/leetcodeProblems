def occures_in_str(example_ar, s):
    index = 0
    while index < len(example_ar):
        if example_ar[index] == s[index]:
            return index
        else:
            index += 1
    return -1


example = "sadbutsad"
needle = "sad"
resoult = occures_in_str(example, needle)

print(resoult)
