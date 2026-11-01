
import streamlit as st
from datetime import datetime

# =========================================================
# 1. 기본 설정
# =========================================================

st.set_page_config(
    page_title="CELL VISION | Mission Briefing",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# 2. 작전 브리핑 전용 디자인
# =========================================================

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap'
    );

    :root {
        --bg: #020810;
        --panel: #06121e;
        --cyan: #24d9f5;
        --cyan-soft: #57d9e8;
        --text: #d9edf8;
        --muted: #7899ad;
        --line: #17465a;
    }

    html, body, [class*="css"] {
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
    }

    .stApp {
        background:
            radial-gradient(
                ellipse at 50% 42%,
                rgba(0, 94, 133, 0.15),
                transparent 54%
            ),
            linear-gradient(180deg, #030b14 0%, #020810 100%);
        color: var(--text);
    }

    /* 시작 화면에서는 사이드바와 기본 페이지 메뉴를 표시하지 않음 */
    [data-testid="stSidebar"],
    [data-testid="stSidebarNav"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1600px;
        padding: 1.1rem 2.5rem 1.5rem;
    }

    /* 상단 시스템 바 */

    .system-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        flex-wrap: wrap;
        border-bottom: 1px solid var(--line);
        padding: 10px 4px 17px;
        margin-bottom: 30px;
    }

    .brand {
        color: #e6f6ff;
        font-size: clamp(17px, 2vw, 25px);
        font-weight: 700;
        letter-spacing: 3px;
    }

    .brand-symbol {
        color: var(--cyan);
        margin-right: 12px;
    }

    .brand-sub {
        color: var(--muted);
        font-size: 10px;
        letter-spacing: 1.6px;
        margin-left: 12px;
    }

    .system-status {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 1.3px;
        text-align: right;
    }

    /* 메인 브리핑 프레임 */

    .briefing-frame {
        position: relative;
        overflow: hidden;
        background:
            linear-gradient(
                135deg,
                rgba(7, 24, 39, 0.97),
                rgba(2, 9, 17, 0.99) 68%
            );
        border: 1px solid #17627a;
        border-top: 2px solid var(--cyan);
        padding: clamp(22px, 4vw, 58px);
        box-shadow:
            0 0 28px rgba(0, 190, 235, 0.06),
            inset 0 0 35px rgba(0, 115, 160, 0.035);
    }

    .briefing-frame::before {
        content: "";
        position: absolute;
        inset: 7px;
        border: 1px solid rgba(39, 128, 156, 0.18);
        pointer-events: none;
    }

    .briefing-topline {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
        color: var(--cyan);
        font-size: 11px;
        letter-spacing: 2px;
        border-bottom: 1px solid #16465a;
        padding-bottom: 13px;
        margin-bottom: 28px;
    }

    .mission-index {
        color: #8bc7d9;
    }

    .hero-title {
        color: #e8f7ff;
        font-size: clamp(40px, 6vw, 78px);
        line-height: 1.08;
        letter-spacing: 3px;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 0 24px rgba(45, 198, 255, 0.13);
    }

    .hero-subtitle {
        color: var(--cyan);
        font-size: clamp(11px, 1.5vw, 18px);
        letter-spacing: clamp(2px, 0.5vw, 6px);
        margin-top: 12px;
        font-weight: 600;
    }

    .hero-tagline {
        color: #a6d9ed;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: clamp(14px, 1.6vw, 19px);
        margin-top: 19px;
        line-height: 1.8;
    }

    .cyan-divider {
        height: 1px;
        background: linear-gradient(
            90deg,
            var(--cyan),
            #17546b 68%,
            transparent
        );
        margin: 26px 0;
    }

    /* 상태 정보 */

    .status-panel {
        background: rgba(3, 16, 27, 0.7);
        border-left: 2px solid var(--cyan);
        padding: 14px 18px;
        margin-bottom: 20px;
    }

    .status-label {
        color: var(--muted);
        font-size: 9px;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }

    .status-value {
        color: #bdefff;
        font-size: 12px;
        line-height: 1.9;
    }

    .online {
        color: #7ce5b4;
    }

    /* 작전 설명 */

    .section-label {
        color: var(--cyan);
        font-size: 11px;
        letter-spacing: 2px;
        margin-bottom: 17px;
    }

    .welcome-title {
        color: #e3f5ff;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: clamp(19px, 2vw, 27px);
        line-height: 1.6;
        font-weight: 700;
        margin-bottom: 16px;
    }

    .briefing-text {
        color: #9fc3d5;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 14px;
        line-height: 2;
    }

    .final-directive {
        color: var(--cyan);
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 14px;
        font-weight: 700;
        margin-top: 17px;
    }

    /* 임무 목표 */

    .objectives-panel {
        background: rgba(4, 18, 30, 0.78);
        border: 1px solid #19536a;
        padding: 22px;
        height: 100%;
        box-sizing: border-box;
    }

    .objective {
        display: flex;
        align-items: flex-start;
        gap: 15px;
        padding: 13px 0;
        border-bottom: 1px solid rgba(33, 83, 104, 0.4);
    }

    .objective:last-child {
        border-bottom: none;
    }

    .objective-number {
        color: var(--cyan);
        font-size: 22px;
        font-weight: 700;
        min-width: 34px;
    }

    .objective-title {
        color: #d9eff9;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 14px;
        font-weight: 600;
    }

    .objective-description {
        color: #789fb2;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 11px;
        line-height: 1.8;
        margin-top: 5px;
    }

    /* 시작 버튼 */

    div[data-testid="stButton"] {
        margin: 0 auto;
        max-width: 600px;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        min-height: 76px;
        background: linear-gradient(
            105deg,
            #06263a,
            #08415a 50%,
            #06263a
        ) !important;
        color: #40e4ff !important;
        border: 2px solid #19cbe9 !important;
        border-radius: 0 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: clamp(15px, 2vw, 21px) !important;
        font-weight: 700 !important;
        letter-spacing: 3px !important;
        box-shadow:
            0 0 12px rgba(0, 204, 245, 0.14),
            inset 0 0 18px rgba(0, 188, 230, 0.08);
        transition: all 0.2s ease;
    }

    div[data-testid="stButton"] > button:hover {
        background: #0c3c53 !important;
        color: #ffffff !important;
        border-color: #8cf2ff !important;
        box-shadow:
            0 0 25px rgba(0, 211, 255, 0.28),
            inset 0 0 20px rgba(0, 188, 230, 0.14);
        transform: translateY(-1px);
    }

    div[data-testid="stButton"] > button:focus {
        box-shadow: 0 0 0 2px #020810,
                    0 0 0 4px var(--cyan) !important;
    }

    .button-caption {
        text-align: center;
        color: #66899c;
        font-size: 9px;
        letter-spacing: 2px;
        margin-top: 12px;
    }

    /* 하단 정보 */

    .system-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
        border-top: 1px solid #15394b;
        padding: 15px 4px 0;
        margin-top: 25px;
        color: #66889b;
        font-size: 9px;
        letter-spacing: 1.2px;
        line-height: 1.8;
    }

    .footer-highlight {
        color: var(--cyan);
    }

    @media (max-width: 800px) {
        .block-container {
            padding: 0.7rem 1rem 1rem;
        }

        .system-header {
            margin-bottom: 16px;
        }

        .briefing-frame {
            padding: 20px 16px;
        }

        .hero-title {
            letter-spacing: 1px;
        }

        .hero-subtitle {
            letter-spacing: 2px;
        }

        .objectives-panel {
            margin-top: 12px;
        }

        div[data-testid="stButton"] > button {
            min-height: 64px;
            letter-spacing: 1.5px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 3. 상단 시스템 헤더
# =========================================================

current_time = datetime.now().strftime("%Y.%m.%d")

st.markdown(
    """
    <div class="system-header">
        <div>
            <span class="brand">
                <span class="brand-symbol">⬡</span>CELL VISION
            </span>
            <span class="brand-sub">
                BIOLOGICAL OPERATIONS UNIT
            </span>
        </div>
        <div class="system-status">
            SYSTEM / <span class="online">ONLINE ●</span>
            &nbsp;&nbsp; | &nbsp;&nbsp;
            ACCESS MODE / EDUCATIONAL
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 4. 작전 브리핑 메인 화면
# =========================================================

st.markdown(
    """
    <div class="briefing-frame">

        <div class="briefing-topline">
            <span>MISSION BRIEFING // 001</span>
            <span class="mission-index">CELL VISION / CLASSIFIED</span>
        </div>

        <div class="hero-title">CELL VISION</div>

        <div class="hero-subtitle">
            BIOLOGICAL OPERATIONS UNIT
        </div>

        <div class="hero-tagline">
            세포의 비밀을 탐색하는, 당신의 미션이 시작됩니다.
        </div>

        <div class="cyan-divider"></div>

        <div class="status-panel">
            <div class="status-label">
                OPERATION STATUS / MISSION CONTROL
            </div>
            <div class="status-value">
                TARGET &nbsp;&nbsp;&nbsp; / CELLULAR SYSTEM<br>
                OBJECTIVE / ANALYZE &amp; UNDERSTAND<br>
                STATUS &nbsp;&nbsp;&nbsp; / <span class="online">READY</span>
            </div>
        </div>

        <div class="section-label">// 작전 개요</div>

        <div class="welcome-title">
            대원, 환영한다.<br>
            당신은 지금 세포 내부로 향하는 특별한 작전에 투입되었다.
        </div>

        <div class="briefing-text">
            이 임무의 목표는 세포를 구성하는 핵심 소기관들을 탐색하고,<br>
            각 구조의 기능과 상호작용을 분석하는 것이다.<br>
            제공된 분석 자료를 활용해 세포 시스템의 작동 원리를 파악하라.
        </div>

        <div class="final-directive">
            지금부터, 세포의 세계로 들어가자.
        </div>

        <div class="cyan-divider"></div>

        <div class="section-label">// OPERATION OBJECTIVES</div>

        <div class="objectives-panel">

            <div class="objective">
                <div class="objective-number">01</div>
                <div>
                    <div class="objective-title">세포 내부 구조 탐색</div>
                    <div class="objective-description">
                        9개의 소기관을 식별하고 각 구조의 특징을 파악할 것
                    </div>
                </div>
            </div>

            <div class="objective">
                <div class="objective-number">02</div>
                <div>
                    <div class="objective-title">소기관별 기능 분석</div>
                    <div class="objective-description">
                        각 소기관의 역할과 작동 원리를 이해할 것
                    </div>
                </div>
            </div>

            <div class="objective">
                <div class="objective-number">03</div>
                <div>
                    <div class="objective-title">세포 시스템 이해 완성</div>
                    <div class="objective-description">
                        소기관 사이의 연결 관계와 물질 이동을 분석할 것
                    </div>
                </div>
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 5. START MISSION 버튼
# =========================================================

st.write("")
st.write("")

button_col_left, button_col_center, button_col_right = st.columns(
    [1, 2, 1]
)

with button_col_center:
    start_mission = st.button(
        ">>>  START MISSION  <<<",
        use_container_width=True,
        type="primary",
    )

    st.markdown(
        '<div class="button-caption">'
        'INITIALIZE SYSTEM // ENTER CELLULAR ANALYSIS'
        '</div>',
        unsafe_allow_html=True,
    )

if start_mission:
    st.switch_page("app.py")

# =========================================================
# 6. 하단 시스템 정보
# =========================================================

st.markdown(
    f"""
    <div class="system-footer">
        <div>
            <span class="footer-highlight">CELL VISION</span>
            &nbsp; / BIOLOGICAL OPERATIONS UNIT<br>
            EXPLORE · ANALYZE · UNDERSTAND · SAVE LIFE
        </div>
        <div>
            MISSION READY &nbsp; / &nbsp; {current_time}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
