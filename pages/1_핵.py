import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CELL VISION | BIO-01 NUCLEUS",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "images" / "nucleus.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&family=Noto+Sans+KR:wght@400;500;700&display=swap');
.stApp{background:radial-gradient(ellipse at 50% 0%,#102433,transparent 46%),#050b12;color:#dceaf0}
[data-testid="stHeader"]{background:#050b12;border-bottom:1px solid #172d3b}
[data-testid="stSidebar"]{background:#07111b;border-right:1px solid #244454}
[data-testid="stSidebar"] *{color:#c9dce5}
.block-container{max-width:1450px;padding-top:1.2rem}
h1,h2,h3,p,li,label{color:#dceaf0}
.top-strip{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:10px 14px;margin-bottom:18px;border-top:2px solid #7d9aa9;border-bottom:1px solid #244454;background:#0c1b28;font:10px 'IBM Plex Mono';letter-spacing:1px;color:#9cb7c4}
.top-strip strong,.eyebrow{color:#57d9e8}
.eyebrow{font:10px 'IBM Plex Mono';letter-spacing:2px}
.page-title{font-size:clamp(28px,3vw,42px);font-weight:700;color:#edf8fc}
.subtitle{font:13px 'Noto Sans KR';color:#89a6b6;line-height:1.8}
.section-bar{background:#0d1d2a;border-left:3px solid #57d9e8;border-bottom:1px solid #294958;padding:11px 13px;margin:20px 0 13px;font:600 11px 'IBM Plex Mono';letter-spacing:1px}
.panel{background:linear-gradient(145deg,#0c1b28,#07111a);border:1px solid #284655;border-top:2px solid #5d8b9e;padding:16px;margin-bottom:12px}
.panel-label{font:10px 'IBM Plex Mono';color:#7fa1b2;letter-spacing:1.3px;margin-bottom:8px}
.panel-text{font:13px/1.95 'Noto Sans KR';color:#c5d9e2}
.callout{background:#081722;border:1px solid #294958;border-left:3px solid #3988bd;padding:14px 16px;margin:12px 0;font:13px/1.9 'Noto Sans KR';color:#c5d9e2}
div[data-testid="stButton"]>button{background:#0b1c29;color:#cceaf1;border:1px solid #315568;border-radius:0;font:11px 'IBM Plex Mono'}
div[data-testid="stButton"]>button:hover{background:#123044;color:white;border-color:#57d9e8}
[data-testid="stImage"] img{border:1px solid #1d3949}
</style>
""", unsafe_allow_html=True)

if st.button("← RETURN TO COMMAND CENTER"):
    st.switch_page("app.py")

st.markdown("""
<div class="top-strip">
<span>CELL VISION // BIOLOGICAL INTELLIGENCE SYSTEM</span>
<span>FILE STATUS: <strong>AVAILABLE</strong></span>
<span>CLASSIFICATION: BIO-RESTRICTED</span>
</div>
<div class="eyebrow">BIOLOGICAL INTELLIGENCE FILE // BIO-01</div>
<h1 class="page-title">핵 <span style="color:#57d9e8">/ NUCLEUS</span></h1>
<div class="subtitle">CELLULAR STRUCTURE ANALYSIS · FUNCTION · SYSTEM CONNECTIONS</div>
<div class="section-bar">01 / TARGET OVERVIEW</div>
""", unsafe_allow_html=True)

image_col, overview_col = st.columns([1, 1.35], gap="large")

with image_col:
    if IMAGE_PATH.exists():
        st.image(str(IMAGE_PATH), use_container_width=True)
    else:
        st.warning("이미지를 찾을 수 없습니다. images/nucleus.png 파일을 확인해 주세요.")

with overview_col:
    st.markdown("""
    <div class="panel">
    <div class="panel-label">CORE FUNCTION</div>
    <div class="panel-text">핵은 DNA를 보관하고 유전 정보가 RNA로 전사되는 과정과 유전자 발현을 조절하는 진핵세포의 소기관입니다.</div>
    </div>
    <div class="panel">
    <div class="panel-label">INTELLIGENCE FILE</div>
    <div class="panel-text">BIO-01 // 핵 · NUCLEUS</div>
    </div>
    <div class="callout">
    <b style="color:#57d9e8">SYSTEM NOTE</b><br>
    핵의 기능은 리보솜, 소포체, 골지체 등과 연결되어 세포의 생명 활동을 유지합니다.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-bar">02 / STRUCTURAL ANALYSIS</div>', unsafe_allow_html=True)

STRUCTURES = [
    ("핵막", "핵막은 핵 내부와 세포질을 구분하는 이중막 구조입니다. 핵 내부 환경을 유지하며, 바깥쪽 막은 소포체 막과 연결되어 있습니다."),
    ("핵공", "핵공은 핵막에 있는 단백질 복합체로 핵과 세포질 사이의 물질 이동을 선택적으로 조절합니다. 가공된 전령 RNA와 특정 단백질은 운반 체계의 도움을 받아 핵공을 통과합니다."),
    ("염색질", "염색질은 DNA와 히스톤 등의 단백질이 결합한 물질입니다. DNA를 핵 안에 정리하고 유전 정보의 접근성을 조절합니다. 세포 분열 시 염색질은 응축되어 염색체 형태로 관찰됩니다."),
    ("인", "인은 리보솜 RNA가 합성되고 리보솜을 구성하는 RNA와 단백질이 결합해 소단위체가 조립되는 데 중요한 역할을 합니다."),
]

for title, body in STRUCTURES:
    st.markdown(
        f'<div class="panel"><div class="panel-label">STRUCTURE // {title}</div><div class="panel-text">{body}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-bar">03 / OPERATIONAL PROCESS</div>', unsafe_allow_html=True)

PROCESSES = [
    ("전사", "전사는 DNA의 특정 부분을 주형으로 RNA를 합성하는 과정입니다. RNA 중합효소가 DNA 염기서열을 읽어 상보적인 RNA 가닥을 만듭니다."),
    ("RNA 가공", "진핵세포에서 전령 RNA는 5′ 말단 캡 형성, 3′ 말단 폴리-A 꼬리 추가, 스플라이싱 등의 가공을 거칠 수 있습니다. 스플라이싱에서는 인트론이 제거되고 엑손이 연결됩니다."),
    ("유전자 발현 조절", "세포는 전사 조절 등을 통해 어떤 유전자를 언제 얼마나 발현할지 조절합니다. 이 과정은 세포 종류와 상태에 따라 서로 다른 단백질이 만들어지도록 합니다."),
]

for title, body in PROCESSES:
    st.markdown(
        f'<div class="panel"><div class="panel-label">PROCESS // {title}</div><div class="panel-text">{body}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-bar">04 / INTER-ORGANELLE CONNECTIONS</div>', unsafe_allow_html=True)

CONNECTIONS = [
    ("리보솜", "핵의 인에서 조립된 리보솜 소단위체와 핵에서 전사된 mRNA는 세포질로 이동해 단백질 합성에 연결됩니다."),
    ("소포체", "핵막 바깥쪽 막은 소포체와 연결되어 있습니다. 소포체는 일부 단백질의 합성, 접힘 및 초기 가공을 담당합니다."),
    ("골지체", "소포체에서 전달된 단백질과 지질은 골지체에서 추가 가공·분류되어 목적지로 운반될 수 있습니다."),
]

for title, body in CONNECTIONS:
    st.markdown(
        f'<div class="panel"><div class="panel-label">SYSTEM LINK // {title}</div><div class="panel-text">{body}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("""
<div class="callout">
<b style="color:#57d9e8">ANALYSIS SUMMARY</b><br>
핵의 구조와 기능을 다른 소기관과 연결해 이해하면 세포 전체에서 물질과 에너지가 이동하고 이용되는 과정을 더 정확하게 설명할 수 있습니다.
</div>
""", unsafe_allow_html=True)

st.caption("CELL VISION // BIO-01 NUCLEUS · EDUCATIONAL USE")
