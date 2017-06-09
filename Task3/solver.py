import re
import json


def count_pseudoknot(opening, ending, seq):
    """
    Function counts number of pseudoknots of a given type in a dot-bracket structure.
    
    :param opening:     Character representing opening of a pseudoknot, example: [
    :type opening:      basestring
    :param ending:      Character representing ending of a pseudoknot, example: ]
    :type ending:       basestring
    :param seq:         Dot-bracket sequence to count pseudoknots in
    :type seq:          basestring
    :return:            Number of found pseudoknots of given type
    :rtype:             int
    """
    count = 0
    if opening in seq and ending in seq:
        pseudoknot_opening_count = seq.count(opening)
        pseudoknot_ending_count = seq.count(ending)
        count = int((pseudoknot_opening_count + pseudoknot_ending_count) / 2)
    return count


def solve(input):
    """
    Function checks given input string in dot-bracket notation for highest level of pseudoknot complexity
    and highest level of junction.
    
    Example input:
    "(....((()...().......()....()...().......)).)Aa(....()...()....().......()....()........()...().......))...)
     (()...()......()........()....().....()......()..){..}<...>[...](..)((....))"
     Example output:
     '{"junction_type": 8, "junction_count": 2, "pseudoknot_complexity": "Aa", "pseudoknot_count": 1}'
     
    
    :param input:   Dot-bracket notation string
    :type input:    basestring
    :return:        JSON string, example: {"junction_type": 4, "junction_count": 1, 
                                          "pseudoknot_complexity": "Aa", "pseudoknot_count": 1}
    :rtype:         basestring
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

    n_junction = 0
    junction_limit = 50
    seq_counter_dict = {
        "hairpin": 0,
        "bulge": 0,
        "inner-loop": 0
    }

    solution = {
        "junction_type": None,
        "junction_count": 0,
        "pseudoknot_complexity": None,
        "pseudoknot_count": 0
    }

    max_junction = None
    temp_seq = ""
    for s in input:
        if s == "(" or s == ")" or s == ".":
            temp_seq += s
    hairpin_pattern = r"(\(\.+\))"
    bulge_pattern_1 = r"(\(\.+\()"
    bulge_pattern_2 = r"(\)\.+\))"
    inner_loop_pattern = r"(\(\.+\(+\)+\.+\))"
    match = re.findall(hairpin_pattern, temp_seq)
    if match:
        seq_counter_dict["hairpin"] = len(match)
    match = re.findall(bulge_pattern_1, temp_seq)
    if match:
        seq_counter_dict["bulge"] += len(match)
    match = re.findall(bulge_pattern_2, temp_seq)
    if match:
        seq_counter_dict["bulge"] += len(match)
    match = re.findall(inner_loop_pattern, temp_seq)
    if match:
        seq_counter_dict["inner-loop"] = len(match)
    junction_pattern_element = "\(+\)+\.*"
    for junction in range(3, junction_limit):
        junction_pattern = junction_pattern_element * (junction - 1)
        junction_pattern = "(\(+\.*" + junction_pattern + "\)+)"
        match = re.findall(junction_pattern, temp_seq)
        if match:
            max_junction = (junction, len(match))
            if n_junction == junction:
                seq_counter_dict["%s-junction" % max_junction[0]] = max_junction[1]

    if max_junction and not n_junction:
        seq_counter_dict["%s-junction" % max_junction[0]] = max_junction[1]

    if max_junction:
        solution["junction_type"] = max_junction[0]
        solution["junction_count"] = max_junction[1]

    count = count_pseudoknot("[", "]", input)
    if count:
        seq_counter_dict["[] pseudoknot count"] = count
        seq_counter_dict["Highest pseudoknot complexity"] = "[]"
    count = count_pseudoknot("{", "}", input)
    if count:
        seq_counter_dict["{} pseudoknot count"] = count
        seq_counter_dict["Highest pseudoknot complexity"] = "{}"
    count = count_pseudoknot("<", ">", input)
    if count:
        seq_counter_dict["<> pseudoknot count"] = count
        seq_counter_dict["Highest pseudoknot complexity"] = "<>"

    for pseudoknot in range(ord("A"), ord("Z") + 1):
        count = count_pseudoknot(chr(pseudoknot), chr(pseudoknot + 32), input)
        if count:
            seq_counter_dict["%s%s pseudoknot count" % (chr(pseudoknot), chr(pseudoknot + 32))] = count
            seq_counter_dict["Highest pseudoknot complexity"] = "%s%s" % (chr(pseudoknot), chr(pseudoknot + 32))
    solution["pseudoknot_complexity"] = seq_counter_dict.get("Highest pseudoknot complexity")
    solution["pseudoknot_count"] = seq_counter_dict.get("%s pseudoknot count" %
                                                    seq_counter_dict.get("Highest pseudoknot complexity"), 0)

    return json.dumps(solution)
