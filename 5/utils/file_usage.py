from pathlib import Path


class FileUsage:
    __slots__ = ('path', )

    def __init__(self, folder_path):
        self.path = Path(folder_path)

    def get_file_names(self):
        return [file.stem.lower() for file in self.path.iterdir() if file.is_file()]

    def read_file(self, name: str):
        update_name = name.capitalize() + '.txt'
        path_to_file = self.path / update_name
        return path_to_file.read_text(encoding='utf-8')
