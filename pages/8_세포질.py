
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cell Vision - 세포질", layout="wide")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "cytosol.png"

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

st.title("세포질")
st.caption("Cytoplasm · 세포 내부에서 여러 대사 반응과 물질 이동이 이루어지는 공간")

st.divider()
image_col, overview_col = st.columns([1, 1.25], gap="large")
with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width="stretch")
    else:
        st.warning("images/cytosol.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    세포질은 일반적으로 핵을 제외한 세포 내부의 영역을 가리키며,
    세포질액과 여러 세포소기관 및 세포골격 등을 포함한다. 세포질액은
    물과 이온, 단백질, 여러 대사 물질이 녹아 있는 액체 성분이다.
    세포질에서는 해당과정과 같은 대사 반응이 일어나며, 물질이
    세포 안의 여러 장소로 이동하고 신호를 전달하는 과정도 이루어진다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="article-section">

## 구조

### 세포질액

세포질액은 세포 내부를 채우는 수용액 성분으로, 물을 비롯해
이온, 당, 아미노산, 단백질 및 여러 대사 물질을 포함한다.
물질들은 세포질액에 녹아 서로 이동하거나 효소 반응에 참여한다.

### 세포소기관이 존재하는 공간

세포질에는 미토콘드리아, 소포체, 골지체, 리소좀 등 다양한
세포소기관이 존재한다. 각 소기관은 막이나 내부 구조를 통해
특정 반응이 일어나기 적합한 환경을 제공한다. 이러한 구획화는
서로 다른 반응이 효율적으로 조절되도록 돕는다.

### 세포골격

세포골격은 세포질 내부에 그물처럼 분포하는 단백질 섬유 구조이다.
세포의 형태를 유지하고 세포소기관의 위치를 지지하며,
세포 내부에서 소낭과 여러 물질이 이동하는 데에도 관여한다.

## 주요 기능

### 대사 반응의 장소

세포질에서는 포도당을 분해하는 해당과정 등 여러 대사 반응이
일어난다. 효소는 각 반응의 진행을 촉진하며, 생성물은 다른
대사 경로에 이용될 수 있다. 세포질의 물질 조성과 조건은
대사 반응의 속도와 방향에 영향을 준다.

### 물질의 이동과 분배

세포 안의 물질은 세포질액에서 확산하거나 수송 단백질과
세포골격의 도움을 받아 이동한다. 다만 모든 물질이 세포질
전체를 자유롭게 이동하는 것은 아니며, 세포소기관의 막과
수송 체계가 이동 경로를 조절한다.

### 세포 내부 환경 유지

세포질액의 이온 농도와 산성도 등은 효소의 작용과 세포의
정상적인 기능에 영향을 준다. 세포는 막 수송과 대사 반응을
통해 이러한 조건을 조절한다.

## 작동 원리

### 효소 반응

세포질에는 여러 효소가 존재한다. 효소는 특정 반응의 활성화
에너지를 낮추어 반응이 빠르게 진행되도록 돕는다. 반응물은
효소와 결합해 생성물로 전환되며, 생성물은 다른 반응에 사용될 수 있다.

### 해당과정

해당과정은 세포질에서 일어나는 대표적인 대사 경로이다.
포도당 한 분자가 여러 단계를 거쳐 피루브산 두 분자로 분해되며,
이 과정에서 ATP와 NADH가 생성된다. 산소를 이용하는 세포 호흡에서는
피루브산이 미토콘드리아로 이동해 추가적인 산화 과정을 거친다.

### 확산과 세포 내부 수송

작은 분자와 이온은 농도 차이에 따라 확산할 수 있지만,
세포 내부의 장거리 물질 이동은 세포골격과 운동 단백질,
막성 소낭 등의 도움을 받기도 한다. 이러한 수송 체계는 물질이
필요한 장소에 적절하게 전달되도록 한다.

## 다른 세포소기관과의 관계

### 미토콘드리아

세포질에서 일어나는 해당과정의 생성물은 미토콘드리아로
전달되어 세포 호흡에 이용된다. 미토콘드리아에서 만들어진 ATP는
다시 세포질의 다양한 반응에 사용될 수 있다.

### 리보솜

세포질의 자유 리보솜은 세포질에서 기능하는 여러 단백질을 합성한다.
합성된 단백질은 세포질에 남아 효소나 구조 단백질로 작용하거나
다른 세포 내 장소로 이동할 수 있다.

### 세포골격과 세포막

세포골격은 세포질 내부의 형태와 물질 이동을 지원한다.
세포막은 세포질과 외부 환경 사이의 물질 교환을 조절하여
세포질의 조건이 유지되도록 돕는다.

</div>
""", unsafe_allow_html=True)
