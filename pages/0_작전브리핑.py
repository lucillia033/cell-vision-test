
import streamlit as st

st.set_page_config(
    page_title="Cell Vision - Mission Briefing",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {
        background: #070C13;
    }

    [data-testid="stSidebar"] {
        background: #101923;
    }

    [data-testid="stSidebarNav"] {
        display: none;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 5rem;
        padding-bottom: 3rem;
    }

    .briefing-label {
        color: #43B9FF;
        font-size: 12px;
        letter-spacing: 4px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    .briefing-title {
        color: #F1F5F9;
        font-size: clamp(38px, 6vw, 66px);
        line-height: 1.1;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 12px;
    }

    .briefing-subtitle {
        color: #43B9FF;
        font-size: 17px;
        letter-spacing: 3px;
        font-weight: 700;
        margin-bottom: 35px;
    }

    .briefing-text {
        color: #B8C5D3;
        font-size: 16px;
        line-height: 1.9;
    }

    .mission-panel {
        background: #0D1621;
        border: 1px solid #26394B;
        border-left: 3px solid #43B9FF;
        padding: 24px 28px;
        margin-top: 24px;
        margin-bottom: 24px;
    }

    .mission-heading {
        color: #43B9FF;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    .mission-item {
        color: #E2E8F0;
        font-size: 14px;
        line-height: 1.8;
        margin-bottom: 8px;
    }

    div.stButton > button {
        width: 100%;
        min-height: 54px;
        background: #168BD2;
        color: white;
        border: 1px solid #43B9FF;
        border-radius: 3px;
        font-weight: 800;
        letter-spacing: 2px;
    }

    div.stButton > button:hover {
        background: #0873B5;
        color: white;
        border-color: #7ACDFF;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="briefing-label">CLASSIFIED // PERSONNEL ONLY</div>
    <div class="briefing-title">MISSION BRIEFING</div>
    <div class="briefing-subtitle">OPERATION CELL SHIELD</div>

    <div class="briefing-text">
        대원, 긴급 작전이 하달되었습니다.<br><br>
        인체를 구성하는 세포 내부에서 이상 상황이 발생했습니다.
        임무를 완수하려면 세포를 구성하는 각 소기관의 구조와 기능을
        정확하게 파악해야 합니다.<br><br>
        귀하는 <b>TASK FORCE CELL VISION</b>의 작전 요원입니다.
        지금부터 생물학적 정보를 수집하고 분석하여 최종 작전에 대비하십시오.
        확보한 지식은 마지막 작전에서 핵심적인 역할을 하게 됩니다.
    </div>

    <div class="mission-panel">
        <div class="mission-heading">MISSION OBJECTIVES</div>
        <div class="mission-item">
            <b>01 / INTELLIGENCE</b><br>
            세포와 주요 소기관의 구조 및 기능을 학습하십시오.
        </div>
        <div class="mission-item">
            <b>02 / ANALYSIS</b><br>
            각 소기관의 정보를 확인하고 작전에 필요한 지식을 확보하십시오.
        </div>
        <div class="mission-item">
            <b>03 / FINAL OPERATION</b><br>
            학습한 지식을 활용해 최종 작전을 수행하십시오.
        </div>
    </div>

    <div class="briefing-text">
        <b>작전 지침:</b> 충분한 정보를 확보하기 전에는 최종 작전에 진입하지 마십시오.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

if st.button("START OPERATION", use_container_width=True):
    st.session_state["briefing_completed"] = True
    st.switch_page("app.py")
