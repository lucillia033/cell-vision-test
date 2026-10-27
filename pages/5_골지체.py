
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cell Vision - 골지체", layout="wide")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "golgi.png"

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

st.title("골지체")
st.caption("Golgi Apparatus · 단백질과 지질을 가공하고 분류하여 운반하는 소기관")

st.divider()
image_col, overview_col = st.columns([1, 1.25], gap="large")
with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width="stretch")
    else:
        st.warning("images/golgi.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    골지체는 납작한 막성 주머니들이 층층이 쌓인 구조이다. 소포체에서
    전달된 단백질과 지질을 추가로 가공하고, 목적지에 따라 분류하여
    운반 소낭에 포장한다. 이러한 기능을 통해 세포는 만들어진 물질을
    세포막이나 세포 밖, 특정 소기관 등 필요한 장소로 보낼 수 있다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="article-section">

## 구조

### 시스면

시스면은 소포체에서 온 운반 소낭을 받아들이는 쪽이다. 소포체에서
합성되고 초기 가공을 거친 단백질과 지질이 이쪽으로 전달되어
골지체 내부의 처리 과정을 시작한다.

### 시스터나

시스터나는 골지체를 이루는 납작한 막성 주머니이다. 여러 시스터나가
층층이 배열되어 있으며, 각각의 구획에는 특정 물질을 가공하는
효소가 분포한다. 물질은 구획을 거치면서 단계적으로 변형될 수 있다.

### 트랜스면

트랜스면은 가공된 물질을 분류하여 내보내는 쪽이다. 단백질과
지질은 목적지에 따라 서로 다른 운반 소낭에 포장되어 세포막,
분비 경로 또는 특정 소기관으로 이동한다.

## 주요 기능

### 단백질과 지질의 가공

골지체는 단백질과 지질에 당 사슬을 붙이거나 기존의 당 사슬을
변형하는 등 여러 화학적 가공에 관여한다. 이러한 변형은 단백질의
안정성, 인식 기능, 이동 경로 등에 영향을 줄 수 있다.

### 물질의 분류와 포장

세포에서 만들어지는 모든 단백질이 같은 장소로 이동하는 것은 아니다.
골지체는 단백질과 지질에 포함된 분자적 표지와 운반 체계를 이용해
물질을 분류하고 적절한 운반 소낭에 포장한다.

### 분비와 막의 유지

골지체에서 만들어진 운반 소낭은 세포막과 융합해 내용물을 세포 밖으로
분비하거나 막의 구성 요소를 전달한다. 이를 통해 세포막의 구성과
세포 표면의 단백질 및 지질이 유지된다.

## 작동 원리

### 소포체에서 물질 받기

소포체에서 나온 운반 소낭은 골지체의 시스면과 융합하여 내용물을
전달한다. 단백질과 지질은 골지체 내부에서 여러 효소를 만나
단계적인 가공 과정을 거친다.

### 단계적 가공

골지체의 구획마다 서로 다른 효소가 작용할 수 있다. 이에 따라
단백질의 당 사슬이 변형되거나 특정 물질이 추가·제거된다.
가공 과정은 단백질의 종류와 최종 목적지에 따라 달라진다.

### 분류와 운반

트랜스면에서는 가공된 물질이 목적지에 따라 분류된다. 물질은
운반 소낭에 담겨 세포막으로 이동하거나 분비되며, 일부는 리소좀과
같은 소기관으로 전달된다. 소낭의 막은 목적지 막과 융합해 물질을
전달한다.

## 다른 세포소기관과의 관계

### 소포체

소포체는 골지체에 가공할 단백질과 지질을 전달한다. 두 소기관은
막으로 둘러싸인 운반 소낭을 통해 연결되어 세포 내 물질 수송 경로를
이룬다.

### 리소좀

리소좀에서 작용하는 여러 분해 효소는 소포체에서 합성된 뒤
골지체에서 가공·분류되어 전달된다. 이 과정을 통해 리소좀은
세포 안으로 들어온 물질이나 오래된 세포 구성 요소를 분해할 수 있다.

### 세포막

골지체에서 만들어진 소낭이 세포막과 융합하면 단백질과 지질이
막에 전달되거나 소낭 내부의 물질이 세포 밖으로 분비된다.
따라서 골지체는 세포막의 구성과 분비 활동을 유지하는 데 기여한다.

</div>
""", unsafe_allow_html=True)
