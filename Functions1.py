def char_frequency(str1):
    dictionary = {}
    for i in str1:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    # Sort the dictionary items by values in descending order
    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dictionary

result = char_frequency('Mississippi')

for i, count in result.items():
    print(f"{i} = {count:02d}", end=" ")
    #count:02d will  formats the count as a zero-padded integer with at least two digits
