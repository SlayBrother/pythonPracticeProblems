def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_set = {}
    vowels = 'aeiou'
    for vowel in phrase:
        if vowel.lower() in vowels:
            vowel_set[vowel.lower()] = vowel_set.get(vowel.lower(), 0) + 1
    return vowel_set