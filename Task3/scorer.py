import json


def score(input, correct_output, user_output):
    """
    Function to score dot-bracket task.

    :param input:           Dot-bracket string, example: '((((....))))((.))(.....()..)(((...)))(.....()........()......().....()..()........)[...])....)).....)((((...))))(....()......()........()......)((...))).....)'
    :type input:            string
    :param correct_output:  Correct JSON string, example: '{"junction_type": 8, "junction_count": 1, "pseudoknot_complexity": "Cc", "pseudoknot_count": 1}'
    :type correct_output:   string
    :param user_output:     User JSON string, example: '{"junction_type": 8, "junction_count": 1, "pseudoknot_complexity": "Cc", "pseudoknot_count": 1}'
    :type user_output:      string
    :return: 
    """
    correct_output = json.loads(correct_output)
    user_output = json.loads(user_output)
    for key in correct_output.keys():
        if correct_output[key] != user_output[key]:
            return False
    return True
