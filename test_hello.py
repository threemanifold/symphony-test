from hello import goodbye, greet, reverse, shout, tell_age, whisper


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


def test_whisper_uppercase_text() -> None:
    assert whisper("HELLO") == "hello..."


def test_whisper_mixed_case_text() -> None:
    assert whisper("Symphony") == "symphony..."


def test_whisper_empty_text() -> None:
    assert whisper("") == "..."


def test_reverse_lowercase_text() -> None:
    assert reverse("hello") == "olleh"


def test_reverse_mixed_case_text() -> None:
    assert reverse("Symphony") == "ynohpmyS"


def test_reverse_empty_text() -> None:
    assert reverse("") == ""
