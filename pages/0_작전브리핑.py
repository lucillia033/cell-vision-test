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

    .objectives {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
    }

    .objective {
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
        font-weight: 
