"""
    Created on: 2/3/2017
    Author: Rain Li

"""

import urllib

URL_ENCODE_TYPE = "utf8"
PAIR_SEPARATOR = ","  # delimitor between each key value pair
KEY_VALUE_DELIM = "="  # delimitor between key and value
ERROR_DICT = {'error': 'true'}


def convertString2Dictionary(inputString=""):
    """ Returns dictionary of url encoded input string

    This function converts url encoded string to key value dictionary.

    - general info
        1. key-value pairs are seprated by commas +space*
        2. "key=value" decoded

    - invalid rules
        1. must be key value paired
        2. key must be one alphanumeric word starting in with a letter
        3. value must be one word and alphnumeric only
        4: key cant be repeated

    example usage:
        import softwareprocess.convertString2Dictionary as url2d

        outputValue = url2d.convertString2Dictionary(inputString = inputValue)

    """
    if inputString == '':
        return ERROR_DICT
    
    url = urllib.unquote(inputString).decode(URL_ENCODE_TYPE)
    # print url
    key_value_pairs = url.split(PAIR_SEPARATOR)
    key_list = []
    valid_dict = {}
    # print key_value_pairs
    
    for pair in key_value_pairs:
        # print pair
        # valid pair only has one delimitor
        if pair.count(KEY_VALUE_DELIM) != 1:
            return ERROR_DICT
        
        splitted = pair.split(KEY_VALUE_DELIM)
        key = splitted[0].strip()
        value = splitted[1].strip()
        
        # key validity
        if is_valid_key(key) and key not in key_list:
            if is_valid_value(value):
                key_list.append(key)
                valid_dict[key] = value
            else:  # value is not valid
                return ERROR_DICT
        else:  # key is not valid or is repeated
            return ERROR_DICT
    
    return valid_dict


def is_valid_key(key):
    """
        Return false if key is not alphnumeric or start with letter
    """
    if key == "": return False
    # check if no invalid charaters
    if key.isalnum():
        # check if first char is letter
        return key[:1].isalpha()
    return False


def is_valid_value(value):
    """
    returns false if value is not alphnumeric or empty
    """
    if value == "": return False
    return value.strip().isalnum()


def error_dict():
    """
    returns error dictionary, used for testing
    """
    return ERROR_DICT
