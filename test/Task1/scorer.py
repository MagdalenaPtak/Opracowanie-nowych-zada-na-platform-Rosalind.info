import pytest


def test_can_import_Task1_score():
    from Task1.scorer import score


def test_scorer_raises_TypeError_when_not_recieving_string_as_inputs(scorer, invalid_inputs):
    with pytest.raises(TypeError):
        scorer(invalid_inputs[0], invalid_inputs[1], invalid_inputs[2])



def test_scorer_raises_TypeError_when_recieving_empty_strings_as_inputs(scorer):
    with pytest.raises(TypeError):
        scorer("", "", "")


def test_scorer_raises_JSONDecodeError_when_recieving_imporper_strings(scorer, invalid_strings):
    import json
    with pytest.raises(json.JSONDecodeError):
        scorer(invalid_strings[0], invalid_strings[1], invalid_strings[2])


def test_scorer_can_accept_JSON_dict_strings(scorer):
    assert scorer("ACTG", "{}", "{}")


def test_scorer_can_accept_generated_outputs(scorer, generated_output, solution):
    assert scorer(generated_output, solution, solution)


def test_scorer_fails_user_input_when_recieving_wrong_number_of_keys_in_user_input(scorer, generated_output, solution):
    wrong_solution = solution
    import json
    wrong_solution = json.loads(wrong_solution)
    del wrong_solution["UUA"]
    wrong_solution = json.dumps(wrong_solution)
    assert not scorer(generated_output, solution, wrong_solution)

def test_scorer_fails_user_input_when_recieving_not_matching_solutions(scorer, generated_output, solution):
    wrong_solution = solution
    import json
    wrong_solution = json.loads(wrong_solution)
    wrong_solution["UUA"] += 1
    wrong_solution = json.dumps(wrong_solution)
    assert not scorer(generated_output, solution, wrong_solution)

#######################################################################################################################

@pytest.fixture()
def generated_output():
    from Task1.generator import generate
    return generate()


@pytest.fixture()
def solution(generated_output):
    from Task1.solver import solve
    return solve(generated_output)


@pytest.fixture()
def scorer():
    from Task1.scorer import score
    return score


@pytest.fixture(params=[(None, None, None),
                        ("AAA", "BBB", object),
                        (1, 2, "TTT"),
                        ("1", None, ["AAA"])
                        ])
def invalid_inputs(request):
    return request.param


@pytest.fixture(params=[("AAA", "BBB", "CCC"),
                        ("1", "[]", "TTT"),
                        ("[]", "[111]", "AAA")
                        ])
def invalid_strings(request):
    return request.param
