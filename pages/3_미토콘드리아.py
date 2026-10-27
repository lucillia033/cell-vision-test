
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cell Vision - 미토콘드리아", layout="wide")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "mitochondria.png"

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

st.title("미토콘드리아")
st.caption("Mitochondrion · 세포 호흡을 통해 ATP를 합성하는 소기관")

st.divider()
image_col, overview_col = st.columns([1, 1.25], gap="large")
with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width="stretch")
    else:
        st.warning("images/mitochondria.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    미토콘드리아는 유기물에 저장된 에너지를 이용해 ATP를 합성하는
    세포소기관이다. 내부와 외부에 두 겹의 막이 있으며, 안쪽 막은
    크리스타라고 하는 주름진 구조를 이룬다. 기질과 내막은 세포 호흡의
    여러 반응이 일어나는 장소를 제공한다. 미토콘드리아는 자체 DNA와
    리보솜도 가지고 있다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="article-section">

## 구조

### 외막

외막은 미토콘드리아의 바깥을 둘러싼 막이다. 여러 물질의 출입에
관여하는 단백질이 존재하며, 미토콘드리아의 내부 환경을 외부와
구분한다.

### 내막과 크리스타

내막은 외막보다 선택적으로 물질의 이동을 조절한다. 내막이 안쪽으로
접혀 형성된 크리스타에는 전자 전달계의 단백질과 ATP 합성효소가
존재한다. 주름진 구조는 막의 표면적을 넓혀 에너지 합성에 필요한
단백질이 작용할 공간을 제공한다.

### 기질

기질은 내막 안쪽을 채우는 공간이다. 이곳에는 여러 대사 효소와
미토콘드리아 DNA, 리보솜이 존재한다. 피루브산 산화와 시트르산
회로의 주요 반응이 기질에서 일어난다.

## 주요 기능

### ATP 합성

ATP는 세포에서 다양한 반응에 에너지를 전달하는 분자이다.
미토콘드리아는 유기물이 분해되는 과정에서 방출되는 에너지를 이용해
ADP와 무기 인산으로부터 ATP를 합성한다.

### 대사 조절

미토콘드리아는 세포 호흡뿐 아니라 세포 내 칼슘 농도 조절,
활성산소 생성과 제거의 균형, 세포 사멸 신호 등에도 관여한다.
따라서 미토콘드리아의 역할은 단순히 에너지를 생산하는 데 그치지 않는다.

## 작동 원리

### 해당과정과 피루브산의 이동

포도당의 해당과정은 세포질에서 일어나며, 포도당이 분해되어
피루브산과 소량의 ATP가 생성된다. 산소를 이용하는 세포 호흡에서는
피루브산이 미토콘드리아로 이동해 추가적인 산화 과정을 거친다.

### 시트르산 회로

피루브산에서 유래한 아세틸-CoA는 기질에서 시트르산 회로에
들어간다. 이 과정에서 이산화탄소가 방출되고, 전자 운반체인
NADH와 FADH₂가 생성된다. 이 운반체는 높은 에너지를 가진 전자를
전자 전달계로 전달한다.

### 전자 전달계와 화학 삼투

전자 전달계는 내막에 위치한 여러 단백질 복합체로 이루어진다.
전자가 전달되는 동안 방출되는 에너지로 수소 이온이 기질에서
막 사이 공간으로 이동한다. 이로 인해 내막 양쪽에 수소 이온의
농도 차와 전기적 차이가 형성된다.

수소 이온은 ATP 합성효소를 통과해 기질 쪽으로 이동한다.
이 흐름에서 얻은 에너지를 ATP 합성효소가 이용하여 ATP를 만든다.
이 원리를 화학 삼투라고 한다. 산소는 전자 전달계의 마지막
전자 수용체로 작용하며, 전자와 수소 이온을 받아 물이 생성된다.

## 다른 세포소기관과의 관계

### 세포질

해당과정은 세포질에서 일어나며, 여기서 생성된 피루브산은
미토콘드리아로 이동한다. 따라서 세포질과 미토콘드리아의 대사
작용은 연속적으로 연결되어 있다.

### 핵

미토콘드리아의 여러 단백질은 핵의 DNA에 있는 유전 정보에 따라
세포질의 리보솜에서 합성된 뒤 미토콘드리아로 운반된다. 미토콘드리아는
자체 DNA도 가지고 있지만, 기능에 필요한 모든 단백질을 자체적으로
만들지는 못한다.

### 세포막

세포막의 수송체는 포도당 등 세포 호흡에 필요한 물질의 세포 내
유입에 관여한다. 미토콘드리아에서 만들어진 ATP는 세포질에서
일어나는 능동 수송과 다양한 생명 활동에 사용된다.

</div>
""", unsafe_allow_html=True)
