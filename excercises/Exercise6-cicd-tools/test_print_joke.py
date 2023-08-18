from print_joke import get_random_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert isinstance(reaction, str)


def test_get_random_reaction_repeats():
    reaction1 = get_random_reaction()
    reaction2 = get_random_reaction()
    assert reaction1 != reaction2


def test_contains_reaction():
    output = get_random_reaction()
    assert len(output) != 0
