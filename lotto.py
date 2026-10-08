import streamlit as st
import random

# 페이지 제목 설정
st.set_page_config(page_title="로또 번호 생성기")
st.title("🎲 로또 번호 생성기")

# 세션 상태(session_state) 초기화: 생성된 로또 번호 목록을 저장
if 'lotto_history' not in st.session_state:
    st.session_state.lotto_history = []

# 로또 번호의 범위에 따라 공의 색상을 반환하는 함수
def get_lotto_color(num):
    if num <= 10:
        return "#fbc400" # 노란색
    elif num <= 20:
        return "#69c8f2" # 파란색
    elif num <= 30:
        return "#ff7272" # 빨간색
    elif num <= 40:
        return "#aaaaaa" # 회색
    else:
        return "#b0d840" # 초록색

# [로또번호 생성] 버튼 클릭 시 동작
if st.button("로또번호 생성"):
    # 1부터 45 사이의 숫자 중 중복 없이 6개 추출 후 정렬
    new_lotto = sorted(random.sample(range(1, 46), 6))
    
    # 5개를 초과하면 가장 오래된 번호(첫 번째)를 삭제하여 최대 5개 유지
    if len(st.session_state.lotto_history) >= 5:
        st.session_state.lotto_history.pop(0)
        
    # 새로운 로또 번호 세트 추가
    st.session_state.lotto_history.append(new_lotto)

# 구분선과 소제목 출력
st.markdown("---")
st.subheader("생성된 로또 번호 목록 (최대 5게임)")

# 저장된 로또 번호 세트를 화면에 출력
for i, lotto in enumerate(st.session_state.lotto_history):
    # 각 게임별로 한 줄(flex)로 정렬하기 위해 HTML/CSS 사용
    html_str = f"<div style='display: flex; align-items: center; margin-bottom: 15px;'>"
    html_str += f"<span style='width: 60px; font-weight: bold; color: #333;'>{i+1}게임</span>"
    
    # 각 번호별로 원형 디자인(동그란 공 모양) 적용
    for num in lotto:
        color = get_lotto_color(num)
        html_str += f"""
            <div style='background-color: {color}; color: white; border-radius: 50%; 
                        width: 40px; height: 40px; display: flex; justify-content: center; 
                        align-items: center; margin-right: 10px; font-weight: bold;'>
                {num}
            </div>
        """
    html_str += "</div>"
    
    # HTML 렌더링을 허용하여 화면에 그리기
    st.markdown(html_str, unsafe_allow_html=True)