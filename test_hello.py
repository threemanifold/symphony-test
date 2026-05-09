from hello import goodbye, greet, shout, tell_age


def test_greet_default_name() -> None:
    assert greet() == "Hello, World!"


def test_greet_custom_name() -> None:
    assert greet("Symphony") == "Hello, Symphony!"


def test_goodbye_default_name() -> None:
    assert goodbye() == "Goodbye, World!"


def test_goodbye_custom_name() -> None:
    assert goodbye("Symphony") == "Goodbye, Symphony!"


def test_tell_age_singular() -> None:
    assert tell_age("Symphony", 1) == "Symphony is 1 year old."


def test_tell_age_plural() -> None:
    assert tell_age("Symphony", 2) == "Symphony is 2 years old."


def test_shout_lowercase_text() -> None:
    assert shout("hello") == "HELLO!"


def test_shout_mixed_case_text() -> None:
    assert shout("Symphony") == "SYMPHONY!"


def test_shout_empty_text() -> None:
    assert shout("") == "!"
