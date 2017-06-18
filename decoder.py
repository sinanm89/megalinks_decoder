# def replacement(_input, inquiry, key=None):
#     if key == _input:


#     return output

# def shift(input, inquiry):
#     return output

# # find character \n indexes
# # see if each index corresponds to a case

# def string_cases(input_string):
#     k = len(input_string)
#     char = input_string[0]
#     check_case(input_string)

#     if char is not " ":
#         output, word, key = string_cases(input_string[k/2:])
#         output, word, key = string_cases(input_string[:k/2])

#     char = input_string[0]
#     for i, char in enumerate(input_string):
#         if char == " ":
#             continue
#         if char == "\n":
#             output, word, key = string_cases(input_string[i:])
# #
# # KMP_SEARCH
# def kmp_search(input_string, char):
#     m = 0
#     i = 0
#     T = []
#     inp_string_length = len(input_string)
#     while m + i < inp_string_length:ter
#         if input_string[i] == case[m]
#         if

# hash_table = {
#     ' ': (0, [False]),
#     '\n': (1, [False]),
#     '!': (1, ['!']),
#     '/': (2, ['#', True]),
#     '#': (3, ['!', True]),
#     ':': (4, [':']),
#     'a': (5, ['c', 'd', 's']),
#     'c': (6, ['e']),
#     'd': (7, ['d', ':']),
#     'e': (8, ['p', ':']),
#     'i': (9, ['n']),
#     'k': (10, [':']),
#     'l': (11, ['a']),
#     'n': (12, ['k']),
#     'p': (13, ['a', 'l']),
#     'r': (14, ['d', 'e']),
#     's': (15, ['s', 'w']),
#     'w': (16, ['o']),
# }

search_strings = ['link:', 'password:', 'replace', 'add']


# def trigger_command(command):
#     # do the action of the command
#     # remove command pathways after possible commands are exhausted.
#     # re-calculate the character weight table
#     return output


class last_occurrence(object):
    """Last occurrence functor."""

    def __init__(self, pattern, alphabet):
        """Generate a dictionary with the last occurrence of each alphabet
        letter inside the pattern.

        Note: This function uses str.rfind, which already is a pattern
        matching algorithm. There are more 'basic' ways to generate this
        dictionary."""
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        """Return last position of the specified letter inside the pattern.
        Return -1 if letter not found in pattern."""
        return self.occurrences[letter]


def boyer_moore_alg(input_string):
    '''
    Maybe commands:
        # add = 1
        # link = 2
        # password = 3
        # replace = 4
    '''

    # find all distinct characters in a string
    alphabet = set(input_string)
    pattern = search_strings[0]
    last = last_occurrence(pattern, alphabet)

    n = len(input_string)
    m = len(pattern)

    inp_index = n - 1
    search_index = m - 1

    start_appending = False
#
    alphabet = set(input_string)
    last = last_occurrence(pattern, alphabet)
    pattern_len = len(pattern)
    n = len(input_string)
    i = pattern_len - 1  # input_string index
    j = pattern_len - 1  # pattern index

    while i < n:
        if input_string[i] == pattern[j]:
            # input_string[i] == 'k':
            #     get_link(input_string[i+1])
            # print '-'*90; print '-'*90; import ipdb; ipdb.set_trace(context=13)  # breakpoint 9547f268  noqa  //
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(input_string[i])
            i = i + pattern_len - min(j, 1 + l)
            j = pattern_len - 1
    return -1
    # while inp_index < n:
    #     print inp_index
    #     if input_string[inp_index] in ['\n', ' ', '!']:
    #         if input_string[inp_index] == '!':
    #             print 'found !'
    #             start_appending = not(start_appending)
    #     elif input_string[inp_index] == search_string[search_index]:
    #         if search_index == 0:
    #             return inp_index
    #         else:
    #             inp_index -= 1
    #             search_index -= 1
    #     else:
    #         l = last(input_string[search_index])
    #         inp_index = search_index + m - min(search_index, 1 + l)
    #         search_index = m - 1
    # return -1


    # k = len(input_string)
    # char = input_string[index]
    # char_weight, next_characters = hash_table.get(char, (-1, None))
    # if char_weight < 0:
    #     if maybe_command:
    #         decoded_string.append(char)
    #     # add or pass
    # continue_command = next_characters[0]
    # trigger = '!'
    # if char == trigger:
    #     output = trigger_command(maybe_command,)

    # while continue_command and char is not trigger:
    #     m = index + 1
    #     if m > k:
    #         break
    #     char = input_string[m]
    #     # O(m) > max length of the hash table maps
    #     if char in next_characters:
    #         break


def main():
    input_string = (
        'bullshit\ngreeting\nlink: /#!tmB3WbZQ\nreplace W with T\npossible-bullshit\npassword: '
        '!i2_r2FsdZveTGlCVN-gwI2cI4YQnCX0Kq1YaJUJDgQU\nbullshit\ngood\nfucking\n\\/\/bye.'
    )
    print boyer_moore_alg(input_string)

    # hash_table = {
    #     'key': None
    # }
    # k = len(input_string)
    # hash_table = string_cases(input_string, hash_table)
    # # comp = o/2
    # # log(comp) = log(o) - log(2)
    # # complexity = log(o)
    # if hash_table.get('inquiry') == "replace":
    #     # W with T
    #     output = replacement(_input, inquiry, key=)
    # if inquiry == "shift":
    #     output = shift(_input, inqury)

if __name__ == '__main__':
    main()
