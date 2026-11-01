
import streamlit as st

# =========================================================
# 1. 기본 설정
# =========================================================

st.set_page_config(
    page_title="TASK FORCE BIO | Operation Cell Vision",
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

    .directive {
        grid-template-columns: 1fr;
        gap: 12px;
    }
}
</style>
""")

# =========================================================
# 3. 상단 보안 상태
# =========================================================

st.html("""
<div class="top-strip">
    <span>TASK FORCE BIO // SPECIAL OPERATIONS</span>
    <span>SECURITY: <strong>RESTRICTED</strong></span>
    <span>CHANNEL: <strong>COMMAND BRIEFING</strong></span>
    <span>STATUS: <strong>AWAITING DEPLOYMENT</strong></span>
</div>

<div class="briefing-label">CLASSIFIED // PERSONNEL ONLY</div>
<div class="briefing-title">MISSION BRIEFING</div>
<div class="briefing-subtitle">OPERATION CELL VISION</div>
""")

# =========================================================
# 4. 메인 작전 브리핑
# =========================================================

st.html("""
<div class="hero">
    <div class="hero-inner">

        <div class="classification">
            CLASSIFIED // AUTHORIZED PERSONNEL ONLY
        </div>

        <div class="hero-kicker">
            TASK FORCE BIO // PERSONNEL BRIEFING
        </div>

        <h1 class="hero-title">
            OPERATION<br>
            <span>CELL VISION</span>
        </h1>

        <div class="hero-subtitle">
            KNOW THE CELL. STOP THE THREAT.
        </div>

        <div class="hero-rule"></div>

        <div class="briefing-copy">
            대원, 브리핑에 집중해라.<br><br>

            최근 우리 정보부가 적대 세력의 비밀 작전 자료를 확보했다.
            분석 결과, 그들은 세포 내부의 생명 유지 시스템을 장악하고
            전체 기능을 마비시키려는 계획을 추진하고 있다.<br><br>

            적의 표적은 세포를 구성하는 핵심 소기관들이다.
            유전 정보를 관리하는 핵부터 단백질을 합성하는 리보솜,
            에너지를 생산하는 미토콘드리아까지.
            각 소기관은 서로 긴밀하게 연결되어 있다.
            한 부분의 기능이 무너지면 다른 시스템까지 연쇄적으로 영향을 받는다.<br><br>

            우리가 확보한 자료에는 적의 작전 계획을 파악할 수 있는
            중요한 정보가 담겨 있다. 하지만 자료는 아직 완전히 분석되지 않았다.
            소기관의 구조와 기능을 정확히 이해해야만 숨겨진 정보를 해독하고
            적의 다음 행동을 예측할 수 있다.<br><br>

            <strong>네 임무는 명확하다.</strong><br><br>

            먼저 분석실에 진입해 우리가 확보한 기밀 자료를 조사해라.
            세포 소기관의 구조와 기능, 그리고 소기관 사이의 상호작용을 학습해라.
            이 지식은 적의 계획을 분석하기 위한 핵심 정보다.<br><br>

            모든 분석을 마친 뒤 최종 작전에 투입되어라.
            학습한 지식을 활용해 적의 계략을 무너뜨리고
            세포 시스템을 지켜내는 것이 최종 목표다.<br><br>

            <strong>정보 없이 돌입하지 마라.</strong>
            준비되지 않은 채 진입하면 임무는 실패한다.
            충분한 정보를 확보하고, 정확하게 분석하고,
            마지막 순간까지 판단력을 유지해라.<br><br>

            <strong>TASK FORCE BIO는 네 분석 능력을 믿는다.</strong>
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
        적의 이름은 CELL REQUIEM이다.
        그들의 계획을 저지하려면 먼저 우리가 확보한 자료부터 분석해야 한다.
        분석실에서 소기관 정보를 학습하고, 모든 준비를 마친 뒤 최종 작전에 진입해라.
        명심해라, 대원. 정확한 분석 없이는 임무를 완수할 수 없다.
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
    <span>TASK FORCE BIO // SPECIAL OPERATIONS</span>
    <span>OPERATION CELL VISION</span>
    <span>END OF BRIEFING</span>
</div>
""")
