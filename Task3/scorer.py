import json


def score(input, correct_output, user_output):
    """
    Function to score dot-bracket task.

    :param input:           Dot-bracket string, example: '((((....))))((.))(.....()..)(((...)))
                            (.....()........()......().....()..()........)[...])....)).....)
                            ((((...))))(....()......()........()......)((...))).....)'
    :type input:            basestring
    :param correct_output:  Correct JSON string, example: '{"junction_type": 8, "junction_count": 1, 
                            "pseudoknot_complexity": "Cc", "pseudoknot_count": 1}'
    :type correct_output:   basestring
    :param user_output:     User JSON string, example: '{"junction_type": 8, "junction_count": 1, 
                            "pseudoknot_complexity": "Cc", "pseudoknot_count": 1}'
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
    for key in correct_output.keys():
        if correct_output[key] != user_output[key]:
            return False
    return True
