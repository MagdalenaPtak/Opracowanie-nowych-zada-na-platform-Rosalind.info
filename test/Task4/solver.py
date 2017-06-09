import pytest


def test_can_import_Task4_solve():
    from Task4.solver import solve


def test_task4_solver_raises_TypeError_when_not_recieving_string(task4_solver, task4_invalid_types):
    with pytest.raises(TypeError):
        task4_solver(task4_invalid_types)


def test_task4_solver_raises_TypeError_when_recieving_improper_dot_bracket_input_string(task4_solver,
                                                                                        task4_incorrect_outputs):
    with pytest.raises(TypeError):
        task4_solver(task4_incorrect_outputs)


def test_task4_solver_raises_exception_when_recieving_improper_json_input_string(task4_solver):
    import json
    try:
        exception = json.JSONDecodeError
    except:
        exception = ValueError
    with pytest.raises(exception):
        task4_solver("ABCD")


def test_task4_solver_accepts_proper_list_of_dot_bracket_input_strings(task4_solver):
    assert task4_solver('["(((....)))----", "(((....)))----"]')


def test_task4_solver_accepts_generated_RNA_input_string(task4_solver, task4_generated_output):
    assert task4_solver(task4_generated_output)


def test_task4_solver_generates_string_output(task4_solution):
    assert isinstance(task4_solution, str)


def test_task4_solver_generates_json_string(task4_solution):
    import json
    assert json.loads(task4_solution)


def test_task4_solver_generates_dict_after_loading_from_json(task4_solution):
    import json
    output = json.loads(task4_solution)
    assert isinstance(output, dict)


def test_task4_solver_generates_proper_dict(dict_task4_solution, task4_proper_dict_keys):
    assert len(dict_task4_solution) == len(task4_proper_dict_keys)
    for key in dict_task4_solution.keys():
        assert key in task4_proper_dict_keys


#######################################################################################################################

@pytest.fixture()
def task4_generated_output():
    from Task4.generator import generate
    return generate()


@pytest.fixture()
def task4_solver():
    from Task4.solver import solve
    return solve


@pytest.fixture(params=[["(((..*..)))----", "(((....)))----"],
                        ["(((....)))----", "(((.*.)))----"],
                        ["(((..+.)))----", "(((.*.)))----"],
                       ])
def task4_incorrect_outputs(request):
    import json
    return json.dumps(request.param)


@pytest.fixture(params=[None, [], (), 1, object])
def task4_invalid_types(request):
    return request.param


@pytest.fixture(params=["Z", "()", "1", "object", "t", "", "AUCD"])
def task4_invalid_strings(request):
    return request.param


@pytest.fixture()
def dict_task4_solution(task4_solution):
    import json
    return json.loads(task4_solution)


@pytest.fixture()
def task4_proper_dict_keys():
    return ["(", ")", ".", "pseudoknot"]
