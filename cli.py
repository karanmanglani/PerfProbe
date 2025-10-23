# This is the main entrypoint

import typer
import yaml

app = typer.Typer()

def load_config(config_file):
    with open(f"config/{config_file}.yaml","r") as f:
        return yaml.safe_load(f)
@app.command()
def run(
        url : str = None,
        users : int = None,
        rps : int = None,
        duration : int = None,
        report : str = None,
        config: str = "default"
):
    config = load_config(config)
    final_config = {
        "url" : url or config["url"],
        "users" : users or config["users"],
        "rps" : rps or config["rps"],
        "duration" : duration or config["duration"],
        "report" : report or config["report"]
    }
    for key,value in final_config.items():
        typer.echo(f"{key}: {value}")

if __name__ == "__main__":
    app()