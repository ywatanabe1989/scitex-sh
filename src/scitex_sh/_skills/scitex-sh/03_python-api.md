---
description: |
  [TOPIC] scitex-sh Python API
  [DETAILS] Public callables — sh, sh_run, execute, quote, plus legacy run_shellcommand / run_shellscript.
tags: [scitex-sh-python-api]
---

# Python API

## Imports

```python
from scitex_sh import (
    sh,
    sh_run,
    execute,                # lower-level (used by sh / sh_run)
    quote,                  # shlex.quote-style helper
    run_shellcommand,       # legacy
    run_shellscript,        # legacy
)
```

## `sh(command, *, verbose=True, return_as="dict", timeout=None, stream_output=False)`

Run a command. `command` **must** be a list of strings.

| Param           | Default | Notes                                          |
|-----------------|---------|------------------------------------------------|
| `verbose`       | `True`  | Print command + output to stderr               |
| `return_as`     | `"dict"`| `"dict"` → `ShellResult`; `"str"` → stdout/stderr string |
| `timeout`       | `None`  | Seconds; `subprocess.TimeoutExpired` on expiry |
| `stream_output` | `False` | Tail stdout/stderr to terminal in real time    |

`ShellResult` keys: `stdout`, `stderr`, `exit_code`, `success`.

## `sh_run(command, *, verbose=True) -> ShellResult`

Same as `sh(command, return_as="dict")` — kept for explicit use when
you always want the structured result.

## `execute(command, *, verbose=True, timeout=None, stream_output=False) -> ShellResult`

Lower-level primitive used by `sh` / `sh_run`. Use directly when you
want to bypass the `return_as` switch.

## `quote(s) -> str`

POSIX shell quoting (alias of `shlex.quote`). Use only when emitting
shell snippets for human consumption — not when assembling `sh()`
arguments (which take a list).

## Legacy

`run_shellcommand` and `run_shellscript` are kept for backwards
compatibility with `scitex.gen` callers. Prefer `sh` / `sh_run` for new
code.

## Two import paths

```python
import scitex_sh        # standalone
import scitex.sh        # umbrella (requires `pip install scitex`)
```

## Security note

Only list form is allowed. Each argument is treated as a literal
string — no shell expansion, globbing, or interpolation. For pipes,
redirects, or `&&` chains, compose in Python by calling `sh()` multiple
times and threading their outputs.
