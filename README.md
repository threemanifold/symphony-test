Flat Python hello module used to validate Symphony orchestration.

## Usage

```python
from hello import goodbye, greet, repeat, reverse, shout, tell_age, whisper

print(greet("Symphony"))
print(goodbye("Symphony"))
print(tell_age("Symphony", 1))
print(shout("Symphony"))
print(whisper("Symphony"))
print(reverse("Symphony"))
print(repeat("ha", 3))
```

## Tests

```sh
uvx pytest -v
```
