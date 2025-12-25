'''CLI entry point for Py-ECM'''

import typer

app = typer.Typer(name="py-ecm", help="Enterprise Content Manager - CLI for content lifecycle operations", add_completion=False,)

@app.command()
def version():
    '''Display Py-ECM version.'''
    from py_ecm import __version__
    typer.echo(f"Py-ECM v{__version__}")


def main():
    '''Main entry point.'''
    app()


if __name__ == '__main__':
    main()
