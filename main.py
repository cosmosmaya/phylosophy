# app.py

import streamlit as st
from philosophy_data import philosophy_db

st.set_page_config(page_title="철학 백과", layout="centered")

st.title("🔍 철학 정보 검색 앱")
st.markdown("**사상가, 이론, 개념, 서적 제목 등을 입력하세요.**")

query = st.text_input("검색어를 입력하세요:", "")

if query:
    result = philosophy_db.get(query)
    
    if result:
        st.success(f"🔎 '{query}'에 대한 정보입니다:")
        st.markdown(f"**사상가:** {result['사상가']}")
        st.markdown(f"**시대:** {result['시대']}")
        st.markdown(f"**지역:** {result['지역']}")
        st.markdown(f"**개념:** {result['개념']}")
        st.markdown(f"**관련 서적:** {', '.join(result['관련 서적'])}")
        st.markdown(f"**설명:** {result['설명']}")
    else:
        st.warning(f"'{query}'에 대한 정보를 찾을 수 없습니다. 데이터베이스를 확인해주세요.")

st.markdown("---")
st.caption("© 2025 철학 백과 앱")
