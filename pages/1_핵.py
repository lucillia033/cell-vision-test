
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cell Vision | 핵",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent.parent
NUCLEUS_IMAGE = ROOT_DIR / "images" / "nucleus.png"

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
        line-height: 1.9;
    }

    .system-banner {
        border: 1px solid #25465A;
        border-left: 4px solid #38BDF8;
        background: linear-gradient(110deg, #101D2B, #0A1420);
        padding: 18px 22px;
        margin-bottom: 28px;
        border-radius: 5px;
    }

    .system-name {
        color: #67E8F9;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.2em;
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
        letter-spacing: 0.16em;
        margin-bottom: 8px;
    }

    .overview-panel {
        background: #101B2A;
        border: 1px solid #26394C;
        border-top: 3px solid #38BDF8;
        padding: 22px 24px;
        border-radius: 5px;
        line-height: 2;
        color: #DCE8F3;
    }

    .article-section {
        background: #0D1724;
        border: 1px solid #223447;
        border-radius: 5px;
        padding: 24px 28px;
        margin-top: 22px;
        line-height: 1.95;
    }

    .article-section h2 {
        color: #F3F8FC !important;
        border-bottom: 1px solid #2B455B;
        padding-bottom: 12px;
        margin-top: 12px;
        margin-bottom: 18px;
    }

    .article-section h3 {
        color: #67DDF5 !important;
        margin-top: 24px;
        margin-bottom: 8px;
    }

    div.stButton > button {
        background: #142538;
        color: #EAF6FF;
        border: 1px solid #31536C;
        border-radius: 4px;
        padding: 0.55rem 1rem;
    }

    div.stButton > button:hover {
        background: #1B354A;
        color: #FFFFFF;
        border-color: #38BDF8;
    }

    hr {
        border-color: #26394C;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="system-banner">
        <div class="system-name">CELL VISION // BIOLOGICAL INTELLIGENCE SYSTEM</div>
        <div class="system-subtitle">CELLULAR STRUCTURE DATABASE · NUCLEUS</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

st.title("핵")
st.caption(
    "Nucleus · 세포의 유전 정보를 보관하고 유전자 발현을 조절하는 소기관"
)

st.divider()

image_col, overview_col = st.columns([1, 1.25], gap="large")

with image_col:
    st.markdown('<div class="section-label">STRUCTURE VISUALIZATION</div>',
                unsafe_allow_html=True)

    if NUCLEUS_IMAGE.is_file():
        st.image(str(NUCLEUS_IMAGE), use_container_width=True)
    else:
        st.warning(
            "핵 이미지를 찾을 수 없습니다. "
            "프로젝트의 images 폴더에 nucleus.png 파일이 있는지 확인해 주세요."
        )

with overview_col:
    st.markdown('<div class="section-label">ORGANELLE PROFILE</div>',
                unsafe_allow_html=True)
    st.subheader("개요")

    st.markdown(
        """
        <div class="overview-panel">
        핵은 진핵세포에서 유전 물질인 DNA를 보관하고,
        유전 정보가 세포의 구조와 기능에 활용되는 과정을 조절하는
        세포소기관이다. DNA에는 단백질 합성 및 세포 활동에 필요한
        유전 정보가 담겨 있다.

        핵은 핵막으로 둘러싸여 있으며, 핵 내부에는 염색질과 인 등이
        존재한다. 핵막의 핵공을 통해 RNA와 단백질을 비롯한 물질이
        핵과 세포질 사이를 이동한다.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="article-section">

    ## 구조

    ### 핵막

    핵막은 핵 내부와 세포질을 구분하는 막 구조이다. 일반적으로
    두 겹의 막으로 이루어져 있으며, 핵막의 바깥쪽 막은
    소포체 막과 연결되어 있다. 핵막은 핵 내부 환경을 유지하고
    유전 물질이 세포질의 다른 구성 요소와 직접 섞이지 않도록
    구획을 형성한다.

    ### 핵공

    핵공은 핵막에 존재하는 단백질 복합체로, 핵과 세포질 사이의
    물질 이동을 조절한다. 작은 분자는 조건에 따라 통과할 수 있으며,
    RNA나 단백질과 같은 큰 분자는 운반 체계의 도움을 받아 이동한다.
    예를 들어, 핵에서 만들어진 전령 RNA는 핵공을 통해 세포질로
    이동하여 단백질 합성에 이용된다.

    ### 염색질

    염색질은 DNA와 단백질이 결합한 물질이다. DNA는 히스톤 단백질
    등의 도움을 받아 정리되고 포장된다. 세포가 분열할 때에는
    염색질이 응축되어 염색체의 형태로 관찰된다. 염색질의 포장
    상태는 유전 정보에 접근할 수 있는 정도와도 관련이 있다.

    ### 인

    인은 핵 내부에 존재하는 구조로, 리보솜을 구성하는 리보솜 RNA와
    단백질이 결합하는 과정에 중요한 역할을 한다. 인에서 만들어진
    리보솜의 구성 요소는 핵공을 통해 세포질로 이동하고,
    그곳에서 리보솜의 기능적 구조를 형성한다.

    ## 주요 기능

    ### 유전 정보의 보관

    핵은 DNA를 보관하여 세포가 단백질을 합성하고 생명 활동을
    유지하는 데 필요한 유전 정보를 보호한다. DNA에 저장된 정보는
    세포의 특성과 기능에 영향을 준다.

    ### 유전자 발현 조절

    핵에서는 DNA의 특정 부분에 담긴 정보가 RNA로 전사되는 과정이
    일어난다. 어떤 유전자가 언제 얼마나 발현되는지는 세포의 종류,
    발달 단계, 외부 환경 등에 따라 조절된다. 이러한 조절은 세포가
    필요한 단백질을 적절한 시점에 만들도록 하는 데 중요하다.

    ### 세포 분열과 유전 정보 전달

    세포가 분열할 때에는 DNA가 복제되고 유전 물질이 딸세포에
    적절히 분배되어야 한다. 염색질은 분열 과정에서 염색체 형태로
    응축되며, 이를 통해 유전 물질이 정돈된 상태로 이동할 수 있다.

    ## 작동 원리

    ### 전사

    전사는 DNA의 유전 정보를 RNA로 옮기는 과정이다. RNA 중합효소가
    DNA의 특정 부분을 주형으로 삼아 상보적인 RNA 가닥을 합성한다.
    단백질 합성에 사용되는 전령 RNA는 이 과정을 통해 만들어진다.

    진핵세포에서는 전령 RNA가 만들어진 뒤 가공 과정을 거친다.
    이 과정에는 인트론 제거와 엑손 연결 등이 포함될 수 있다.
    가공된 전령 RNA는 핵공을 통해 세포질로 이동한다.

    ### 단백질 합성으로 이어지는 과정

    핵에서 만들어진 전령 RNA는 세포질의 리보솜으로 전달된다.
    리보솜은 전령 RNA의 코돈을 읽고, 운반 RNA가 가져온 아미노산을
    순서대로 연결하여 폴리펩타이드를 합성한다.

    이처럼 핵은 단백질을 직접 합성하는 장소는 아니지만,
    단백질 합성에 필요한 유전 정보를 제공한다는 점에서
    세포의 단백질 생산 과정에 핵심적인 역할을 한다.

    ## 다른 세포소기관과의 관계

    ### 리보솜

    핵의 인에서는 리보솜 RNA와 리보솜 단백질이 결합하는 과정이
    이루어진다. 리보솜의 구성 요소는 세포질로 이동하여 기능적인
    리보솜을 형성한다. 리보솜은 핵에서 전달된 전령 RNA의 정보를
    바탕으로 단백질을 합성한다.

    ### 소포체

    핵막의 바깥쪽 막은 소포체와 연결되어 있다. 특히 거친면
    소포체에는 리보솜이 붙어 있어 세포 밖으로 분비되거나 세포막,
    특정 소기관의 막에 사용될 단백질을 합성하고 가공하는 과정에
    관여한다.

    ### 골지체

    골지체는 소포체에서 전달된 단백질과 지질을 추가로 가공하고
    분류하여 필요한 장소로 운반한다. 따라서 핵에서 시작된 유전
    정보의 발현은 리보솜, 소포체, 골지체의 활동과 연결되어
    세포가 필요한 물질을 생산하고 배치하는 과정으로 이어진다.

    </div>
    """,
    unsafe_allow_html=True,
)
