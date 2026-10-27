
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

# =========================================================
# 2. 소기관 정보
# 이미지 파일은 모두 PNG 형식
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
# 3. 전술 분석실 디자인
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
        margin-bottom: 10px;
        min-height: 205px;
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
# 4. 사이드바: 작전 메뉴
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div class="side-brand">
            <div class="side-brand-title">CELL VISION</div>
            <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
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

    st.markdown(
        """
        <div class="side-section">03 / SYSTEM MONITOR</div>
        <div class="side-info">
            SYSTEM STATUS&nbsp;&nbsp; <span style="color:#8bd9b0;">ONLINE</span><br>
            DATABASE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; LOCAL FILES<br>
            SECURITY LEVEL&nbsp; BIO-RESTRICTED<br>
            ACCESS MODE&nbsp;&nbsp;&nbsp;&nbsp; EDUCATIONAL
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("CELL VISION / INTERNAL USE")

# =========================================================
# 5. 상단 전술 시스템 바
# =========================================================

current_time = datetime.now().strftime("%Y-%m-%d")

st.markdown(
    f"""
    <div class="top-strip">
        <span>CV // BIOLOGICAL INTELLIGENCE SYSTEM</span>
        <span>SECURITY LEVEL: <strong>RESTRICTED</strong></span>
        <span>SYSTEM STATUS: <strong>OPERATIONAL</strong></span>
        <span>{current_time}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="eyebrow">TACTICAL BIOLOGY INTERFACE // TERMINAL 01</div>
    <h1 class="main-title">COMMAND CENTER</h1>
    <div class="subtitle">
        CELLULAR STRUCTURE ANALYSIS · BIOLOGICAL INTELLIGENCE · MISSION CONTROL
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 6. 상황 정보 패널
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
            <div class="panel-value"><span class="status-dot">●</span> STANDING BY</div>
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
# 7. 중앙 분석 화면
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
# 8. 소기관 정보 파일
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
                    <div class="intel-code">{organelle["code"]} // INTELLIGENCE FILE</div>
                    <div class="intel-name">{organelle["name"]}</div>
                    <div class="intel-description">{organelle["description"]}</div>
                    <div class="intel-status">● DATA FILE / BIOLOGICAL</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

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

            page_path = ROOT_DIR / organelle["page"]

            if page_path.exists():
                st.page_link(
                    organelle["page"],
                    label=f'ACCESS FILE / {organelle["name"]}',
                )
            else:
                st.caption(
                    f'상세 페이지 파일 확인 필요: {organelle["page"]}'
                )

# =========================================================
# 9. 작전 지침
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

st.markdown(
    """
    <div class="footer-line">
        <span>CELL VISION // BIOLOGICAL OPERATIONS UNIT</span>
        <span>INTERNAL SYSTEM · EDUCATIONAL USE</span>
        <span>END OF TRANSMISSION</span>
    </div>
    """,
    unsafe_allow_html=True,
)
