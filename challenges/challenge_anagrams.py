def is_anagram(first_string, second_string):
    ord_first_string = "".join(selection_sort(list(first_string.casefold())))
    ord_second_string = "".join(selection_sort(list(second_string.casefold())))
    boolean = ord_first_string == ord_second_string
    return (ord_first_string, ord_second_string, boolean)


def selection_sort(string):
    for letter in range(len(string) - 1):
        min_letter = letter
        for index in range(letter + 1, len(string)):
            if string[index] < string[min_letter]:
                min_letter = index
        current_letter = string[letter]
        string[letter] = string[min_letter]
        string[min_letter] = current_letter
    return string
