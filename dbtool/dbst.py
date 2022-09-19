from databricks import sql
import os


def querydb(query="SELECT * FROM default.diamonds LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DBS_HOST"),
        http_path=os.getenv("DBS_HTTP_PATH"),
        access_token=os.getenv("DBS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

if __name__ == "__main__":
    querydb()