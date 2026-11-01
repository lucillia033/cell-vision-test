
import streamlit as st
from pathlib import Path
from common import render_sidebar

st.set_page_config(
    page_title="CELL VISION | Operation Briefing",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent.parent

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    .stApp {
        background:
            radial-gradient(ellipse at 50% 0%, #102433 0%, transparent 50%),
            #050b12;
        color: #dceaf0;
    }

    [data-testid="stHeader"] {
        background: rgba(5, 11, 18, 0.96);
    }

    [data-testid="stSidebar"] {
        background: #07111b;
        border-right: 1px solid #244454;
    }

    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    .briefing-panel {
        background: linear-gradient(145deg, #0c1b28, #07111a);
        border: 1px solid #315568;
        border-top: 3px solid #57d9e8;
        padding: clamp(22px, 5vw, 54px);
        margin: 20px 0;
    }

    .briefing-kicker {
        color: #57d9e8;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 11px;
        letter-spacing: 2px;
        line-height: 1.8;
    }

    .briefing-title {
        color: #edf8fc;
        font-family: 'IBM Plex Mono', monospace;
        font-size: clamp(32px, 6vw, 58px);
        font-weight: 700;
        line-height: 1.2;
        margin: 22px 0;
    }

    .briefing-text {
        color: #c5d9e2;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 14px;
        line-height: 2;
    }

    .briefing-divider {
        border-top: 1px solid #284655;
        margin: 26px 0;
    }

    div[data-testid="stButton"] > button {
        background: #0b1c29;
        color: #cceaf1;
        border: 1px solid #57d9e8;
        border-radius: 0;
        min-height: 48px;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
        font-size: 13px;
        font-weight: 600;
    }

    div[data-testid="stButton"] > button:hover {
        background: #123044;
        color: white;
        border-color: #57d9e8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

render_sidebar(current_page="briefing")

st.markdown(
    """
    <div class="briefing-panel">
        <div class="briefing-kicker">
            BIOLOGICAL OPERATIONS UNIT<br>
            PERSONNEL BRIEFING // CLASSIFIED
        </div>

        <div class="briefing-title">
            OPERATION<br>
            CELL SHIELD
        </div>

        <div class="briefing-text">
            대원, 귀하에게 새로운 임무가 부여되었습니다.<br><br>

            귀하는 생명 시스템을 분석하는 특수작전 부대의 일원입니다.
            임무를 완수하려면 표적이 되는 세포의 구조와 작동 원리를
            정확하게 파악해야 합니다.<br><br>

            핵의 유전 정보 관리, 리보솜의 단백질 합성,
            미토콘드리아의 에너지 전환, 소포체와 골지체의 물질 처리,
            리소좀의 분해 작용 등 각 소기관은 서로 다른 역할을 수행합니다.<br><br>

            각 소기관의 정보 파일을 확보하고 기능 간의 연결 관계를 학습하십시오.
            이후 학습한 생물학적 지식을 활용해 최종 작전을 수행해야 합니다.
        </div>

        <div class="briefing-divider"></div>

        <div class="briefing-kicker">MISSION OBJECTIVES</div>

        <div class="briefing-text">
            OBJECTIVE 01 — 세포 구조 식별<br>
            OBJECTIVE 02 — 소기관 기능 분석<br>
            OBJECTIVE 03 — 세포 내 물질 이동 이해<br>
            OBJECTIVE 04 — 최종 작전 수행
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<p style="color:#7993a3;font-size:11px;letter-spacing:1px;">'
    'BRIEFING STATUS: READY FOR DEPLOYMENT</p>',
    unsafe_allow_html=True,
)

if st.button("START MISSION  /  작전 시작", use_container_width=True):
    st.session_state["briefing_completed"] = True
    st.switch_page("app.py")

st.caption(
    "작전 브리핑은 사이드바의 BRIEFING 메뉴에서 언제든지 다시 확인할 수 있습니다."
)
