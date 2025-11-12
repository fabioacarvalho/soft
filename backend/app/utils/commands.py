# app/commands.py
import click
from flask.cli import with_appcontext
from app.models.core_model import User


@click.command("create-superadmin")
@with_appcontext
def create_superadmin():
    """Cria o usuário superadmin, caso não exista"""
    User.create_superadmin_if_not_exists()
    click.echo("Superadmin verificado/criado com sucesso!")