
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Vision",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent
IMAGE_DIR = ROOT_DIR / "images"

ORGANELLES = {
    "핵": {
        "image": "nucleus.png",
        "page": "pages/1_핵.py",
        "description": "유전 정보 보관과 발현 조절",
    },
    "리보솜": {
        "image": "ribosome.png",
        "page": "pages/2_리보솜.py",
        "description": "단백질 합성",
    },
    "미토콘드리아": {
        "image": "mitochondria.png",
        "page": "pages/3_미토콘드리아.py",
        "description": "세포 호흡과 ATP 합성",
    },
    "소포체": {
        "image": "er.png",
        "page": "pages/4_소포체.py",
        "description": "단백질과 지질의 합성 및 수송",
    },
    "골지체": {
        "image": "golgi.png",
        "page": "pages/5_골지체.py",
        "description": "물질의 가공과 분류",
    },
    "리소좀": {
        "image": "lysosome.png",
        "page": "pages/6_리소좀.py",
        "description": "세포 내 소화와 물질 재활용",
    },
    "세포막": {
        "image": "membrane.png",
        "page": "pages/7_세포막.py",
        "description": "물질 이동과 세포 보호",
    },
    "세포질": {
        "image": "cytosol.png",
        "page": "pages/8_세포질.py",
        "description": "세포 내 대사 반응",
    },
    "세포골격": {
        "image": "cytoskeleton.png",
        "page": "pages/9_세포골격.py",
        "description": "세포 형태 유지와 내부 수송",
    },
}

# 공통 디자인
st.markdown(
    """
    <style>
    .stApp {
        background: #080E17;
        color: #EAF2FA;
    }

    [data-testid="stSidebar"] {
        background: #101B2A;
        border-right: 1px solid #26394C;
    }

    [data-testid="stHeader"] {
        background: #080E17;
    }

    /* Streamlit이 자동 생성하는 위쪽 페이지 메뉴 숨기기 */
    [data-testid="stSidebarNav"] {
        display: none;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #F3F8FC !important;
    }

    p, li, label {
        color: #D0DCE8;
    }

    .system-banner {
        background: #101B2A;
        border: 1px solid #26394C;
        border-left: 4px solid #38BDF8;
        border-radius: 5px;
        padding: 18px 22px;
        margin-bottom: 26px;
    }

    .system-name {
        color: #67E8F9;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.16em;
    }

    .system-subtitle {
        color: #91A8BC;
        font-size: 0.85rem;
        margin-top: 7px;
    }

    .section-label {
        color: #67E8F9;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        margin-bottom: 10px;
    }

    .intro-panel {
        background: #101B2A;
        border: 1px solid #26394C;
        border-top: 3px solid #38BDF8;
        border-radius: 5px;
        padding: 20px 24px;
        line-height: 1.9;
        color: #DCE8F3;
        margin-bottom: 25px;
    }

    .organelles-heading {
        border-bottom: 1px solid #26394C;
        padding-bottom: 12px;
        margin-top: 32px;
        margin-bottom: 20px;
    }

    [data-testid="stSidebar"] [data-testid="stPageLink"] a {
        background: #142538;
        border: 1px solid #263F54;
        border-radius: 5px;
        padding: 9px 12px;
        margin-bottom: 5px;
        color: #EAF2FA !important;
    }

    [data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
        background: #1B354A;
        border-color: #38BDF8;
    }

    [data-testid="stSidebar"] [data-testid="stPageLink"] p {
        color: #EAF2FA !important;
    }

    hr {
        border-color: #26394C;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# 사이드바: 하나의 통합 메뉴
# --------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 12px 4px 18px 4px;">
            <div style="
                color:#67E8F9;
                font-size:0.78rem;
                font-weight:700;
                letter-spacing:0.16em;">
                CELL VISION
            </div>
            <div style="
                color:#91A8BC;
                font-size:0.78rem;
                margin-top:6px;">
                BIOLOGICAL NAVIGATION
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        '<div class="section-label">MAIN</div>',
        unsafe_allow_html=True,
    )

    # app 버튼: 메인 화면으로 이동
    st.page_link(
        "app.py",
        label="app",
        icon=None,
    )

    st.divider()

    st.markdown(
        '<div class="section-label">CELL ORGANELLES</div>',
        unsafe_allow_html=True,
    )

    # 소기관 이동 메뉴는 이 한 세트만 표시
    for organelle_name, organelle_info in ORGANELLES.items():
        st.page_link(
            organelle_info["page"],
            label=organelle_name,
            icon=None,
        )

    st.divider()

    st.caption("CELL VISION · ORGANELLE EXPLORER")

# --------------------------------------------------
# 메인 화면
# --------------------------------------------------
st.markdown(
    """
    <div class="system-banner">
        <div class="system-name">
            CELL VISION // BIOLOGICAL INTELLIGENCE SYSTEM
        </div>
        <div class="system-subtitle">
            CELLULAR STRUCTURE DATABASE · MAIN TERMINAL
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.title("Cell Vision")
st.caption("동물세포의 구조와 세포소기관 탐구")

st.markdown(
    """
    <div class="intro-panel">
        세포를 구성하는 주요 소기관을 탐색하고 각 구조의 특징,
        기능, 작동 원리 및 다른 소기관과의 관계를 살펴보세요.
        아래의 소기관 목록이나 왼쪽 탐색 메뉴에서 원하는 항목을 선택할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True,
)

# 전체 세포 이미지
CELL_IMAGE = IMAGE_DIR / "cell.png"

if CELL_IMAGE.is_file():
    image_col, info_col = st.columns([1.2, 1], gap="large")

    with image_col:
        st.image(
            str(CELL_IMAGE),
            use_container_width=True,
        )

    with info_col:
        st.markdown(
            '<div class="section-label">CELL OVERVIEW</div>',
            unsafe_allow_html=True,
        )
        st.subheader("세포 구조 탐색")

        st.markdown(
            """
            동물세포는 서로 다른 구조와 기능을 가진 여러 세포소기관으로
            이루어져 있습니다. 각 소기관은 독립적인 기능을 수행하면서도
            서로 물질과 정보를 주고받아 세포의 생명 활동을 유지합니다.

            **탐색 방법**

            1. 왼쪽 메뉴에서 소기관을 선택합니다.
            2. 각 페이지에서 이미지와 개요를 확인합니다.
            3. 구조, 주요 기능, 작동 원리 및 다른 소기관과의 관계를 살펴봅니다.
            """
        )
else:
    st.warning(
        "전체 세포 이미지를 찾을 수 없습니다. "
        "images 폴더에 cell.png 파일이 있는지 확인해 주세요."
    )

st.markdown(
    '<div class="organelles-heading"><h2>소기관 목록</h2></div>',
    unsafe_allow_html=True,
)

# 소기관 카드
organelles_list = list(ORGANELLES.items())
columns_per_row = 3

for start in range(0, len(organelles_list), columns_per_row):
    row_items = organelles_list[start:start + columns_per_row]
    columns = st.columns(columns_per_row, gap="large")

    for column, (organ_name, organ_info) in zip(columns, row_items):
        with column:
            st.markdown(
                """
                <div style="
                    background:#101B2A;
                    border:1px solid #26394C;
                    border-top:3px solid #234B65;
                    border-radius:5px;
                    padding:15px;
                    min-height:90px;">
                """,
                unsafe_allow_html=True,
            )

            image_path = IMAGE_DIR / organ_info["image"]

            if image_path.is_file():
                st.image(
                    str(image_path),
                    use_container_width=True,
                )
            else:
                st.warning(
                    f"{organ_name} 이미지를 찾을 수 없습니다."
                )

            st.subheader(organ_name)
            st.caption(organ_info["description"])

            st.page_link(
                organ_info["page"],
                label=f"{organ_name} 페이지 열기",
                icon=None,
                use_container_width=True,
            )

            st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.caption(
    "Cell Vision · Animal Cell Organelle Explorer"
)
