# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

#    Define base case
    
#    If lenght of string is 1
    if len(sequence) == 1:
        return [sequence]
    
    
    
    else:
        permutation_list = []
        first_char = sequence[0]
        next_chars = sequence[1:]
        permutations_subsequence = get_permutations(next_chars)
        for chars in permutations_subsequence:
            for i in range(len(chars)+1):
                new_seq = chars[0:i] + first_char + chars[i:len(chars)+1]
                permutation_list.append(new_seq)
                
    skimmed_permutation_list = list(set(permutation_list))
                
    return skimmed_permutation_list
                
print(get_permutations('heaven'))





if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

