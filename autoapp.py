import click
from mmm.factory import create_app
from mmm import db


application = create_app(settings_override='mmm.config.Development', static_folder='../static')

@application.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')
    db.create_all()
    db.session.add(p)
    db.session.commit()


@application.cli.command()
@click.confirmation_option('--yes', is_flag=True, expose_value=False, prompt='Do you want to continue?')
def dropdb():
    """Initialize the database."""
    click.echo('Dropping the db')
    db.drop_all()
