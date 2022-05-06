import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', True)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 10605524))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', "a4ccc51331a895285a4c57ce10d49f95")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5257644826:AAHUlM4qDhsitRE6O3z0Leg2J96hXj2QMzI")
    DATABASE_URL = os.environ.get('DATABASE_URL', "postgres://zzlrfwmp:75B5tfrr7ocO6MOsfogvSPn2XmZccKIF@chunee.db.elephantsql.com/zzlrfwmp")
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', "bombleebas")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 10605524
    API_HASH = "a4ccc51331a895285a4c57ce10d49f95"
    BOT_TOKEN = "5257644826:AAHUlM4qDhsitRE6O3z0Leg2J96hXj2QMzI"
    DATABASE_URL = "postgres://zzlrfwmp:75B5tfrr7ocO6MOsfogvSPn2XmZccKIF@chunee.db.elephantsql.com/zzlrfwmp"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "bombleebas"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
