import pytest


def test_can_import_Task1_solve():
    from Task1.solver import solve


def test_solver_raises_TypeError_when_not_recieving_string(solver, invalid_types):
    with pytest.raises(TypeError):
        solver(invalid_types)


def test_solver_raises_TypeError_when_not_recieving_DNA_string(solver, invalid_strings):
    with pytest.raises(TypeError):
        solver(invalid_strings)


def test_solver_accepts_proper_DNA_input_string(solver):
    assert solver("ATCG")


def test_solver_accepts_generated_DNA_input_string(solver, generated_output):
    assert solver(generated_output)


def test_solver_generates_string_output(solution):
    assert isinstance(solution, str)


def test_solver_generates_json_string(solution):
    import json
    assert json.loads(solution)


def test_solver_generates_dict_after_loading_from_json(solution):
    import json
    output = json.loads(solution)
    assert isinstance(output, dict)


def test_solver_generates_proper_dict(dict_solution, proper_dict_keys):
    assert len(dict_solution) == len(proper_dict_keys)
    for key in dict_solution.keys():
        assert key in proper_dict_keys


#######################################################################################################################

@pytest.fixture()
def generated_output():
    from Task1.generator import generate
    return generate()


@pytest.fixture()
def solver():
    from Task1.solver import solve
    return solve


@pytest.fixture()
def solution(solver, generated_output):
    return solver(generated_output)


@pytest.fixture()
def dict_solution(solution):
    import json
    return json.loads(solution)


@pytest.fixture()
def proper_dict_keys():
    return ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]


@pytest.fixture(params=[None, [], (), 1, object])
def invalid_types(request):
    return request.param


@pytest.fixture(params=["Z", "()", "1", "object", "t", "", "ATCD"])
def invalid_strings(request):
    return request.param
