##    Two children, Lily and Ron, want to share a chocolate bar. Each of the
##    squares has an integer on it.
##
##    Lily decides to share a contiguous segment of the bar selected such that:
##
##        The length of the segment matches Ron's birth month, and,
##        The sum of the integers on the squares is equal to his birth day.
##
##    Determine how many ways she can divide the chocolate.

##### ##### ##### #####

#   the given inputs are s, d, m
#   I changed the variable names to make things easier to follow
#   s = integer_list
#   d = target_amount
#   m = window_size

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the length of integer_list
#   Algo:
#       'two finger'
#       we use index pointers to create a 'window' and scan across the list
#       suming the contents of the 'window' and checking this sum against
#       the target sum. when a match is found a solution counter is incremented.
#       return solution counter

#   I think it is important to note that a naive approach to this problem
#   will lead to an O(n*m) solution where n is the length of integer_list and
#   m is the length of the window_size.
#   The problem can arise if you try to recompute the entire sum for every window.
#   The key realization is that when the window shifts by one index to the right
#   only the first and last integers in the window will be different.
#   Therefor only an addition and subtraction are required instead of an entire re-sum.
#   These are a constant number of operations.
#   Reducing a potentially O(m) operations to O(4)

def birthday(integer_list, target_amount, window_size):

    number_of_solutions = 0

    start_window = 0
    end_window = window_size - 1

    sum_current = sum(integer_list[start_window:end_window+1])

    if sum_current == target_amount:

        number_of_solutions += 1

    while start_window < (len(integer_list) - window_size):

        sum_current -= integer_list[start_window]
        start_window += 1
        end_window += 1
        sum_current += integer_list[end_window]

        if sum_current == target_amount:

            number_of_solutions += 1

    return number_of_solutions
