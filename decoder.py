"""Decode reddit megalinks using the bayer moore algorithm with dynamic search patterns."""
# as per http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/StringMatch/boyerMoore.htm
#  Knuth-Morris-Pratt is a better approach to this problem. We're essentially searching for the last
# character of the pattern (a binary string?) so I will follow this educational page.

# also how hard is it to explain this algorithm with this?!:
# BOYER_MOORE_MATCHER (T, P)

# Input:    Text with n characters and Pattern with m characters
# Output: Index of the first substring of T matching P

# Compute function last
# i ← m-1
# j ← m-1
# Repeat
#     If P[j] = T[i] then
#         if j=0 then
#             return i        // we have a match
#         else
#             i ← i -1
#             j ← j -1
#     else
#         i ← i + m - Min(j, 1 + last[T[i]])
#         j ← m -1
# until i > n -1
# Return "no match"
# # Honestly...
search_strings = ['link:', 'password:', 'replace ', 'add ']


def get_link(input_string, index, output_link=None):
    """Get the link string."""
    if input_string[index] == '\n':
        return output_link
    elif output_link is not None:
        output_link += input_string[index]
        return get_link(input_string[index + 1:], 1, input_string[index + 1])
    elif input_string[index] == '!':
        return get_link(input_string[index + 1:], 1, input_string[index + 1])
    elif input_string[index] == '#':
        return get_link(input_string[index + 1:], 0)
    # elif input_string[index] == ' ':
        # return get_link(input_string[index + 1:], index)


def get_password(input_string, index, output_link=None):
    """Get the password string."""
    if input_string[index] == '\n':
        return output_link
    elif output_link is not None:
        output_link += input_string[index]
        return get_link(input_string[index + 1:], 1, input_string[index + 1])
    elif input_string[index] == '!':
        return get_link(input_string[index + 1:], 1, input_string[index + 1])
    else:
        print '===============wow exception'
        raise Exception


class LastOccurance(object):

    """Last occurrence functor."""

    def __init__(self, pattern, alphabet):
        """
        Generate a dictionary with the last occurrence of each alphabet
        letter inside the pattern.

        Note: This function uses str.rfind, which already is a pattern
        matching algorithm. There are more 'basic' ways to generate this
        dictionary.

        pre-process the string?
        """
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
    pattern = 'link:'
    alphabet = set(input_string)
    last = LastOccurance(pattern, alphabet)
    pattern_len = len(pattern)
    n = len(input_string)
    i = pattern_len - 1  # input_string index
    # if link: is pattern start at 5th index and search backwards
    j = pattern_len - 1  # pattern index
    # if pattern is link: start from its end as well

    data = {
        'url': None,
        'password': None
    }
    while i < n:
        # find the : character
        if input_string[i] == pattern[j]:
            # lin(k)
            if input_string[i - 1] == 'k':
                print 'found link ', i
                link = get_link(input_string[i:], 0)
                data['url'] = link
                pattern = 'password:'
                # reset the pattern index into the new pattern
                j = len(pattern) - 1
                i = i + len(pattern) - 1
            # passwor(d)
            if input_string[i - 1] == 'd':
                # a (dd) - I know this sucks but add is easier to write than concatonate.
                if input_string[i] == ':':
                    password = get_password(input_string[i:], 0)
                    data['password'] = password
                    pattern = 'add '
                    # reset pattern - this ones experimental.
                    j = len(pattern) - 1
                    i = i + len(pattern) - 1
                    # print data
                elif input_string[i] == ' ':
                    # do addition decode
                    return -9000
            # replac(e)
            if input_string[i - 1] == 'e':
                # do replace
                return -80000
            if j == 0:
                return i
            else:
                print 'else j = ', j
                print 'else i = ', i
                i -= 1
                j -= 1
        else:
            l = last(input_string[i])
            # 4 + 4 + 1
            print '-'*90; print '-'*90; import ipdb; ipdb.set_trace(context=13)  # breakpoint 3c8d7843  noqa  //

            i = i + pattern_len - min(j, 1 + l)
            j = pattern_len - 1
    print '&&&'*30
    print pattern
    print '-'*30
    print input_string
    print 'i: ',i
    print 'j: ',j
    return -1


def main():
    """Main funciton."""
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
