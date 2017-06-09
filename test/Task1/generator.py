import pytest


def test_can_import_Task1_generate():
    from Task1.generator import generate


def test_generator_can_generate_string_output(generated_output):
    assert isinstance(generated_output, str)


def test_generator_can_generate_proper_DNA_sequence(generated_output, allowed_dna_characters):
    for element in generated_output:
        assert element in allowed_dna_characters, element


def test_generator_can_generate_a_100_element_DNA_sequence(generated_output):
    assert len(generated_output) == 100, len(generated_output)


#######################################################################################################################

@pytest.fixture()
def generated_output():
    from Task1.generator import generate
    return generate()


@pytest.fixture()
def allowed_dna_characters():
    return "TGAC"
