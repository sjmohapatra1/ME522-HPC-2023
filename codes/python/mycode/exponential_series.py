#!usr/bin/python


def exp_series(x, n=100):
    """
    Calculates the exponential of x using the exponential series with n terms.

    Args:
        x (float): The number to calculate the exponential of.
        n (int, optional): The number of terms in the series. Default is 100.

    Returns:
        float: The exponential of x.
    """
    # Initialize variables
    exp = 1.0
    term = 1.0

    # Calculate the series
    for i in range(1, n+1):
        term *= x / i
        exp += term

    # Check convergence
    if abs(term) > 1e-15:
        print("Warning: Series may not have converged.")

    return exp



