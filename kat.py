import streamlit as st
import random
import requests

st.set_page_config(page_title="고양이 한 마디", page_icon="🐱", layout="centered")

st.title("🐱 랜덤 고양이 + 명언")
st.caption("귀여운 고양이와 함께 오늘 하루도 힘내요!")

# 명언 리스트
quotes = [
    "작은 고양이도 큰 사자의 마음을 가질 수 있다.",
    "오늘도 너는 충분히 잘하고 있어!",
    "고양이처럼 느긋하게, 인생을 즐기자.",
    "실패해도 괜찮아. 다시 일어나면 돼.",
    "너는 생각보다 훨씬 멋진 사람이야 😺",
]

# 버튼 클릭 시
if st.button("고양이 가져오기!"):
    # 고양이 이미지 URL
    cat_url = "https://cataas.com/cat"
    quote = random.choice(quotes)

    st.image(cat_url, caption="야옹~", use_column_width=True)
    st.markdown(f"### 💬 {quote}")
else:
    st.info("버튼을 눌러 고양이를 소환해보세요!")
