import pytest
from testing_pytest.file_manager import FileManager
from pathlib import Path

@pytest.fixture
def filemanager_setup(tmp_path):
    path = tmp_path
    filename = "sample.txt"
    return FileManager(), path, filename

def test_save_file(filemanager_setup):
    filemanager, path, filename = filemanager_setup
    filemanager.save_file(path, filename, content="Hello")

    #Did not use FileManager.read_file since there can be error in read_file (haven't tested yet) 
    assert (path/filename).read_text() == "Hello" 

def test_read_file(filemanager_setup):
    filemanager, path, filename = filemanager_setup
    filemanager.save_file(path, filename, content="Hello")
    assert filemanager.read_file(path/filename) == "Hello" 

def test_read_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="File does not exist"):
        FileManager().read_file(tmp_path/"abc.txt") 