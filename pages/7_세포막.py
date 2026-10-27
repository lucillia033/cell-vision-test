
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cell Vision - 세포막", layout="wide")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "membrane.png"

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

st.title("세포막")
st.caption("Cell Membrane · 세포 내부와 외부를 구분하고 물질 이동을 조절하는 막")

st.divider()
image_col, overview_col = st.columns([1, 1.25], gap="large")
with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width="stretch")
    else:
        st.warning("images/membrane.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    세포막은 세포의 내부와 외부를 구분하는 얇은 막이다. 기본적으로
    인지질 이중층으로 이루어져 있으며, 여러 막단백질과 탄수화물 등이
    함께 존재한다. 세포막은 모든 물질을 똑같이 통과시키지 않고
    물질의 성질과 세포의 필요에 따라 이동을 조절한다. 또한 외부 신호를
    감지하고 세포 사이의 상호작용을 돕는다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="article-section">

## 구조

### 인지질 이중층

인지질은 물과 잘 섞이는 친수성 머리와 물을 피하는 소수성 꼬리를
가진다. 물속에서 인지질은 머리가 세포 안팎의 수용액을 향하고
꼬리는 서로 마주 보는 이중층을 형성한다. 이 구조는 많은 이온과
극성 물질이 막을 자유롭게 통과하기 어렵게 만든다.

### 막단백질

막단백질은 물질의 이동, 외부 신호의 인식, 세포 사이의 부착 등
다양한 기능을 수행한다. 통로 단백질과 운반체 단백질은 특정 물질의
이동을 돕고, 수용체 단백질은 외부 신호 분자와 결합해 세포 내부에
신호를 전달할 수 있다.

### 콜레스테롤과 막 탄수화물

동물세포의 세포막에는 콜레스테롤이 존재하여 막의 유동성과
안정성을 조절한다. 막 바깥쪽의 일부 단백질과 지질에는 탄수화물
사슬이 붙어 있어 세포의 인식과 상호작용에 관여한다.

## 주요 기능

### 선택적 투과성

세포막은 물질마다 다른 투과성을 보인다. 작은 비극성 분자는
인지질 이중층을 비교적 쉽게 통과할 수 있지만, 이온이나 크기가 큰
극성 물질은 통로 단백질이나 운반체 등의 도움을 필요로 하는 경우가 많다.
이러한 선택적 투과성은 세포 내부의 조건을 일정하게 유지하는 데 중요하다.

### 신호 전달

세포막의 수용체는 호르몬과 같은 신호 분자를 인식할 수 있다.
신호가 수용체에 결합하면 세포 내부의 여러 반응이 활성화되거나
억제된다. 이를 통해 세포는 주변 환경의 변화에 대응한다.

### 세포 인식과 부착

세포막의 단백질과 탄수화물은 세포가 다른 세포를 인식하고
서로 결합하는 데 관여한다. 이러한 상호작용은 조직의 형성과
유지, 면역 반응 등 여러 생명 현상에 중요하다.

## 작동 원리

### 단순 확산

단순 확산은 물질이 농도가 높은 쪽에서 낮은 쪽으로 순이동하는
현상이다. 물질이 인지질 이중층을 직접 통과할 수 있다면 별도의
막 운반 단백질이나 ATP가 필요하지 않다.

### 촉진 확산

촉진 확산은 통로 단백질이나 운반체 단백질의 도움으로 물질이
농도 기울기를 따라 이동하는 방식이다. 물질은 높은 농도에서 낮은
농도로 순이동하며, 일반적으로 ATP를 직접 사용하지 않는다.

### 삼투

삼투는 선택적으로 투과하는 막을 사이에 두고 물이 이동하는 현상이다.
물은 용질 농도 차이와 막의 투과성에 따라 순이동한다. 삼투로 인해
세포의 부피가 달라질 수 있으므로 세포는 주변 용액의 농도에 영향을 받는다.

### 능동 수송

능동 수송은 물질을 농도 기울기에 거슬러 이동시키는 방식이다.
막단백질이 ATP 등의 에너지를 직접 이용하거나 다른 이온의
농도 기울기에 저장된 에너지를 이용한다. 이를 통해 세포는 필요한
이온 농도와 내부 환경을 유지한다.

### 세포내섭취와 세포외배출

세포내섭취에서는 세포막이 물질을 둘러싸 소낭을 형성해 세포 안으로
들여보낸다. 세포외배출에서는 소낭이 세포막과 융합하여 내부의
물질을 세포 밖으로 내보낸다. 큰 분자나 많은 양의 물질을 이동시킬 때
이러한 소낭 수송이 이용된다.

## 다른 세포소기관과의 관계

### 소포체와 골지체

소포체와 골지체는 세포막에 전달될 막단백질과 지질을 만들고
가공한다. 이 물질들은 운반 소낭을 통해 세포막으로 이동하여
막의 성장과 유지에 이용된다.

### 미토콘드리아

미토콘드리아에서 합성된 ATP는 세포막의 능동 수송 단백질이
물질을 이동시키는 데 사용될 수 있다. 따라서 에너지 대사와
세포막의 물질 수송은 서로 연결되어 있다.

### 리소좀

세포막은 세포내섭취로 외부 물질을 받아들이며, 그 물질은
세포 내 수송 경로를 거쳐 리소좀에서 분해될 수 있다.
반대로 리소좀 관련 소낭과 다른 소낭의 세포막 융합은 막의
구성과 재활용에도 기여한다.

</div>
""", unsafe_allow_html=True)
