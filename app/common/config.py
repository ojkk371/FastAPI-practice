from pydantic import BaseModel
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


class Config(BaseModel):
    """
    `General Configuration`\n
    """
    BASE_DIR = base_dir
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://travis@localhost/noti_api?charset=utf8mb4"


class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    """
    get_configuration\n
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))



if __name__ == "__main__":

    c = conf()
    import pdb;pdb.set_trace();
