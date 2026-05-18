#!/usr/bin/env python3
# Timestamp: "2026-05-18 (ywatanabe)"
# File: tests/scitex_sh/test__security.py

"""Tests for shell command security functions.

This module tests the security functionality of the sh module:
- validate_command: Validates commands for security issues
- quote: Safely quotes arguments for shell use
- DANGEROUS_CHARS: List of dangerous shell characters
"""

import pytest


# ---------------------------------------------------------------------------
# TestValidateCommandBasic
# ---------------------------------------------------------------------------


def test_validate_command_function_is_not_none_after_import():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    fn = validate_command
    # Assert
    assert fn is not None


def test_validate_command_function_is_callable_after_import():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    is_callable = callable(validate_command)
    # Assert
    assert is_callable is True


def test_validate_command_accepts_ls_flag_list_without_raising():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["ls", "-la"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_echo_arg_list_without_raising():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "hello"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_single_pwd_list_without_raising():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["pwd"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_raises_typeerror_for_string_input():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(TypeError)
    # Assert
    with ctx:
        validate_command("ls -la")


def test_validate_command_typeerror_message_mentions_string_not_allowed():
    # Arrange
    from scitex_sh._security import validate_command
    message = ""
    # Act
    try:
        validate_command("ls -la")
    except TypeError as exc:
        message = str(exc)
    # Assert
    assert "String commands are not allowed" in message


def test_validate_command_typeerror_message_mentions_security_reasons():
    # Arrange
    from scitex_sh._security import validate_command
    message = ""
    # Act
    try:
        validate_command("ls -la")
    except TypeError as exc:
        message = str(exc)
    # Assert
    assert "security reasons" in message


def test_validate_command_rejects_string_with_pipe_metachar():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(TypeError)
    # Assert
    with ctx:
        validate_command("ls | grep test")


def test_validate_command_rejects_string_with_semicolon_metachar():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(TypeError)
    # Assert
    with ctx:
        validate_command("ls; rm -rf /")


# ---------------------------------------------------------------------------
# TestValidateCommandNullByte
# ---------------------------------------------------------------------------


def test_validate_command_raises_valueerror_for_null_byte_in_argument():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(ValueError)
    # Assert
    with ctx:
        validate_command(["echo", "test\0malicious"])


def test_validate_command_null_byte_error_message_mentions_null_byte():
    # Arrange
    from scitex_sh._security import validate_command
    message = ""
    # Act
    try:
        validate_command(["echo", "test\0malicious"])
    except ValueError as exc:
        message = str(exc)
    # Assert
    assert "null byte" in message


def test_validate_command_null_byte_error_message_mentions_shell_injection():
    # Arrange
    from scitex_sh._security import validate_command
    message = ""
    # Act
    try:
        validate_command(["echo", "test\0malicious"])
    except ValueError as exc:
        message = str(exc)
    # Assert
    assert "shell injection" in message


def test_validate_command_raises_valueerror_for_null_byte_in_command_name():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(ValueError)
    # Assert
    with ctx:
        validate_command(["ls\0", "-la"])


def test_validate_command_raises_valueerror_for_null_byte_at_argument_start():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(ValueError)
    # Assert
    with ctx:
        validate_command(["echo", "\0malicious"])


def test_validate_command_raises_valueerror_for_null_byte_at_argument_end():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(ValueError)
    # Assert
    with ctx:
        validate_command(["echo", "test\0"])


def test_validate_command_raises_valueerror_for_multiple_null_bytes_in_argument():
    # Arrange
    from scitex_sh._security import validate_command
    # Act
    ctx = pytest.raises(ValueError)
    # Assert
    with ctx:
        validate_command(["echo", "a\0b\0c"])


# ---------------------------------------------------------------------------
# TestValidateCommandValidCases
# ---------------------------------------------------------------------------


def test_validate_command_accepts_simple_single_word_command():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["ls"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_command_with_short_and_long_flags():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["ls", "-la", "--color=auto"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_command_with_absolute_path_argument():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["cat", "/etc/passwd"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_command_with_user_home_subpath_argument():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["ls", "/home/user/Documents"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_argument_with_internal_spaces():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "Hello World"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_filename_argument_with_spaces():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["touch", "file with spaces.txt"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_semicolon_as_literal_argument_text():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "test; rm -rf /"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_pipe_as_literal_argument_text():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "test | grep foo"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_logical_and_as_literal_argument_text():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "test && echo bar"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_japanese_unicode_argument():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "日本語"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_cyrillic_unicode_argument():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "Привет мир"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_empty_string_argument():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", ""]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


# ---------------------------------------------------------------------------
# TestQuoteFunction
# ---------------------------------------------------------------------------


def test_quote_function_is_not_none_after_import():
    # Arrange
    from scitex_sh._security import quote
    # Act
    fn = quote
    # Assert
    assert fn is not None


def test_quote_function_is_callable_after_import():
    # Arrange
    from scitex_sh._security import quote
    # Act
    is_callable = callable(quote)
    # Assert
    assert is_callable is True


def test_quote_simple_word_returns_unquoted_or_singly_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("hello")
    # Assert
    assert result == "hello" or result == "'hello'"


def test_quote_string_with_spaces_wraps_value_in_single_quotes():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("hello world")
    # Assert
    assert result == "'hello world'"


def test_quote_dangerous_string_with_semicolon_returns_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    dangerous = "file; rm -rf /"
    # Act
    result = quote(dangerous)
    # Assert
    assert "'" in result


def test_quote_dangerous_string_with_semicolon_differs_from_input():
    # Arrange
    from scitex_sh._security import quote
    dangerous = "file; rm -rf /"
    # Act
    result = quote(dangerous)
    # Assert
    assert result != dangerous


def test_quote_string_with_inline_semicolon_returns_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("test;command")
    # Assert
    assert "'" in result


def test_quote_string_with_inline_pipe_returns_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("test|command")
    # Assert
    assert "'" in result


def test_quote_string_with_inline_ampersand_returns_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("test&command")
    # Assert
    assert "'" in result


def test_quote_string_with_dollar_sign_returns_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("$HOME")
    # Assert
    assert "'" in result


def test_quote_string_with_backtick_returns_quoted_form():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("`whoami`")
    # Assert
    assert "'" in result


def test_quote_empty_string_returns_pair_of_single_quotes():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("")
    # Assert
    assert result == "''"


def test_quote_string_with_single_quote_preserves_leading_text():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("it's a test")
    # Assert
    assert "it" in result


def test_quote_string_with_single_quote_preserves_trailing_text():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("it's a test")
    # Assert
    assert "a test" in result


def test_quote_string_with_double_quotes_preserves_inner_word():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote('say "hello"')
    # Assert
    assert "hello" in result


def test_quote_round_trips_through_shlex_split_to_original():
    # Arrange
    import shlex
    from scitex_sh._security import quote
    original = "test data 123"
    # Act
    unquoted = shlex.split(quote(original))[0]
    # Assert
    assert unquoted == original


def test_quote_string_with_newline_returns_quoted_or_literal_newline():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("line1\nline2")
    # Assert
    assert "\n" in result or "'" in result


def test_quote_string_with_tab_returns_quoted_or_literal_tab():
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote("col1\tcol2")
    # Assert
    assert "\t" in result or "'" in result


# ---------------------------------------------------------------------------
# TestDangerousChars
# ---------------------------------------------------------------------------


def test_dangerous_chars_constant_is_not_none_after_import():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    value = DANGEROUS_CHARS
    # Assert
    assert value is not None


def test_dangerous_chars_constant_is_a_python_list_instance():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    value = DANGEROUS_CHARS
    # Assert
    assert isinstance(value, list)


def test_dangerous_chars_list_contains_semicolon_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert ";" in members


def test_dangerous_chars_list_contains_pipe_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "|" in members


def test_dangerous_chars_list_contains_ampersand_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "&" in members


def test_dangerous_chars_list_contains_dollar_sign_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "$" in members


def test_dangerous_chars_list_contains_backtick_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "`" in members


def test_dangerous_chars_list_contains_newline_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "\n" in members


def test_dangerous_chars_list_contains_greater_than_redirect():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert ">" in members


def test_dangerous_chars_list_contains_less_than_redirect():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "<" in members


def test_dangerous_chars_list_contains_left_parenthesis_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "(" in members


def test_dangerous_chars_list_contains_right_parenthesis_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert ")" in members


def test_dangerous_chars_list_contains_left_brace_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "{" in members


def test_dangerous_chars_list_contains_right_brace_metachar():
    # Arrange
    from scitex_sh._security import DANGEROUS_CHARS
    # Act
    members = DANGEROUS_CHARS
    # Assert
    assert "}" in members


# ---------------------------------------------------------------------------
# TestSecurityIntegration
# ---------------------------------------------------------------------------


@pytest.fixture
def dangerous_chars_list():
    from scitex_sh._security import DANGEROUS_CHARS
    return DANGEROUS_CHARS


@pytest.mark.parametrize(
    "char",
    [";", "|", "&", "$", "`", "\n", ">", "<", "(", ")", "{", "}"],
)
def test_quote_wraps_dangerous_metachar_input_in_single_quotes(char):
    # Arrange
    from scitex_sh._security import quote
    dangerous_str = f"test{char}malicious"
    # Act
    quoted = quote(dangerous_str)
    # Assert
    assert "'" in quoted


def test_validate_command_accepts_argument_with_semicolon_in_list_form():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "test; rm -rf /"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_argument_with_dollar_subshell_in_list_form():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo", "$(whoami)"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_accepts_argument_with_backtick_subshell_in_list_form():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["cat", "file`id`"]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_string_error_mentions_list_format_alternative():
    # Arrange
    from scitex_sh._security import validate_command
    message = ""
    # Act
    try:
        validate_command("ls -la")
    except TypeError as exc:
        message = str(exc)
    # Assert
    assert "list" in message.lower()


def test_validate_command_string_error_mentions_security_topic():
    # Arrange
    from scitex_sh._security import validate_command
    message = ""
    # Act
    try:
        validate_command("ls -la")
    except TypeError as exc:
        message = str(exc)
    # Assert
    assert "security" in message.lower()


# ---------------------------------------------------------------------------
# TestEdgeCases
# ---------------------------------------------------------------------------


def test_validate_command_accepts_thousand_argument_command_list():
    # Arrange
    from scitex_sh._security import validate_command
    cmd = ["echo"] + [f"arg{i}" for i in range(1000)]
    # Act
    result = validate_command(cmd)
    # Assert
    assert result is None


def test_validate_command_handles_empty_list_without_typeerror():
    # Arrange
    from scitex_sh._security import validate_command
    raised_type_error = False
    # Act
    try:
        validate_command([])
    except TypeError:
        raised_type_error = True
    except (ValueError, IndexError):
        pass
    # Assert
    assert raised_type_error is False


def test_quote_very_long_string_returns_value_at_least_as_long_as_input():
    # Arrange
    from scitex_sh._security import quote
    long_str = "a" * 10000
    # Act
    result = quote(long_str)
    # Assert
    assert len(result) >= len(long_str)


@pytest.mark.parametrize(
    "value",
    ["日本語", "Ñoño", "émoji 🎉", "αβγ", "中文测试"],
)
def test_quote_unicode_value_returns_string_containing_original_or_single_quote(
    value,
):
    # Arrange
    from scitex_sh._security import quote
    # Act
    result = quote(value)
    # Assert
    assert value in result or "'" in result


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])

# EOF
