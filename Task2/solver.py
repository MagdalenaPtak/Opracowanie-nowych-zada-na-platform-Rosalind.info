import json


def can_mutate(possible_mutant, mutation_to_check):
    """
    Function checks if given RNA input can mutate into given STOP codon
    
    :param possible_mutant:     RNA to check for possible mutation
    :type possible_mutant:      basestring
    :param mutation_to_check:   RNA stop codon
    :type mutation_to_check:    basestring
    :return: 
    """

    if not isinstance(possible_mutant, str):
        raise TypeError(possible_mutant)
    if not isinstance(mutation_to_check, str):
        raise TypeError(mutation_to_check)
    if len(possible_mutant) != 3 or len(mutation_to_check) != 3:
        raise Exception("Incorrect string length")

    if possible_mutant[0:2] == mutation_to_check[0:2]:
        return True
    elif possible_mutant[1:3] == mutation_to_check[1:3]:
        return True
    elif possible_mutant[0] == mutation_to_check[0] and possible_mutant[2] == mutation_to_check[2]:
        return True
    return False


def solver(input):
    """
    Function checks for possible single element mutations into STOP codons in RNA triplets.
    
    Example input:
    "UGUCUGAGUAACUUGUCGGUCGUAUACAGUGGUAUUGUGCGGAAACAACCGUAGGGAGGUGUUACUGCUGGGAACAGCCUUUCGUUCGCCAGGCAAUAC"
    
    Example output:
    '{"UAG": ["UUG", "UCG", "UAC", "UAG", "UCG", "UAC"], 
     "UAA": ["UAC", "AAA", "CAA", "UAG", "CAA", "UAC"], 
     "UGA": ["UGU", "GGA"]}'
    
    :param input:   RNS sequence to check
    :return: 
    """
    stops = {"UAG": [],
             "UAA": [],
             "UGA": []}
    if len(input) % 3 != 0:
        raise Exception("Incorrect string length")

    for triplet_range in range(0, len(input), 3):
        triplet = input[triplet_range:triplet_range+3]
        for key in stops.keys():
            if can_mutate(triplet, key):
                stops[key].append(triplet)

    return json.dumps(stops)
