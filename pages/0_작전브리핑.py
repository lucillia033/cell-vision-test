
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

st.markdown(
    """
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
            radial-gradient(ellipse at 76% 12%, rgba(20, 76, 100, 0.24), transparent 38%),
            radial-gradient(ellipse at 8% 90%, rgba(13, 47, 67, 0.24), transparent 40%),
            linear-gradient(135deg, #040910 0%, #07111b 55%, #040910 100%);
        color: var(--white);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: #07111b;
        border-right: 1px solid #294554;
    }

    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    .block-container {
        max-width: 100% !important;
        width: 100% !important;
        padding: 1.2rem 4vw 2rem 4vw !important;
    }

    h1, h2, h3, p {
        color: var(--white);
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

    .hero {
        position: relative;
        overflow: hidden;
        width: 100%;
        box-sizing: border-box;
        padding: clamp(28px, 5vw, 70px);
        margin-top: 22px;
        border: 1px solid #2d5063;
        border-top: 3px solid var(--cyan);
        background:
            linear-gradient(110deg, rgba(7, 18, 29, 0.98) 0%,
            rgba(9, 27, 41, 0.95) 57%,
            rgba(7, 17, 27, 0.97) 100%);
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
            rgba(87, 217, 232, 0.035) 18px,
            rgba(87, 217, 232, 0.035) 19px
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
        border: 1px solid rgba(227, 107, 114, 0.55);
        background: rgba(112, 28, 38, 0.17);
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
        line-height: 0.98;
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
        margin: 22px 0 14px 0;
        border-bottom: 1px solid var(--line);
    }

    .objective {
        height: 100%;
        min-height: 180px;
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
        grid-template-columns: minmax(130px, 0.7fr) 3fr;
        gap: 20px;
        align-items: start;
        padding: 22px 25px;
        margin-top: 24px;
        background: rgba(10, 26, 39, 0.78);
        border: 1px solid #294554;
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
        min-height: 62px;
        width: 100%;
        background: linear-gradient(90deg, #116c8e, #1284a0) !important;
        color: #ffffff !important;
        border: 1px solid #57d9e8 !important;
        border-radius: 0 !important;
        font-family: 'IBM Plex Mono', 'Noto Sans KR', monospace !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        transition: 0.18s ease-in-out;
    }

    div[data-testid="stButton"] > button:hover {
        background: #1598b5 !important;
        border-color: #b3f6ff !important;
        box-shadow: 0 0 24px rgba(87, 217, 232, 0.17);
        color: #ffffff !important;
    }

    [data-testid="stAlert"] {
        border-radius: 0;
        background: #0b1b28;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 0.8rem 4vw 1.5rem 4vw !important;
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

        .objective {
            min-height: auto;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 3. 상단 보안 상태 표시
# =========================================================

st.markdown(
    """
    <div class="top-strip">
        <span>CV // BIOLOGICAL OPERATIONS UNIT</span>
        <span>SECURITY: <strong>RESTRICTED</strong></span>
        <span>CHANNEL: <strong>COMMAND BRIEFING</strong></span>
        <span>STATUS: <strong>AWAITING DEPLOYMENT</strong></span>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 4. 메인 작전 브리핑
# =========================================================

st.markdown(
    """
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
                대원, 집중해라. 지금부터 작전 브리핑을 시작한다.<br><br>

                네 임무는 세포 내부의 생명 시스템을 분석하고,
                최종 작전을 완수하는 것이다. 단순히 용어 몇 개 외우고
                끝낼 생각은 버려라. 현장에서 필요한 건 암기가 아니라
                정확한 판단이다.<br><br>

                핵은 유전 정보를 관리한다. 리보솜은 단백질을 합성하고,
                미토콘드리아는 세포 활동에 필요한 에너지를 생산한다.
                소포체와 골지체는 물질을 처리하고 전달한다.
                세포막은 세포 안팎의 물질 이동을 조절한다.<br><br>

                <strong>각 소기관의 역할과 연결 관계를 파악해라.</strong>
                하나의 기능만 알아서는 부족하다. 세포가 어떻게 작동하는지
                전체 흐름을 이해해야 한다.<br><br>

                먼저 분석실에 진입해 자료를 확보한다. 소기관별 정보를
                학습하고 준비 상태를 확인해라. 학습을 마친 뒤에만
                최종 작전에 도전한다.<br><br>

                <strong>명심해라. 정보가 없으면 판단도 없다.</strong>
                준비를 마치고, 명령을 기다려라.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 5. 임무 목표
# =========================================================

st.markdown(
    '<div class="section-label">MISSION OBJECTIVES // 작전 목표</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(
        """
        <div class="objective">
            <div class="objective-number">OBJECTIVE / 01</div>
            <div class="objective-title">정보 확보</div>
            <div class="objective-text">
                분석실에 진입해 세포 전체 구조를 확인해라.
                각 소기관의 위치와 기본 정보를 확보한다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="objective">
            <div class="objective-number">OBJECTIVE / 02</div>
            <div class="objective-title">기능 분석</div>
            <div class="objective-text">
                각 소기관의 역할을 정확히 파악해라.
                단백질 합성, 물질 수송, 에너지 생산의 연결 관계를 분석한다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="objective">
            <div class="objective-number">OBJECTIVE / 03</div>
            <div class="objective-title">최종 작전</div>
            <div class="objective-text">
                확보한 생물학적 지식을 활용해 주어진 문제를 해결해라.
                준비가 끝났다면 최종 작전에 투입한다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# 6. 지휘관의 최종 지시
# =========================================================

st.markdown(
    """
    <div class="directive">
        <div class="directive-label">COMMAND DIRECTIVE</div>
        <div class="directive-text">
            첫 번째 명령이다. 분석실로 이동해 소기관 자료를 확보해라.
            각 자료의 학습을 마친 뒤 최종 작전에 진입한다.
            서두르지 마라. 상황을 이해하고, 정확하게 판단해라.
            준비가 끝나면 작전을 개시한다.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# =========================================================
# 7. 작전 시작
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

st.markdown(
    """
    <div class="bottom-strip">
        <span>CELL VISION // BIOLOGICAL OPERATIONS UNIT</span>
        <span>AWAITING OPERATOR CONFIRMATION</span>
        <span>END OF BRIEFING</span>
    </div>
    """,
    unsafe_allow_html=True,
)
