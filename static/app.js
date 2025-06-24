function editMemo(event) {
  console.log(event.target);
}

function displayMemo(memo) {
  console.log(memo);
  const ul = document.querySelector("#memo-ul");

  // 라인 태그 생성
  const li = document.createElement("li");
  li.innerText = `[id: ${memo.id}] ${memo.content}`;

  // 버튼 태그 생성
  // const editBtn = document.createElement("button");
  // editBtn.innerText = "수정하기";
  // editBtn.addEventListener("click", editMemo);
  // editBtn.dataset.id = memo.id;

  // li.appendChild(editBtn);
  ul.appendChild(li);
}

async function readMemo() {
  // 서버에서 배열 값 가져오기
  const res = await fetch("/memos");
  const resJson = await res.json();
  console.log(resJson);

  // ul 초기화
  const ul = document.querySelector("#memo-ul");
  ul.innerHTML = "";
  resJson.forEach(displayMemo);
}

async function createMemo(value) {
  // 입력 값을 서버에 전송하기
  const res = await fetch("/memos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: new Date().getTime(),
      content: value,
    }),
  });

  // 서버로부터의 응답 값을 출력하기
  const jsonRes = await res.json();
  readMemo();
}

function handleSubmit(event) {
  // submit에서 redirection 방지 코드
  event.preventDefault();
  //   console.log("제출!");

  const input = document.querySelector("#memo-input");
  createMemo(input.value);
}

const form = document.querySelector("#memo-form");
form.addEventListener("submit", handleSubmit);

readMemo();
