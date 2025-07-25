import os
import pytest
from sandyie_read.readers.txt_reader import read_txt
from sandyie_read.exceptions import SandyieException

def test_read_txt_success(tmp_path):
    test_file = tmp_path / "sample.txt"
    content = "Hello, this is a test file."
    test_file.write_text(content)

    result = read_txt(str(test_file))
    assert result == content

def test_read_txt_file_not_found():
    with pytest.raises(SandyieException) as exc_info:
        read_txt("non_existent.txt")
    assert "Text file not found" in str(exc_info.value)

def test_read_txt_invalid_file(tmp_path):
    invalid_file = tmp_path / "sample.txt"
    invalid_file.write_bytes(b'\x80\x81')  # invalid utf-8

    with pytest.raises(SandyieException) as exc_info:
        read_txt(str(invalid_file))
    assert "Failed to read TXT file" in str(exc_info.value)
