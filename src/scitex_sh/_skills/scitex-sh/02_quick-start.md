---
description: |
  [TOPIC] scitex-sh Quick start
  [DETAILS] sh(['cmd', 'arg']) — list-only safe subprocess; dict / str return formats; timeout; streaming.
tags: [scitex-sh-quick-start]
---

# Quick Start

## Run a command (list form is mandatory)

```python
from scitex_sh import sh

result = sh(["ls", "-la", "/home"])         # default return_as="dict"
print(result["stdout"])
print(result["exit_code"])
```

List-only by design — no shell interpolation means no shell injection.

## Get just stdout

```python
text = sh(["git", "status", "--porcelain"], return_as="str", verbose=False)
```

## Timeout

```python
sh(["sleep", "10"], timeout=5)              # raises after 5s
```

## Stream output in real time

```python
sh(["./long-build.sh"], stream_output=True) # tails output live
```

## Detailed result via sh_run

```python
from scitex_sh import sh_run

r = sh_run(["python", "script.py"])
if r["success"]:
    print(r["stdout"])
else:
    print("FAILED:", r["stderr"])
```

## Pipes / redirects — chain in Python

```python
ls = sh(["ls", "-la"], return_as="str", verbose=False)
py_files = [l for l in ls.split("\n") if ".py" in l]
```

Don't try to pass `"ls | grep"` as a single string — that's exactly the
shell-injection surface this package eliminates.

## Next

- [03_python-api.md](03_python-api.md) — full surface
- [SKILL.md](SKILL.md) — overview
