import pytest


def test_can_import_Task1_score():
    from Task1.scorer import score


def test_task1_scorer_raises_TypeError_when_not_recieving_string_as_inputs(task1_scorer, task1_invalid_inputs):
    with pytest.raises(TypeError):
        task1_scorer(task1_invalid_inputs[0], task1_invalid_inputs[1], task1_invalid_inputs[2])



def test_task1_scorer_raises_TypeError_when_recieving_empty_strings_as_inputs(task1_scorer):
    with pytest.raises(TypeError):
        task1_scorer("", "", "")


def test_task1_scorer_raises_JSONDecodeError_when_recieving_imporper_strings(task1_scorer, task1_invalid_strings):
    import json
    try:
        exception = json.JSONDecodeError
    except:
        exception = ValueError
    with pytest.raises(exception):
        task1_scorer(task1_invalid_strings[0], task1_invalid_strings[1], task1_invalid_strings[2])


def test_task1_scorer_can_accept_JSON_dict_strings(task1_scorer):
    assert task1_scorer("ACTG", "{}", "{}")


def test_task1_scorer_can_accept_task1_generated_outputs(task1_scorer, task1_generated_output, task1_solution):
    assert task1_scorer(task1_generated_output, task1_solution, task1_solution)


def test_task1_scorer_fails_user_input_when_recieving_wrong_number_of_keys_in_user_input(task1_scorer, task1_generated_output, task1_solution):
    wrong_task1_solution = task1_solution
    import json
    wrong_task1_solution = json.loads(wrong_task1_solution)
    del wrong_task1_solution["UUA"]
    wrong_task1_solution = json.dumps(wrong_task1_solution)
    assert not task1_scorer(task1_generated_output, task1_solution, wrong_task1_solution)

def test_task1_scorer_fails_user_input_when_recieving_not_matching_task1_solutions(task1_scorer, task1_generated_output, task1_solution):
    wrong_task1_solution = task1_solution
    import json
    wrong_task1_solution = json.loads(wrong_task1_solution)
    wrong_task1_solution["UUA"] += 1
    wrong_task1_solution = json.dumps(wrong_task1_solution)
    assert not task1_scorer(task1_generated_output, task1_solution, wrong_task1_solution)

#######################################################################################################################

@pytest.fixture()
def task1_generated_output():
    from Task1.generator import generate
    return generate()


@pytest.fixture()
def task1_solution(task1_generated_output):
    from Task1.solver import solve
    return solve(task1_generated_output)


@pytest.fixture()
def task1_scorer():
    from Task1.scorer import score
    return score


@pytest.fixture(params=[(None, None, None),
                        ("AAA", "BBB", object),
                        (1, 2, "TTT"),
                        ("1", None, ["AAA"])
                        ])
def task1_invalid_inputs(request):
    return request.param


@pytest.fixture(params=[("AAA", "BBB", "CCC"),
                        ("1", "[]", "TTT"),
                        ("[]", "[111]", "AAA")
                        ])
def task1_invalid_strings(request):
    return request.param
