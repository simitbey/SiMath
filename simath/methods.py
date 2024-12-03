from enum import Enum

def avg(*args):
    """
    :param args: The numbers to be averaged.
    :return: The average of the given numbers.
    """
    if len(args) < 2:
        raise ValueError("At least two arguments are required for finding an average.")
    return sum(args) / len(args)

def intervalize(interval, step):
    """
    Divides the given interval into smaller sub-intervals based on the step size.

    :param interval: An ordered pair representing the interval to be divided.
    :type interval: tuple
    :param step: The step size to further divide the interval.
    :type step: float
    :return: A list of ordered pairs, each representing a sub-interval.
    :rtype: list
    """
    if step > interval[1] - interval[0]:
        raise ValueError("Step size must be less than the interval size.")
    k = int((interval[1] - interval[0]) / step)
    l = [[interval[0] + i * step, interval[0] + (i + 1) * step] for i in range(k)]
    return l

def rmsum(func_or_table, interval_or_type, step=None, type=None, verbose=False):
    """
    Calculates the Riemann Sum based on the given type.
    :param func_or_table: The function to be evaluated or a dictionary of table values.
    :type func_or_table: function or dict
    :param step: The step size.
    :type step: float
    :param interval_or_type: The interval to evaluate the function over or the type of Riemann Sum if a table is provided.
    :type interval_or_type: tuple or str
    :param type: The type of Riemann Sum.
    :type type: str
    :param verbose: Verbose mode. Will print the values of f(x) for each x in the interval.
    :type verbose: bool
    :return: The calculated Riemann Sum.
    :rtype: float
    """
    if isinstance(func_or_table, dict):
        table = func_or_table
        type = interval_or_type
        keys = sorted(table.keys())
        step = keys[1] - keys[0]
        interval = [(keys[i], keys[i+1]) for i in range(len(keys)-1)]
        if verbose: print(interval), print(step)
        func = lambda x: table[x]
    else:
        func = func_or_table
        interval = intervalize(interval_or_type, step)

    if type is None or type == "":
        if verbose:
            print("Type not specified. Defaulting to Midpoint Riemann Sum.")
        type = "midpoint"

    if type == "right":
        result = sum(func(x[1]) * (x[1] - x[0]) for x in interval)
        if verbose:
            for x in interval:
                print(f"f({x[1]}) = {func(x[1])} * ({x[1]} - {x[0]})")

    elif type == "left":
        result = sum(func(x[0]) * (x[1] - x[0]) for x in interval)
        if verbose:
            for x in interval:
                print(f"f({x[0]}) = {func(x[0])} * ({x[1]} - {x[0]})")

    elif type == "trapezoidal":
        result = sum(avg(func(x[0]), func(x[1])) * (x[1] - x[0]) for x in interval)
        if verbose:
            for x in interval:
                print(f"mp(f({x[0]}), f({x[1]})) = {avg(func(x[0]), func(x[1]))} * ({x[1]} - {x[0]})")
    elif type == "midpoint":
        result = sum(func(avg(x[0], x[1])) * (x[1] - x[0]) for x in interval)
        if verbose:
            for x in interval:
                print(f"f(mp({x[0]}, {x[1]})) = {func(avg(x[0], x[1]))} * ({x[1]} - {x[0]})")
    else:
        raise ValueError(f"Type must be one of; right, left, trapezoidal, midpoint. Got: {type} instead.")

    if verbose:
        print(f"Riemann Sum: {result}")
    return result
