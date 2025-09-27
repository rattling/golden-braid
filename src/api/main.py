from fastapi import FastAPI

app = FastAPI(title="Braid API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


# placeholder PGM endpoint
@app.get("/pgm/ping")
def pgm_ping():
    return {"message": "PGM placeholder"}
