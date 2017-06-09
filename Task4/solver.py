import json


def calculate_prediction(correct, total):
    """
    Function calculates prediction rate based on given correct count and total count,
    
    :param correct:     Correct count of elements
    :type correct:      int
    :param total:       Total count of elements
    :type total:        int
    :return:            Correct percentage
    :rtype:             basestring
    """
    if not isinstance(correct, int):
        raise TypeError(correct)

    if not isinstance(total, int):
        raise TypeError(total)

    if total:
        return "%.2f%%" % ((correct / total) * 100)
    else:
        return "100%"


def solve(input):
    """
    Function compares given input tuple of dot-bracket strings for correct prediction rate.
    For input:
    '["(.....(<.>A...a(..().......()........()........()..)
      (....([](((....)))(...(((((.....)))){...}(...(", 
     "(.....(<.>A...a(..().......()........()........()..)
      (....([](((....)))(...(((((.....)))){...}(...("]'
    Example output:
    '{"(": "100.00%", ")": "100.00%", ".": "100.00%", "pseudoknot": "100.00%"}'
    
    For input:
    '["(.....().()......().....)(..((..({}[..]).....)((....)))...)
      (.....()..()..().......().....().....()......)(.....()...().......().....().))..))....)", 
     "(.....().()....(.().-.-.)(..((..({}[..]).....)((....)))...)
      (.....()..()..().......((.....().)....)......)(.....()...().......().....-).))..))....)"]'
    Example Output:
    '{"(": "90.91%", ")": "96.15%", ".": "95.74%", "pseudoknot": "100.00%"}'
    
    :param input:       JSON list containing correct dot-bracket string and predicted dot-bracket string
    :type input:       basestring
    :return:            JSON string containing prediction rates
    :rtype:             basestring
    """

    if not isinstance(input, str):
        raise TypeError(input)

    string = "()[]{}<>.-"
    for char in range(ord("A"), ord("Z") + 1):
        string += chr(char)
        string += chr(char + 32)

    for element in input:
        if element not in string:
            raise TypeError

    input = json.loads(input)
    if not isinstance(input, list):
        raise TypeError("Incorrect JSON format for input")
    correct_structure = input[0]
    predicted_structure = input[1]

    predicted_positions = {
        "(": {
                "total": 0,
                "correct": 0
             },
        ")": {
                "total": 0,
                "correct": 0
             },
        ".": {
                "total": 0,
                "correct": 0
             },
        "pseudoknot": {
                         "total": 0,
                         "correct": 0
                      },
    }

    predicted_index = 0
    correct_index = 0
    while predicted_index != len(predicted_structure) and correct_index != len(correct_structure):

        predicted_element = predicted_structure[predicted_index]
        correct_element = correct_structure[correct_index]
        while predicted_element == "-" and len(predicted_structure) != len(correct_structure):
            predicted_index += 1
            predicted_element = predicted_structure[predicted_index]

        while correct_element == "-" and len(predicted_structure) != len(correct_structure):
            correct_index += 1
            correct_element = correct_structure[correct_index]

        if correct_element == "(":
            if correct_element == predicted_element:
                predicted_positions["("]["total"] += 1
                predicted_positions["("]["correct"] += 1
            else:
                predicted_positions["("]["total"] += 1
        elif correct_element == ")":
            if correct_element == predicted_element:
                predicted_positions[")"]["total"] += 1
                predicted_positions[")"]["correct"] += 1
            else:
                predicted_positions[")"]["total"] += 1
        elif correct_element == ".":
            if correct_element == predicted_element:
                predicted_positions["."]["total"] += 1
                predicted_positions["."]["correct"] += 1
            else:
                predicted_positions["."]["total"] += 1
        else:
            if correct_element == predicted_element:
                predicted_positions["pseudoknot"]["total"] += 1
                predicted_positions["pseudoknot"]["correct"] += 1
            else:
                predicted_positions["pseudoknot"]["total"] += 1
        predicted_index += 1
        correct_index += 1

    solution = {
        "(": calculate_prediction(predicted_positions["("]["correct"], predicted_positions["("]["total"]),
        ")": calculate_prediction(predicted_positions[")"]["correct"], predicted_positions[")"]["total"]),
        ".": calculate_prediction(predicted_positions["."]["correct"], predicted_positions["."]["total"]),
        "pseudoknot": calculate_prediction(predicted_positions["pseudoknot"]["correct"],
                                           predicted_positions["pseudoknot"]["total"]),
    }

    return json.dumps(solution)
