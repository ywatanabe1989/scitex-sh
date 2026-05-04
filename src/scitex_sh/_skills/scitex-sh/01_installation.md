---
description: |
  [TOPIC] scitex-sh Installation
  [DETAILS] pip install scitex-sh (pure Python, stdlib subprocess); smoke verify with import + sh.
tags: [scitex-sh-installation]
---

# Installation

## Standard

```bash
pip install scitex-sh
```

Pure-Python; no required runtime dependencies (built on stdlib
`subprocess`).

## Verify

```bash
python -c "import scitex_sh; print(scitex_sh.__version__)"
python -c "from scitex_sh import sh, execute; print('ok')"
python -c "from scitex_sh import sh; print(sh(['echo', 'ok'], verbose=False))"
```

## Editable install (development)

```bash
git clone https://github.com/ywatanabe1989/scitex-sh
cd scitex-sh
pip install -e '.[dev]'
```

## Umbrella alternative

```bash
pip install scitex   # exposes scitex.sh as a submodule
```
