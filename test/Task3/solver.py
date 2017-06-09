import pytest


def test_can_import_Task2_solve():
    from Task2.solver import solve


def test_task2_solver_raises_TypeError_when_not_recieving_string(task2_solver, task2_invalid_types):
    with pytest.raises(TypeError):
        task2_solver(task2_invalid_types)


def test_task2_solver_raises_Exception_when_recieving_string_not_divisiable_by_3(task2_solver):
    for length in range(1, 99):
        if not length % 3:
            continue
        input_tmp = "A" * length
        with pytest.raises(Exception):
            task2_solver(input_tmp)


def test_task2_solver_accepts_proper_RNA_input_string(task2_solver):
    assert task2_solver("AUCGAU")


def test_task2_solver_accepts_generated_RNA_input_string(task2_solver, task2_generated_output):
    assert task2_solver(task2_generated_output)


def test_task2_solver_generates_string_output(task2_solution):
    assert isinstance(task2_solution, str)


def test_task2_solver_generates_json_string(task2_solution):
    import json
    assert json.loads(task2_solution)


def test_task2_solver_generates_dict_after_loading_from_json(task2_solution):
    import json
    output = json.loads(task2_solution)
    assert isinstance(output, dict)


def test_task2_solver_generates_proper_dict(dict_task2_solution, task2_proper_dict_keys):
    assert len(dict_task2_solution) == len(task2_proper_dict_keys)
    for key in dict_task2_solution.keys():
        assert key in task2_proper_dict_keys


#######################################################################################################################

@pytest.fixture()
def task2_generated_output():
    from Task2.generator import generate
    return generate()


@pytest.fixture()
def task2_solver():
    from Task2.solver import solve
    return solve


@pytest.fixture(params=[None, [], (), 1, object])
def task2_invalid_types(request):
    return request.param


@pytest.fixture(params=["Z", "()", "1", "object", "t", "", "AUCD"])
def task2_invalid_strings(request):
    return request.param


@pytest.fixture()
def dict_task2_solution(task2_solution):
    import json
    return json.loads(task2_solution)


@pytest.fixture()
def task2_proper_dict_keys():
    return ["UAG", "UAA", "UGA"]
