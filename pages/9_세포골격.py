
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cell Vision - 세포골격", layout="wide")
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "cytoskeleton.png"

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

st.title("세포골격")
st.caption("Cytoskeleton · 세포의 형태와 내부 구조를 지지하고 움직임을 돕는 단백질 섬유 체계")

st.divider()
image_col, overview_col = st.columns([1, 1.25], gap="large")
with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), width="stretch")
    else:
        st.warning("images/cytoskeleton.png 파일을 찾을 수 없습니다.")

with overview_col:
    st.subheader("개요")
    st.markdown("""
    <div class="overview">
    세포골격은 세포 내부에 분포하는 단백질 섬유의 체계이다. 세포의
    형태를 지지하고 세포소기관의 위치를 유지하며, 세포 내부의 물질
    수송과 세포 운동에도 관여한다. 주요 구성 요소에는 미세소관,
    미세섬유, 중간섬유가 있으며, 각각의 구조와 성질에 따라 서로 다른
    기능을 수행한다.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="article-section">

## 구조

### 미세소관

미세소관은 튜불린 단백질로 이루어진 속이 빈 관 형태의 섬유이다.
세포 내부에서 물질이 이동하는 경로가 되며, 세포 분열 때 염색체를
분리하는 방추사의 주요 구성 요소가 된다. 일부 세포에서는 섬모와
편모의 구조를 형성하는 데에도 관여한다.

### 미세섬유

미세섬유는 주로 액틴 단백질로 이루어진 가는 섬유이다. 세포막
아래쪽에 분포하여 세포의 형태를 유지하고, 세포의 모양 변화와
이동, 근육 수축, 세포질 분열 등에 관여한다.

### 중간섬유

중간섬유는 여러 종류의 섬유 단백질로 구성되며, 세포에 기계적
강도를 제공한다. 세포가 당기거나 눌리는 힘을 받을 때 구조를
지지하고, 핵과 세포 내부의 일부 구조가 안정적으로 유지되도록 돕는다.

## 주요 기능

### 세포 형태 유지

세포골격은 세포 내부에 지지 구조를 제공하여 세포가 일정한
형태를 유지하도록 돕는다. 세포 종류와 기능에 따라 섬유의
배열과 밀도가 달라질 수 있다.

### 세포 내 물질 수송

미세소관은 소낭과 일부 세포소기관이 이동하는 경로로 작용한다.
운동 단백질은 ATP의 에너지를 이용해 이러한 구조물을 섬유를 따라
운반한다. 이를 통해 물질이 세포 내부의 적절한 장소에 전달된다.

### 세포 분열

세포 분열 과정에서 미세소관은 방추사를 형성한다. 방추사는
염색체에 연결되어 염색체가 딸세포로 분배되도록 돕는다.
액틴 미세섬유는 동물세포의 세포질 분열에서 수축환을 형성해
세포가 두 개로 나뉘는 과정에 관여한다.

### 세포 운동

액틴과 미오신의 상호작용은 세포의 형태 변화와 이동, 근육 수축에
중요하다. 미세소관과 운동 단백질은 섬모와 편모의 움직임에도
관여할 수 있다.

## 작동 원리

### 섬유의 조립과 분해

세포골격 섬유는 고정된 구조가 아니라 구성 단백질이 결합하거나
분리되면서 재구성될 수 있다. 세포는 섬유의 조립과 분해를 조절하여
필요한 위치에 구조를 만들거나 이동 방향을 바꾼다.

### 운동 단백질의 작용

키네신과 다이네인은 주로 미세소관을 따라 물질을 운반하는
운동 단백질이다. 미오신은 액틴과 상호작용하여 힘을 발생시킨다.
이들 단백질은 ATP의 에너지를 이용해 구조적 변화를 일으키며,
세포 내부의 물질 이동과 움직임을 가능하게 한다.

### 세포 분열 중 방추사 형성

세포 분열이 진행되면 미세소관이 재배열되어 방추사를 형성한다.
방추사는 염색체에 연결되고, 미세소관의 길이 변화와 운동 단백질의
작용을 통해 염색체가 서로 반대쪽으로 이동하도록 돕는다.

## 다른 세포소기관과의 관계

### 핵

중간섬유의 한 종류인 라민은 핵막 안쪽에서 핵막을 지지하는
핵라미나를 형성한다. 핵라미나는 핵의 형태 유지와 염색질의
배열 및 핵 기능 조절에도 관여한다.

### 소포체와 골지체

소포체와 골지체에서 만들어진 운반 소낭은 세포골격과 운동 단백질의
도움을 받아 이동할 수 있다. 이러한 수송은 단백질과 지질이
세포 내부의 목적지로 전달되는 데 중요하다.

### 세포막

세포골격은 세포막 안쪽과 연결되어 세포의 형태를 지지하고
막의 일부 단백질이 위치를 유지하도록 돕는다. 액틴 섬유의 재구성은
세포막의 돌출과 세포 이동 등에도 관여한다.

### 미토콘드리아

미토콘드리아를 포함한 세포소기관은 세포 내부에서 위치를 바꾸거나
특정 영역에 분포할 수 있다. 세포골격과 운동 단백질은 일부
세포소기관의 이동과 분포 조절에 관여한다.

</div>
""", unsafe_allow_html=True)
