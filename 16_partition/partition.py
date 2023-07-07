def partition(lst, fn):
    """Partition lst by predicate.
    
    - lst: list of items
    - fn: function that returns True or False
    
    Returns new list: [a, b], where `a` are items that passed fn test,
    and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    true_result = []
    false_result = []
    if fn == 'is_even':
        for num in lst:
            if num % 2 == 0:
                true_result.append(num)
            else:
                false_result.append(num)
    if fn == 'is_string':
        for str in lst:
            if type(str) == str:
                true_result.append(str)
            else:
                false_result.append(str)
    return [true_result,false_result]
