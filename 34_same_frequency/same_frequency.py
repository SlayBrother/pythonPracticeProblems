def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_str1 = str(num1)
    num_str2 = str(num2)
    if sorted(num_str1) == sorted(num_str2):
        return True
    else:
        return False
