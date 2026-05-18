#!/usr/bin/env python3
# Timestamp: "2026-05-18 (ywatanabe)"
# File: tests/scitex_sh/test__types.py

"""Tests for shell command type definitions.

This module tests the type definitions used in the sh module:
- ShellResult TypedDict for command execution results
- CommandInput type alias for command arguments
- ReturnFormat literal type for return format specification
"""

from typing import get_args, get_origin, get_type_hints


# ---------------------------------------------------------------------------
# TestShellResult
# ---------------------------------------------------------------------------


def test_shell_result_class_is_not_none_after_import():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    value = ShellResult
    # Assert
    assert value is not None


def test_shell_result_typeddict_exposes_annotations_attribute():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    has_annotations = hasattr(ShellResult, "__annotations__")
    # Assert
    assert has_annotations is True


def test_shell_result_annotations_include_stdout_key():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    annotations = ShellResult.__annotations__
    # Assert
    assert "stdout" in annotations


def test_shell_result_annotations_include_stderr_key():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    annotations = ShellResult.__annotations__
    # Assert
    assert "stderr" in annotations


def test_shell_result_annotations_include_exit_code_key():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    annotations = ShellResult.__annotations__
    # Assert
    assert "exit_code" in annotations


def test_shell_result_annotations_include_success_key():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    annotations = ShellResult.__annotations__
    # Assert
    assert "success" in annotations


def test_shell_result_stdout_field_resolves_to_str_type():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    hints = get_type_hints(ShellResult)
    # Assert
    assert hints["stdout"] is str


def test_shell_result_stderr_field_resolves_to_str_type():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    hints = get_type_hints(ShellResult)
    # Assert
    assert hints["stderr"] is str


def test_shell_result_exit_code_field_resolves_to_int_type():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    hints = get_type_hints(ShellResult)
    # Assert
    assert hints["exit_code"] is int


def test_shell_result_success_field_resolves_to_bool_type():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    hints = get_type_hints(ShellResult)
    # Assert
    assert hints["success"] is bool


def test_shell_result_instance_preserves_stdout_value():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "output text",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["stdout"] == "output text"


def test_shell_result_instance_preserves_empty_stderr_value():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "output text",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["stderr"] == ""


def test_shell_result_instance_preserves_exit_code_value():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "output text",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["exit_code"] == 0


def test_shell_result_instance_preserves_success_boolean_value():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "output text",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["success"] is True


def test_shell_result_for_successful_command_has_success_true():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "Hello World",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["success"] is True


def test_shell_result_for_successful_command_has_exit_code_zero():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "Hello World",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["exit_code"] == 0


def test_shell_result_for_failed_command_has_success_false():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "",
        "stderr": "File not found",
        "exit_code": 1,
        "success": False,
    }
    # Assert
    assert result["success"] is False


def test_shell_result_for_failed_command_has_exit_code_one():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "",
        "stderr": "File not found",
        "exit_code": 1,
        "success": False,
    }
    # Assert
    assert result["exit_code"] == 1


def test_shell_result_for_failed_command_preserves_stderr_message():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "",
        "stderr": "File not found",
        "exit_code": 1,
        "success": False,
    }
    # Assert
    assert "File not found" in result["stderr"]


def test_shell_result_multiline_stdout_preserves_newline_count():
    # Arrange
    from scitex_sh._types import ShellResult
    multiline_output = "line1\nline2\nline3"
    # Act
    result: ShellResult = {
        "stdout": multiline_output,
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["stdout"].count("\n") == 2


def test_shell_result_unicode_stdout_preserves_exact_content():
    # Arrange
    from scitex_sh._types import ShellResult
    unicode_output = "日本語テスト 中文测试 한국어테스트"
    # Act
    result: ShellResult = {
        "stdout": unicode_output,
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert result["stdout"] == unicode_output


# ---------------------------------------------------------------------------
# TestCommandInput
# ---------------------------------------------------------------------------


def test_command_input_type_alias_is_not_none_after_import():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    value = CommandInput
    # Assert
    assert value is not None


def test_command_input_type_alias_has_list_origin():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    origin = get_origin(CommandInput)
    # Assert
    assert origin is list


def test_command_input_type_alias_has_str_type_argument():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    args = get_args(CommandInput)
    # Assert
    assert args == (str,)


def test_command_input_valid_ls_flag_list_is_list_instance():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["ls", "-la"]
    # Assert
    assert isinstance(cmd, list)


def test_command_input_valid_ls_flag_list_has_all_string_items():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["ls", "-la"]
    # Assert
    assert all(isinstance(arg, str) for arg in cmd)


def test_command_input_valid_echo_two_word_list_is_list_instance():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["echo", "Hello World"]
    # Assert
    assert isinstance(cmd, list)


def test_command_input_valid_git_commit_message_list_is_list_instance():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["git", "commit", "-m", "message"]
    # Assert
    assert isinstance(cmd, list)


def test_command_input_valid_python_inline_script_list_is_list_instance():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["python", "-c", 'print("test")']
    # Assert
    assert isinstance(cmd, list)


def test_command_input_single_command_list_has_length_one():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["pwd"]
    # Assert
    assert len(cmd) == 1


def test_command_input_single_command_list_holds_pwd_at_index_zero():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    cmd: CommandInput = ["pwd"]
    # Assert
    assert cmd[0] == "pwd"


# ---------------------------------------------------------------------------
# TestReturnFormat
# ---------------------------------------------------------------------------


def test_return_format_type_alias_is_not_none_after_import():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    value = ReturnFormat
    # Assert
    assert value is not None


def test_return_format_type_alias_origin_is_literal():
    # Arrange
    from typing import Literal
    from scitex_sh._types import ReturnFormat
    # Act
    origin = get_origin(ReturnFormat)
    # Assert
    assert origin is Literal


def test_return_format_type_alias_contains_dict_literal_value():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    allowed = get_args(ReturnFormat)
    # Assert
    assert "dict" in allowed


def test_return_format_type_alias_contains_str_literal_value():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    allowed = get_args(ReturnFormat)
    # Assert
    assert "str" in allowed


def test_return_format_type_alias_allows_exactly_two_values():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    allowed = get_args(ReturnFormat)
    # Assert
    assert len(allowed) == 2


def test_return_format_assignment_to_dict_preserves_literal_value():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    format_type: ReturnFormat = "dict"
    # Assert
    assert format_type == "dict"


def test_return_format_assignment_to_str_preserves_literal_value():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    format_type: ReturnFormat = "str"
    # Assert
    assert format_type == "str"


# ---------------------------------------------------------------------------
# TestModuleExports
# ---------------------------------------------------------------------------


def test_shell_result_export_is_not_none_from_types_module():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    value = ShellResult
    # Assert
    assert value is not None


def test_command_input_export_is_not_none_from_types_module():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    value = CommandInput
    # Assert
    assert value is not None


def test_return_format_export_is_not_none_from_types_module():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    value = ReturnFormat
    # Assert
    assert value is not None


def test_command_input_assignment_in_consistency_scenario_is_list():
    # Arrange
    from scitex_sh._types import CommandInput
    # Act
    command: CommandInput = ["echo", "test"]
    # Assert
    assert isinstance(command, list)


def test_return_format_assignment_in_consistency_scenario_is_allowed_value():
    # Arrange
    from scitex_sh._types import ReturnFormat
    # Act
    return_format: ReturnFormat = "dict"
    # Assert
    assert return_format in ("dict", "str")


def test_shell_result_assignment_in_consistency_scenario_is_dict_instance():
    # Arrange
    from scitex_sh._types import ShellResult
    # Act
    result: ShellResult = {
        "stdout": "test",
        "stderr": "",
        "exit_code": 0,
        "success": True,
    }
    # Assert
    assert isinstance(result, dict)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# EOF
