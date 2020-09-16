def intersection(arrays):
    # Step 1: Get the length of the arrays, to check how many items are in the arrays
    # Step 2: Loop over each item in the first array
    # Step 3: Add the items to the hash table as keys, and values as 1
    # Step 4: Continue for all arrays

    list_length = len(arrays)
    dictionary = {}
    result = []

    #Adding first array to dictionary
    for item in arrays[0]:
        dictionary[item] = 1
    #Loop over two other arrays, and check to see if number is in array
    for item2 in range(1,list_length):
        for num in arrays[item2]:
            if num in dictionary:
                dictionary[num] += 1

    #Returning numbers that are in the list
    for key in dictionary.keys():
        if dictionary[key] == list_length:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
