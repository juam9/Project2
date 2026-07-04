import streamlit as st
import random

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(page_title="가위바위보 게임", layout="wide")

# session_state 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"

if "score" not in st.session_state:
    st.session_state.score = 0

if "computer" not in st.session_state:
    st.session_state.computer = "❔"

if "result" not in st.session_state:
    st.session_state.result = ""

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background-color:#0b1f4d;
}

/* 제목 */
.title{
    color:white;
    font-size:60px;
    font-weight:bold;
    text-align:center;
    margin-top:120px;
}

/* 컴퓨터 선택 */
.computer{
    color:white;
    font-size:100px;
    text-align:center;
}

/* 결과 */
.result{
    color:white;
    font-size:35px;
    text-align:center;
    font-weight:bold;
}

/* 버튼 */
div.stButton > button{
    width:100%;
    background:white;
    color:black;
    font-size:22px;
    font-weight:bold;
    border-radius:12px;
    border:none;
    padding:10px;
}

/* 점수 */
.score{
    color:white;
    font-size:28px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 승패 판정
# -----------------------------
emoji = {
    "바위":"✊",
    "가위":"✌️",
    "보":"✋"
}

choices = list(emoji.keys())

def play(user):

    computer = random.choice(choices)

    st.session_state.computer = emoji[computer]

    if user == computer:
        st.session_state.score += 1
        st.session_state.result = "😐 비겼습니다!"

    elif (
        (user=="가위" and computer=="보") or
        (user=="바위" and computer=="가위") or
        (user=="보" and computer=="바위")
    ):
        st.session_state.score += 2
        st.session_state.result = "😊 이겼습니다!"

    else:
        st.session_state.result = "😢 졌습니다!"

# -----------------------------
# 메인 화면
# -----------------------------
if st.session_state.page == "main":

    st.markdown(
        '<div class="title">가위바위보 게임</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    left, center, right = st.columns([2,1,2])

    with center:
        if st.button("시작하기", use_container_width=True):
            st.session_state.page = "game"
            st.session_state.score = 0
            st.session_state.computer = "❔"
            st.session_state.result = ""
            st.rerun()

# -----------------------------
# 게임 화면
# -----------------------------
else:

    left, right = st.columns([1,1])

    with left:
        st.markdown(
            f'<div class="score">⭐ Score : {st.session_state.score}</div>',
            unsafe_allow_html=True
        )

    with right:
        c1,c2 = st.columns([2,1])
        with c2:
            if st.button("끝내기"):
                st.session_state.page = "main"
                st.session_state.score = 0
                st.session_state.computer = "❔"
                st.session_state.result = ""
                st.rerun()

    st.write("")
    st.write("")
    st.write("")

    st.markdown(
        f'<div class="computer">{st.session_state.computer}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="result">{st.session_state.result}</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("✊ 바위", use_container_width=True):
            play("바위")
            st.rerun()

    with col2:
        if st.button("✌️ 가위", use_container_width=True):
            play("가위")
            st.rerun()

    with col3:
        if st.button("✋ 보", use_container_width=True):
            play("보")
            st.rerun()
