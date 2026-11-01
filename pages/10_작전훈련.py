from pathlib import Path

code = r'''import random
from pathlib import Path

import streamlit as st

# =========================================================
# CELL VISION | TACTICAL TRAINING
# 파일 위치: pages/10_작전훈련.py
# =========================================================

st.set_page_config(
    page_title="CELL VISION | Tactical Training",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# 1. 공통 디자인
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    .stApp {
        background: radial-gradient(ellipse at top, #102433 0%, #050b12 58%);
        color: #dceaf0;
        font-family: 'Noto Sans KR', sans-serif;
    }
    [data-testid="stSidebar"] {
        background: #07111b;
        border-right: 1px solid #244454;
    }
    [data-testid="stHeader"] { background: #050b12; }
    .block-container {
        max-width: 1600px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, p, li, label { color: #dceaf0; }
    h1 { font-family: 'IBM Plex Mono', monospace !important; letter-spacing: 1px; }
    .stCaption, [data-testid="stCaptionContainer"] { color: #7993a3 !important; }
    .stButton > button {
        background: #0b1c29;
        color: #dceaf0;
        border: 1px solid #315568;
        border-radius: 2px;
        min-height: 42px;
    }
    .stButton > button:hover {
        background: #123044;
        color: #57d9e8;
        border-color: #57d9e8;
    }
    [data-testid="stSidebarNav"] { display: none; }
    .side-brand {
        border-top: 2px solid #6d95a7;
        border-bottom: 1px solid #284655;
        padding: 13px 6px;
        background: linear-gradient(110deg, #122533, #07111b);
        margin-bottom: 20px;
    }
    .side-brand-title {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 21px;
        font-weight: 700;
        letter-spacing: 2px;
        color: #dceaf0;
    }
    .side-brand-sub {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 9px;
        letter-spacing: 1px;
        color: #57d9e8;
        margin-top: 5px;
    }
    .side-section {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 10px;
        letter-spacing: 1px;
        color: #57d9e8;
        border-bottom: 1px solid #244454;
        padding-bottom: 7px;
        margin: 18px 0 10px;
    }
    .side-info {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 10px;
        line-height: 1.9;
        color: #7993a3;
    }
    [data-testid="stSidebar"] [data-testid="stPageLink"] a {
        border: 1px solid transparent;
        border-radius: 2px;
        padding: 8px 10px;
    }
    [data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
        background: #0b1c29;
        border-color: #315568;
    }
    [data-testid="stSidebar"] [data-testid="stPageLink"] p {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 12px;
    }
    .top-strip {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        flex-wrap: wrap;
        border-top: 1px solid #315568;
        border-bottom: 1px solid #244454;
        padding: 9px 0;
        margin-bottom: 25px;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 10px;
        letter-spacing: 1px;
        color: #7993a3;
    }
    .eyebrow {
        font-family: 'IBM Plex Mono', monospace;
        color: #57d9e8;
        font-size: 11px;
        letter-spacing: 2px;
        margin-bottom: 7px;
    }
    .overview {
        background: linear-gradient(110deg, #102533, #091722);
        border-left: 3px solid #57d9e8;
        padding: 18px 22px;
        line-height: 1.9;
        color: #dceaf0;
        margin: 18px 0;
        border-top: 1px solid #244454;
        border-bottom: 1px solid #244454;
    }
    .info-label {
        font-family: 'IBM Plex Mono', monospace;
        color: #57d9e8;
        font-size: 10px;
        letter-spacing: 1px;
    }
    .mission-card {
        background: linear-gradient(110deg, #102533, #091722);
        border: 1px solid #315568;
        border-left: 3px solid #57d9e8;
        padding: 17px 18px;
        min-height: 145px;
        margin-bottom: 8px;
    }
    .mission-code {
        color: #57d9e8;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 11px;
        letter-spacing: 1px;
    }
    .mission-title {
        color: #dceaf0;
        font-size: 20px;
        font-weight: 700;
        margin: 8px 0;
    }
    .mission-desc { color: #9eb3bf; font-size: 13px; line-height: 1.7; }
    .report-box {
        background: #0b1c29;
        border: 1px solid #315568;
        padding: 16px 18px;
        margin: 12px 0;
        line-height: 1.9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 2. 소기관별 문제 자료
# 주의: 문제는 학습용 초안이며 필요하면 수업 자료에 맞춰 검토하세요.
# 각 미션은 10문제로 구성합니다.
# =========================================================

MISSIONS = {
    "핵": {
        "code": "BIO-01",
        "english": "NUCLEUS",
        "summary": "유전 정보의 보관과 세포 활동 조절",
        "briefing": "핵의 구조와 유전 정보의 역할을 분석하고 핵의 주요 기능을 확인하십시오.",
        "questions": [
            ("핵의 주요 기능으로 가장 적절한 것은 무엇인가요?", ["세포의 유전 정보를 보관하고 세포 활동을 조절한다", "세포 호흡으로 ATP를 주로 생산한다", "세포 내 물질을 소화한다", "단백질을 목적지별로 포장한다"], 0, "핵은 DNA를 보관하며 유전자 발현 조절을 통해 세포 활동에 관여합니다."),
            ("핵막의 역할로 적절한 것은 무엇인가요?", ["아미노산을 운반한다", "핵 내부와 세포질을 구분한다", "ATP를 합성한다", "세포 골격을 직접 만든다"], 1, "핵막은 핵과 세포질을 구분하는 이중막 구조입니다."),
            ("핵공이 관여하는 기능은 무엇인가요?", ["핵과 세포질 사이의 물질 이동", "세포막의 인지질 합성만 수행", "세포 내 소화", "포도당 분해의 모든 단계"], 0, "핵공은 핵과 세포질 사이에서 RNA와 단백질 등의 이동을 조절합니다."),
            ("염색질은 주로 무엇으로 이루어져 있나요?", ["인지질과 셀룰로스", "DNA와 단백질", "포도당과 지방산", "ATP와 물"], 1, "염색질은 DNA와 히스톤 등의 단백질을 포함합니다."),
            ("핵소체의 주요 기능은 무엇인가요?", ["리보솜 구성 요소의 생성에 관여한다", "세포의 ATP를 모두 생산한다", "세포막을 통한 확산을 수행한다", "노폐물을 직접 분해한다"], 0, "핵소체에서는 rRNA 합성과 리보솜 소단위체 형성에 관여하는 과정이 일어납니다."),
            ("DNA의 유전 정보가 단백질 합성에 이용되기 위해 일반적으로 먼저 만들어지는 것은 무엇인가요?", ["전령 RNA", "글리코젠", "인지질 이중층", "리소좀"], 0, "전사 과정에서 DNA 정보를 바탕으로 RNA가 만들어집니다."),
            ("전령 RNA가 핵에서 세포질로 이동할 때 통과하는 구조는 무엇인가요?", ["크리스타", "핵공", "골지체 낭", "리소좀 막"], 1, "전령 RNA는 핵공을 통해 핵 밖으로 이동할 수 있습니다."),
            ("핵과 리보솜의 관계를 가장 잘 설명한 것은 무엇인가요?", ["핵의 유전 정보가 RNA를 통해 단백질 합성에 이용된다", "리보솜이 핵의 DNA를 소화한다", "핵이 단백질을 골지체처럼 포장한다", "리보솜이 핵막을 만든다"], 0, "DNA 정보는 전사로 RNA에 전달되고, 리보솜은 전령 RNA를 읽어 단백질을 합성합니다."),
            ("다음 중 핵의 기능으로 보기 어려운 것은 무엇인가요?", ["유전 정보 보관", "유전자 발현 조절", "핵공을 통한 물질 이동 조절", "세포의 주요 ATP 생산"], 3, "세포 호흡에 따른 ATP 생산은 주로 미토콘드리아와 관련됩니다."),
            ("핵공의 기능이 크게 저해되면 어떤 과정에 직접적인 문제가 생길 수 있나요?", ["핵과 세포질 사이의 RNA 이동", "세포막의 모든 인지질이 즉시 사라지는 과정", "세포벽의 셀룰로스 합성만", "크리스타의 형광 발생"], 0, "핵공은 핵과 세포질 사이의 물질 교환에 관여하므로 RNA 이동에 영향을 줄 수 있습니다."),
        ],
    },
    "리보솜": {
        "code": "BIO-02",
        "english": "RIBOSOME",
        "summary": "유전 정보를 바탕으로 단백질 합성",
        "briefing": "리보솜의 구성과 번역 과정을 분석하고 단백질 합성 체계를 점검하십시오.",
        "questions": [
            ("리보솜의 주요 기능은 무엇인가요?", ["단백질 합성", "ATP의 주요 생산", "세포 내 소화", "유전 정보의 장기 보관"], 0, "리보솜은 전령 RNA의 정보를 바탕으로 아미노산을 연결해 단백질을 합성합니다."),
            ("리보솜은 주로 어떤 구성 요소로 이루어져 있나요?", ["rRNA와 단백질", "DNA와 셀룰로스", "인지질과 글리코젠", "ATP와 지방산"], 0, "리보솜은 리보솜 RNA와 단백질로 이루어진 복합체입니다."),
            ("작은 소단위체의 주요 역할은 무엇인가요?", ["전령 RNA와 결합하고 유전 암호를 읽는 데 관여한다", "단백질을 분비 소낭에 포장한다", "ATP를 생산한다", "세포 내 노폐물을 분해한다"], 0, "작은 소단위체는 전령 RNA와 결합하고 코돈을 읽는 과정에 관여합니다."),
            ("큰 소단위체의 역할로 적절한 것은 무엇인가요?", ["펩타이드 결합 형성을 촉진한다", "DNA를 보관한다", "핵공을 만든다", "세포막을 통한 확산만 수행한다"], 0, "큰 소단위체는 아미노산 사이의 펩타이드 결합 형성에 핵심적으로 관여합니다."),
            ("전령 RNA의 염기 세 개로 이루어진 단위는 무엇인가요?", ["코돈", "크리스타", "핵공", "시스터나"], 0, "코돈은 전령 RNA의 염기 세 개로 이루어져 아미노산 또는 번역 신호를 지정합니다."),
            ("운반 RNA(tRNA)의 역할은 무엇인가요?", ["특정 아미노산을 리보솜으로 운반한다", "DNA를 핵 안에 보관한다", "단백질을 분해한다", "세포막의 인지질을 모두 합성한다"], 0, "운반 RNA는 특정 아미노산을 리보솜으로 가져오고 안티코돈으로 코돈을 인식합니다."),
            ("번역이 종결 코돈에 도달하면 일반적으로 어떤 일이 일어나나요?", ["종결 인자가 작용하여 폴리펩타이드가 방출된다", "DNA가 즉시 두 배가 된다", "리보솜이 미토콘드리아로 변한다", "핵막이 사라진다"], 0, "종결 코돈에서 종결 인자가 작용해 번역이 끝나고 폴리펩타이드가 방출됩니다."),
            ("거친면 소포체에 결합한 리보솜이 주로 합성하는 단백질은 무엇인가요?", ["분비 단백질이나 막 단백질 등", "모든 세포질 단백질만", "DNA 자체", "인지질 이중층 자체만"], 0, "거친면 소포체에 결합한 리보솜은 분비 단백질과 막 단백질 등의 합성에 관여합니다."),
            ("자유 리보솜과 소포체 결합 리보솜에 대한 설명으로 옳은 것은 무엇인가요?", ["기본적인 단백질 합성 기능은 같고 단백질의 목적지에 따라 작용 위치가 달라진다", "자유 리보솜은 단백질을 합성할 수 없다", "소포체 결합 리보솜은 DNA를 복제한다", "두 종류는 구성 성분이 완전히 다르다"], 0, "두 리보솜의 기본 합성 기능은 같으며 만들어지는 단백질의 용도에 따라 위치가 달라집니다."),
            ("리보솜에서 만들어진 단백질이 골지체로 이동할 수 있는 대표적인 경로는 무엇인가요?", ["거친면 소포체를 거쳐 운반 소낭으로 이동한다", "핵 DNA에 직접 삽입된다", "크리스타를 통해 세포 밖으로 바로 나간다", "세포골격이 단백질을 DNA로 바꾼다"], 0, "일부 단백질은 거친면 소포체에서 가공된 뒤 운반 소낭을 통해 골지체로 이동합니다."),
        ],
    },
    "미토콘드리아": {
        "code": "BIO-03",
        "english": "MITOCHONDRION",
        "summary": "세포 호흡과 ATP 생산",
        "briefing": "미토콘드리아의 막 구조와 에너지 전환 기능을 분석하십시오.",
        "questions": [
            ("미토콘드리아의 주요 기능은 무엇인가요?", ["세포 호흡을 통한 ATP 생산", "유전 정보의 대부분을 보관", "단백질을 최종 분류", "세포 내 소화만 수행"], 0, "미토콘드리아는 세포 호흡에 관여하며 ATP 생산의 중요한 장소입니다."),
            ("미토콘드리아를 둘러싼 막의 특징은 무엇인가요?", ["외막과 내막으로 이루어진다", "막이 전혀 없다", "셀룰로스 벽 하나만 있다", "핵막과 완전히 동일하다"], 0, "미토콘드리아는 외막과 내막을 가진 이중막 구조입니다."),
            ("크리스타는 무엇인가요?", ["미토콘드리아 내막이 접힌 구조", "핵막의 구멍", "리보솜의 작은 소단위체", "골지체의 운반 소낭"], 0, "크리스타는 내막이 접혀 형성되며 내막의 표면적을 넓힙니다."),
            ("미토콘드리아 기질(matrix)에 대한 설명으로 적절한 것은 무엇인가요?", ["내막 안쪽 공간으로 여러 대사 반응이 일어난다", "핵과 세포질 사이의 통로다", "단백질 분류를 전담한다", "세포막 바깥쪽 공간이다"], 0, "기질은 미토콘드리아 내막 안쪽 공간이며 여러 효소와 DNA 등이 존재합니다."),
            ("ATP는 세포에서 주로 어떤 역할을 하나요?", ["세포 활동에 이용되는 에너지를 전달한다", "유전 암호를 저장한다", "세포막을 완전히 대체한다", "아미노산의 종류를 직접 결정한다"], 0, "ATP는 다양한 세포 활동에 에너지를 공급하는 데 이용됩니다."),
            ("미토콘드리아 내막이 중요한 이유로 적절한 것은 무엇인가요?", ["전자 전달과 ATP 합성에 관련된 단백질이 존재한다", "DNA를 모두 저장하는 유일한 장소다", "단백질을 분비 소낭에 포장한다", "세포 내 모든 RNA를 분해한다"], 0, "내막에는 전자 전달계와 ATP 합성효소 등이 있어 ATP 생산에 중요합니다."),
            ("미토콘드리아가 많은 세포의 특징으로 예상할 수 있는 것은 무엇인가요?", ["에너지 요구량이 높은 활동을 수행할 수 있다", "유전 정보가 전혀 없다", "단백질을 합성할 수 없다", "세포막이 필요 없다"], 0, "에너지 수요가 큰 세포는 미토콘드리아가 상대적으로 많을 수 있습니다."),
            ("미토콘드리아와 세포질의 관계를 설명한 것으로 적절한 것은 무엇인가요?", ["세포 호흡 과정은 여러 세포 구획에서 이어진다", "모든 대사 반응은 미토콘드리아 안에서만 일어난다", "세포질은 미토콘드리아를 구성하는 막이다", "미토콘드리아는 세포질과 관계가 없다"], 0, "세포 호흡은 세포질에서 일어나는 해당 과정과 미토콘드리아의 여러 과정 등이 연결됩니다."),
            ("미토콘드리아 기능이 저하되어 ATP 공급이 줄면 어떤 영향이 나타날 수 있나요?", ["에너지를 필요로 하는 세포 활동이 영향을 받을 수 있다", "모든 단백질이 즉시 DNA로 변한다", "핵공이 자동으로 늘어난다", "골지체가 사라지면 에너지가 무한히 생긴다"], 0, "ATP 공급 감소는 에너지를 필요로 하는 다양한 세포 과정에 영향을 줄 수 있습니다."),
            ("크리스타의 접힌 구조가 내막의 표면적을 넓히는 것은 어떤 점에서 유리한가요?", ["에너지 전환에 관여하는 단백질이 자리할 공간을 늘린다", "핵 DNA를 모두 외부로 방출한다", "리보솜을 골지체로 바꾼다", "세포막의 선택적 투과성을 없앤다"], 0, "내막 표면적이 넓으면 전자 전달과 ATP 합성에 관여하는 구성 요소가 자리할 수 있는 공간이 커집니다."),
        ],
    },
    "소포체": {
        "code": "BIO-04",
        "english": "ENDOPLASMIC RETICULUM",
        "summary": "단백질과 지질의 합성 및 가공",
        "briefing": "조면 소포체와 활면 소포체의 기능을 구분하고 세포 내 합성 체계를 확인하십시오.",
        "questions": [
            ("조면 소포체 표면이 거칠게 보이는 주된 이유는 무엇인가요?", ["리보솜이 붙어 있기 때문", "크리스타가 있기 때문", "핵공이 많기 때문", "셀룰로스 벽이 있기 때문"], 0, "조면 소포체 표면에는 리보솜이 붙어 있어 거칠게 보입니다."),
            ("조면 소포체의 주요 기능은 무엇인가요?", ["분비 단백질과 막 단백질의 합성 및 초기 가공", "ATP의 주요 생산", "유전 정보의 장기 보관", "세포 내 소화만 수행"], 0, "조면 소포체는 단백질 합성과 접힘, 품질 관리 등에 관여합니다."),
            ("활면 소포체의 특징으로 적절한 것은 무엇인가요?", ["표면에 리보솜이 붙어 있지 않다", "DNA만으로 이루어진다", "핵막의 일부가 아니다", "단백질 합성만 수행한다"], 0, "활면 소포체는 표면에 리보솜이 붙어 있지 않습니다."),
            ("활면 소포체가 관여할 수 있는 기능은 무엇인가요?", ["지질 합성 및 물질 해독 등에 관여", "유전 암호 번역만 수행", "핵공을 통한 RNA 이동만 수행", "크리스타 형성만 수행"], 0, "활면 소포체는 지질 합성, 해독, 일부 세포에서는 칼슘 저장 등에 관여합니다."),
            ("소포체 내부에서 새 단백질이 거치는 과정으로 적절한 것은 무엇인가요?", ["접힘과 품질 관리", "DNA를 셀룰로스로 바꾸기", "ATP를 핵 DNA에 저장하기", "염색체를 분해해 인지질 만들기"], 0, "소포체는 단백질의 접힘과 품질 관리에 관여합니다."),
            ("소포체와 골지체의 관계를 가장 잘 설명한 것은 무엇인가요?", ["소포체에서 처리된 일부 물질이 소낭을 통해 골지체로 이동한다", "골지체가 소포체의 DNA를 복제한다", "두 구조는 같은 구조의 다른 이름이다", "소포체는 골지체와 물질을 교환하지 않는다"], 0, "소포체에서 나온 운반 소낭은 골지체로 물질을 전달할 수 있습니다."),
            ("리보솜이 조면 소포체와 결합하는 대표적인 경우는 무엇인가요?", ["분비되거나 막에 삽입될 단백질을 합성할 때", "ATP를 만들 때만", "DNA를 핵 안에 보관할 때", "세포막의 모든 확산을 멈출 때"], 0, "분비 단백질과 막 단백질을 합성하는 리보솜은 조면 소포체와 연결되어 작용합니다."),
            ("소포체가 막으로 연결된 관과 주머니의 망상 구조를 이루는 점은 어떤 기능에 유리한가요?", ["세포 내부에서 물질을 합성하고 이동시키는 데 도움을 준다", "유전 정보가 필요 없게 만든다", "세포막을 완전히 없앤다", "모든 효소 작용을 중단한다"], 0, "소포체의 막 구조는 물질 합성 및 세포 내부 수송에 유리합니다."),
            ("다음 중 조면 소포체보다 활면 소포체와 더 관련이 큰 기능은 무엇인가요?", ["지질 합성", "분비 단백질 합성의 시작", "전령 RNA의 코돈 읽기", "DNA의 유전 정보 보관"], 0, "지질 합성은 활면 소포체의 대표적인 기능입니다."),
            ("소포체에서 단백질의 접힘과 품질 관리가 제대로 이루어지지 않으면 어떤 문제가 생길 수 있나요?", ["정상적으로 기능하지 못하는 단백질이 생길 수 있다", "모든 ATP가 DNA로 바뀐다", "세포막이 자동으로 핵이 된다", "전령 RNA가 아미노산으로 변한다"], 0, "단백질 접힘과 품질 관리가 실패하면 기능에 문제가 있는 단백질이 생길 수 있습니다."),
        ],
    },
    "골지체": {
        "code": "BIO-05",
        "english": "GOLGI APPARATUS",
        "summary": "단백질과 지질의 가공·분류·수송",
        "briefing": "골지체의 층상 구조와 물질 분류 및 수송 기능을 확인하십시오.",
        "questions": [
            ("골지체의 주요 기능은 무엇인가요?", ["단백질과 지질의 가공·분류·수송", "DNA의 보관", "ATP의 주요 생산", "세포질의 모든 물질을 소화"], 0, "골지체는 소포체에서 온 물질을 가공하고 분류해 목적지로 보냅니다."),
            ("골지체는 일반적으로 어떤 구조로 이루어져 있나요?", ["납작한 막 주머니가 겹쳐진 구조", "이중 나선 DNA만으로 된 구조", "크리스타가 접힌 구조", "리보솜 두 소단위체"], 0, "골지체는 시스터나라고 하는 납작한 막 주머니가 여러 겹 쌓인 구조입니다."),
            ("소포체에서 골지체로 물질을 전달하는 데 주로 관여하는 것은 무엇인가요?", ["운반 소낭", "핵소체", "염색질", "크리스타"], 0, "운반 소낭은 소포체와 골지체 사이에서 물질을 전달합니다."),
            ("골지체에서 이루어질 수 있는 과정은 무엇인가요?", ["단백질의 추가 가공과 분류", "DNA의 모든 복제", "세포 호흡의 모든 단계", "전령 RNA의 코돈 읽기"], 0, "골지체는 단백질과 지질을 추가로 가공하고 분류합니다."),
            ("골지체가 물질을 분류하는 이유로 적절한 것은 무엇인가요?", ["각 물질이 알맞은 세포 내 위치나 세포 밖으로 이동하도록 하기 위해", "모든 단백질을 DNA로 바꾸기 위해", "ATP를 핵에 저장하기 위해", "세포막의 투과성을 모두 없애기 위해"], 0, "골지체는 물질을 목적지에 맞게 분류하고 수송 경로로 보냅니다."),
            ("골지체와 리소좀의 관계를 설명한 것으로 적절한 것은 무엇인가요?", ["골지체는 리소좀으로 향하는 일부 효소의 분류·수송에 관여한다", "리소좀은 골지체의 DNA를 저장한다", "골지체는 리소좀과 물질을 주고받지 않는다", "두 소기관은 같은 구조다"], 0, "골지체는 리소좀으로 향하는 효소 등을 분류하고 전달하는 과정에 관여합니다."),
            ("골지체의 시스터나에 대한 설명으로 적절한 것은 무엇인가요?", ["골지체를 이루는 납작한 막 주머니", "핵막의 구멍", "미토콘드리아의 DNA", "리보솜의 작은 소단위체"], 0, "시스터나는 골지체를 구성하는 납작한 막 주머니입니다."),
            ("분비 단백질이 세포 밖으로 나가기 전 거칠게 거치는 경로로 적절한 것은 무엇인가요?", ["리보솜·조면 소포체 → 골지체 → 분비 소낭", "핵공 → 크리스타 → 염색질", "리소좀 → 핵소체 → DNA", "세포골격 → DNA → 핵막"], 0, "분비 단백질은 조면 소포체와 골지체에서 처리된 뒤 분비 소낭을 통해 이동할 수 있습니다."),
            ("골지체 기능이 저해되면 직접적으로 영향받을 가능성이 큰 것은 무엇인가요?", ["단백질의 분류와 목적지 전달", "DNA 염기서열 자체의 저장", "미토콘드리아 내막의 모든 반응", "리보솜의 유전 암호 읽기만"], 0, "골지체 기능 저하는 단백질의 가공, 분류, 수송에 영향을 줄 수 있습니다."),
            ("골지체가 세포 내 수송 체계에서 중요한 이유는 무엇인가요?", ["물질을 적절히 가공하고 목적지에 맞게 분류하기 때문", "세포의 모든 에너지를 직접 만들기 때문", "모든 DNA를 합성하기 때문", "세포막이 필요 없게 만들기 때문"], 0, "골지체는 세포 내 물질 처리와 목적지별 수송을 연결하는 역할을 합니다."),
        ],
    },
    "리소좀": {
        "code": "BIO-06",
        "english": "LYSOSOME",
        "summary": "세포 내 소화와 물질 재활용",
        "briefing": "리소좀의 분해 기능과 세포 내 재활용 과정을 확인하십시오.",
        "questions": [
            ("리소좀의 주요 기능은 무엇인가요?", ["세포 내 물질의 분해와 재활용", "유전 정보의 보관", "ATP의 주요 생산", "단백질 합성의 직접 수행"], 0, "리소좀은 가수분해 효소를 이용해 여러 물질을 분해합니다."),
            ("리소좀 내부가 산성 환경인 것은 어떤 점에서 중요한가요?", ["리소좀 효소가 작용하기 적합한 조건을 제공한다", "DNA를 세포막으로 바꾼다", "ATP를 모두 저장한다", "핵공을 열어 둔다"], 0, "리소좀의 산성 환경은 내부 가수분해 효소의 기능에 중요합니다."),
            ("리소좀에서 작용하는 효소의 대표적인 역할은 무엇인가요?", ["큰 분자를 더 작은 분자로 분해한다", "유전 암호를 복제한다", "빛을 흡수해 포도당을 만든다", "막을 통해 산소만 운반한다"], 0, "리소좀의 가수분해 효소는 여러 생체 분자를 분해합니다."),
            ("세포가 손상된 일부 구성 요소를 분해하고 재활용하는 과정과 관련된 소기관은 무엇인가요?", ["리소좀", "핵소체", "리보솜의 작은 소단위체", "핵공"], 0, "리소좀은 세포 내 분해와 재활용에 관여합니다."),
            ("리소좀의 막이 중요한 이유로 적절한 것은 무엇인가요?", ["분해 효소와 내부 환경을 세포질로부터 구분한다", "세포의 모든 DNA를 보관한다", "리보솜의 코돈을 읽는다", "크리스타를 만든다"], 0, "리소좀 막은 내부 효소와 산성 환경을 세포질과 구분합니다."),
            ("골지체는 리소좀 형성과 관련해 어떤 역할을 할 수 있나요?", ["리소좀으로 향하는 효소의 가공·분류·수송에 관여한다", "리소좀 DNA를 직접 복제한다", "리소좀을 미토콘드리아로 바꾼다", "세포막을 없앤다"], 0, "골지체는 리소좀에 필요한 효소의 분류와 수송에 관여합니다."),
            ("리소좀의 분해 기능이 저해되면 어떤 현상이 나타날 수 있나요?", ["분해할 물질이 세포 안에 축적될 수 있다", "단백질 합성이 무조건 두 배가 된다", "모든 DNA가 사라진다", "ATP가 무한히 생산된다"], 0, "분해가 원활하지 않으면 처리해야 할 물질이 축적될 수 있습니다."),
            ("세포 내 소화가 필요한 이유로 적절한 것은 무엇인가요?", ["불필요하거나 손상된 물질을 분해하고 구성 성분을 재활용하기 위해", "모든 유전 정보를 제거하기 위해", "세포막을 없애기 위해", "단백질 합성을 영구히 멈추기 위해"], 0, "세포 내 소화는 불필요하거나 손상된 물질의 처리와 재활용에 기여합니다."),
            ("리소좀과 리보솜의 기능을 올바르게 짝지은 것은 무엇인가요?", ["리소좀: 분해 / 리보솜: 단백질 합성", "리소좀: 단백질 합성 / 리보솜: ATP 생산", "리소좀: DNA 보관 / 리보솜: 지질 분류", "리소좀: 광합성 / 리보솜: 세포막 형성만"], 0, "리소좀은 분해, 리보솜은 단백질 합성을 담당합니다."),
            ("리소좀의 역할을 가장 잘 설명한 것은 무엇인가요?", ["세포 내부의 분해 및 재활용 체계의 일부", "세포의 모든 유전 정보를 저장하는 장소", "세포의 유일한 에너지 생산 장소", "세포막을 통한 모든 물질 이동의 통로"], 0, "리소좀은 세포 내 물질 분해와 재활용을 담당하는 중요한 소기관입니다."),
        ],
    },
    "세포막": {
        "code": "BIO-07",
        "english": "CELL MEMBRANE",
        "summary": "세포 경계 형성과 선택적 물질 이동",
        "briefing": "세포막의 구조와 선택적 투과성, 물질 이동 방식을 확인하십시오.",
        "questions": [
            ("세포막의 기본 구조로 적절한 것은 무엇인가요?", ["인지질 이중층과 여러 막 단백질", "셀룰로스만으로 된 이중층", "DNA 이중 나선", "리보솜 소단위체"], 0, "세포막은 인지질 이중층을 기본으로 하며 단백질 등이 포함됩니다."),
            ("세포막의 선택적 투과성이 의미하는 것은 무엇인가요?", ["물질에 따라 막을 통과하는 정도가 다르다", "모든 물질이 자유롭게 통과한다", "어떤 물질도 통과하지 못한다", "DNA만 통과할 수 있다"], 0, "세포막은 물질의 종류와 운반 방식에 따라 이동을 선택적으로 조절합니다."),
            ("농도 기울기를 따라 물질이 이동하며 직접 에너지를 쓰지 않는 수송은 무엇인가요?", ["수동 수송", "능동 수송", "DNA 복제", "번역"], 0, "수동 수송은 물질이 농도 기울기를 따라 이동하며 직접적인 에너지 투입을 요구하지 않습니다."),
            ("물 분자가 선택적으로 투과되는 막을 통해 이동하는 현상은 무엇인가요?", ["삼투", "전사", "번역", "세포 내 소화"], 0, "삼투는 물이 선택적 투과성 막을 통해 이동하는 현상입니다."),
            ("농도 기울기에 거슬러 물질을 이동시키는 수송은 일반적으로 무엇을 필요로 하나요?", ["에너지", "염색질", "핵소체", "리보솜의 작은 소단위체만"], 0, "능동 수송은 농도 기울기에 거슬러 물질을 이동시키며 에너지를 필요로 합니다."),
            ("막 단백질이 수행할 수 있는 기능은 무엇인가요?", ["물질 수송이나 신호 수용", "DNA를 핵에 보관하는 일만", "세포 내 모든 단백질 분해", "크리스타 형성만"], 0, "막 단백질은 수송체, 통로, 수용체 등 다양한 역할을 합니다."),
            ("산소처럼 작고 비극성인 분자가 인지질 이중층을 통과하는 대표적인 방식은 무엇인가요?", ["단순 확산", "능동 수송만", "번역", "세포 내 소화"], 0, "산소 같은 작은 비극성 분자는 인지질 이중층을 통한 단순 확산이 가능합니다."),
            ("세포막과 세포 항상성의 관계를 설명한 것으로 적절한 것은 무엇인가요?", ["물질 출입을 조절해 내부 환경 유지에 기여한다", "세포의 모든 유전 정보를 합성한다", "ATP를 모두 직접 생산한다", "단백질을 모두 분해한다"], 0, "세포막은 물질 출입을 조절해 세포 내부 환경 유지에 기여합니다."),
            ("세포막의 인지질이 이중층을 이루는 이유를 가장 잘 설명한 것은 무엇인가요?", ["친수성 부분과 소수성 부분을 모두 가지기 때문", "인지질이 DNA로 이루어져 있기 때문", "인지질이 모두 물에 녹지 않기 때문", "리보솜이 인지질을 둘러싸기 때문"], 0, "인지질은 친수성 머리 부분과 소수성 꼬리 부분을 가져 수용액에서 이중층을 형성합니다."),
            ("세포막의 수송 단백질 기능이 저해되면 어떤 문제가 생길 수 있나요?", ["특정 물질의 막 통과가 어려워질 수 있다", "모든 물질이 자동으로 자유롭게 통과한다", "핵이 즉시 사라진다", "DNA가 ATP로 바뀐다"], 0, "수송 단백질은 특정 이온이나 분자의 이동을 돕기 때문에 기능 저하가 이동에 영향을 줄 수 있습니다."),
        ],
    },
    "세포질": {
        "code": "BIO-08",
        "english": "CYTOPLASM",
        "summary": "세포 내부 공간과 다양한 대사 반응",
        "briefing": "세포질의 구성과 세포 내 반응이 일어나는 환경을 분석하십시오.",
        "questions": [
            ("세포질을 설명한 것으로 가장 적절한 것은 무엇인가요?", ["세포막 안쪽에서 핵을 제외한 영역을 가리키며 세포질 기질과 여러 구조를 포함한다", "핵 내부의 DNA만을 뜻한다", "세포 밖의 액체만 뜻한다", "미토콘드리아 내막만 뜻한다"], 0, "세포질은 핵을 제외한 세포 내부 영역을 가리키며, 문맥에 따라 세포질 기질과 소기관을 구분해 설명합니다."),
            ("세포질 기질(cytosol)에 대한 설명으로 적절한 것은 무엇인가요?", ["세포질의 액체 성분으로 여러 대사 반응이 일어난다", "핵막 바깥쪽의 빈 공간만 뜻한다", "세포벽을 이루는 셀룰로스다", "골지체의 시스터나다"], 0, "세포질 기질은 세포 내부의 수용성 환경으로 여러 대사 반응이 일어납니다."),
            ("해당 과정(glycolysis)이 일어나는 대표적인 장소는 어디인가요?", ["세포질 기질", "핵소체", "골지체 내부", "핵공"], 0, "해당 과정은 세포질 기질에서 일어납니다."),
            ("세포질이 세포 활동에 중요한 이유는 무엇인가요?", ["여러 물질과 구조가 존재하고 대사 반응 및 물질 이동이 이루어지기 때문", "모든 DNA를 단독으로 보관하기 때문", "세포막을 완전히 대체하기 때문", "세포 밖에만 존재하기 때문"], 0, "세포질은 여러 세포 구조가 자리하며 대사 반응과 물질 이동이 이루어지는 환경입니다."),
            ("세포질 기질과 세포소기관의 관계를 설명한 것으로 적절한 것은 무엇인가요?", ["세포소기관은 세포 내부에서 특화된 기능을 수행한다", "세포소기관은 모두 세포질 밖에 있다", "세포질 기질은 모든 소기관과 같은 구조다", "세포소기관은 세포질과 물질을 교환하지 않는다"], 0, "세포소기관은 세포 내부에서 각기 특화된 기능을 수행하며 주변 환경과 물질을 교환합니다."),
            ("세포질에서 물질이 이동하는 것이 중요한 이유는 무엇인가요?", ["대사에 필요한 물질과 생성물이 적절한 위치로 이동해야 하기 때문", "세포가 유전 정보를 필요로 하지 않기 때문", "모든 반응이 핵 안에서만 일어나기 때문", "세포막이 없어도 되기 때문"], 0, "세포 내부의 물질 이동은 대사 과정과 소기관 간 기능 연결에 중요합니다."),
            ("세포질과 리보솜의 관계로 적절한 것은 무엇인가요?", ["자유 리보솜이 세포질에서 단백질을 합성할 수 있다", "리보솜은 세포질에 존재할 수 없다", "세포질은 리보솜을 DNA로 바꾼다", "리보솜은 세포질을 모두 소화한다"], 0, "자유 리보솜은 세포질에서 기능하는 단백질 등을 합성합니다."),
            ("세포질 기질과 미토콘드리아의 관계를 설명한 것으로 적절한 것은 무엇인가요?", ["세포 호흡의 일부 과정은 세포질 기질에서 일어나고 다른 과정은 미토콘드리아에서 일어난다", "세포 호흡은 전부 핵소체에서 일어난다", "미토콘드리아는 세포질과 물질을 교환하지 않는다", "세포질은 ATP를 사용할 수 없다"], 0, "세포 호흡의 해당 과정은 세포질 기질에서, 여러 후속 과정은 미토콘드리아에서 일어납니다."),
            ("세포질에 대한 설명으로 옳지 않은 것은 무엇인가요?", ["여러 대사 반응이 일어날 수 있다", "세포 내 물질 이동의 환경이 된다", "자유 리보솜이 존재할 수 있다", "핵과 세포질은 완전히 같은 공간이다"], 3, "핵과 세포질은 핵막으로 구분되며 물질은 핵공을 통해 이동합니다."),
            ("세포질의 환경이 크게 변하면 어떤 결과가 생길 수 있나요?", ["효소 작용과 여러 대사 과정에 영향을 줄 수 있다", "모든 유전 정보가 자동으로 복제된다", "모든 소기관이 즉시 같은 기능을 한다", "세포막이 필요 없어지게 된다"], 0, "세포질의 조건은 효소와 대사 반응에 영향을 줄 수 있습니다."),
        ],
    },
    "세포골격": {
        "code": "BIO-09",
        "english": "CYTOSKELETON",
        "summary": "세포 형태 유지와 내부 이동",
        "briefing": "세포골격의 구성 요소와 형태 유지, 세포 내 이동 기능을 분석하십시오.",
        "questions": [
            ("세포골격의 주요 기능은 무엇인가요?", ["세포 형태 유지와 내부 구조의 지지 및 이동", "유전 정보의 보관만", "ATP의 주요 생산", "단백질의 최종 분류만"], 0, "세포골격은 세포 형태와 기계적 지지를 제공하며 세포 내 이동에도 관여합니다."),
            ("세포골격을 이루는 대표적인 구조가 아닌 것은 무엇인가요?", ["미세소관", "미세섬유", "중간섬유", "핵공"], 3, "미세소관, 미세섬유, 중간섬유는 세포골격의 주요 구성 요소입니다."),
            ("미세소관의 구성 단백질은 무엇인가요?", ["튜불린", "액틴만", "콜라겐만", "히스톤만"], 0, "미세소관은 튜불린 단백질로 이루어집니다."),
            ("미세섬유의 주요 구성 단백질은 무엇인가요?", ["액틴", "튜불린", "히스톤", "DNA 중합효소"], 0, "미세섬유는 주로 액틴 단백질로 이루어집니다."),
            ("중간섬유의 대표적인 기능은 무엇인가요?", ["세포에 기계적 강도와 구조적 안정성을 제공한다", "전령 RNA의 코돈을 읽는다", "ATP를 직접 합성한다", "DNA의 염기서열을 복제한다"], 0, "중간섬유는 세포와 조직에 기계적 강도와 안정성을 제공합니다."),
            ("세포 내 소낭의 이동에 관여할 수 있는 세포골격 구조는 무엇인가요?", ["미세소관", "염색질", "핵소체", "핵공만"], 0, "미세소관은 운동 단백질과 함께 세포 내 수송 경로로 이용될 수 있습니다."),
            ("세포골격이 세포 분열에서 수행할 수 있는 역할은 무엇인가요?", ["염색체 분리와 세포질 분열에 관여한다", "DNA를 아미노산으로 바꾼다", "단백질을 모두 소화한다", "세포막을 없앤다"], 0, "미세소관은 방추사 형성 및 염색체 분리에 관여하고 액틴은 세포질 분열에 관여할 수 있습니다."),
            ("세포골격이 동적인 구조라는 설명의 의미는 무엇인가요?", ["필요에 따라 구성 요소가 조립되고 해체될 수 있다", "항상 고정되어 변하지 않는다", "DNA로만 이루어져 있다", "세포 밖에서만 작용한다"], 0, "세포골격 구성 요소는 세포의 상태와 필요에 따라 조립·해체될 수 있습니다."),
            ("세포골격과 세포막의 관계로 적절한 것은 무엇인가요?", ["세포골격은 세포막의 형태와 일부 막 단백질의 위치 유지에 도움을 줄 수 있다", "두 구조는 같은 구조다", "세포골격은 세포막과 상호작용하지 않는다", "세포막이 세포골격의 DNA를 저장한다"], 0, "세포골격은 세포막의 형태 유지와 막 단백질의 위치 조절에 기여할 수 있습니다."),
            ("세포골격 기능이 손상되면 나타날 수 있는 결과는 무엇인가요?", ["세포 형태 유지나 세포 내 물질 이동에 문제가 생길 수 있다", "모든 단백질이 자동으로 합성된다", "세포가 유전 정보를 잃지 않고 분열만 빨라진다", "세포막의 선택적 투과성이 무조건 증가한다"], 0, "세포골격은 형태 유지와 이동에 관여하므로 기능 이상은 관련 과정에 영향을 줄 수 있습니다."),
        ],
    },
}

# 모든 미션이 정확히 10문제인지 검사
for mission_data in MISSIONS.values():
    if len(mission_data["questions"]) != 10:
        raise ValueError("각 미션은 반드시 10문제로 구성되어야 합니다.")

# =========================================================
# 3. 사이드바
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div class="side-brand">
          <div class="side-brand-title">CELL VISION</div>
          <div class="side-brand-sub">BIOLOGICAL OPERATIONS UNIT</div>
        </div>
        <div class="side-section">01 / COMMAND MENU</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("**COMMAND CENTER**")
    st.caption("현재 화면 · 작전 훈련실")
    st.page_link("app.py", label="메인 화면")

    st.markdown(
        '<div class="side-section">02 / INTELLIGENCE FILES</div>',
        unsafe_allow_html=True,
    )
    pages = [
        ("BIO-01 / 핵", "pages/1_핵.py"),
        ("BIO-02 / 리보솜", "pages/2_리보솜.py"),
        ("BIO-03 / 미토콘드리아", "pages/3_미토콘드리아.py"),
        ("BIO-04 / 소포체", "pages/4_소포체.py"),
        ("BIO-05 / 골지체", "pages/5_골지체.py"),
        ("BIO-06 / 리소좀", "pages/6_리소좀.py"),
        ("BIO-07 / 세포막", "pages/7_세포막.py"),
        ("BIO-08 / 세포질", "pages/8_세포질.py"),
        ("BIO-09 / 세포골격", "pages/9_세포골격.py"),
    ]
    for label, path in pages:
        st.page_link(path, label=label)

    st.markdown(
        """
        <div class="side-section">03 / SYSTEM MONITOR</div>
        <div class="side-info">
        SYSTEM STATUS · ONLINE<br>
        TRAINING MODE · ACTIVE<br>
        DATABASE · LOCAL QUESTION BANK<br>
        ACCESS MODE · EDUCATIONAL
        </div>
        <br><hr>
        <div class="side-info">CELL VISION / INTERNAL USE</div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 4. 상태 초기화 및 공통 헤더
# =========================================================

if "cv_game_mission" not in st.session_state:
    st.session_state.cv_game_mission = None
if "cv_game_questions" not in st.session_state:
    st.session_state.cv_game_questions = []
if "cv_game_index" not in st.session_state:
    st.session_state.cv_game_index = 0
if "cv_game_answers" not in st.session_state:
    st.session_state.cv_game_answers = {}
if "cv_game_submitted" not in st.session_state:
    st.session_state.cv_game_submitted = False
if "cv_game_finished" not in st.session_state:
    st.session_state.cv_game_finished = False

st.markdown(
    """
    <div class="top-strip">
      <span>SYSTEM / CELLULAR INTELLIGENCE</span>
      <span>STATUS / ONLINE</span>
      <span>MODULE / TACTICAL TRAINING</span>
    </div>
    <div class="eyebrow">TACTICAL BIOLOGY INTERFACE // TRAINING DIVISION</div>
    """,
    unsafe_allow_html=True,
)

st.title("작전 훈련실 | TACTICAL TRAINING")
st.caption("CELL VISION · 소기관별 학습 내용 검증 시스템")

# =========================================================
# 5. 미션 시작 / 재시작 함수
# =========================================================

def start_mission(organelle_name):
    st.session_state.cv_game_mission = organelle_name
    st.session_state.cv_game_questions = list(range(10))
    random.shuffle(st.session_state.cv_game_questions)
    st.session_state.cv_game_index = 0
    st.session_state.cv_game_answers = {}
    st.session_state.cv_game_submitted = False
    st.session_state.cv_game_finished = False


def return_to_main():
    st.switch_page("app.py")


def return_to_mission_select():
    st.session_state.cv_game_mission = None
    st.session_state.cv_game_questions = []
    st.session_state.cv_game_index = 0
    st.session_state.cv_game_answers = {}
    st.session_state.cv_game_submitted = False
    st.session_state.cv_game_finished = False
    st.rerun()


# =========================================================
# 6. 미션 선택 화면
# =========================================================

if st.session_state.cv_game_mission is None:
    st.markdown(
        """
        <div class="overview">
          <div class="info-label">MISSION BRIEFING / 작전 브리핑</div>
          <br>
          각 소기관의 정보 파일에서 학습한 내용을 확인하십시오.
          미션 하나는 10문제로 구성되며, 정답 수에 따라 작전 결과가 판정됩니다.
          <br><br>
          <b>MISSION OBJECTIVE</b> · 구조 분석 / 기능 판별 / 작동 원리 / 소기관 간 관계
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("## 작전 선택 | SELECT OPERATION")
    st.caption("검증할 소기관을 선택하면 해당 소기관 전용 미션이 시작됩니다.")

    organelle_names = list(MISSIONS.keys())
    for start in range(0, len(organelle_names), 3):
        row_names = organelle_names[start:start + 3]
        columns = st.columns(3, gap="large")
        for col, name in zip(columns, row_names):
            data = MISSIONS[name]
            with col:
                st.markdown(
                    f"""
                    <div class="mission-card">
                      <div class="mission-code">{data['code']} / INTELLIGENCE FILE</div>
                      <div class="mission-title">{name}</div>
                      <div class="mission-desc">{data['summary']}<br>QUESTIONS · 10<br>STATUS · READY</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(
                    f"{data['code']} 작전 시작",
                    key=f"start_{data['code']}",
                    use_container_width=True,
                ):
                    start_mission(name)
                    st.rerun()

    st.markdown("---")
    st.markdown(
        """
        <div class="side-info">
        RULES OF ENGAGEMENT / 작전 규칙<br>
        01 · 각 미션은 10문제로 구성됩니다.<br>
        02 · 정답 0~4개: MISSION FAILED<br>
        03 · 정답 5~8개: MISSION COMPROMISED<br>
        04 · 정답 9~10개: MISSION COMPLETE
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 7. 문제 풀이 화면
# =========================================================

else:
    mission_name = st.session_state.cv_game_mission
    mission = MISSIONS[mission_name]
    question_order = st.session_state.cv_game_questions
    question_index = st.session_state.cv_game_index
    question_number = question_index + 1
    question_data_index = question_order[question_index]
    question, options, correct_index, explanation = mission["questions"][question_data_index]

    st.markdown(
        f"""
        <div class="overview">
          <div class="info-label">MISSION BRIEFING / {mission['code']}</div>
          <h3 style="margin-top:10px;">{mission_name} 작전 · {mission['english']}</h3>
          {mission['briefing']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    top_left, top_right = st.columns([2, 1])
    with top_left:
        st.markdown(f"### QUESTION {question_number:02d} / 10")
        st.caption("INTELLIGENCE ANALYSIS · 정보 분석")
    with top_right:
        st.markdown(f"**MISSION STATUS:** `ACTIVE`")
        st.markdown(f"**FILE:** `{mission['code']}`")

    st.progress(question_number / 10, text=f"MISSION PROGRESS · {question_number}/10")

    st.markdown(
        f"""
        <div class="report-box">
          <div class="info-label">INTELLIGENCE REPORT / {question_number:02d}</div>
          <br>
          <div style="font-size:20px;font-weight:600;color:#dceaf0;">{question}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    answer_key = f"{mission_name}_{question_data_index}"
    previous_answer = st.session_state.cv_game_answers.get(answer_key)

    with st.form(key=f"question_form_{mission_name}_{question_index}"):
        chosen = st.radio(
            "분석 결과를 선택하십시오.",
            options=list(range(len(options))),
            format_func=lambda i: f"{chr(65 + i)}. {options[i]}",
            index=previous_answer if previous_answer is not None else None,
            key=f"answer_radio_{mission_name}_{question_index}",
        )
        submitted = st.form_submit_button("답안 제출 / SUBMIT INTELLIGENCE", use_container_width=True)

    if submitted:
        st.session_state.cv_game_answers[answer_key] = chosen
        st.session_state.cv_game_submitted = True
        st.rerun()

    if st.session_state.cv_game_submitted:
        current_answer = st.session_state.cv_game_answers.get(answer_key)
        if current_answer == correct_index:
            st.markdown(
                """
                <div class="report-box" style="border-left:3px solid #57d9e8;">
                  <div class="info-label">ANALYSIS CONFIRMED</div>
                  <b>정보 분석 성공</b><br>정확한 판단입니다. 다음 분석 단계로 진행하십시오.
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="report-box" style="border-left:3px solid #b86b6b;">
                  <div style="color:#d16b6b;font-family:'IBM Plex Mono',monospace;font-size:11px;">ANALYSIS ERROR</div>
                  <b>정보 분석 오류</b><br>정답과 해설을 확인하고 내용을 검토하십시오.
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="report-box">
              <div class="info-label">INTELLIGENCE NOTES / 해설</div>
              {explanation}
            </div>
            """,
            unsafe_allow_html=True,
        )

        if question_index < 9:
            if st.button("다음 분석 단계로 / NEXT QUESTION", use_container_width=True):
                st.session_state.cv_game_index += 1
                st.session_state.cv_game_submitted = False
                st.rerun()
        else:
            if st.button("최종 작전 평가 / FINAL DEBRIEF", use_container_width=True):
                st.session_state.cv_game_finished = True
                st.rerun()

    # =====================================================
    # 8. 최종 결과 화면
    # =====================================================

    if st.session_state.cv_game_finished:
        correct_count = 0
        answer_details = []
        for idx, qdata in enumerate(mission["questions"]):
            key = f"{mission_name}_{idx}"
            user_answer = st.session_state.cv_game_answers.get(key)
            is_correct = user_answer == qdata[2]
            if is_correct:
                correct_count += 1
            answer_details.append((idx, qdata, user_answer, is_correct))

        wrong_count = 10 - correct_count
        score = correct_count * 10

        if correct_count <= 4:
            status = "MISSION FAILED"
            korean_status = "작전 실패"
            status_color = "#d16b6b"
            report = "작전 목표 달성에 실패했습니다. 오답 분석을 진행하고 해당 소기관의 정보 파일을 다시 검토하십시오."
            followup = "OBJECTIVE FAILED / 재훈련 및 재도전 필요"
        elif correct_count <= 8:
            status = "MISSION COMPROMISED"
            korean_status = "부분적 작전 성공"
            status_color = "#d9a45e"
            report = "작전 목표는 일부 달성했지만 분석 과정에서 오류가 확인되었습니다. 오답 해설을 검토해 정보 정확도를 높이십시오."
            followup = "OBJECTIVE PARTIALLY SECURED / 오류 항목 보완 필요"
        else:
            status = "MISSION COMPLETE"
            korean_status = "작전 성공"
            status_color = "#57d9e8"
            report = "분석 목표를 달성했습니다. 해당 소기관의 핵심 정보를 정확하게 이해하고 있습니다."
            followup = "ALL OBJECTIVES SECURED / 작전 성공"

        st.markdown("---")
        st.markdown(
            f"""
            <div class="top-strip">
              <span>MISSION DEBRIEF / 작전 결과 판정</span>
              <span>FILE / {mission['code']}</span>
              <span>STATUS / REVIEW</span>
            </div>
            <div class="eyebrow">OPERATIONAL ASSESSMENT // FINAL REPORT</div>
            <h1 style="color:{status_color};">{status}</h1>
            <h2>{korean_status}</h2>
            <div class="report-box" style="border-left:3px solid {status_color};">
              <div style="color:{status_color};font-family:'IBM Plex Mono',monospace;font-size:11px;">OBJECTIVE STATUS / {status}</div>
              {report}
            </div>
            """,
            unsafe_allow_html=True,
        )

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("MISSION SCORE", f"{score} / 100")
        metric2.metric("CORRECT ANSWERS", f"{correct_count} / 10")
        metric3.metric("ERROR REPORT", f"{wrong_count} / 10")

        st.markdown(
            f"""
            <div class="report-box">
              <div class="info-label">RECOMMENDED ACTION / 후속 조치</div>
              {followup}
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("오답 및 정답 전체 보고서 / REVIEW ANSWERS"):
            for idx, qdata, user_answer, is_correct in answer_details:
                qtext, opts, correct_idx, explain = qdata
                label = "분석 성공" if is_correct else "분석 오류"
                st.markdown(f"**{idx + 1:02d}. {qtext}**")
                if user_answer is None:
                    st.write("제출 기록 없음")
                else:
                    st.write(f"선택한 답: {chr(65 + user_answer)}. {opts[user_answer]}")
                st.write(f"정답: {chr(65 + correct_idx)}. {opts[correct_idx]}")
                st.caption(f"{label} · {explain}")
                st.markdown("---")

        if correct_count <= 8:
            if st.button("재도전 / RETURN TO COMMAND CENTER", use_container_width=True):
                return_to_main()
        else:
            if st.button("작전 성공 확인 / RETURN TO COMMAND CENTER", use_container_width=True):
                return_to_main()

        if st.button("다른 소기관 미션 선택 / SELECT ANOTHER MISSION", use_container_width=True):
            return_to_mission_select()
'''

path = Path("/mnt/data/10_작전훈련.py")
path.write_text(code, encoding="utf-8")
print(f"생성 완료: {path}")
print(f"파일 크기: {path.stat().st_size:,} bytes")
