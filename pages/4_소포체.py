
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cell Vision - 소포체", layout="wide")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "er.png"

st.markdown("""
<style>
.stApp{background:#101820;color:#F1F5F9}
[data-testid="stSidebar"]{background:#17232E}
[data-testid="stHeader"]{background:#101820}
.block-container{padding-top:2rem;padding-bottom:3rem;max-width:1150px}
h1,h2,h3{color:#F1F5F9!important}
p,li,span,label{color:#D9E2EC}
.overview{background:#17232E;border-left:4px solid #63B3ED;border-radius:8px;padding:18px 22px;line-height:1.8;color:#E2E8F0}
.article-section{margin-top:30px;line-height:1.9}
.article-section h2{border-bottom:1px solid #344454;padding-bottom:9px;margin-bottom:15px}
.article-section h3{color:#90CDF4!important;margin-top:22px;margin-bottom:8px}
div.stButton>button{background:#233647;color:#F1F5F9;border:1px solid #52677A;border-radius:8px}
div.stButton>button:hover{background:#304B61;color:#FFF;border-color:#90CDF4}
hr{border-color:#344454}
</style>
""", unsafe_allow_html=True)

if st.button("← 메인 화면으로 돌아가기"):
    st.switch_page("app.py")

st.title("소포체")
st.caption("Endoplasmic Reticulum · 단백질과 지질의 합성 및 가공에 관여하는 막성 소기관")

st.divider()
image_col, overview_col = st.columns([1, 1.25], gap="large")
with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width="stretch")
    else:
        st.warning("images/er.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    소포체는 막으로 둘러싸인 관과 주머니가 연결된 구조로, 핵막과
    연결되어 있다. 리보솜이 붙어 있는 거친면 소포체는 주로 단백질의
    합성과 가공에 관여하고, 리보솜이 붙어 있지 않은 매끈면 소포체는
    지질 합성, 칼슘 이온 저장, 특정 물질의 대사 등에 관여한다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="article-section">

## 구조

### 거친면 소포체

거친면 소포체의 표면에는 리보솜이 결합해 있어 현미경으로 관찰하면
표면이 거칠게 보인다. 이곳에서는 세포 밖으로 분비될 단백질이나
세포막 및 일부 소기관의 막에 들어갈 단백질이 합성된다.
소포체 내부 공간은 단백질이 접히고 가공되는 환경을 제공한다.

### 매끈면 소포체

매끈면 소포체에는 표면에 결합한 리보솜이 없다. 막의 효소들은
인지질과 스테로이드 등의 지질 합성에 관여한다. 세포 종류에 따라
칼슘 이온을 저장하거나 약물과 유해 물질의 대사에 관여하기도 한다.

### 소포체 내부 공간

소포체 내부 공간은 단백질이 접히고 특정 화학적 변형을 받는 장소이다.
단백질은 올바른 입체 구조를 형성해야 기능을 수행할 수 있으므로,
소포체는 단백질의 품질 관리에도 중요한 역할을 한다.

## 주요 기능

### 단백질 합성과 가공

거친면 소포체와 연결된 리보솜에서 만들어지는 단백질 중 일부는
소포체 내부로 들어간다. 소포체에서는 단백질이 접히고,
일부 단백질에 당 사슬이 붙는 등의 가공이 일어난다.
정상적으로 접히지 않은 단백질은 품질 관리 과정을 거친다.

### 지질 합성

매끈면 소포체는 세포막과 소기관 막의 주요 구성 물질인 지질을
합성하는 데 관여한다. 합성된 지질은 세포 내 막의 성장과 유지에
사용된다.

### 칼슘 저장과 물질 대사

특정 세포의 소포체는 칼슘 이온을 저장했다가 필요할 때 방출하여
세포 신호와 근육 수축 등의 과정을 조절한다. 간세포 등에서는
특정 효소를 이용해 약물이나 여러 화합물의 대사에도 관여한다.

## 작동 원리

### 단백질의 소포체 진입

일부 단백질이 합성되기 시작하면 단백질에 있는 신호 서열이
이를 인식하는 운반 체계와 결합한다. 리보솜은 소포체 막에 연결되고,
단백질은 합성과 동시에 소포체 내부로 들어가거나 막에 삽입된다.

### 접힘과 품질 관리

소포체 내부의 보조 단백질은 새로 만들어진 단백질이 올바른
입체 구조를 형성하도록 돕는다. 잘못 접힌 단백질은 다시 접히는
과정을 거치거나 분해 경로로 보내진다. 이 과정은 기능하지 않는
단백질이 세포 안에 축적되는 것을 방지한다.

### 운반 소낭 형성

가공을 마친 단백질과 지질은 운반 소낭에 실려 소포체에서 떨어져
나온다. 운반 소낭은 골지체와 융합하여 내용물을 전달한다.
이러한 막의 이동을 통해 세포 내부의 물질이 목적지로 운반된다.

## 다른 세포소기관과의 관계

### 핵

소포체는 핵막의 바깥쪽 막과 연결되어 있다. 핵에서 전사된
전령 RNA는 세포질로 이동하고, 그 정보에 따라 만들어진 일부
단백질은 소포체로 들어간다.

### 리보솜

거친면 소포체 표면의 리보솜은 단백질을 합성한다. 합성되는
단백질의 신호 서열과 종류에 따라 리보솜이 소포체와 연결되어
작용할 수 있다.

### 골지체

소포체에서 만들어지고 가공된 물질은 골지체로 이동한다.
골지체는 이를 추가로 가공하고 분류하여 세포막이나 분비 소낭 등
적절한 장소로 전달한다.

</div>
""", unsafe_allow_html=True)
