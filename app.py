
import streamlit as st
from pathlib import Path
from datetime import datetime

# =========================================================
# 1. 기본 설정
# =========================================================

st.set_page_config(
    page_title="CELL VISION | Tactical Command",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

TEAM_NAME = "TASK FORCE CELL VISION"

# 최초 접속 시에는 작전 브리핑부터 표시합니다.
if "mission_started" not in st.session_state:
    st.session_state["mission_started"] = False


# =========================================================
# 2. 작전 브리핑 화면
# =========================================================

def show_mission_briefing():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

        :root {
            --bg: #050b12;
            --panel: #091521;
            --line: #244454;
            --cyan: #57d9e8;
            --text: #dceaf0;
            --muted: #7993a3;
        }

        html, body, [class*="css"] {
            font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
        }

        .stApp {
            background:
                radial-gradient(ellipse at 50% 0%, #102c40 0%, transparent 55%),
                #050b12;
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: rgba(5, 11, 18, 0.96);
            border-bottom: 1px solid #172d3b;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        [data-testid="stSidebarCollapsedControl"] {
            display: none;
        }

        .block-container {
            max-width: 1050px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .briefing-top {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
            padding: 12px 15px;
            border-top: 2px solid #7d9aa9;
            border-bottom: 1px solid #244454;
            background: linear-gradient(90deg, #132431, #07111b);
            color: #9cb7c4;
            font-size: 10px;
            letter-spacing: 1.5px;
        }

        .briefing-cyan {
            color: #57d9e8;
        }

        .briefing-hero {
            padding: 40px 28px 30px 28px;
            margin-top: 18px;
            background: linear-gradient(145deg, #0c1b28, #07111a);
            border: 1px solid #284655;
            border-top: 3px solid #57d9e8;
        }

        .briefing-label {
            color: #57d9e8;
            font-size: 11px;
            letter-spacing: 2.5px;
            margin-bottom: 16px;
        }

        .briefing-title {
            color: #edf8fc;
            font-size: clamp(30px, 5vw, 56px);
            font-weight: 700;
            letter-spacing: 2px;
            line-height: 1.15;
            margin: 0;
        }

        .briefing-team {
            color: #57d9e8;
            font-size: clamp(15px, 2vw, 21px);
            font-weight: 600;
            letter-spacing: 1.2px;
            margin-top: 15px;
            overflow-wrap: anywhere;
        }

        .briefing-subtitle {
            color: #8da9b9;
            font-size: 11px;
            letter-spacing: 1.5px;
            line-height: 1.8;
            margin-top: 9px;
        }

        .briefing-divider {
            border-top: 1px solid #284655;
            margin: 25px 0;
        }

        .briefing-heading {
            color: #57d9e8;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 2px;
            margin-bottom: 12px;
        }

        .briefing-text {
            color: #c7d8e2;
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 14px;
            line-height: 2;
        }

        .briefing-quote {
            color: #edf8fc;
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 17px;
            font-weight: 600;
            line-height: 1.8;
            border-left: 3px solid #57d9e8;
            padding: 12px 0 12px 17px;
            margin: 20px 0;
        }

        .objective {
            display: flex;
            align-items: flex-start;
            gap: 15px;
            padding: 15px 0;
            border-bottom: 1px solid #1e3949;
        }

        .objective-number {
            color: #57d9e8;
            font-size: 20px;
            font-weight: 700;
            min-width: 35px;
        }

        .objective-title {
            color: #e5f4f9;
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .objective-description {
            color: #91aab8;
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 12px;
            line-height: 1.8;
        }

        .briefing-status {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
            border-top: 1px solid #284655;
            padding-top: 15px;
            margin-top: 25px;
            color: #7993a3;
            font-size: 10px;
            letter-spacing: 1px;
        }

        div[data-testid="stButton"] > button {
            background: #0b2635 !important;
            color: #dffaff !important;
            border: 1px solid #57d9e8 !important;
            border-radius: 0 !important;
            min-height: 52px;
            font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
            font-size: 13px !important;
            font-weight: 700 !important;
            letter-spacing: 1.5px;
            transition: 0.15s ease-in-out;
        }

        div[data-testid="stButton"] > button:hover {
            background: #16445a !important;
            border-color: #a4f5ff !important;
            color: #ffffff !important;
        }

        @media (max-width: 600px) {
            .briefing-hero {
                padding: 25px 17px;
            }

            .briefing-text {
                font-size: 13px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    current_time = datetime.now().strftime("%Y-%m-%d")

    st.markdown(
        f"""
        <div class="briefing-top">
            <span>CLASSIFIED // BIOLOGICAL OPERATIONS</span>
            <span>SECURITY LEVEL: <b class="briefing-cyan">RESTRICTED</b></span>
            <span>{current_time}</span>
        </div>

        <div class="briefing-hero">
            <div class="briefing-label">
                MISSION BRIEFING // OPERATION 001
            </div>

            <h1 class="briefing-title">CELL VISION</h1>

            <div class="briefing-team">
                {TEAM_NAME}
            </div>

            <div class="briefing-subtitle">
                ELITE BIOLOGICAL OPERATIONS UNIT<br>
                IDENTIFY. ANALYZE. ELIMINATE.
            </div>

            <div class="briefing-divider"></div>

            <div class="briefing-heading">
                INCOMING TRANSMISSION // COMMAND
            </div>

            <div class="briefing-quote">
                "대원, 브리핑에 집중해라. 지금부터 네 첫 번째 임무를 설명하겠다."
            </div>

            <div class="briefing-text">
                당신은 미지의 생물학적 위협에 대응하기 위해 창설된
                <b>TASK FORCE CELL VISION</b>의 신규 대원이다.<br><br>

                적을 제압하고 임무를 완수하려면, 먼저 작전 지역인
                <b>세포 내부의 구조와 작동 원리</b>를 이해해야 한다.
                세포는 수많은 소기관이 각자의 역할을 수행하며 협력하는
                복잡한 생명 시스템이다.<br><br>

                핵, 리보솜, 미토콘드리아를 비롯한 9개 소기관의 정보를 확보하라.
                각 소기관의 기능과 역할을 제대로 이해해야 주어진 임무를 수행할 수 있다.
                학습을 마친 뒤에는 최종 작전에서 습득한 지식을 증명해야 한다.<br><br>

                명심해라. 이 작전에서 지식은 네가 임무를 완수하기 위한 가장 중요한 도구다.
            </div>

            <div class="briefing-divider"></div>

            <div class="briefing-heading">
                MISSION OBJECTIVES // PRIMARY
            </div>

            <div class="objective">
                <div class="objective-number">01</div>
                <div>
                    <div class="objective-title">정보 확보 // INTELLIGENCE</div>
                    <div class="objective-description">
                        9개 세포 소기관의 구조와 기능을 학습하고 핵심 정보를 확보한다.
                    </div>
                </div>
            </div>

            <div class="objective">
                <div class="objective-number">02</div>
                <div>
                    <div class="objective-title">전투 준비 // PREPARATION</div>
                    <div class="objective-description">
                        습득한 생물학 지식을 바탕으로 상황을 판단하고 임무 수행 능력을 검증한다.
                    </div>
                </div>
            </div>

            <div class="objective">
                <div class="objective-number">03</div>
                <div>
                    <div class="objective-title">최종 작전 // FINAL OPERATION</div>
                    <div class="objective-description">
                        최종 전투에서 적을 제압하고 주어진 임무를 완수한다.
                    </div>
                </div>
            </div>

            <div class="briefing-quote">
                "지식은 네 무기다. 모든 정보를 숙지하고 작전에 투입될 준비를 마쳐라."
            </div>

            <div class="briefing-status">
                <span>UNIT: TASK FORCE CELL VISION</span>
                <span>MISSION STATUS: AWAITING DEPLOYMENT</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    _, button_col, _ = st.columns([1, 2, 1])

    with button_col:
        if st.button(
            ">>>  START MISSION  <<<",
            use_container_width=True,
            key="start_mission_button",
        ):
            st.session_state["mission_started"] = True
            st.rerun()

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#607b8b;
            font-size:10px;
            letter-spacing:1.2px;
            margin-top:15px;
        ">
            TASK FORCE CELL VISION // AUTHORIZED PERSONNEL ONLY
        </div>
        """,
        unsafe_allow_html=True,
    )


# 아직 작전을 시작하지 않았다면 브리핑만 표시합니다.
if not st.session_state["mission_started"]:
    show_mission_briefing()
    st.stop()


# =========================================================
# 3. 소기관 정보
# =========================================================

ORGANELLES = [
    {
        "name": "핵",
        "code": "BIO-01",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "description": "유전 정보를 보관하고 세포의 활동을 조절합니다.",
    },
    {
        "name": "리보솜",
        "code": "BIO-02",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "description": "유전 정보에 따라 단백질을 합성합니다.",
    },
    {
        "name": "미토콘드리아",
        "code": "BIO-03",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "description": "세포 호흡을 통해 ATP를 생성합니다.",
    },
    {
        "name": "소포체",
        "code": "BIO-04",
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "description": "단백질과 지질의 합성 및 이동에 관여합니다.",
    },
    {
        "name": "골지체",
        "code": "BIO-05",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "description": "물질을 가공하고 분류하여 목적지로 보냅니다.",
    },
    {
        "name": "리소좀",
        "code": "BIO-06",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "description": "세포 내 물질과 노폐물을 분해합니다.",
    },
    {
        "name": "세포막",
        "code": "BIO-07",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "description": "세포 안팎의 물질 이동을 조절합니다.",
    },
    {
        "name": "세포질",
        "code": "BIO-08",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "description": "다양한 세포 소기관이 존재하고 여러 화학 반응이 일어나는 공간입니다.",
    },
    {
        "name": "세포골격",
        "code": "BIO-09",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "description": "세포의 형태를 유지하고 세포 내 물질 이동을 돕습니다.",
    },
]


# =========================================================
# 4. 전술 분석실 디자인
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    :root {
        --bg: #050b12;
        --panel: #091521;
        --line: #244454;
        --cyan: #57d9e8;
        --text: #dceaf0;
        --muted: #7993a3;
        --green: #8bd9b0;
    }

    html, body, [class*="css"] {
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 50% 0%, #102433 0%, transparent 46%),
            #050b12;
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(5, 11, 18, 0.96);
        border-bottom: 1px solid #172d3b;
    }

    [data-testid="stSidebar"] {
        background: #07111b;
        border-right: 1px solid #244454;
    }

    [data-testid="stSidebar"] > div:first-child {
        background: #07111b;
    }

    [data-testid="stSidebar"] * {
        color: #c9dce5;
    }

    .block-container {
        max-width: 1800px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, li, label {
        color: var(--text);
    }

    .top-strip {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        padding: 9px 14px;
        margin-bottom: 18px;
        border-top: 2px solid #7d9aa9;
        border-bottom: 1px solid var(--line);
        background: linear-gradient(90deg, #132431, #07111b 75%);
        font-size: 10px;
        letter-spacing: 1.6px;
        color: #9cb7c4;
    }

    .top-strip strong {
        color: var(--cyan);
        font-weight: 600;
    }

    .eyebrow {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }

    .main-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: clamp(26px, 3vw, 42px);
        font-weight: 700;
        letter-spacing: 2px;
        line-height: 1.15;
        color: #edf8fc;
        margin: 0;
    }

    .subtitle {
        font-size: 12px;
        color: #89a6b6;
        letter-spacing: 1px;
        margin-top: 9px;
        margin-bottom: 20px;
    }

    .section-bar {
        background: #0d1d2a;
        border-left: 3px solid var(--cyan);
        border-bottom: 1px solid #294958;
        padding: 10px 12px;
        margin: 12px 0;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #d8eef5;
    }

    .panel {
        background: linear-gradient(145deg, #0c1b28, #07111a);
        border: 1px solid #284655;
        border-top: 2px solid #5d8b9e;
        padding: 15px;
        margin-bottom: 12px;
        min-height: 112px;
    }

    .panel-label {
        font-size: 9px;
        color: #7fa1b2;
        letter-spacing: 1.6px;
        margin-bottom: 9px;
    }

    .panel-value {
        font-size: 17px;
        font-weight: 700;
        color: #e6f4fa;
        letter-spacing: 0.5px;
        overflow-wrap: anywhere;
    }

    .panel-note {
        font-size: 10px;
        color: #87a3b2;
        margin-top: 8px;
        line-height: 1.6;
    }

    .status-dot {
        color: var(--green);
        font-weight: 700;
    }

    .intel-card {
        background: linear-gradient(140deg, #0c1b28, #07111a);
        border: 1px solid #284655;
        border-top: 2px solid #426c80;
        padding: 12px;
        margin-bottom: 0;
        min-height: 195px;
    }

    .intel-code {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 1.5px;
        margin-bottom: 6px;
    }

    .intel-name {
        color: #e8f5fa;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .intel-description {
        color: #91aab8;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 12px;
        line-height: 1.7;
        min-height: 42px;
    }

    .intel-status {
        border-top: 1px solid #203a49;
        margin-top: 10px;
        padding-top: 8px;
        color: #86c9d5;
        font-size: 9px;
        letter-spacing: 1px;
    }

    .side-brand {
        border-top: 2px solid #6d95a7;
        border-bottom: 1px solid #284655;
        padding: 13px 6px;
        margin-bottom: 18px;
        background: linear-gradient(90deg, #122533, #07111b);
    }

    .side-brand-title {
        font-size: 21px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #e5f4f9;
    }

    .side-brand-sub {
        font-size: 9px;
        color: var(--cyan);
        letter-spacing: 1.4px;
        margin-top: 5px;
    }

    .side-section {
        color: #70c7d9;
        font-size: 10px;
        letter-spacing: 1.5px;
        padding: 9px 0 5px 0;
        border-bottom: 1px solid #1e3949;
        margin: 12px 0 8px 0;
    }

    .side-info {
        color: #7894a5;
        font-size: 10px;
        line-height: 1.9;
    }

    .mission-box {
        background: #081722;
        border: 1px solid #294958;
        border-left: 3px solid #3988bd;
        padding: 14px;
        margin: 8px 0 15px 0;
    }

    .mission-box-title {
        color: var(--cyan);
        font-size: 10px;
        letter-spacing: 1.7px;
        margin-bottom: 8px;
    }

    .mission-box-text {
        color: #c5d9e2;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 12px;
        line-height: 1.8;
    }

    .data-row {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        padding: 8px 0;
        border-bottom: 1px solid #1a3442;
        font-size: 10px;
    }

    .data-row span:first-child {
        color: #7e9baa;
    }

    .data-row span:last-child {
        color: #d6e8ef;
        text-align: right;
    }

    .footer-line {
        border-top: 1px solid #284655;
        margin-top: 25px;
        padding-top: 10px;
        color: #658292;
        font-size: 9px;
        letter-spacing: 1.2px;
        display: flex;
        justify-content: space-between;
        gap: 10px;
        flex-wrap: wrap;
    }

    div[data-testid="stButton"] > button,
    div[data-testid="stPageLink"] a {
        background: #0b1c29 !important;
        color: #cceaf1 !important;
        border: 1px solid #315568 !important;
        border-radius: 0 !important;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
        font-size: 11px !important;
        letter-spacing: 0.4px;
        transition: 0.15s ease-in-out;
    }

    div[data-testid="stButton"] > button:hover,
    div[data-testid="stPageLink"] a:hover {
        background: #123044 !important;
        border-color: var(--cyan) !important;
        color: #ffffff !important;
    }

    [data-testid="stImage"] img {
        border: 1px solid #1d3949;
    }

    [data-testid="stAlert"] {
        background: #0b1b28;
        border-radius: 0;
    }

    hr {
        border-color: #203b4b;
    }

    @media (max-width: 800px) {
        .top-strip {
            flex-wrap: wrap;
        }

        .main-title {
            font-size: 25px;
        }

        .panel {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 5. 사이드바: 작전 메뉴
# =========================================================

with st.sidebar:
    st.markdown(
        f"""
        <div class="side-brand">
            <div class="side-brand-title">CELL VISION</div>
            <div class="side-brand-sub">{TEAM_NAME}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="side-section">01 / COMMAND MENU</div>',
        unsafe_allow_html=True,
    )

    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 지휘 통제실")

    st.markdown(
        '<div class="side-section">02 / INTELLIGENCE FILES</div>',
        unsafe_allow_html=True,
    )

    for organelle in ORGANELLES:
        if (ROOT_DIR / organelle["page"]).exists():
            st.page_link(
                organelle["page"],
                label=f'{organelle["code"]} / {organelle["name"]}',
            )

    # 기존 작전 페이지가 있을 때만 메뉴에 표시합니다.
    game_page = ROOT_DIR / "pages" / "10_작전.py"

    if game_page.exists():
        st.page_link(
            "pages/10_작전.py",
            label="BIO-10 / 작전",
        )

    st.markdown(
        """
        <div class="side-section">03 / SYSTEM MONITOR</div>
        <div class="side-info">
            SYSTEM STATUS&nbsp;&nbsp;
            <span style="color:#8bd9b0;">ONLINE</span><br>
            DATABASE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOCAL FILES<br>
            SECURITY LEVEL&nbsp; BIO-RESTRICTED<br>
            ACCESS MODE&nbsp;&nbsp;&nbsp;&nbsp; EDUCATIONAL
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("TASK FORCE CELL VISION / INTERNAL USE")


# =========================================================
# 6. 상단 전술 시스템 바
# =========================================================

current_time = datetime.now().strftime("%Y-%m-%d")

st.markdown(
    f"""
    <div class="top-strip">
        <span>CV // BIOLOGICAL INTELLIGENCE SYSTEM</span>
        <span>UNIT: <strong>TASK FORCE CELL VISION</strong></span>
        <span>SYSTEM STATUS: <strong>OPERATIONAL</strong></span>
        <span>{current_time}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="eyebrow">
        TACTICAL BIOLOGY INTERFACE // TERMINAL 01
    </div>
    <h1 class="main-title">COMMAND CENTER</h1>
    <div class="subtitle">
        CELLULAR STRUCTURE ANALYSIS · BIOLOGICAL INTELLIGENCE · MISSION CONTROL
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 7. 상황 정보 패널
# =========================================================

status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">OPERATION IDENTIFIER</div>
            <div class="panel-value">BIO-OPS / 001</div>
            <div class="panel-note">MISSION: CELLULAR ANALYSIS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with status_col2:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">CURRENT OPERATION STATUS</div>
            <div class="panel-value">
                <span class="status-dot">●</span> STANDING BY
            </div>
            <div class="panel-note">AWAITING ANALYSIS INPUT</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with status_col3:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">TARGET PROFILE</div>
            <div class="panel-value">ANIMAL CELL</div>
            <div class="panel-note">BIOLOGICAL STRUCTURE / CLASSIFIED</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 8. 중앙 분석 화면
# =========================================================

st.markdown(
    '<div class="section-bar">LIVE ANALYSIS // TARGET RECONNAISSANCE</div>',
    unsafe_allow_html=True,
)

left_col, center_col, right_col = st.columns(
    [0.85, 1.8, 1.0],
    gap="medium",
)

with left_col:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">MISSION DIRECTIVE</div>
            <div class="panel-value">CELL / 001</div>
            <div class="panel-note">
                세포의 주요 구조를 식별하고 각 소기관의 기능 및 상호작용을 분석하십시오.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-bar">PRIMARY OBJECTIVES</div>
        <div class="data-row"><span>OBJECTIVE 01</span><span>구조 식별</span></div>
        <div class="data-row"><span>OBJECTIVE 02</span><span>기능 분석</span></div>
        <div class="data-row"><span>OBJECTIVE 03</span><span>물질 이동</span></div>
        <div class="data-row"><span>OBJECTIVE 04</span><span>시스템 이해</span></div>
        """,
        unsafe_allow_html=True,
    )

with center_col:
    st.markdown(
        '<div class="section-bar">TARGET IMAGE // CELLULAR OVERVIEW</div>',
        unsafe_allow_html=True,
    )

    cell_image = IMAGE_DIR / "cell.png"

    if cell_image.exists():
        st.image(
            str(cell_image),
            use_container_width=True,
            caption="TARGET 001 / ANIMAL CELL STRUCTURE",
        )
    else:
        st.warning(
            "세포 전체 이미지가 없습니다. images 폴더에 cell.png 파일이 있는지 확인해 주세요."
        )

    st.markdown(
        """
        <div class="mission-box">
            <div class="mission-box-title">COMMAND DIRECTIVE // 001</div>
            <div class="mission-box-text">
                세포는 여러 소기관이 유기적으로 협력하는 생명 시스템입니다.
                각 소기관의 구조와 기능을 확인하고, 물질 합성·수송·에너지 전환 과정이
                어떻게 연결되는지 분석하십시오.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <div class="section-bar">SYSTEM INTELLIGENCE</div>
        <div class="panel">
            <div class="panel-label">ANALYSIS MODE</div>
            <div class="panel-value">BIO / SCAN</div>
            <div class="panel-note">STRUCTURAL RECONNAISSANCE</div>
        </div>
        <div class="panel">
            <div class="panel-label">DATA CLASSIFICATION</div>
            <div class="panel-value">BIO-RESTRICTED</div>
            <div class="panel-note">EDUCATIONAL INTELLIGENCE FILES</div>
        </div>
        <div class="panel">
            <div class="panel-label">ANALYSIS PROTOCOL</div>
            <div class="panel-value">CELL SYSTEM</div>
            <div class="panel-note">IDENTIFY / ANALYZE / UNDERSTAND</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 9. 소기관 정보 파일
# =========================================================

st.markdown(
    '<div class="section-bar">INTELLIGENCE FILES // ORGANELLE DATABASE</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="subtitle">
        SELECT AN INTELLIGENCE FILE TO ACCESS DETAILED BIOLOGICAL INFORMATION.
    </div>
    """,
    unsafe_allow_html=True,
)

for start in range(0, len(ORGANELLES), 3):
    row_items = ORGANELLES[start:start + 3]
    columns = st.columns(3, gap="medium")

    for column, organelle in zip(columns, row_items):
        with column:
            st.markdown(
                f"""
                <div class="intel-card">
                    <div class="intel-code">
                        {organelle["code"]} // INTELLIGENCE FILE
                    </div>
                    <div class="intel-name">{organelle["name"]}</div>
                    <div class="intel-description">
                        {organelle["description"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            status_col, button_col = st.columns(
                [1.35, 1],
                vertical_alignment="center",
                gap="small",
            )

            with status_col:
                st.markdown(
                    """
                    <div class="intel-status">
                        ● DATA FILE / BIOLOGICAL
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with button_col:
                page_path = ROOT_DIR / organelle["page"]

                if page_path.exists():
                    st.page_link(
                        organelle["page"],
                        label="ACCESS FILE",
                        use_container_width=True,
                    )
                else:
                    st.caption("상세 페이지 파일을 찾을 수 없습니다.")

            image_path = IMAGE_DIR / organelle["image"]

            if image_path.exists():
                st.image(
                    str(image_path),
                    use_container_width=True,
                )
            else:
                st.warning(
                    f'이미지 파일을 찾을 수 없습니다: images/{organelle["image"]}'
                )


# =========================================================
# 10. 작전 지침
# =========================================================

st.markdown(
    '<div class="section-bar">FIELD INSTRUCTIONS // OPERATION PROTOCOL</div>',
    unsafe_allow_html=True,
)

protocols = [
    (
        "PROTOCOL 01 — OBSERVE",
        "세포 전체 이미지를 관찰하고 각 소기관의 위치와 형태를 확인하십시오.",
    ),
    (
        "PROTOCOL 02 — IDENTIFY",
        "소기관 정보 파일에 접근하여 구조, 기능, 세포 내 역할을 분석하십시오.",
    ),
    (
        "PROTOCOL 03 — CONNECT",
        "단백질 합성 및 이동, 세포 호흡 등 세포 내 과정의 연결 관계를 이해하십시오.",
    ),
]

for title, description in protocols:
    st.markdown(
        f"""
        <div class="mission-box">
            <div class="mission-box-title">{title}</div>
            <div class="mission-box-text">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 11. 하단 정보
# =========================================================

st.markdown(
    f"""
    <div class="footer-line">
        <span>CELL VISION // {TEAM_NAME}</span>
        <span>INTERNAL SYSTEM · EDUCATIONAL USE</span>
        <span>END OF TRANSMISSION</span>
    </div>
    """,
    unsafe_allow_html=True,
)
