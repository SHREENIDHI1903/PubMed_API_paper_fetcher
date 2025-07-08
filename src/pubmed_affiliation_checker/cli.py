# src/pubmed_affiliation_checker/cli.py

import click
import pandas as pd
from .fetch import fetch_and_filter

@click.command(
    help="Fetch PubMed papers based on a search query, identify non-academic authors affiliated with pharmaceutical/biotech companies using LLM, and export to CSV or console."
)
@click.argument("query", type=str)
@click.option(
    "-f", "--file",
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    help="Optional: File path to save output CSV. If not provided, results are printed to console."
)
@click.option(
    "-d", "--debug",
    is_flag=True,
    default=False,
    help="Enable debug mode. Prints detailed logs and LLM responses."
)
def main(query: str, file: str | None, debug: bool) -> None:
    """
    Command-line interface entry point.
    """
    try:
        results: pd.DataFrame = fetch_and_filter(query, debug=debug)
        if results.empty:
            click.secho("No results found with company-affiliated authors.", fg="yellow")
            return

        if file:
            results.to_csv(file, index=False)
            click.secho(f"✅ CSV saved to {file}", fg="green")
        else:
            click.echo(results.to_csv(index=False))
    
    except Exception as e:
        click.secho(f"❌ Unexpected error: {e}", fg="red")
