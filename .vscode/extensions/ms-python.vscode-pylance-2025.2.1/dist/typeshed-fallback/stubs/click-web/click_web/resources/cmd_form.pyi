import click

def get_form_for(command_path: str) -> str: ...
def _get_commands_by_path(command_path: str) -> list[tuple[click.Context, click.Command]]: ...
def _generate_form_data(ctx_and_commands: list[tuple[click.Context, click.Command]]): ...
def _process_help(help_text: bool) -> str: ...
