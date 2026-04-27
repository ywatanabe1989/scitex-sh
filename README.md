# scitex-sh

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-sh.svg)](https://pypi.org/project/scitex-sh/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-sh.svg)](https://pypi.org/project/scitex-sh/)
[![Tests](https://github.com/ywatanabe1989/scitex-sh/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-sh/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-sh/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-sh/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-sh/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-sh)
[![Docs](https://readthedocs.org/projects/scitex-sh/badge/?version=latest)](https://scitex-sh.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


Safe subprocess wrapper extracted from the [SciTeX](https://github.com/ywatanabe1989/scitex-python) ecosystem as a standalone, zero-dep package.

List-only (no shell-string parsing) → no shell-injection. Stream output, timeouts, structured `ShellResult` return.

## Install

```bash
pip install scitex-sh
```

## API

```python
import scitex_sh as sh

# Dict result with stdout/stderr/returncode/success
res = sh.sh(["git", "status"])
# {"success": True, "stdout": "...", "stderr": "", "returncode": 0, ...}

# String result
out = sh.sh(["ls", "-la"], return_as="str")

# Streamed
sh.sh(["./long-running.sh"], stream_output=True)

# Timeout
sh.sh(["sleep", "10"], timeout=2)

# Lower-level
res = sh.sh_run(["echo", "hi"])
sh.quote("hello world")  # 'hello world' (POSIX-quoted)
```

## Status

Standalone fork of `scitex.sh`. Zero deps (pure stdlib). The umbrella package's
`scitex.sh` import path is preserved via a `sys.modules`-alias bridge. The
`scitex.str.color_text` dep used for terminal output is replaced with a tiny
inline ANSI helper that respects `NO_COLOR` and TTY detection.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).
