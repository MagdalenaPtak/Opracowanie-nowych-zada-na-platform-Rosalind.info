import pytest


def test_can_import_Task4_generate():
    from Task4.generator import generate


def test_task4_generator_can_generate_string_output(task4_generated_output):
    assert isinstance(task4_generated_output, str)


def test_task4_generator_can_generate_proper_dot_bracket_sequence_with_JSON_characters(
        task4_generated_output, allowed_dot_bracket_characters_with_json_elements):
    for element in task4_generated_output:
        assert element in allowed_dot_bracket_characters_with_json_elements, element


#######################################################################################################################

@pytest.fixture()
def task4_generated_output():
    from Task4.generator import generate
    return generate()


@pytest.fixture()
def allowed_dot_bracket_characters_with_json_elements():
    string = '()[]{}<>.-," '
    for char in range(ord("A"), ord("Z") + 1):
        string += chr(char)
        string += chr(char + 32)
    return string
