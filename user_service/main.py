from fastapi import FastAPI
import routes, database

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(routes.router)



@app.get("/")
def health_check():
    return {"Health_check": "ok"}