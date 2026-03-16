def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """

    for step in range(steps):
        f_dash_x =  2 * a * x0 + b
        x = x0 - lr * f_dash_x
        x0 = x
    
    return x