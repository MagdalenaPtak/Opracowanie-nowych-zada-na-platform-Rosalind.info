import pytest


def test_can_import_Task4_score():
    from Task4.scorer import score


def test_task4_scorer_raises_TypeError_when_not_recieving_string_as_inputs(task4_scorer, task4_invalid_inputs):
    with pytest.raises(TypeError):
        task4_scorer(task4_invalid_inputs[0], task4_invalid_inputs[1], task4_invalid_inputs[2])



def test_task4_scorer_raises_TypeError_when_recieving_empty_strings_as_inputs(task4_scorer):
    with pytest.raises(TypeError):
        task4_scorer("", "", "")


def test_task4_scorer_raises_JSONDecodeError_when_recieving_imporper_strings(task4_scorer, task4_invalid_strings):
    import json
    try:
        exception = json.JSONDecodeError
    except AttributeError:
        exception = ValueError
    with pytest.raises(exception):
        task4_scorer(task4_invalid_strings[0], task4_invalid_strings[1], task4_invalid_strings[2])


def test_task4_scorer_can_accept_JSON_dict_strings(task4_scorer):
    assert task4_scorer("()....", "{}", "{}")


def test_task4_scorer_can_accept_task4_generated_outputs(task4_scorer, task4_generated_output, task4_solution):
    assert task4_scorer(task4_generated_output, task4_solution, task4_solution)


def test_task4_scorer_fails_user_input_when_recieving_wrong_number_of_keys_in_user_input(task4_scorer, task4_generated_output, task4_solution):
    wrong_task4_solution = task4_solution
    import json
    wrong_task4_solution = json.loads(wrong_task4_solution)
    del wrong_task4_solution["("]
    wrong_task4_solution = json.dumps(wrong_task4_solution)
    assert not task4_scorer(task4_generated_output, task4_solution, wrong_task4_solution)


def test_task4_scorer_fails_user_input_when_recieving_not_matching_task4_solutions(task4_scorer, task4_generated_output, task4_solution):
    wrong_task4_solution = task4_solution
    import json
    wrong_task4_solution = json.loads(wrong_task4_solution)
    wrong_task4_solution["("] = "-1%"
    wrong_task4_solution = json.dumps(wrong_task4_solution)
    assert not task4_scorer(task4_generated_output, task4_solution, wrong_task4_solution)

#######################################################################################################################

@pytest.fixture()
def task4_generated_output():
    from Task4.generator import generate
    return generate()


@pytest.fixture()
def task4_solution(task4_generated_output):
    from Task4.solver import solve
    return solve(task4_generated_output)


@pytest.fixture()
def task4_scorer():
    from Task4.scorer import score
    return score


@pytest.fixture(params=[(None, None, None),
                        ("AAA", "BBB", object),
                        (1, 2, "TTT"),
                        ("1", None, ["AAA"])
                        ])
def task4_invalid_inputs(request):
    return request.param


@pytest.fixture(params=[("AAA", "BBB", "CCC"),
                        ("1", "[]", "TTT"),
                        ("[]", "[111]", "AAA")
                        ])
def task4_invalid_strings(request):
    return request.param
