import pytest


def test_can_import_Task1_solve():
    from Task1.solver import solve


def test_task1_solver_raises_TypeError_when_not_recieving_string(task1_solver, task1_invalid_types):
    with pytest.raises(TypeError):
        task1_solver(task1_invalid_types)


def test_task1_solver_raises_TypeError_when_not_recieving_DNA_string(task1_solver, task1_invalid_strings):
    with pytest.raises(TypeError):
        task1_solver(task1_invalid_strings)


def test_task1_solver_accepts_proper_DNA_input_string(task1_solver):
    assert task1_solver("ATCG")


def test_task1_solver_accepts_generated_DNA_input_string(task1_solver, task1_generated_output):
    assert task1_solver(task1_generated_output)


def test_task1_solver_generates_string_output(task1_solution):
    assert isinstance(task1_solution, str)


def test_task1_solver_generates_json_string(task1_solution):
    import json
    assert json.loads(task1_solution)


def test_task1_solver_generates_dict_after_loading_from_json(task1_solution):
    import json
    output = json.loads(task1_solution)
    assert isinstance(output, dict)


def test_task1_solver_generates_proper_dict(dict_task1_solution, task1_proper_dict_keys):
    assert len(dict_task1_solution) == len(task1_proper_dict_keys)
    for key in dict_task1_solution.keys():
        assert key in task1_proper_dict_keys


#######################################################################################################################

@pytest.fixture()
def task1_generated_output():
    from Task1.generator import generate
    return generate()


@pytest.fixture()
def task1_solver():
    from Task1.solver import solve
    return solve


@pytest.fixture()
def task1_solution(task1_solver, task1_generated_output):
    return task1_solver(task1_generated_output)


@pytest.fixture()
def dict_task1_solution(task1_solution):
    import json
    return json.loads(task1_solution)


@pytest.fixture()
def task1_proper_dict_keys():
    return ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]


@pytest.fixture(params=[None, [], (), 1, object])
def task1_invalid_types(request):
    return request.param


@pytest.fixture(params=["Z", "()", "1", "object", "t", "", "ATCD"])
def task1_invalid_strings(request):
    return request.param
