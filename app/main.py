import uvicorn
from fastapi import FastAPI
from app.database.conn import db
from app.common.config import conf
from app.routes import index, auth

def create_app():
    """
    `create app`\n
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = c.dict()
    db.init_app(app, **conf_dict)
    # db init

    # redis init (session db)

    # middle_ware define

    # router define
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/auth")
    return app

app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
