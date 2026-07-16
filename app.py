
import streamlit as st
import pandas as pd

# 2개의 열이 생성되고 열의 크기 3:1로 지정
col1, col2 = st.columns([3, 3])

# 컬럼 영역 구분을 위한 css 코드 추가
st.markdown(
    '''
    <style>
        .custom-column {
            background-color: green;
            padding: 5px;
        }
    </style>
    ''', unsafe_allow_html=True
)

header = ['학번', '이름', '전공']
students = [
    ['202601', '홍길동', '컴퓨터공학'],
    ['202602', '이순신', '데이터사이언스'],
    ['202603', '유관순', '인공지능학'],
]

df = pd.DataFrame(students, columns=header)

st.dataframe(df)

col2.subheader("column 3")
col2.markdown('<div class = "custom-column">', unsafe_allow_html=True)
col2.table(df)
