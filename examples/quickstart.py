"""scitex-sh quickstart: run a shell command safely (list-only, no shell injection)."""

import scitex_sh


def main():
    # 1. Run a basic command, capture stdout/stderr/exit_code as a dict.
    result = scitex_sh.sh(["echo", "hello from scitex-sh"], verbose=False)
    print("exit_code:", result["exit_code"])
    print("stdout:", result["stdout"].strip())
    assert result["exit_code"] == 0
    assert "hello from scitex-sh" in result["stdout"]

    # 2. Return the stdout directly as a string.
    out = scitex_sh.sh(["python", "-c", "print(2 + 3)"], verbose=False, return_as="str")
    print("python result:", out.strip())
    assert out.strip() == "5"

    # 3. Demonstrate the safety guard: only list form is accepted.
    try:
        scitex_sh.sh("echo unsafe; rm -rf /tmp/nonexistent", verbose=False)
    except Exception as exc:
        print("rejected string form as expected:", type(exc).__name__)


if __name__ == "__main__":
    main()
