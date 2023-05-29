import os
from typing import Union
import uvicorn
from fastapi import Depends, FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import user, administrator, auth, departamento, conserje
from api.dependencies import get_current_user
from data.models import Administrator, Conserje
from schemas.administrator import Administrator as SCAdmin
from schemas.conserje import Conserje as SCCon

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.user_router)
app.include_router(administrator.administrator_router)
app.include_router(auth.auth_router)
app.include_router(departamento.departamento_router)
app.include_router(conserje.conserje_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Parking System API."}


@app.get("/me", response_model=Union[SCAdmin, SCCon], tags=["User"])
def get_me(user: Union[Administrator, Conserje] = Depends(get_current_user)):
    return user

if __name__ == "__main__":
    port = os.getenv("PORT", default=8000)
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
