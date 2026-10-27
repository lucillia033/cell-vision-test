
import streamlit as st
from pathlib import Path
from datetime import datetime

# ==========================================
# 기본 설정
# ==========================================

st.set_page_config(
    page_title="Cell Vision | Command Center",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

# ==========================================
# 세포 소기관 데이터
# ==========================================

ORGANELLES = [
    {
        "name": "핵",
        "code": "BIO-01",
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "description": "유전 정보를 보관하고 세포의 활동을 조절합니다.",
        "role": "GENETIC CONTROL",
    },
    {
        "name": "리보솜",
        "code": "BIO-02",
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "description": "mRNA의 유전 정보를 바탕으로 단백질을 합성합니다.",
        "role": "PROTEIN SYNTHESIS",
    },
    {
        "name": "미토콘드리아",
        "code": "BIO-03",
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "description": "세포 호흡을 통해 ATP를 생성합니다.",
        "role": "ENERGY PRODUCTION",
    },
    {
        "name": "소포체",
        "code": "BIO-04",
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "description": "단백질과 지질의 합성 및 세포 내 수송에 관여합니다.",
        "role": "INTRACELLULAR TRANSPORT",
    },
    {
        "name": "골지체",
        "code": "BIO-05",
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "description": "물질을 변형하고 분류하여 필요한 곳으로 보냅니다.",
        "role": "PROCESSING & SORTING",
    },
    {
        "name": "리소좀",
        "code": "BIO-06",
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "description": "가수 분해 효소로 세포 내 물질을 분해합니다.",
        "role": "INTRACELLULAR DIGESTION",
    },
    {
        "name": "세포막",
        "code": "BIO-07",
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "description": "세포 안팎의 물질 이동을 조절합니다.",
        "role": "SELECTIVE BARRIER",
    },
    {
        "name": "세포질",
        "code": "BIO-08",
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "description": "다양한 세포 구성 요소가 존재하며 여러 대사 반응이 일어납니다.",
        "role": "METABOLIC ENVIRONMENT",
    },
    {
        "name": "세포골격",
        "code": "BIO-09",
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "description": "세포의 형태를 유지하고 세포 내 이동을 돕습니다.",
        "role": "STRUCTURAL NETWORK",
    },
]

# ==========================================
# 디자인
# ==========================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    :root {
        --bg: #070b10;
        --panel: #0c131c;
        --panel-light: #111d29;
        --line: #26394a;
        --blue: #62c7e8;
        --blue-dim: #2b718e;
        --text: #e4edf4;
        --muted: #8295a6;
        --green: #80d6b0;
    }

    html, body, [class*="css"] {
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 50% 0%, #142536 0%, #070b10 52%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(7, 11, 16, 0.9);
    }

    [data-testid="stSidebar"] {
        background: #090f16;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div {
        padding-top: 1.2rem;
    }

    .block-container {
        max-width: 1600px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, label {
        color: var(--text);
    }

    .eyebrow {
        color: var(--blue);
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
    }

    .main-title {
        font-size: clamp(1.8rem, 3vw, 2.7rem);
        font-weight: 700;
        letter-spacing: 0.07em;
        color: #f1f7fb;
        line-height: 1.2;
        margin: 0.35rem 0 0.5rem 0;
    }

    .subtitle {
        color: var(--muted);
        font-size: 0.85rem;
        line-height: 1.7;
    }

    .top-strip {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
        padding: 0.75rem 1rem;
        margin-bottom: 1.4rem;
        border: 1px solid var(--line);
        background: rgba(12, 19, 28, 0.85);
        color: var(--muted);
        font-size: 0.72rem;
        letter-spacing: 0.08em;
    }

    .top-strip strong {
        color: var(--blue);
        font-weight: 600;
    }

    .section-heading {
        border-left: 3px solid var(--blue);
        padding-left: 0.8rem;
        margin: 1.6rem 0 1rem 0;
    }

    .section-heading h3 {
        margin: 0;
        font-size: 1rem;
        letter-spacing: 0.08em;
    }

    .section-heading p {
        color: var(--muted);
        font-size: 0.72rem;
        margin: 0.3rem 0 0 0;
    }

    .status-panel {
        border: 1px solid var(--line);
        background: linear-gradient(145deg, #101b27, #0a1018);
        padding: 1rem;
        min-height: 100px;
    }

    .status-label {
        font-size: 0.68rem;
        color: var(--muted);
        letter-spacing: 0.12em;
        margin-bottom: 0.6rem;
    }

    .status-value {
        font-size: 1.15rem;
        color: var(--blue);
        font-weight: 600;
    }

    .status-note {
        color: var(--muted);
        font-size: 0.7rem;
        margin-top: 0.35rem;
    }

    .analysis-panel {
        background: rgba(10, 17, 25, 0.92);
        border: 1px solid var(--line);
        padding: 1rem;
        min-height: 100%;
    }

    .panel-heading {
        color: var(--blue);
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        margin-bottom: 0.8rem;
    }

    .data-line {
        border-bottom: 1px solid #1c2a37;
        padding: 0.55rem 0;
        color: var(--muted);
        font-size: 0.74rem;
        line-height: 1.6;
    }

    .data-line strong {
        color: var(--text);
        font-weight: 500;
    }

    .directive {
        border-left: 2px solid var(--blue-dim);
        padding: 0.7rem 0.9rem;
        background: rgba(29, 71, 91, 0.16);
        color: #b9d5e3;
        font-size: 0.78rem;
        line-height: 1.8;
        margin-top: 1rem;
    }

    .organelle-card {
        background: linear-gradient(155deg, #101a25, #0a1017);
        border: 1px solid #263747;
        padding: 1rem;
        margin-bottom: 1rem;
        min-height: 100%;
    }

    .organelle-code {
        color: var(--blue);
        font-size: 0.68rem;
        letter-spacing: 0.12em;
        margin-bottom: 0.35rem;
    }

    .organelle-name {
        color: #edf5fa;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .organelle-description {
        color: #9eafbd;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 0.78rem;
        line-height: 1.8;
        min-height: 3rem;
        margin-bottom: 0.8rem;
    }

    .role-tag {
        color: #8fb6c9;
        font-size: 0.64rem;
        letter-spacing: 0.06em;
        margin: 0.6rem 0;
        overflow-wrap: anywhere;
    }

    .file-status {
        color: #a5bac8;
        font-size: 0.66rem;
        letter-spacing: 0.03em;
        line-height: 1.5;
        overflow-wrap: anywhere;
    }

    .file-status .dot {
        color: var(--green);
        font-size: 0.8rem;
    }

    .footer {
        border-top: 1px solid var(--line);
        margin-top: 2rem;
        padding-top: 1rem;
        color: #657989;
        font-size: 0.67rem;
        line-height: 1.8;
        letter-spacing: 0.04em;
    }

    div.stButton > button,
    div[data-testid="stPageLink"] a {
        border: 1px solid #35738e;
        border-radius: 0;
        background: #102431;
        color: #aeeaff;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        min-height: 2.35rem;
    }

    div.stButton > button:hover,
    div[data-testid="stPageLink"] a:hover {
        border-color: var(--blue);
        background: #173649;
        color: #ffffff;
    }

    div[data-testid="stPageLink"] a {
        justify-content: center;
        text-decoration: none;
        padding: 0.55rem 0.65rem;
    }

    div[data-testid="stImage"] {
        border: 1px solid #1b2a37;
        background: #080d13;
        padding: 0.35rem;
    }

    [data-testid="stMetric"] {
        background: #0c141d;
        border: 1px solid var(--line);
        padding: 0.8rem;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted);
    }

    [data-testid="stMetricValue"] {
        color: var(--blue);
    }

    hr {
        border-color: var(--line);
    }

    @media (max-width: 700px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .main-title {
            font-size: 1.7rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 사이드바
# ==========================================

with st.sidebar:
    st.markdown('<div class="eyebrow">CELL VISION / SYSTEM</div>', unsafe_allow_html=True)
    st.markdown("## COMMAND CENTER")
    st.caption("BIOLOGICAL INTELLIGENCE UNIT")

    st.divider()

    st.markdown("**MISSION MENU**")

    st.markdown(
        """
        <div class="data-line">01 / COMMAND CENTER</div>
        <div class="data-line">02 / CELL ANALYSIS</div>
        <div class="data-line">03 / INTELLIGENCE FILES</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")
    if st.button("RETURN TO COMMAND CENTER", use_container_width=True):
        st.switch_page("app.py")

    st.divider()

    st.markdown('<div class="eyebrow">SYSTEM STATUS</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="data-line">DATABASE <strong>LOCAL FILES</strong></div>
        <div class="data-line">INTERFACE <strong>ONLINE</strong></div>
        <div class="data-line">MODE <strong>RECONNAISSANCE</strong></div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")
    st.caption("CELL VISION // BIOLOGICAL DATA INTERFACE")

# ==========================================
# 상단 헤더
# ==========================================

current_time = datetime.now().strftime("%Y-%m-%d / %H:%M")

st.markdown(
    f"""
    <div class="top-strip">
        <span><strong>● SYSTEM ONLINE</strong> &nbsp; / &nbsp; BIOLOGICAL RECONNAISSANCE</span>
        <span>OPERATION: CELL ZERO</span>
        <span>LOCAL TIME: {current_time}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">BIOLOGICAL INTELLIGENCE / FIELD REPORT 001</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">CELL VISION</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">세포의 구조와 기능을 분석하는 생물학 정보 시스템입니다. '
    '각 소기관의 상세 자료에 접근하여 세포 내부의 작동 원리를 확인하세요.</div>',
    unsafe_allow_html=True,
)

st.markdown("")

# ==========================================
# 현황 패널
# ==========================================

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown(
        """
        <div class="status-panel">
            <div class="status-label">DATABASE / ORGANELLES</div>
            <div class="status-value">09 FILES</div>
            <div class="status-note">등록된 세포 구성 요소</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_b:
    st.markdown(
        """
        <div class="status-panel">
            <div class="status-label">ANALYSIS MODE</div>
            <div class="status-value">CELL STRUCTURE</div>
            <div class="status-note">세포 구조 및 기능 분석</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_c:
    available_images = sum(
        1 for item in ORGANELLES
        if (IMAGE_DIR / item["image"]).is_file()
    )
    st.markdown(
        f"""
        <div class="status-panel">
            <div class="status-label">IMAGE DATABASE</div>
            <div class="status-value">{available_images:02d} / 09</div>
            <div class="status-note">확인된 소기관 이미지 파일</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================
# 중앙 분석 영역
# ==========================================

st.markdown(
    """
    <div class="section-heading">
        <h3>01 / TARGET RECON</h3>
        <p>PRIMARY CELL ANALYSIS // TARGET OVERVIEW</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left_panel, center_panel, right_panel = st.columns([1, 1.6, 1], gap="medium")

with left_panel:
    st.markdown('<div class="analysis-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-heading">MISSION PARAMETERS</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="data-line">TARGET TYPE<br><strong>EUKARYOTIC CELL</strong></div>
        <div class="data-line">CELL CATEGORY<br><strong>ANIMAL CELL</strong></div>
        <div class="data-line">PRIMARY OBJECTIVE<br><strong>STRUCTURE IDENTIFICATION</strong></div>
        <div class="data-line">DATA CLASSIFICATION<br><strong>BIOLOGICAL</strong></div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with center_panel:
    st.markdown('<div class="analysis-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-heading">CELL OVERVIEW / VISUAL SCAN</div>', unsafe_allow_html=True)

    cell_image = IMAGE_DIR / "cell.png"

    if cell_image.is_file():
        st.image(str(cell_image), use_container_width=True)
    else:
        st.warning(
            "전체 세포 이미지 파일을 찾을 수 없습니다. "
            "저장소의 images 폴더에 cell.png가 있는지 확인하세요."
        )

    st.markdown(
        """
        <div class="directive">
            <strong>MISSION DIRECTIVE</strong><br>
            세포의 주요 소기관을 확인하고 각 구성 요소의 구조와 기능을 분석하세요.
            아래 데이터 파일에서 상세 정보에 접근할 수 있습니다.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with right_panel:
    st.markdown('<div class="analysis-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-heading">SYSTEM INTELLIGENCE</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="data-line">STRUCTURAL UNIT<br><strong>ORGANELLES</strong></div>
        <div class="data-line">ENERGY SYSTEM<br><strong>MITOCHONDRIA</strong></div>
        <div class="data-line">GENETIC ARCHIVE<br><strong>NUCLEUS</strong></div>
        <div class="data-line">PROTEIN FACTORY<br><strong>RIBOSOME</strong></div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="directive">
            ANALYSIS NOTE<br>
            소기관들은 독립적으로 작동하는 것이 아니라 서로 물질과 정보를 주고받으며
            세포의 생명 활동을 유지합니다.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 소기관 데이터베이스
# ==========================================

st.markdown(
    """
    <div class="section-heading">
        <h3>02 / INTELLIGENCE FILES</h3>
        <p>ORGANELLE DATABASE // SELECT A FILE TO ACCESS DETAILED INFORMATION</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "각 소기관의 설명을 확인한 뒤 해당 파일의 ACCESS FILE 버튼을 눌러 상세 페이지로 이동하세요."
)

for start in range(0, len(ORGANELLES), 3):
    row_items = ORGANELLES[start:start + 3]
    columns = st.columns(3, gap="medium")

    for column, item in zip(columns, row_items):
        with column:
            st.markdown('<div class="organelle-card">', unsafe_allow_html=True)

            st.markdown(
                f'<div class="organelle-code">{item["code"]} / BIOLOGICAL DATA</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="organelle-name">{item["name"]}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="organelle-description">{item["description"]}</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="role-tag">FUNCTION / {item["role"]}</div>',
                unsafe_allow_html=True,
            )

            # DATA FILE 문구와 ACCESS FILE 버튼을 같은 행에 배치
            status_col, button_col = st.columns(
                [1.35, 1],
                vertical_alignment="center",
                gap="small",
            )

            with status_col:
                st.markdown(
                    '<div class="file-status">'
                    '<span class="dot">●</span> DATA FILE / BIOLOGICAL'
                    '</div>',
                    unsafe_allow_html=True,
                )

            with button_col:
                page_path = ROOT_DIR / item["page"]

                if page_path.is_file():
                    st.page_link(
                        item["page"],
                        label="ACCESS FILE",
                        use_container_width=True,
                    )
                else:
                    st.button(
                        "FILE UNAVAILABLE",
                        key=f"missing_{item['code']}",
                        disabled=True,
                        use_container_width=True,
                    )

            # 소기관 이미지는 상태 문구와 버튼 아래에 표시
            image_path = IMAGE_DIR / item["image"]

            if image_path.is_file():
                st.image(str(image_path), use_container_width=True)
            else:
                st.warning(
                    f"이미지 파일을 찾을 수 없습니다: images/{item['image']}"
                )

            st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 하단 안내
# ==========================================

st.markdown(
    """
    <div class="footer">
        CELL VISION // BIOLOGICAL INTELLIGENCE INTERFACE<br>
        EDUCATIONAL PROJECT / CELL STRUCTURE AND FUNCTION<br>
        SYSTEM NOTICE: 상세 페이지 이동을 위해서는 pages 폴더에 해당 파이썬 파일이 있어야 합니다.
    </div>
    """,
    unsafe_allow_html=True,
)
