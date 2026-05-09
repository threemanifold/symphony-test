from hello import goodbye, greet


def test_greet_default_name() -> None:
    assert greet() == "Hello, World!"


def test_greet_custom_name() -> None:
    assert greet("Symphony") == "Hello, Symphony!"


def test_goodbye_default_name() -> None:
    assert goodbye() == "Goodbye, World!"


def test_goodbye_custom_name() -> None:
    assert goodbye("Symphony") == "Goodbye, Symphony!"
