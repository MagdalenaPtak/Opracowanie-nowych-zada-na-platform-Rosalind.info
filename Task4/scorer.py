import json


def score(input, correct_output, user_output):
    """
    Function to score dot-bracket comparison task.

    :param input:           JSON containing list of 2 elements: correct structure in dot-bracket notation and 
                            predicted structure in dot bracket notation
    :type input:            basestring
    :param correct_output:  Correct JSON string, example: '{"(": "90.91%", ")": "96.15%", 
                                                            ".": "95.74%", "pseudoknot": "100.00%"}'
    :type correct_output:   basestring
    :param user_output:     User JSON string, example: '{"(": "91.91%", ")": "96.15%", 
                                                         ".": "95.00%", "pseudoknot": "100.00%"}'
    :type user_output:      basestring
    :return:                Pass/Fail mark
    :rtype:                 bool
    """

    correct_output = json.loads(correct_output)
    user_output = json.loads(user_output)

    if not isinstance(correct_output, dict):
        raise TypeError("Incorrect JSON format for correct_output")
    if not isinstance(user_output, dict):
        raise TypeError("Incorrect JSON format for user_output")
    if len(correct_output.keys()) != len(user_output.keys()):
        return False
    for key in correct_output.keys():
        if correct_output[key] != user_output[key]:
            return False
    return True
