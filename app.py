import streamlit as st
import random
import time

st.set_page_config(
    page_title="가위바위보 게임",
    layout="wide"
)

# ------------------------
# Session State
# ------------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

if "score" not in st.session_state:
    st.session_state.score = 0

if "computer" not in st.session_state:
    st.session_state.computer = "❔"

if "result" not in st.session_state:
    st.session_state.result = ""

# ------------------------
# CSS
# ------------------------
st.markdown("""
<style>

.stApp{
    background-color:#F5F7FA;
}

.title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#222;
    margin-top:130px;
}

.score{
    font-size:28px;
    font-weight:bold;
    color:#222;
}

.computer{
    text-align:center;
    font-size:120px;
}

.result{
    text-align:center;
    font-size:35px;
    font-weight:bold;
    color:#222;
}

div.stButton > button{
    width:100%;
    background:white;
    color:black;
    font-size:22px;
    font-weight:bold;
    border-radius:15px;
    border:none;
    padding:12px;
    transition:0.3s;
}

div.stButton > button:hover{
    background:#E8ECF5;
}

</style>
""", unsafe_allow_html=True)

emoji = {
    "바위":"✊",
    "가위":"✌️",
    "보":"✋"
}

choices = list(emoji.keys())

# ------------------------
# 게임 함수
# ------------------------
def play(user):

    thinking = st.empty()

    thinking.markdown(
        "<h1 style='text-align:center;'>🤔 컴퓨터가 생각 중...</h1>",
        unsafe_allow_html=True
    )

    time.sleep(1)

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

    thinking.empty()

# ------------------------
# 메인 화면
# ------------------------
if st.session_state.page == "main":

    st.markdown(
        """
        <div class="title">
        🎮 가위바위보 게임
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    left, center, right = st.columns([2,1,2])

    with center:
        if st.button("시작하기", use_container_width=True):
            st.session_state.page="game"
            st.session_state.score=0
            st.session_state.computer="❔"
            st.session_state.result=""
            st.rerun()

# ------------------------
# 게임 화면
# ------------------------
else:

    left,right = st.columns([1,1])

    with left:
        st.markdown(
            f'<div class="score">⭐ Score : {st.session_state.score}</div>',
            unsafe_allow_html=True
        )

    with right:

        a,b = st.columns([2,1])

        with b:

            if st.button("끝내기"):
                st.session_state.page="main"
                st.session_state.score=0
                st.session_state.computer="❔"
                st.session_state.result=""
                st.rerun()

    st.write("")
    st.write("")
    # 컴퓨터 선택 표시
    st.markdown(
        f'<div class="computer">{st.session_state.computer}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # 결과 표시
    st.markdown(
        f'<div class="result">{st.session_state.result}</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # 사용자 선택 버튼 (하단)
    left, center = st.columns([1, 8])

    with center:

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

    st.write("")
    st.write("")

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#888;
            font-size:18px;">
            버튼을 눌러 계속 플레이하세요!
        </div>
        """,
        unsafe_allow_html=True
    )
