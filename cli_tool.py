#!/usr/bin/env python
import click
from dbtool.dbst import querydb, checkData, beautify

@click.group()
def cli():
    '''CLI to query SQL database'''


@cli.command()
@click.option("--connect", default="SELECT * FROM default.diamonds LIMIT 2", help="check SQL connection from databricks")
def cli_connect(connect):
    '''
    Check if codebase is connected to databricks in Azure based on databricks default dataset diamonds
    '''
    res = querydb(connect)
    print(res)

@cli.command()
@click.option("--code", default="", help="query record based on code")
def cli_query(code):
    '''
    Query record based on code
    '''
    res = beautify(checkData(code))
    if not res: print("no record with code: "+ code) 
    else: print(res)

if __name__ == "__main__":
    cli()