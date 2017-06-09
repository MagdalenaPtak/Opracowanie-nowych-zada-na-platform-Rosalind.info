import pytest


def test_can_import_Task2_generate():
    from Task2.generator import generate


def test_task2_generator_can_generate_string_output(task2_generated_output):
    assert isinstance(task2_generated_output, str)


def test_task2_generator_can_generate_proper_RNA_sequence(task2_generated_output, allowed_rna_characters):
    for element in task2_generated_output:
        assert element in allowed_rna_characters, element


def test_task2_generator_can_generate_a_99_element_RNA_sequence(task2_generated_output):
    assert len(task2_generated_output) == 99, len(task2_generated_output)


#######################################################################################################################

@pytest.fixture()
def task2_generated_output():
    from Task2.generator import generate
    return generate()


@pytest.fixture()
def allowed_rna_characters():
    return "UGAC"
