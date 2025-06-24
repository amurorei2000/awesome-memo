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
    return memo

@app.get("/memos")
def get_memo():
    # return {"status": 200, "message": "success", "content": memos}
    return memos

@app.put("/memos/{id}")
def put_memo(newMemo: Memo):
    for memo in memos:
        if memo.id == newMemo.id:
            memo.content = newMemo.content
            return "수정 성공"
    return f"그런 아이디가 없습니다.: {newMemo.id}"

@app.delete("/memos/{id}")
def delete_memo(id):
    for i, memo in enumerate(memos):
        print(memo.id)
        if memo.id == int(id):
            memos.pop(i)
            return "삭제 성공"
    return f"그런 아이디가 없습니다.: {id}"

# html 마운트
app.mount("/", StaticFiles(directory='static', html=True), name='static')