import pytest


def test_can_import_Task3_generate():
    from Task3.generator import generate


def test_task3_generator_can_generate_string_output(task3_generated_output):
    assert isinstance(task3_generated_output, str)


def test_task3_generator_can_generate_proper_dot_bracket_sequence(task3_generated_output, allowed_dot_bracket_characters):
    for element in task3_generated_output:
        assert element in allowed_dot_bracket_characters, element


#######################################################################################################################

@pytest.fixture()
def task3_generated_output():
    from Task3.generator import generate
    return generate()


@pytest.fixture()
def allowed_dot_bracket_characters():
    string = "()[]{}<>.-"
    for char in range(ord("A"), ord("Z") + 1):
        string += chr(char)
        string += chr(char + 32)
    return string
