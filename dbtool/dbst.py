from databricks import sql
import os


def querydb(query="SELECT * FROM default.diamonds LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DBS_HOST"),
        http_path=os.getenv("DBS_HTTP_PATH"),
        access_token=os.getenv("DBS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS money (code string, people string, target string, amount float)"
            )
            cursor.execute(query)
            result = cursor.fetchall()

    return result


def checkData(code):
    return querydb('SELECT * FROM money where code="{code}"'.format(code=code))


def insertData(code, name, target, amount):
    with sql.connect(
        server_hostname=os.getenv("DBS_HOST"),
        http_path=os.getenv("DBS_HTTP_PATH"),
        access_token=os.getenv("DBS_TOKEN"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS money (code string, people string, target string, amount DECIMAL(5,2))"
            )
            values = ",".join(
                ['"' + key + '"' for key in [code, name, target]] + [str(amount)]
            )
            cursor.execute(
                f"INSERT INTO money (code, people, target, amount) VALUES ({values})"
            )


if __name__ == "__main__":
    insertData("ff6db9b0", "yifan", "all", 100.2)
