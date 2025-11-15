import streamlit as st

# 제목
st.title('Streamlit 예제')

# 텍스트 입력
user_input = st.text_input("이름을 입력하세요:")

# 사용자 입력에 따른 출력
if user_input:
    st.write(f"안녕하세요, {user_input}님!")
else:
    st.write("이름을 입력해 주세요.")
