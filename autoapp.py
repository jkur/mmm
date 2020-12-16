import click
from mmm.factory import create_app
from mmm import db
from mmm.models import Account, Role, Domain
from mmm.services import pwd_context

application = create_app(settings_override='mmm.config.Development', static_folder='../static')

@application.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')
    db.create_all()
    db.session.commit()
    with application.app_context():
        if not Account.query.filter(Account.username == 'admin').first():
            domain = Domain(
                name = "postly.de"
            )

            account = Account(
                username = 'admin',
                # password='hallo15'
                password = pwd_context.hash('hallo15'),
                domain = domain
            )
            account.roles.append(Role(name='Admin'))
            db.session.add(domain)
            db.session.add(account)
            db.session.commit()
            print("Added ADmin User!")


@application.cli.command()
@click.confirmation_option('--yes', is_flag=True, expose_value=False, prompt='Do you want to continue?')
def dropdb():
    """Initialize the database."""
    click.echo('Dropping the db')
    db.drop_all()
