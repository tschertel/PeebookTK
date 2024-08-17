import configparser
#from os import getenv, path

config = configparser.ConfigParser()

# CONFIGFILE = path.join(getenv("LOCALAPPDATA"), "peebookrc")
CONFIGFILE = "peebookrc"


def save_config(header, session, value):
    config.set(header, session, value)
    with open(CONFIGFILE, "w", encoding="utf-8") as config_file:
        config.write(config_file)


def load_config(header, session):
    config.read(CONFIGFILE, encoding="utf-8")
    if not session:
        setting = config.items(header)
    else:
        setting = config.get(header, session)
    return setting
