
import streamlit as st
from pathlib import Path
from datetime import datetime

# =========================================================
# 1. 기본 설정
# =========================================================

st.set_page_config(
    page_title="CELL VISION | Command Center",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"
PAGES_DIR = ROOT_DIR / "pages"

# =========================================================
# 2. 소기관 및 상세 페이지 정보
# =========================================================

ORGANELLES = {
    "핵": {
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "code": "BIO-01",
        "description": "유전 정보 보관 및 세포 활동 조절",
    },
    "리보솜": {
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "code": "BIO-02",
        "description": "유전 정보에 따른 단백질 합성",
    },
    "미토콘드리아": {
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "code": "BIO-03",
        "description": "세포 호흡과 ATP 생성",
    },
    "소포체": {
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "code": "BIO-04",
        "description": "단백질 및 지질의 합성과 수송",
    },
    "골지체": {
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "code": "BIO-05",
        "description": "물질의 변형, 분류 및 포장",
    },
    "리소좀": {
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "code": "BIO-06",
        "description": "세포 내 물질의 분해와 재활용",
    },
    "세포막": {
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "code": "BIO-07",
        "description": "세포 안팎의 물질 이동 조절",
    },
    "세포질": {
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "code": "BIO-08",
        "description": "다양한 세포 활동이 일어나는 공간",
    },
    "세포골격": {
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "code": "BIO-09",
        "description": "세포의 형태 유지와 세포 내 이동",
    },
}

# =========================================================
# 3. 공통 디자인
# =========================================================

st.markdown(
    """
    <style>
    :root {
        --bg-main: #080F1D;
        --bg-panel: #101B2D;
        --bg-panel-light: #14243B;
        --line: #243D5D;
        --blue: #58A6FF;
        --blue-light: #8BC5FF;
        --text-main: #E8F0FC;
        --text-sub: #91A5C1;
        --green: #76D7B0;
    }

    .stApp {
        background: var(--bg-main);
        color: var(--text-main);
    }

    [data-testid="stHeader"] {
        background: rgba(8, 15, 29, 0.96);
    }

    [data-testid="stSidebar"] {
        background: #0B1525;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] * {
        color: var(--text-main);
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, p, label {
        color: var(--text-main);
    }

    .eyebrow {
        color: var(--blue);
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.20em;
        margin-bottom: 0.55rem;
    }

    .main-title {
        color: #F3F7FF;
        font-size: clamp(2rem, 4vw, 3.5rem);
        font-weight: 800;
        letter-spacing: 0.035em;
        line-height: 1.15;
        margin: 0;
    }

    .subtitle {
        color: var(--text-sub);
        font-size: 0.98rem;
        margin-top: 0.7rem;
        line-height: 1.8;
    }

    .classified {
        display: inline-block;
        color: var(--blue-light);
        border: 1px solid #315D8B;
        background: #102642;
        padding: 0.35rem 0.65rem;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
    }

    .panel {
        background: var(--bg-panel);
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }

    .panel-label {
        color: var(--text-sub);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        margin-bottom: 0.6rem;
    }

    .panel-value {
        color: var(--blue-light);
        font-size: 1.35rem;
        font-weight: 800;
    }

    .panel-description {
        color: var(--text-sub);
        font-size: 0.84rem;
        line-height: 1.7;
        margin-top: 0.45rem;
    }

    .section-heading {
        color: #DDEBFF;
        font-size: 1.05rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        border-left: 3px solid var(--blue);
        padding-left: 0.75rem;
        margin: 1.4rem 0 1rem 0;
    }

    .organelle-card {
        background: #0D192A;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 1rem;
        min-height: 100px;
        margin-bottom: 0.5rem;
    }

    .organelle-code {
        color: var(--blue);
        font-size: 0.7rem;
        letter-spacing: 0.12em;
        font-weight: 700;
    }

    .organelle-title {
        color: #F0F5FF;
        font-size: 1.05rem;
        font-weight: 750;
        margin-top: 0.35rem;
        margin-bottom: 0.4rem;
    }

    .organelle-description {
        color: var(--text-sub);
        font-size: 0.8rem;
        line-height: 1.6;
    }

    .status-dot {
        display: inline-block;
        width: 7px;
        height: 7px;
        background: var(--green);
        border-radius: 50%;
        margin-right: 0.45rem;
    }

    .footer-note {
        border-top: 1px solid var(--line);
        margin-top: 2rem;
        padding-top: 1rem;
        color: #7287A3;
        font-size: 0.75rem;
        line-height: 1.8;
    }

    div.stButton > button,
    div.stPageLink > a {
        border-radius: 5px;
        border: 1px solid #315D8B;
        background: #102642;
        color: #DDEBFF;
        font-weight: 700;
        transition: 0.15s ease;
    }

    div.stButton > button:hover,
    div.stPageLink > a:hover {
        border-color: var(--blue);
        background: #173658;
        color: #FFFFFF;
    }

    div[data-testid="stImage"] img {
        border-radius: 6px;
    }

    hr {
        border-color: var(--line);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 4. 사이드바
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div class="eyebrow">BIOLOGICAL OPERATIONS UNIT</div>
        <h2 style="font-size:1.45rem; letter-spacing:0.08em;">
            CELL VISION
        </h2>
        <p style="color:#91A5C1; font-size:0.82rem; line-height:1.7;">
            세포 분석 시스템<br>
            생물학 정보 수집 및 임무 수행
        </p>
        <hr>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### 작전 메뉴")

    st.markdown(
        """
        <div class="panel-label">CURRENT LOCATION</div>
        <div style="color:#8BC5FF; font-weight:700;">
            01 / COMMAND CENTER
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("ACCESS LEVEL: BIOLOGY STUDY")
    st.caption("SYSTEM: ONLINE")

    st.markdown("---")
    st.markdown("#### 소기관 데이터베이스")

    for name, info in ORGANELLES.items():
        page_path = ROOT_DIR / info["page"]

        if page_path.is_file():
            st.page_link(
                info["page"],
                label=name,
                icon=None,
            )

# =========================================================
# 5. 상단 작전 정보
# =========================================================

top_left, top_right = st.columns([3, 1])

with top_left:
    st.markdown(
        '<div class="eyebrow">BIOLOGICAL INTELLIGENCE SYSTEM</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<h1 class="main-title">COMMAND CENTER</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="subtitle">
            세포 시스템 분석을 시작합니다.<br>
            목표를 선택하고, 구조와 기능에 관한 정보를 확보하십시오.
        </div>
        """,
        unsafe_allow_html=True,
    )

with top_right:
    st.markdown(
        """
        <div style="text-align:right; padding-top:0.5rem;">
            <div class="classified">RESTRICTED / BIO</div>
            <p style="color:#91A5C1; font-size:0.78rem; margin-top:0.8rem;">
                SYSTEM STATUS
            </p>
            <p style="color:#76D7B0; font-weight:700;">
                ● OPERATIONAL
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# =========================================================
# 6. 임무 현황 패널
# =========================================================

existing_pages = sum(
    1
    for info in ORGANELLES.values()
    if (ROOT_DIR / info["page"]).is_file()
)

existing_images = sum(
    1
    for info in ORGANELLES.values()
    if (IMAGE_DIR / info["image"]).is_file()
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-label">MISSION</div>
            <div class="panel-value">BIO-OPS 001</div>
            <div class="panel-description">
                세포 구조 및 소기관 기능 분석
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-label">DATABASE</div>
            <div class="panel-value">{existing_pages:02d} / {len(ORGANELLES):02d}</div>
            <div class="panel-description">
                연결된 소기관 상세 페이지
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-label">IMAGE ARCHIVE</div>
            <div class="panel-value">{existing_images:02d} / {len(ORGANELLES):02d}</div>
            <div class="panel-description">
                확인된 소기관 이미지 파일
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 7. 주요 임무 안내
# =========================================================

st.markdown(
    '<div class="section-heading">MISSION BRIEFING / 임무 브리핑</div>',
    unsafe_allow_html=True,
)

brief_left, brief_right = st.columns([1.4, 1])

with brief_left:
    st.markdown(
        """
        <div class="panel">
            <div class="eyebrow">OPERATION 01</div>
            <h3 style="margin-top:0;">CELL SYSTEM ANALYSIS</h3>
            <p style="color:#C0CEE2; line-height:1.9;">
                세포의 주요 구조를 확인하십시오.<br>
                각 소기관의 구조와 기능을 분석하고,
                세포 내 물질의 이동 및 에너지 전환 과정을 파악하십시오.
            </p>
            <hr>
            <div class="panel-label">PRIMARY OBJECTIVES</div>
            <p style="color:#91A5C1; line-height:2;">
                01 — 소기관의 위치와 구조 확인<br>
                02 — 소기관의 기능 및 교과 개념 분석<br>
                03 — 소기관 간 기능적 관계 파악
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with brief_right:
    st.markdown(
        """
        <div class="panel">
            <div class="panel-label">MISSION STATUS</div>
            <div class="panel-value">READY FOR ANALYSIS</div>
            <p class="panel-description">
                임무 상태: 대기<br>
                분석 대상: 동물세포<br>
                작전 유형: 생물학 정보 분석
            </p>
            <hr>
            <div class="panel-label">DIRECTIVE</div>
            <p style="color:#DDEBFF; line-height:1.8;">
                목표를 선택하십시오.<br>
                정보를 분석하십시오.<br>
                생물학적 근거로 판단하십시오.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 8. 소기관 데이터베이스
# =========================================================

st.markdown(
    '<div class="section-heading">TARGET RECON / 소기관 데이터베이스</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style="color:#91A5C1; font-size:0.88rem; line-height:1.8;">
        분석할 소기관을 선택하십시오. 각 항목에서 구조와 기능에 관한
        상세 자료를 확인할 수 있습니다.
    </p>
    """,
    unsafe_allow_html=True,
)

items = list(ORGANELLES.items())
columns_per_row = 3

for start in range(0, len(items), columns_per_row):
    row_items = items[start:start + columns_per_row]
    columns = st.columns(columns_per_row)

    for column, (name, info) in zip(columns, row_items):
        with column:
            st.markdown(
                f"""
                <div class="organelle-card">
                    <div class="organelle-code">{info["code"]}</div>
                    <div class="organelle-title">{name}</div>
                    <div class="organelle-description">
                        {info["description"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            image_path = IMAGE_DIR / info["image"]
            page_path = ROOT_DIR / info["page"]

            if image_path.is_file():
                st.image(
                    str(image_path),
                    width=180,
                    caption=None,
                )
            else:
                st.caption(f"이미지 확인 필요: {info['image']}")

            if page_path.is_file():
                st.page_link(
                    info["page"],
                    label=f"{info['code']} 자료 열기",
                    icon=None,
                    use_container_width=True,
                )
            else:
                st.caption("상세 페이지 파일을 확인해야 합니다.")

# =========================================================
# 9. 하단 상태 정보
# =========================================================

st.markdown(
    """
    <div class="footer-note">
        CELL VISION · BIOLOGICAL OPERATIONS UNIT<br>
        교육 목적의 세포 구조 및 기능 분석 시스템입니다.
        표시되는 임무 상태는 학습 화면의 안내 정보이며,
        실제 임무 수행이나 학습 진척을 자동으로 기록하지는 않습니다.
    </div>
    """,
    unsafe_allow_html=True,
)
