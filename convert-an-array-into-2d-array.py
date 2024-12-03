def convert(array):
    resoult = []
    new_array = array
    index = 0
    unical = list(dict.fromkeys(new_array))[::-1]
    if len(unical) == len(new_array):
        resoult.append(unical)
    while new_array:
        if index >= len(unical):
            if len(unical) == len(new_array):
                resoult.append(new_array[:])
            resoult.append(unical)
            unical = list(dict.fromkeys(new_array))[::-1]
            index = 0
        else:
            new_array.remove(unical[index])
            index += 1

    return resoult


array = [1, 3, 4, 1, 2, 3, 1]
resoult = convert(array)
print(resoult)
