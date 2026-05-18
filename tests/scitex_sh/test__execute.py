#!/usr/bin/env python3
# Timestamp: "2026-05-18 (ywatanabe)"
# File: tests/scitex_sh/test__execute.py

"""Tests for shell command execution functions.

This module tests the execution functionality of the sh module:
- execute: Main execution function with options
- _execute_buffered: Buffered output execution
- _execute_with_streaming: Real-time streaming execution
"""

import pytest


# ---------------------------------------------------------------------------
# TestExecuteBasic — execute() happy-path behaviour
# ---------------------------------------------------------------------------


def test_execute_function_is_not_none_after_import():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    fn = execute
    # Assert
    assert fn is not None


def test_execute_function_is_callable_after_import():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    is_callable = callable(execute)
    # Assert
    assert is_callable is True


def test_execute_returns_dict_for_simple_echo_command():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello"], verbose=False)
    # Assert
    assert isinstance(result, dict)


def test_execute_result_dict_contains_stdout_key():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello"], verbose=False)
    # Assert
    assert "stdout" in result


def test_execute_result_dict_contains_stderr_key():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello"], verbose=False)
    # Assert
    assert "stderr" in result


def test_execute_result_dict_contains_exit_code_key():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello"], verbose=False)
    # Assert
    assert "exit_code" in result


def test_execute_result_dict_contains_success_key():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello"], verbose=False)
    # Assert
    assert "success" in result


def test_execute_echo_returns_text_on_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test"], verbose=False)
    # Assert
    assert result["stdout"] == "test"


def test_execute_echo_leaves_stderr_empty():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test"], verbose=False)
    # Assert
    assert result["stderr"] == ""


def test_execute_echo_returns_exit_code_zero():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test"], verbose=False)
    # Assert
    assert result["exit_code"] == 0


def test_execute_echo_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_echo_two_words_preserves_argument():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "Hello World"], verbose=False)
    # Assert
    assert result["stdout"] == "Hello World"


def test_execute_pwd_command_returns_non_empty_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["pwd"], verbose=False)
    # Assert
    assert len(result["stdout"]) > 0


def test_execute_pwd_command_returns_unix_style_path():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["pwd"], verbose=False)
    # Assert
    assert "/" in result["stdout"]


def test_execute_ls_command_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["ls", "-la"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_ls_command_returns_non_empty_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["ls", "-la"], verbose=False)
    # Assert
    assert len(result["stdout"]) > 0


# ---------------------------------------------------------------------------
# TestExecuteErrorHandling
# ---------------------------------------------------------------------------


def test_execute_cat_nonexistent_file_returns_success_false():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["cat", "/nonexistent/path/file.txt"], verbose=False)
    # Assert
    assert result["success"] is False


def test_execute_cat_nonexistent_file_returns_nonzero_exit_code():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["cat", "/nonexistent/path/file.txt"], verbose=False)
    # Assert
    assert result["exit_code"] != 0


def test_execute_cat_nonexistent_file_writes_to_stderr():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["cat", "/nonexistent/path/file.txt"], verbose=False)
    # Assert
    assert len(result["stderr"]) > 0


def test_execute_raises_oserror_for_unknown_executable():
    # Arrange
    from scitex_sh._execute import execute
    cmd = ["nonexistent_command_12345"]
    # Act
    # Either FileNotFoundError or PermissionError depending on $PATH layout;
    # both are OSError subclasses and both signal "cannot invoke this command".
    ctx = pytest.raises(OSError)
    # Assert
    with ctx:
        execute(cmd, verbose=False)


def test_execute_false_command_returns_success_false():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["false"], verbose=False)
    # Assert
    assert result["success"] is False


def test_execute_false_command_returns_exit_code_one():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["false"], verbose=False)
    # Assert
    assert result["exit_code"] == 1


def test_execute_true_command_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["true"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_true_command_returns_exit_code_zero():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["true"], verbose=False)
    # Assert
    assert result["exit_code"] == 0


def test_execute_raises_typeerror_when_command_is_string():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    ctx = pytest.raises(TypeError)
    # Assert
    with ctx:
        execute("echo hello", verbose=False)


# ---------------------------------------------------------------------------
# TestExecuteTimeout
# ---------------------------------------------------------------------------


def test_execute_with_generous_timeout_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "quick"], verbose=False, timeout=10)
    # Assert
    assert result["success"] is True


def test_execute_with_generous_timeout_preserves_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "quick"], verbose=False, timeout=10)
    # Assert
    assert result["stdout"] == "quick"


def test_execute_sleep_longer_than_timeout_returns_success_false():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["sleep", "5"], verbose=False, timeout=1)
    # Assert
    assert result["success"] is False


def test_execute_without_timeout_value_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test"], verbose=False, timeout=None)
    # Assert
    assert result["success"] is True


# ---------------------------------------------------------------------------
# TestExecuteOutput
# ---------------------------------------------------------------------------


def test_execute_printf_multiline_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["printf", "line1\nline2\nline3"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_printf_multiline_yields_three_lines():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["printf", "line1\nline2\nline3"], verbose=False)
    # Assert
    assert len(result["stdout"].split("\n")) == 3


def test_execute_printf_multiline_preserves_first_line_text():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["printf", "line1\nline2\nline3"], verbose=False)
    # Assert
    assert result["stdout"].split("\n")[0] == "line1"


def test_execute_printf_multiline_preserves_second_line_text():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["printf", "line1\nline2\nline3"], verbose=False)
    # Assert
    assert result["stdout"].split("\n")[1] == "line2"


def test_execute_printf_multiline_preserves_third_line_text():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["printf", "line1\nline2\nline3"], verbose=False)
    # Assert
    assert result["stdout"].split("\n")[2] == "line3"


def test_execute_echo_unicode_argument_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "日本語テスト"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_echo_unicode_argument_preserves_characters_in_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "日本語テスト"], verbose=False)
    # Assert
    assert "日本語テスト" in result["stdout"]


def test_execute_true_command_yields_empty_stdout_string():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["true"], verbose=False)
    # Assert
    assert result["stdout"] == ""


def test_execute_captures_text_redirected_to_stderr():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "echo error >&2"], verbose=False)
    # Assert
    assert "error" in result["stderr"]


def test_execute_captures_stdout_when_both_streams_used():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["bash", "-c", "echo stdout; echo stderr >&2"], verbose=False
    )
    # Assert
    assert "stdout" in result["stdout"]


def test_execute_captures_stderr_when_both_streams_used():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["bash", "-c", "echo stdout; echo stderr >&2"], verbose=False
    )
    # Assert
    assert "stderr" in result["stderr"]


# ---------------------------------------------------------------------------
# TestExecuteStreaming
# ---------------------------------------------------------------------------


def test_execute_streaming_mode_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["echo", "streaming test"], verbose=False, stream_output=True
    )
    # Assert
    assert result["success"] is True


def test_execute_streaming_mode_captures_stdout_text():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["echo", "streaming test"], verbose=False, stream_output=True
    )
    # Assert
    assert "streaming test" in result["stdout"]


def test_execute_streaming_multiline_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["printf", "line1\nline2\nline3"],
        verbose=False,
        stream_output=True,
    )
    # Assert
    assert result["success"] is True


def test_execute_streaming_multiline_captures_first_line():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["printf", "line1\nline2\nline3"],
        verbose=False,
        stream_output=True,
    )
    # Assert
    assert "line1" in result["stdout"]


def test_execute_streaming_multiline_captures_second_line():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["printf", "line1\nline2\nline3"],
        verbose=False,
        stream_output=True,
    )
    # Assert
    assert "line2" in result["stdout"]


def test_execute_streaming_multiline_captures_third_line():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["printf", "line1\nline2\nline3"],
        verbose=False,
        stream_output=True,
    )
    # Assert
    assert "line3" in result["stdout"]


def test_execute_streaming_with_timeout_returns_success_false():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(
        ["sleep", "5"], verbose=False, stream_output=True, timeout=1
    )
    # Assert
    assert result["success"] is False


# ---------------------------------------------------------------------------
# TestExecuteVerbose
# ---------------------------------------------------------------------------


def test_execute_verbose_false_runs_without_error(capsys):
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "silent"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_verbose_true_prints_visible_text_to_stdout(capsys):
    # Arrange
    from scitex_sh._execute import execute
    # Act
    execute(["echo", "visible"], verbose=True)
    captured = capsys.readouterr()
    # Assert
    assert "visible" in captured.out or "echo" in captured.out


# ---------------------------------------------------------------------------
# TestExecuteWithFiles
# ---------------------------------------------------------------------------


def test_execute_cat_temp_file_returns_success_true(tmp_path):
    # Arrange
    from scitex_sh._execute import execute
    test_file = tmp_path / "test.txt"
    test_file.write_text("file content")
    # Act
    result = execute(["cat", str(test_file)], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_cat_temp_file_returns_file_contents_on_stdout(tmp_path):
    # Arrange
    from scitex_sh._execute import execute
    test_file = tmp_path / "test.txt"
    test_file.write_text("file content")
    # Act
    result = execute(["cat", str(test_file)], verbose=False)
    # Assert
    assert result["stdout"] == "file content"


def test_execute_wc_word_count_returns_success_true(tmp_path):
    # Arrange
    from scitex_sh._execute import execute
    test_file = tmp_path / "test.txt"
    test_file.write_text("one two three\nfour five")
    # Act
    result = execute(["wc", "-w", str(test_file)], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_wc_word_count_reports_five_words_in_stdout(tmp_path):
    # Arrange
    from scitex_sh._execute import execute
    test_file = tmp_path / "test.txt"
    test_file.write_text("one two three\nfour five")
    # Act
    result = execute(["wc", "-w", str(test_file)], verbose=False)
    # Assert
    assert "5" in result["stdout"]


def test_execute_touch_command_returns_success_true(tmp_path):
    # Arrange
    from scitex_sh._execute import execute
    new_file = tmp_path / "newfile.txt"
    # Act
    result = execute(["touch", str(new_file)], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_touch_command_creates_target_file_on_disk(tmp_path):
    # Arrange
    from scitex_sh._execute import execute
    new_file = tmp_path / "newfile.txt"
    # Act
    execute(["touch", str(new_file)], verbose=False)
    # Assert
    assert new_file.exists()


# ---------------------------------------------------------------------------
# TestExecuteSpecialCharacters
# ---------------------------------------------------------------------------


def test_execute_echo_spaces_in_argument_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello world"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_echo_spaces_in_argument_preserves_text_on_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "hello world"], verbose=False)
    # Assert
    assert result["stdout"] == "hello world"


def test_execute_shell_metachar_argument_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test; echo foo"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_shell_metachar_argument_treated_as_literal_text():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", "test; echo foo"], verbose=False)
    # Assert
    assert "test; echo foo" in result["stdout"]


def test_execute_quoted_substring_argument_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", 'say "hello"'], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_quoted_substring_argument_preserves_quotes_in_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", 'say "hello"'], verbose=False)
    # Assert
    assert '"hello"' in result["stdout"]


# ---------------------------------------------------------------------------
# TestExecuteEnvironment
# ---------------------------------------------------------------------------


def test_execute_inherits_home_env_var_with_success():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "echo $HOME"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_inherits_home_env_var_with_non_empty_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "echo $HOME"], verbose=False)
    # Assert
    assert len(result["stdout"]) > 0


def test_execute_can_invoke_path_lookup_with_success():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["which", "ls"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_which_ls_returns_ls_substring_in_stdout():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["which", "ls"], verbose=False)
    # Assert
    assert "ls" in result["stdout"]


# ---------------------------------------------------------------------------
# TestExecuteExitCodes
# ---------------------------------------------------------------------------


def test_execute_bash_exit_zero_returns_exit_code_zero():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "exit 0"], verbose=False)
    # Assert
    assert result["exit_code"] == 0


def test_execute_bash_exit_zero_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "exit 0"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_bash_exit_one_returns_exit_code_one():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "exit 1"], verbose=False)
    # Assert
    assert result["exit_code"] == 1


def test_execute_bash_exit_one_returns_success_false():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "exit 1"], verbose=False)
    # Assert
    assert result["success"] is False


def test_execute_bash_exit_custom_returns_exit_code_forty_two():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "exit 42"], verbose=False)
    # Assert
    assert result["exit_code"] == 42


def test_execute_bash_exit_custom_returns_success_false():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["bash", "-c", "exit 42"], verbose=False)
    # Assert
    assert result["success"] is False


# ---------------------------------------------------------------------------
# TestBufferedExecution
# ---------------------------------------------------------------------------


def test_execute_buffered_function_is_not_none_after_import():
    # Arrange
    from scitex_sh._execute import _execute_buffered
    # Act
    fn = _execute_buffered
    # Assert
    assert fn is not None


def test_execute_buffered_function_is_callable_after_import():
    # Arrange
    from scitex_sh._execute import _execute_buffered
    # Act
    is_callable = callable(_execute_buffered)
    # Assert
    assert is_callable is True


def test_execute_buffered_echo_returns_success_true():
    # Arrange
    from scitex_sh._execute import _execute_buffered
    # Act
    result = _execute_buffered(["echo", "test"], verbose=False, timeout=None)
    # Assert
    assert result["success"] is True


def test_execute_buffered_echo_returns_test_on_stdout():
    # Arrange
    from scitex_sh._execute import _execute_buffered
    # Act
    result = _execute_buffered(["echo", "test"], verbose=False, timeout=None)
    # Assert
    assert result["stdout"] == "test"


# ---------------------------------------------------------------------------
# TestStreamingExecution
# ---------------------------------------------------------------------------


def test_execute_with_streaming_function_is_not_none_after_import():
    # Arrange
    from scitex_sh._execute import _execute_with_streaming
    # Act
    fn = _execute_with_streaming
    # Assert
    assert fn is not None


def test_execute_with_streaming_function_is_callable_after_import():
    # Arrange
    from scitex_sh._execute import _execute_with_streaming
    # Act
    is_callable = callable(_execute_with_streaming)
    # Assert
    assert is_callable is True


def test_execute_with_streaming_echo_returns_success_true():
    # Arrange
    from scitex_sh._execute import _execute_with_streaming
    # Act
    result = _execute_with_streaming(
        ["echo", "streaming"], verbose=False, timeout=None
    )
    # Assert
    assert result["success"] is True


def test_execute_with_streaming_echo_captures_stdout_text():
    # Arrange
    from scitex_sh._execute import _execute_with_streaming
    # Act
    result = _execute_with_streaming(
        ["echo", "streaming"], verbose=False, timeout=None
    )
    # Assert
    assert "streaming" in result["stdout"]


# ---------------------------------------------------------------------------
# TestExecuteRobustness
# ---------------------------------------------------------------------------


def test_execute_seq_one_to_thousand_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["seq", "1", "1000"], verbose=False)
    # Assert
    assert result["success"] is True


def test_execute_seq_one_to_thousand_returns_thousand_lines():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["seq", "1", "1000"], verbose=False)
    # Assert
    assert len(result["stdout"].split("\n")) == 1000


@pytest.mark.parametrize("index", list(range(10)))
def test_execute_echo_in_rapid_succession_returns_success_true(index):
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", str(index)], verbose=False)
    # Assert
    assert result["success"] is True


@pytest.mark.parametrize("index", list(range(10)))
def test_execute_echo_in_rapid_succession_preserves_argument_on_stdout(index):
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", str(index)], verbose=False)
    # Assert
    assert result["stdout"] == str(index)


def test_execute_echo_with_empty_string_argument_returns_success_true():
    # Arrange
    from scitex_sh._execute import execute
    # Act
    result = execute(["echo", ""], verbose=False)
    # Assert
    assert result["success"] is True


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# EOF
