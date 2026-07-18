import streamlit as st
import pandas as pd

col1, col2 = st.columns([3, 3])

st.markdown(
    '''
    <style>
        .custom-column {
            background-color: green;
            padding: 5px;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

if "students" not in st.session_state:
    st.session_state.students = []

with col1:
    st.subheader("학생 정보 입력")

    student_id = st.text_input("학번 입력")
    name = st.text_input("이름 입력")
    major = st.text_input("전공 입력")

    if st.button("추가"):
        if student_id and name and major:
            st.session_state.students.append(
                [student_id, name, major]
            )
            st.success("학생 정보가 추가되었습니다.")
        else:
            st.warning("모든 항목을 입력해주세요.")

header = ['학번', '이름', '전공']
df = pd.DataFrame(
    st.session_state.students,
    columns=header
)

with col2:
    st.subheader("학생 목록")

    st.markdown(
        '<div class="custom-column">',
        unsafe_allow_html=True
    )

    if not df.empty:
        st.table(df)
    else:
        st.write("입력된 학생 정보가 없습니다.")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )