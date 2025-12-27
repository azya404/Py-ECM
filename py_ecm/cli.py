'''CLI entry point for Py-ECM'''

from pathlib import Path
from typing import Optional
import typer

app = typer.Typer(name="py-ecm", help="Enterprise Content Manager - CLI for content lifecycle operations", add_completion=False,)

@app.command()
def version():
    """Display Py-ECM version."""
    from py_ecm import __version__
    typer.echo(f'Py-ECM v{__version__}')

@app.command()
def create(
    filename: str = typer.Argument(..., help='Name of file to create'),
    directory: Optional[str] = typer.Option(None, '--dir', '-d', help='Directory path (default: current directory)'),
    content: Optional[str] = typer.Option('', '--content', '-c', help='Initial file content'),) -> None:
    """Create a new file with optional content."""
    
    # Determine full path
    if directory:
        base_path = Path(directory)
        if not base_path.exists():
            typer.secho(
                f'ERROR\nDirectory does not exist: {directory}', 
                fg=typer.colors.RED, 
                err=True
            )
            raise typer.Exit(1)
        file_path = base_path / filename
    else:
        file_path = Path.cwd() / filename

    # Check if path/target is a directory
    if file_path.exists() and file_path.is_dir():
        typer.secho(
            f"ERROR\n'{filename}' is a directory",
            fg=typer.colors.RED, 
            err=True
        )
        raise typer.Exit(1)
    
    # Create file with error handling
    try:
        with open(file_path, 'x') as f:
            if content:
                f.write(content)
        
        typer.secho(
            f'File created successfully: {file_path}', 
            fg=typer.colors.GREEN
        )
        
    except FileExistsError:
        typer.secho(
            f'ERROR\nFile already exists: {file_path}',
            fg=typer.colors.RED,  
            err=True
        )
        raise typer.Exit(1)
        
    except PermissionError:
        typer.secho(
            f'ERROR\nPermission denied: {file_path}',  
            fg=typer.colors.RED,
            err=True
        )
        raise typer.Exit(1)
        
    except IsADirectoryError:
        typer.secho(
            f"ERROR\n'{filename}' is a directory name", 
            fg=typer.colors.RED,
            err=True
        )
        raise typer.Exit(1)
        
    except OSError as e:
        typer.secho(
            f'ERROR\nSystem error: {e}', 
            fg=typer.colors.RED,
            err=True
        )
        raise typer.Exit(1)

def main():
    """Main entry point."""
    app()


if __name__ == '__main__':
    main()
