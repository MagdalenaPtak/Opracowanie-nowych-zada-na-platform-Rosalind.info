import pytest


def test_can_import_Task3_score():
    from Task3.scorer import score


def test_task3_scorer_raises_TypeError_when_not_recieving_string_as_inputs(task3_scorer, task3_invalid_inputs):
    with pytest.raises(TypeError):
        task3_scorer(task3_invalid_inputs[0], task3_invalid_inputs[1], task3_invalid_inputs[2])



def test_task3_scorer_raises_TypeError_when_recieving_empty_strings_as_inputs(task3_scorer):
    with pytest.raises(TypeError):
        task3_scorer("", "", "")


def test_task3_scorer_raises_JSONDecodeError_when_recieving_imporper_strings(task3_scorer, task3_invalid_strings):
    import json
    try:
        exception = json.JSONDecodeError
    except AttributeError:
        exception = ValueError
    with pytest.raises(exception):
        task3_scorer(task3_invalid_strings[0], task3_invalid_strings[1], task3_invalid_strings[2])


def test_task3_scorer_can_accept_JSON_dict_strings(task3_scorer):
    assert task3_scorer("ACUG", "{}", "{}")


def test_task3_scorer_can_accept_task3_generated_outputs(task3_scorer, task3_generated_output, task3_solution):
    assert task3_scorer(task3_generated_output, task3_solution, task3_solution)


def test_task3_scorer_fails_user_input_when_recieving_wrong_number_of_keys_in_user_input(task3_scorer, task3_generated_output, task3_solution):
    wrong_task3_solution = task3_solution
    import json
    wrong_task3_solution = json.loads(wrong_task3_solution)
    del wrong_task3_solution["junction_count"]
    wrong_task3_solution = json.dumps(wrong_task3_solution)
    assert not task3_scorer(task3_generated_output, task3_solution, wrong_task3_solution)

def test_task3_scorer_fails_user_input_when_recieving_not_matching_task3_solutions(task3_scorer, task3_generated_output, task3_solution):
    wrong_task3_solution = task3_solution
    import json
    wrong_task3_solution = json.loads(wrong_task3_solution)
    wrong_task3_solution["junction_count"] += 1
    wrong_task3_solution = json.dumps(wrong_task3_solution)
    assert not task3_scorer(task3_generated_output, task3_solution, wrong_task3_solution)

#######################################################################################################################

@pytest.fixture()
def task3_generated_output():
    from Task3.generator import generate
    return generate()


@pytest.fixture()
def task3_solution(task3_generated_output):
    from Task3.solver import solve
    return solve(task3_generated_output)


@pytest.fixture()
def task3_scorer():
    from Task3.scorer import score
    return score


@pytest.fixture(params=[(None, None, None),
                        ("AAA", "BBB", object),
                        (1, 2, "TTT"),
                        ("1", None, ["AAA"])
                        ])
def task3_invalid_inputs(request):
    return request.param


@pytest.fixture(params=[("AAA", "BBB", "CCC"),
                        ("1", "[]", "TTT"),
                        ("[]", "[111]", "AAA")
                        ])
def task3_invalid_strings(request):
    return request.param
