from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles


class Memo(BaseModel):
    id: int
    content: str


app = FastAPI()

memos = []

@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    print(memo.id)
    print(memo.content)
    return {"status": 200,  "message": "success", "content": memos}

@app.get("/memos")
def get_memo():
    return {"status": 200, "message": "success", "content": memos}

# html 마운트
app.mount("/", StaticFiles(directory='static', html=True), name='static')