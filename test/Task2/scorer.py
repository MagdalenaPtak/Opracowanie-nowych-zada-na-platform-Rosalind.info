import pytest


def test_can_import_Task2_score():
    from Task2.scorer import score


def test_task2_scorer_raises_TypeError_when_not_recieving_string_as_inputs(task2_scorer, task2_invalid_inputs):
    with pytest.raises(TypeError):
        task2_scorer(task2_invalid_inputs[0], task2_invalid_inputs[1], task2_invalid_inputs[2])



def test_task2_scorer_raises_TypeError_when_recieving_empty_strings_as_inputs(task2_scorer):
    with pytest.raises(TypeError):
        task2_scorer("", "", "")


def test_task2_scorer_raises_JSONDecodeError_when_recieving_imporper_strings(task2_scorer, task2_invalid_strings):
    import json
    try:
        exception = json.JSONDecodeError
    except AttributeError:
        exception = ValueError
    with pytest.raises(exception):
        task2_scorer(task2_invalid_strings[0], task2_invalid_strings[1], task2_invalid_strings[2])


def test_task2_scorer_can_accept_JSON_dict_strings(task2_scorer):
    assert task2_scorer("ACTG", "{}", "{}")


def test_task2_scorer_can_accept_task2_generated_outputs(task2_scorer, task2_generated_output, task2_solution):
    assert task2_scorer(task2_generated_output, task2_solution, task2_solution)


def test_task2_scorer_fails_user_input_when_recieving_wrong_number_of_keys_in_user_input(task2_scorer, task2_generated_output, task2_solution):
    wrong_task2_solution = task2_solution
    import json
    wrong_task2_solution = json.loads(wrong_task2_solution)
    del wrong_task2_solution["UAG"]
    wrong_task2_solution = json.dumps(wrong_task2_solution)
    assert not task2_scorer(task2_generated_output, task2_solution, wrong_task2_solution)

def test_task2_scorer_fails_user_input_when_recieving_not_matching_task2_solutions(task2_scorer, task2_generated_output, task2_solution):
    wrong_task2_solution = task2_solution
    import json
    wrong_task2_solution = json.loads(wrong_task2_solution)
    wrong_task2_solution["UAG"].append("AAA")
    wrong_task2_solution = json.dumps(wrong_task2_solution)
    assert not task2_scorer(task2_generated_output, task2_solution, wrong_task2_solution)

#######################################################################################################################

@pytest.fixture()
def task2_generated_output():
    from Task2.generator import generate
    return generate()


@pytest.fixture()
def task2_solution(task2_generated_output):
    from Task2.solver import solve
    return solve(task2_generated_output)


@pytest.fixture()
def task2_scorer():
    from Task2.scorer import score
    return score


@pytest.fixture(params=[(None, None, None),
                        ("AAA", "BBB", object),
                        (1, 2, "TTT"),
                        ("1", None, ["AAA"])
                        ])
def task2_invalid_inputs(request):
    return request.param


@pytest.fixture(params=[("AAA", "BBB", "CCC"),
                        ("1", "[]", "TTT"),
                        ("[]", "[111]", "AAA")
                        ])
def task2_invalid_strings(request):
    return request.param
