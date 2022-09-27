def fibonacci_recursive(n):
    # A recursive implementation of an algorithm to compute the
    # nth term in the Fibonacci sequence

    # Base cases: n=0 and n=1 are defined as part of the problem
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: Compute the (n-1)th and (n-2)th
    # term so we can compute the nth term
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci(n):
    # An algorithm to compute the nth term in the Fibonacci sequence
    # that uses a for loop.

    # Trivial cases: If the caller wants the 0th or 1st term, we know them
    # already - no need to do anything else.
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # These variables contain the previous 2 terms. 0 and 1 are
    # precalculated, since they are defined as part of the problem.
    n1 = 0
    n2 = 1

    # This variable contains the accumulated total of Fibonacci terms
    # as we progress through the sequence
    total = 0

    # Progress through the Fibonacci sequence, starting at the 2nd term,
    # until we reach the end.
    for i in range(n - 1):
        total = n1 + n2
        n1 = n2
        n2 = total

    return total
