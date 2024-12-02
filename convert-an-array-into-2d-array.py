def convert(array):
    resoult = []
    new_array = array
    index = 0
    unical = list(dict.fromkeys(new_array))
    while new_array:
        if index >= len(unical):
            print(unical)
            resoult.append(unical)
            unical = list(dict.fromkeys(new_array))
            index = 0
            if len(new_array) <= 2:
                resoult.append(new_array[0:])
        else:
            new_array.remove(unical[index])
            index += 1

    return resoult


array = [3, 1, 2, 1, 3]
resoult = convert(array)
print(resoult)
