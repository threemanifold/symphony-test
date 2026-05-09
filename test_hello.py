from hello import goodbye, greet, tell_age


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
