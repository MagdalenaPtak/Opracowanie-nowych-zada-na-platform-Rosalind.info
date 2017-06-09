import pytest


def test_can_import_Task1_generate():
    from Task1.generator import generate


def test_task1_generator_can_generate_string_output(task1_generated_output):
    assert isinstance(task1_generated_output, str)


def test_task1_generator_can_generate_proper_DNA_sequence(task1_generated_output, allowed_dna_characters):
    for element in task1_generated_output:
        assert element in allowed_dna_characters, element


def test_task1_generator_can_generate_a_100_element_DNA_sequence(task1_generated_output):
    assert len(task1_generated_output) == 100, len(task1_generated_output)


#######################################################################################################################

@pytest.fixture()
def task1_generated_output():
    from Task1.generator import generate
    return generate()


@pytest.fixture()
def allowed_dna_characters():
    return "TGAC"
