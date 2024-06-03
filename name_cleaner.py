



def join_string_list(tokens:list, join_char:str = '_')->str:
    name = tokens.pop(0)
    for token in tokens:
        name = f'{name}{join_char}{token}'

    return name

def remove_cammel_case(name:str)->str:
    split_chars:list = [char for char in name if not char.lower() == char]
    if len(split_chars) == 0:
        return name
    elif name.upper() == name:
        return name.lower()

    tokens:list = []
    for char in split_chars:
        buffer:list = name.split(char,1)
        name = char + buffer[1]
        tokens.append(buffer[0])
    tokens.append(name)
    tokens = [token.lower() for token in tokens]
    name = join_string_list(tokens)

    return name



def separate_by_underscore(name:str)->str:
    """
    The purpose of this function is not obvious at first view but it becomes clear when dealing 
    with a name like favorite.food
    when naming columns the standard convention is word_word but some names use a different seperation
    character (in R for instance . is not used when writing code so some funtions or variables are names word.word)
    so we need to replace the seperation character
    """

    alphabet:str = 'abcdefghijklmnopqrstuvwxyz'
    split_chars = [char for char in name if not char.lower() in alphabet]
    if len(split_chars) == 0:
        return name
    tokens:list = []
    for char in split_chars:
        buffer:list = name.split(char, 1)
        name = buffer[1]
        tokens.append(buffer[0])
    tokens.append(name)
    tokens = [token.lower() for token in tokens]
    name = join_string_list(tokens)

    return name

def text_to_num(text:str)->int:
    Ones: dict = {'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
              }

    numbers: list = []
    for token in text.lower().split(' '):
        if token in Ones:
            numbers.append(Ones[token])
        else:
            raise Exception(f'{token} is not a supported word, or exceeds 99')

    return sum(numbers)


