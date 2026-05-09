def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


def tell_age(name: str, age: int) -> str:
    unit = "year" if age == 1 else "years"
    return f"{name} is {age} {unit} old."


def goodbye(name: str = "World") -> str:
    return f"Goodbye, {name}!"


def shout(text: str) -> str:
    return f"{text.upper()}!"


def whisper(text: str) -> str:
    return f"{text.lower()}..."
