import click
import shutil
from utils.json_commands import add_key_value_to_json, remove_key_from_json


@click.group()
def analyze_system_cli():
    pass


@click.command(name='del_command', help='Name commands, replace space on _')
@click.argument('key')
def delete_command(key):
    remove_key_from_json(key)
    click.echo(f'Command {key} been delete')


@click.command(name='add_command', help='Name command and file name data')
@click.option("--key", "-k", required=True, help="Name command, replace space on _")
@click.option("--value", "-v", required=True, help="File name in data_files folder")
def add_command(key, value):
    add_key_value_to_json(key, value)
    click.echo(f'Command {key} with file {value} been added')


@click.command(name='add_file', help='Path to folder that been added')
@click.argument('path')
def copy_file_to_folder(path):
    shutil.copy2(path, 'data_files')
    click.echo(f'File {path} been add')

analyze_system_cli.add_command(delete_command)
analyze_system_cli.add_command(add_command)
analyze_system_cli.add_command(copy_file_to_folder)

if __name__ == '__main__':
    analyze_system_cli()
