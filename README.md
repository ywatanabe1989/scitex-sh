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

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Safe subprocess wrapper — list-only (no shell-string parsing), structured result, timeouts, streaming.</b></p>

<p align="center">
  <a href="https://scitex-sh.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-sh</code>
</p>

---

## Installation

```bash
pip install scitex-sh
```

## Quick Start

```python
import scitex_sh as sh

res = sh.sh(["git", "status"])
print(res["stdout"])
```

## 1 Interfaces

<details>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_sh as sh

# Dict result (stdout / stderr / returncode / success)
res = sh.sh(["git", "status"])

# String result
out = sh.sh(["ls", "-la"], return_as="str")

# Streamed output
sh.sh(["./long-running.sh"], stream_output=True)

# Timeout
sh.sh(["sleep", "10"], timeout=2)

# Lower-level
res = sh.sh_run(["echo", "hi"])
sh.quote("hello world")            # 'hello world' (POSIX-quoted)
```

</details>

## Status

Standalone fork of `scitex.sh`. Zero deps (pure stdlib). The umbrella package's
`scitex.sh` import path is preserved via a `sys.modules`-alias bridge. The
`scitex.str.color_text` dep used for terminal output is replaced with a tiny
inline ANSI helper that respects `NO_COLOR` and TTY detection.

## Part of SciTeX

`scitex-sh` is part of [**SciTeX**](https://scitex.ai).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
