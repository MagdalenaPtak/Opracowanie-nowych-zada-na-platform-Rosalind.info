import pytest


def test_can_import_Task3_solve():
    from Task3.solver import solve


def test_task3_solver_raises_TypeError_when_not_recieving_string(task3_solver, task3_invalid_types):
    with pytest.raises(TypeError):
        task3_solver(task3_invalid_types)


def test_task3_solver_accepts_proper_RNA_input_string(task3_solver):
    assert task3_solver("AUCGAU")


def test_task3_solver_accepts_generated_RNA_input_string(task3_solver, task3_generated_output):
    assert task3_solver(task3_generated_output)


def test_task3_solver_generates_string_output(task3_solution):
    assert isinstance(task3_solution, str)


def test_task3_solver_generates_json_string(task3_solution):
    import json
    assert json.loads(task3_solution)


def test_task3_solver_generates_dict_after_loading_from_json(task3_solution):
    import json
    output = json.loads(task3_solution)
    assert isinstance(output, dict)


def test_task3_solver_generates_proper_dict(dict_task3_solution, task3_proper_dict_keys):
    assert len(dict_task3_solution) == len(task3_proper_dict_keys)
    for key in dict_task3_solution.keys():
        assert key in task3_proper_dict_keys


#######################################################################################################################

@pytest.fixture()
def task3_generated_output():
    from Task3.generator import generate
    return generate()


@pytest.fixture()
def task3_solver():
    from Task3.solver import solve
    return solve


@pytest.fixture(params=[None, [], (), 1, object])
def task3_invalid_types(request):
    return request.param


@pytest.fixture(params=["Z", "()", "1", "object", "t", "", "AUCD"])
def task3_invalid_strings(request):
    return request.param


@pytest.fixture()
def dict_task3_solution(task3_solution):
    import json
    return json.loads(task3_solution)


@pytest.fixture()
def task3_proper_dict_keys():
    return ["junction_type", "junction_count", "pseudoknot_complexity", "pseudoknot_count"]
