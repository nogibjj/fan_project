#!/usr/bin/env python
import click
from dbtool.dbst import querydb

@click.group()
def cli():
    '''CLI to query SQL database'''


@cli.command()
@click.option("--query", default="SELECT * FROM default.diamonds LIMIT 2", help="SQL query data from databricks")
def query(q):
    '''
    Execute a SQL query
    '''
    querydb(q)

if __name__ == "__main__":
    cli()