from analyze.matcher import Matcher
from analyze.normalize import Normalize
from utils.file_usage import FileUsage
from utils.json_commands import read_json
from analyze.error import MatchError


class Commands:
    def __init__(self, command):
        self.data_file_util = FileUsage('./data_files')
        self.command = Normalize(command)()
        self.standart_commands = {'list': self.list_commands}
        self.commands = self.standart_commands | {name_com: MethExecute(file_data, self.read_data_file)
                                                  for name_com, file_data in read_json().items()}

    def found_command(self):
        for name_com, com in self.commands.items():
            if Matcher(a=self.command, b=name_com).match():
                return name_com, com()
        raise MatchError('Command not found')

    def list_commands(self):
        commands = ''
        for name_com in self.commands.keys():
            commands += f"Command name: {name_com}\n"
        return commands

    def read_data_file(self, file_name):
        return self.data_file_util.read_file(file_name)


class MethExecute:
    def __init__(self, file_name: str, read_meth):
        self.read_meth = read_meth
        self.file_name = file_name

    def __call__(self, *args, **kwargs):
        return self.read_meth(self.file_name)