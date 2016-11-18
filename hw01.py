# Name: Brett Yelverton
# x-number: x97226
# Documentation: CDT Brett Yelverton 20AUG2016, West Point NY. I watched two videos from Khan Academy on the discrete logarithm problem
# and the diffie-helman key exchange in order to better understand the mathematics behind problem number one in the homework.
from decimal import *

# Problem 1
def generate_key(p, g, a, b):
    """
    Calculate the Diffie-Hellman secret key. 

    Args:
        p (int): A prime number.
        g (int): One of p's primitive roots mod p.
        a (int): Alice's secret positive integer.
        b (int): Bob's secret positive integer.

    Returns:
        int: The shared secret key.

    >>> generate_key(23, 5, 6, 15)
    2
    >>> generate_key(34, 27, 42, 13)
    15
    >>> generate_key(71, 53, 27, 69)
    47
    """
    # place your code here
    A = (g**a) % p
    B = (g**b) % p
    s = (B**a) % p
    k = (A**b) % p
    return s
# Problem 2
def passer_rating(comp, att, yds, td, intcpt):
    """
    Calculate a quarterback passer rating.

    Args:
        comp (int): The number of completed passes.
        att (int): The number of pass attempts.
        yds (int): The total passing yards.
        td (int): The number of touchdowns.
        intcpt (int): The number of intercepted passes thrown.

    Returns:
        float: The quarterback's passer rating.

    Payton Manning (career)
    >>> passer_rating(6125, 9380, 71940, 539, 251)
    96.5

    Tom Brady (career)
    >>> passer_rating(4953, 7792, 58028, 428, 150)
    96.4

    Philip Rivers (career)
    >>> passer_rating(3462, 5339, 41447, 281, 135)
    95.5
    """
    # place your code here
    pc = comp/att
    a=(pc-0.3)*5
    ypa = yds/att
    b=(ypa-3)/4
    tpa = td/att
    c = (tpa*20)
    ipa = intcpt/att
    d = 2.375-(25*ipa)
    e = ((a+b+c+d)/6)*100
    f = round(e,1)
    return f

# Problem 3
def bmi(height, weight):
    """
    Calculate BMI and print two values: one assuming that the input uses the metric
    system and another assuming the input uses the imperial system.

    Args:
        height (float): individual height in inches or meters
        weight (float): individual weight in pounds or kilograms

    Returns:
        None

    >>> bmi(68, 165)
    Metric Input  : 0.0
    Imperial Input: 25.1
    >>> bmi(1.7272, 74.8427)
    Metric Input  : 25.1
    Imperial Input: 17638.5
    """
    # place your code here
    metric_bmi = weight/(height**2)
    p_imp_height = height * 0.0254
    p_imp_weight = weight * 0.453592
    p_imp_bmi = p_imp_weight/(p_imp_height**2)
    a = round(metric_bmi, 1)
    b = round(p_imp_bmi, 1)
    string_met = 'Metric Input  : ' + str(a)
    string_p_imp = "Imperial Input: " + str(b)
    print (string_met)
    print (string_p_imp)



if __name__=='__main__':
    import doctest
    doctest.testmod()
