def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    result = []
    for ele in lst:
        if ele:
            result.append(ele)
        # if ele == False:
        #     None
    return result


