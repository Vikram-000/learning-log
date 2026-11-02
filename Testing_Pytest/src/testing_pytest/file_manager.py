
from pathlib import Path


class FileManager:

    def save_file(self, directory: Path, filename: str, content: str):
        file_path = directory / filename
        file_path.write_text(content)
        return file_path

    def read_file(self, file_path: Path):
        if not file_path.exists():
            raise FileNotFoundError("File does not exist")

        return file_path.read_text()

    def delete_file(self, file_path: Path):
        if not file_path.exists():
            return False

        file_path.unlink()
        return True

    def file_exists(self, file_path: Path):
        return file_path.exists()
