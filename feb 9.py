


def pair_sum_count(numbers: set(), A: int):
    '''
    Count the unique pairs in numbers that add up to A

    Inputs:
        - numbers: a list of numbers
        - A: a number
    Output:
        - the count of unique pairs in the numbers list that add up to A
    '''
    counter = set()
    for number_one in numbers:
        for number_two in numbers:
            if number_one + number_two == A:
                counter.add(number_two)
                counter.add(number_one)
    return len(counter)/2

pair_sum_count([1,2,3,4,5,6,7, 1, 4], 5)