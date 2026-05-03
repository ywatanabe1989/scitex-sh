---
name: scitex-sh
description: |
  [WHAT] Safe subprocess wrapper — list-only `execute(['cmd', 'arg'])` API (no shell injection) with sensible defaults for capture, timeout, and error reporting.
  [WHEN] Running a shell command from Python without writing the full `subprocess.run([...], check=True, capture_output=True, text=True)` boilerplate.
  [HOW] `from scitex_sh import sh, execute` — call `sh(['cmd','arg'], return_as='dict')` or `execute([...])`.
tags: [scitex-sh]
primary_interface: python
interfaces:
  python: 2
  cli: 0
  mcp: 0
  skills: 2
  http: 0
---

> **Interfaces:** Python ⭐⭐ · CLI — · MCP — · Skills ⭐⭐ · Hook — · HTTP —

# scitex-sh

Safe subprocess wrapper — `execute(['cmd', 'arg'])` is a list-only API (no shell injection), with sensible defaults for capture, timeout, and error reporting. Drop-in replacement for `subprocess.run([...], check=True, capture_output=True, text=True)` boilerplate.

See README.md and the package's public `__init__.py` for the full
function list. This skill leaf exists so agents discover the package
exists and roughly what shape it has — refer to the source for
signatures.
