Flat Python hello module used to validate Symphony orchestration.

## Usage

```python
from hello import goodbye, greet, shout, tell_age

print(greet("Symphony"))
print(goodbye("Symphony"))
print(tell_age("Symphony", 1))
print(shout("Symphony"))
```

## Tests

```sh
uvx pytest -v
```
