"""
    Created on: 2/3/2017
    Author: Rain Li

"""


import urllib

URL_ENCODE_TYPE = "utf8"
PAIR_SEPARATOR = ","    # delimitor between each key value pair
KEY_VALUE_DELIM = "="   # delimitor between key and value
ERROR_DICT = {'error':'true'}

def convertString2Dictionary(inputString = ""):
    """ Returns dictionary of url encoded input string

    This function converts url encoded string to key value dictionary.

    - general info
        1. key-value pairs are seprated by commas +space*
        2. "key=value" decoded

    - invalid rules
        1. must be key value paired
        2. key must be oneword starting in with a letter
        3. value must be one word
    """
    if inputString == '':
        return ERROR_DICT

    url=urllib.unquote(inputString).decode(URL_ENCODE_TYPE)
    print url
    key_value_pairs = url.split(PAIR_SEPARATOR)
    print key_value_pairs

    for pair in key_value_pairs:
        print pair
        if not is_valid_pair(pair):
            return ERROR_DICT
    #validation passed, convert to dict
    valid_dict = dict((key.strip(), value.strip()) for key,value in
              (pair.split(KEY_VALUE_DELIM) for pair in key_value_pairs))

    return valid_dict


def is_valid_pair(pair):
    """
    check to see if either key or value is invalid
    """
    #valid pair only has one delimitor
    if pair.count(KEY_VALUE_DELIM) != 1:
        return False
    splitted = pair.split(KEY_VALUE_DELIM)

    key = splitted[0]
    value = splitted[1]
    print(value)
    print(key)
    return is_valid_key(key) and is_valid_value

def is_valid_key(key):
    """
        Return false if key is invalid
    """
    #check if no invalid charaters
    key = key.strip()
    if key.isalnum():
        #check if first char is letter
        return key[:1].isalpha()
    return False


def is_valid_value(value):
    """
    returns false if value is invalid
    """
    return value.strip().isalnum()

def error_dict():
    """
    returns error dictionary, used for testing
    """
    return ERROR_DICT
