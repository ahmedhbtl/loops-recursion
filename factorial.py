def factorial_recursive(n):
    # A recursive implementation of a factorial algorithm

    # Base case: 0! is defined as 1
    if n == 0:
        return 1

    # Recursive case: Make the problem smaller by computing the
    # factorial of n-1, then multiplying the result by n
    return n * factorial_recursive(n-1)


def factorial_for(n):
    # A factorial algorithm that uses a for loop

    # This variable will be updated in the loop body.
    # It allows us to calculate the factorial by multiplying
    # it by all numbers from 1 to n.
    answer = 1
    for i in range(1, n+1):
        answer = answer * i

    return answer



def factorial_while(n):
    # A factorial algorithm that uses a while loop

    # This variable will be updated in the loop body.
    # It allows us to calculate the factorial by multiplying
    # it by all numbers from 1 to n.
    answer = 1

    # Since we aren't using a for loop, we have to create
    # and update the value of i ourselves
    i = 1
    while i <= n:
        answer = answer * i
        i = i + 1
    return answer


