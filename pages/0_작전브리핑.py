
import streamlit as st

# =========================================================
# 1. 기본 설정
# =========================================================

st.set_page_config(
    page_title="CELL VISION | Operation Cell Shield",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# 2. 작전 브리핑 디자인
# =========================================================

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;900&display=swap');

:root {
    --bg: #040910;
    --panel: #091521;
    --line: #294554;
    --cyan: #57d9e8;
    --white: #edf8fc;
    --muted: #8ca5b4;
    --red: #e36b72;
}

html, body, [class*="css"] {
    font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace;
}

.stApp {
    background:
        radial-gradient(ellipse at 76% 12%, rgba(20,76,100,.24), transparent 38%),
        radial-gradient(ellipse at 8% 90%, rgba(13,47,67,.24), transparent 40%),
        linear-gradient(135deg, #040910 0%, #07111b 55%, #040910 100%);
    color: var(--white);
}

[data-testid="stAppViewContainer"] {
    background: transparent;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #07111b;
    border-right: 1px solid var(--line);
}

[data-testid="stSidebarNav"] {
    display: none !important;
}

.block-container {
    max-width: 100% !important;
    width: 100% !important;
    padding: 1.2rem 4vw 2rem 4vw !important;
}

.top-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    width: 100%;
    box-sizing: border-box;
    padding: 12px 18px;
    border-top: 2px solid #7897a8;
    border-bottom: 1px solid var(--line);
    background: linear-gradient(90deg, #132431, #07111b 75%);
    color: #9cb7c4;
    font-size: 10px;
    letter-spacing: 1.5px;
}

.top-strip strong {
    color: var(--cyan);
}

.briefing-label {
    color: #43B9FF;
    font-size: 12px;
    letter-spacing: 4px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 14px;
}

.briefing-title {
    color: #F1F5F9;
    font-size: clamp(38px, 6vw, 66px);
    line-height: 1.1;
    font-weight: 900;
    letter-spacing: -2px;
    margin-bottom: 12px;
}

.briefing-subtitle {
    color: #43B9FF;
    font-size: 17px;
    letter-spacing: 2px;
    margin-bottom: 24px;
}

.briefing-text {
    color: #B8C5D3;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 15px;
    line-height: 1.9;
}

.hero {
    position: relative;
    overflow: hidden;
    width: 100%;
    box-sizing: border-box;
    padding: clamp(28px, 5vw, 70px);
    margin-top: 22px;
    border: 1px solid #2d5063;
    border-top: 3px solid var(--cyan);
    background: linear-gradient(
        110deg,
        rgba(7,18,29,.98) 0%,
        rgba(9,27,41,.95) 57%,
        rgba(7,17,27,.97) 100%
    );
}

.hero::before {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    width: 32%;
    height: 100%;
    background: repeating-linear-gradient(
        135deg,
        transparent 0px,
        transparent 17px,
        rgba(87,217,232,.035) 18px,
        rgba(87,217,232,.035) 19px
    );
    pointer-events: none;
}

.hero-inner {
    position: relative;
    z-index: 1;
}

.classification {
    display: inline-block;
    color: #ff9da2;
    border: 1px solid rgba(227,107,114,.55);
    background: rgba(112,28,38,.17);
    padding: 8px 12px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 26px;
}

.hero-kicker {
    color: var(--cyan);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

.hero-title {
    color: var(--white);
    font-family: 'IBM Plex Mono', monospace;
    font-size: clamp(40px, 7vw, 88px);
    font-weight: 700;
    line-height: .98;
    letter-spacing: -2px;
    margin: 0;
    overflow-wrap: anywhere;
}

.hero-title span {
    color: var(--cyan);
}

.hero-subtitle {
    color: #9ab3c2;
    font-size: clamp(12px, 1.5vw, 16px);
    letter-spacing: 2px;
    margin-top: 22px;
}

.hero-rule {
    width: 100%;
    height: 1px;
    margin: 30px 0;
    background: linear-gradient(90deg, var(--cyan), #294554 65%, transparent);
}

.briefing-copy {
    max-width: 1050px;
    color: #d0dfe7;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: clamp(14px, 1.35vw, 17px);
    line-height: 2.05;
}

.briefing-copy strong {
    color: #ffffff;
}

.section-label {
    color: var(--cyan);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    padding: 12px 0;
    margin: 30px 0 14px;
    border-bottom: 1px solid var(--line);
}

.objectives-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
    margin-top: 18px;
}

.objective {
    min-width: 0;
    min-height: 180px;
    height: 100%;
    box-sizing: border-box;
    padding: 23px;
    background: linear-gradient(145deg, #0c1c29, #07111a);
    border: 1px solid #294554;
    border-top: 2px solid #456b7e;
}

.objective-number {
    color: var(--cyan);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 22px;
}

.objective-title {
    color: #edf8fc;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 19px;
    font-weight: 900;
    margin-bottom: 12px;
}

.objective-text {
    color: #91aab8;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 13px;
    line-height: 1.9;
}

.directive {
    display: grid;
    grid-template-columns: minmax(130px, .7fr) 3fr;
    gap: 20px;
    align-items: start;
    padding: 22px 25px;
    margin-top: 24px;
    background: rgba(10,26,39,.78);
    border: 1px solid var(--line);
    border-left: 4px solid var(--cyan);
}

.directive-label {
    color: var(--cyan);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.directive-text {
    color: #d0dfe7;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 14px;
    line-height: 1.9;
}

.bottom-strip {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    padding-top: 16px;
    margin-top: 28px;
    border-top: 1px solid var(--line);
    color: #688696;
    font-size: 9px;
    letter-spacing: 1.3px;
}

div[data-testid="stButton"] > button {
    min-height: 54px;
    width: 100%;
    background: linear-gradient(90deg, #116c8e, #1284a0) !important;
    color: #ffffff !important;
    border: 1px solid var(--cyan) !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    transition: .18s ease-in-out;
}

div[data-testid="stButton"] > button:hover {
    background: #1598b5 !important;
    border-color: #b3f6ff !important;
    box-shadow: 0 0 24px rgba(87,217,232,.17);
    color: #ffffff !important;
}

#MainMenu, footer {
    visibility: hidden;
}

@media (max-width: 700px) {
    .block-container {
        padding: .8rem 4vw 1.5rem !important;
    }

    .hero {
        padding: 25px 20px;
    }

    .hero-title {
        letter-spacing: -1px;
    }

    .objectives-grid {
        grid-template-columns: 1fr;
    }

    .objective {
        min-height: auto;
    }

    .directive {
        grid-template-columns: 1fr;
        gap: 12px;
    }
}
</style>
""")

# =========================================================
# 3. 상단 보안 상태 및 브리핑 안내
# =========================================================

st.html("""
<div class="top-strip">
    <span>CV // BIOLOGICAL OPERATIONS UNIT</span>
    <span>SECURITY: <strong>RESTRICTED</strong></span>
    <span>CHANNEL: <strong>COMMAND BRIEFING</strong></span>
    <span>STATUS: <strong>AWAITING DEPLOYMENT</strong></span>
</div>

<div class="briefing-label">CLASSIFIED // PERSONNEL ONLY</div>
<div class="briefing-title">MISSION BRIEFING</div>
<div class="briefing-subtitle">OPERATION CELL SHIELD</div>

<div class="briefing-text">
    대원, 긴급 작전이 하달되었습니다.<br><br>
    인체를 구성하는 세포 내부에서 이상 상황이 발생했습니다.
    임무를 완수하려면 세포를 구성하는 각 소기관의 구조와 기능을
    정확하게 파악해야 합니다.<br><br>
    귀하는 <b>TASK FORCE CELL VISION</b>의 작전 요원입니다.
    지금부터 생물학적 정보를 수집하고 분석하여 최종 작전에 대비하십시오.
    확보한 지식은 마지막 작전에서 핵심적인 역할을 하게 됩니다.
</div>
""")

# =========================================================
# 4. 메인 작전 브리핑 + 작전 목표
# =========================================================

st.html("""
<div class="hero">
    <div class="hero-inner">
        <div class="classification">
            CLASSIFIED // AUTHORIZED PERSONNEL ONLY
        </div>

        <div class="hero-kicker">
            TASK FORCE CELL VISION // PERSONNEL BRIEFING
        </div>

        <h1 class="hero-title">
            OPERATION<br>
            <span>CELL SHIELD</span>
        </h1>

        <div class="hero-subtitle">
            KNOW THE CELL. COMPLETE THE MISSION.
        </div>

        <div class="hero-rule"></div>

        <div class="briefing-copy">
            대원, 지금부터 네 임무를 설명하겠다.<br><br>

            세포 내부의 생명 시스템을 분석하고, 최종 작전을 수행할 준비를 마쳐라.
            네가 상대할 문제는 단순한 지식 퀴즈가 아니다.
            세포를 구성하는 소기관이 어떤 역할을 맡고, 서로 어떻게 협력하는지
            이해해야 해결할 수 있다.<br><br>

            핵의 유전 정보 관리부터 리보솜의 단백질 합성,
            미토콘드리아의 에너지 전환, 소포체와 골지체의 물질 처리까지.
            각 소기관의 기능을 정확히 파악하고 그 연결 관계를 분석해라.<br><br>

            <strong>정보 없이 돌입하지 마라.</strong>
            먼저 분석실에서 자료를 확보하고, 학습을 마친 뒤 최종 작전에 진입해라.
            네가 확보한 지식이 임무의 성패를 결정한다.
        </div>

        <div class="section-label">
            MISSION OBJECTIVES // 작전 목표
        </div>

        <div class="objectives-grid">
            <div class="objective">
                <div class="objective-number">OBJECTIVE / 01</div>
                <div class="objective-title">정보 확보</div>
                <div class="objective-text">
                    세포 전체 구조를 확인하고 핵심 소기관의 위치와 특징을 파악해라.
                </div>
            </div>

            <div class="objective">
                <div class="objective-number">OBJECTIVE / 02</div>
                <div class="objective-title">기능 분석</div>
                <div class="objective-text">
                    각 소기관의 역할을 학습하고 단백질 합성, 물질 수송,
                    에너지 전환의 연결 관계를 이해해라.
                </div>
            </div>

            <div class="objective">
                <div class="objective-number">OBJECTIVE / 03</div>
                <div class="objective-title">최종 작전</div>
                <div class="objective-text">
                    확보한 생물학적 지식을 활용해 최종 작전의 문제를 해결해라.
                    준비가 끝났다면 임무를 완수해라.
                </div>
            </div>
        </div>
    </div>
</div>
""")

# =========================================================
# 5. 지휘관의 최종 지시
# =========================================================

st.html("""
<div class="directive">
    <div class="directive-label">COMMAND DIRECTIVE</div>
    <div class="directive-text">
        네 첫 번째 임무는 분석실에 진입해 소기관 정보를 확보하는 것이다.
        각 자료를 충분히 학습한 다음 최종 작전에 도전해라.
        임무를 서두르지 마라. 정확한 분석이 승리를 만든다.
    </div>
</div>
""")

st.write("")
st.write("")

# =========================================================
# 6. 작전 시작
# =========================================================

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:
    if st.button(
        "ACKNOWLEDGE BRIEFING  /  작전 개시",
        use_container_width=True,
        type="primary",
    ):
        st.session_state["briefing_completed"] = True
        st.switch_page("app.py")

# =========================================================
# 7. 하단 상태 표시
# =========================================================

st.html("""
<div class="bottom-strip">
    <span>CELL VISION // BIOLOGICAL OPERATIONS UNIT</span>
    <span>ALL SYSTEMS STANDING BY</span>
    <span>END OF BRIEFING</span>
</div>
""")
