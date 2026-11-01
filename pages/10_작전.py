
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cell Vision - Operation Cell Shield",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {
        background: #070C13;
    }
    [data-testid="stSidebar"] {
        background: #101923;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="color:#8ABCE8;font-size:12px;letter-spacing:3px;">
        CELL VISION / BIOLOGICAL OPERATIONS UNIT
    </div>
    <div style="color:#F0F5FA;font-size:30px;font-weight:800;
                letter-spacing:2px;margin-top:4px;">
        OPERATION CELL SHIELD
    </div>
    <div style="color:#8598AD;font-size:13px;margin-top:5px;
                margin-bottom:16px;">
        BLACK VEIL INTERCEPTION PROTOCOL
    </div>
    """,
    unsafe_allow_html=True,
)

game_html = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    color: #edf4fc;
    background: #070c13;
    font-family: Arial, "Malgun Gothic", sans-serif;
}

button { font-family: inherit; }

.game {
    position: relative;
    width: 100%;
    min-height: 720px;
    overflow: hidden;
    border: 1px solid #293d51;
    border-radius: 10px;
    background:
        radial-gradient(ellipse at 50% 30%, #183653, transparent 48%),
        linear-gradient(180deg, #111e2d, #101927 55%, #070b11);
}

.grid {
    position: absolute;
    inset: 0;
    opacity: .13;
    pointer-events: none;
    background-image:
        linear-gradient(#5c8cb1 1px, transparent 1px),
        linear-gradient(90deg, #5c8cb1 1px, transparent 1px);
    background-size: 42px 42px;
}

.topbar {
    position: relative;
    z-index: 3;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
    padding: 19px 18px;
}

.kicker {
    color: #8dbce9;
    font-size: 10px;
    letter-spacing: 2px;
    margin-bottom: 6px;
}

.heading {
    font-size: clamp(16px, 2.5vw, 22px);
    font-weight: 900;
    letter-spacing: 1.3px;
}

.sub {
    color: #8194aa;
    font-size: 10px;
    margin-top: 5px;
    letter-spacing: 1px;
}

.top-actions {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 10px;
}

.enemy-hud { width: min(250px, 32vw); }

.hud-label {
    display: flex;
    justify-content: space-between;
    gap: 8px;
    margin-bottom: 7px;
    color: #d6e0eb;
    font-size: 10px;
    letter-spacing: 1px;
}

.bar-track {
    display: flex;
    gap: 3px;
    height: 12px;
    padding: 2px;
    border: 1px solid #85414b;
    background: #281b24;
}

.enemy-cell {
    flex: 1;
    background: #e24e5d;
    box-shadow: 0 0 6px #a72c3b66;
}

.enemy-cell.empty {
    background: #241b25;
    box-shadow: none;
}

.exit-button {
    flex-shrink: 0;
    padding: 10px 12px;
    border: 1px solid #75869a;
    background: #17212d;
    color: #e3ebf4;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: .7px;
    cursor: pointer;
}

.exit-button:hover {
    border-color: #9bcfff;
    background: #2a3a4b;
}

.arena {
    position: relative;
    height: 300px;
    overflow: hidden;
    border-top: 1px solid #233548;
    border-bottom: 1px solid #314358;
    background:
        radial-gradient(ellipse at 50% 100%, #27445c77, transparent 55%),
        linear-gradient(180deg, transparent 65%, #070c13);
}

.machine {
    position: absolute;
    left: 50%;
    top: 15px;
    width: 190px;
    height: 205px;
    transform: translateX(-50%);
    border: 2px solid #32648c88;
    border-radius: 48% 48% 12% 12%;
    background: linear-gradient(180deg, #214b6c33, #07111d99);
    box-shadow: 0 0 45px #1678ba22, inset 0 0 30px #287db322;
}

.machine::before {
    content: "";
    position: absolute;
    left: 50%;
    top: 12px;
    width: 80px;
    height: 150px;
    transform: translateX(-50%);
    border: 3px solid #69baf2;
    border-radius: 50%;
    box-shadow: 0 0 20px #4ba9ff66, inset 0 0 20px #4ba9ff44;
}

.machine::after {
    content: "BIOLOGICAL CORE";
    position: absolute;
    bottom: 12px;
    left: 0;
    right: 0;
    color: #8bc8f2;
    text-align: center;
    font-size: 9px;
    letter-spacing: 2px;
}

.floor {
    position: absolute;
    z-index: 1;
    bottom: 0;
    left: 0;
    right: 0;
    height: 45px;
    border-top: 2px solid #476580;
    background: linear-gradient(180deg, #1c2b3b, #070b11);
}

.floor::after {
    content: "";
    position: absolute;
    top: 12px;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #54a9ec, transparent);
}

.unit-label {
    position: absolute;
    bottom: 185px;
    z-index: 4;
    color: #a9c7df;
    font-size: 9px;
    letter-spacing: 1px;
    white-space: nowrap;
}

.player-label { left: 5%; }
.enemy-label { right: 5%; color: #e59aa4; }

.fighter {
    position: absolute;
    z-index: 3;
    bottom: 34px;
    width: 112px;
    height: 158px;
}

.player { left: 12%; }
.enemy { right: 12%; transform: scaleX(-1); }

.body-shape {
    position: absolute;
    z-index: 2;
    left: 29px;
    top: 53px;
    width: 55px;
    height: 68px;
    border: 1px solid #71859a;
    background: linear-gradient(90deg, #263a4b, #405469 42%, #152332 75%);
    clip-path: polygon(20% 0, 80% 0, 100% 28%, 88% 100%, 12% 100%, 0 28%);
}

.body-shape::before {
    content: "";
    position: absolute;
    top: 12px;
    left: 12px;
    width: 28px;
    height: 34px;
    border: 1px solid #6d8296;
    background: linear-gradient(135deg, #273c4f, #111b27);
}

.body-shape::after {
    content: "";
    position: absolute;
    top: 8px;
    left: 20px;
    width: 8px;
    height: 46px;
    border-left: 1px solid #8295a8;
    border-right: 1px solid #8295a8;
    background: #101a25;
}

.helmet {
    position: absolute;
    z-index: 4;
    top: 10px;
    left: 32px;
    width: 49px;
    height: 49px;
    border: 2px solid #8798a8;
    border-radius: 43% 43% 27% 27%;
    background: linear-gradient(135deg, #586b7e, #202c3a 60%, #0b1119);
    box-shadow: inset 0 -5px 0 #101925;
}

.helmet::before {
    content: "";
    position: absolute;
    top: 18px;
    left: 5px;
    right: 5px;
    height: 8px;
    border: 1px solid #c5eaff;
    background: #8bcfff;
    box-shadow: 0 0 12px #4bb6ff;
}

.helmet::after {
    content: "";
    position: absolute;
    top: 4px;
    left: 10px;
    width: 24px;
    height: 5px;
    border: 1px solid #71869a;
    background: #182635;
}

.shoulder {
    position: absolute;
    z-index: 3;
    top: 57px;
    width: 25px;
    height: 28px;
    border: 1px solid #788b9e;
    border-radius: 5px;
    background: linear-gradient(135deg, #52687b, #1b2937);
}

.shoulder.left { left: 14px; transform: rotate(12deg); }
.shoulder.right { left: 75px; transform: rotate(-12deg); }

.arm {
    position: absolute;
    z-index: 1;
    top: 77px;
    width: 15px;
    height: 39px;
    border: 1px solid #5c7084;
    border-radius: 4px;
    background: linear-gradient(90deg, #182431, #3b4d5f);
}

.arm.left { left: 20px; transform: rotate(9deg); }
.arm.right { left: 81px; transform: rotate(-9deg); }

.belt {
    position: absolute;
    z-index: 4;
    top: 115px;
    left: 32px;
    width: 49px;
    height: 9px;
    border: 1px solid #677b8e;
    background: #101923;
}

.leg {
    position: absolute;
    z-index: 2;
    top: 119px;
    width: 20px;
    height: 34px;
    border: 1px solid #52687b;
    background: linear-gradient(90deg, #172331, #354657);
}

.leg.left { left: 35px; transform: rotate(4deg); }
.leg.right { left: 57px; transform: rotate(-4deg); }

.boot {
    position: absolute;
    z-index: 3;
    top: 146px;
    width: 25px;
    height: 9px;
    border: 1px solid #526477;
    border-radius: 3px;
    background: #0a1119;
}

.boot.left { left: 31px; }
.boot.right { left: 56px; }

.pouch {
    position: absolute;
    z-index: 4;
    top: 91px;
    left: 72px;
    width: 13px;
    height: 17px;
    border: 1px solid #718398;
    background: #182b3b;
}

.enemy .body-shape {
    border-color: #a45a66;
    background: linear-gradient(90deg, #34252f, #54404a 42%, #17151e 75%);
}

.enemy .helmet {
    border-color: #bd6975;
    background: linear-gradient(135deg, #58404a, #251a24 70%, #0b0b11);
}

.enemy .helmet::before {
    border-color: #ff9aa2;
    background: #fa4856;
    box-shadow: 0 0 12px #fa3349;
}

.enemy .shoulder,
.enemy .arm,
.enemy .leg { border-color: #8f515c; }

.enemy .shoulder {
    background: linear-gradient(135deg, #58313b, #211922);
}

.enemy .body-shape::before {
    border-color: #98515d;
    background: linear-gradient(135deg, #422833, #17121a);
}

.weapon-model {
    position: absolute;
    z-index: 6;
    top: 70px;
    left: 57px;
    width: 59px;
    height: 22px;
}

.weapon-stock {
    position: absolute;
    top: 4px;
    left: 0;
    width: 13px;
    height: 8px;
    border: 1px solid #8ba0b2;
    background: #283b4b;
}

.weapon-body {
    position: absolute;
    top: 2px;
    left: 10px;
    width: 31px;
    height: 12px;
    border: 1px solid #c1d1df;
    background: linear-gradient(180deg, #9aaaba, #37495a 60%, #172330);
}

.weapon-barrel {
    position: absolute;
    top: 5px;
    left: 39px;
    width: 20px;
    height: 5px;
    border: 1px solid #c6d5e2;
    background: #8b9bab;
}

.weapon-scope {
    position: absolute;
    top: -3px;
    left: 19px;
    width: 11px;
    height: 5px;
    border: 1px solid #8ca0b2;
    background: #182432;
}

.weapon-grip {
    position: absolute;
    top: 11px;
    left: 24px;
    width: 6px;
    height: 10px;
    border: 1px solid #718497;
    background: #263848;
    transform: rotate(12deg);
}

.weapon-model.grenade-mode,
.weapon-model.heavy-mode {
    top: 59px;
    left: 68px;
    width: 34px;
    height: 34px;
    transform: rotate(-15deg);
}

.weapon-model.grenade-mode .weapon-stock,
.weapon-model.grenade-mode .weapon-body,
.weapon-model.grenade-mode .weapon-barrel,
.weapon-model.grenade-mode .weapon-scope,
.weapon-model.grenade-mode .weapon-grip,
.weapon-model.heavy-mode .weapon-stock,
.weapon-model.heavy-mode .weapon-body,
.weapon-model.heavy-mode .weapon-barrel,
.weapon-model.heavy-mode .weapon-scope,
.weapon-model.heavy-mode .weapon-grip {
    display: none;
}

.weapon-model.grenade-mode::before {
    content: "";
    position: absolute;
    inset: 3px;
    border: 2px solid #c2d0dc;
    border-radius: 40%;
    background: radial-gradient(circle at 30% 25%, #b8c4cc, #566675 55%, #1b2937);
    box-shadow: 0 0 9px #ffad5d66;
}

.weapon-model.grenade-mode::after {
    content: "";
    position: absolute;
    top: -1px;
    left: 12px;
    width: 7px;
    height: 5px;
    border: 1px solid #f8d4a8;
    background: #e7a66a;
}

.weapon-model.heavy-mode::before {
    content: "";
    position: absolute;
    inset: 3px;
    border: 2px solid #ffb4a2;
    border-radius: 35%;
    background: radial-gradient(circle at 30% 25%, #fff1c9, #ff795a 50%, #812536);
    box-shadow: 0 0 15px #ff593c;
}

.weapon-model.heavy-mode::after {
    content: "H";
    position: absolute;
    top: 9px;
    left: 13px;
    color: white;
    font-size: 12px;
    font-weight: 900;
}

.enemy .weapon-model { left: -7px; }

.enemy .weapon-body {
    border-color: #d6a0a6;
    background: linear-gradient(180deg, #a76a73, #54313b 60%, #23151d);
}

.enemy .weapon-barrel {
    border-color: #d6a0a6;
    background: #9e626d;
}

.player.hit, .enemy.hit {
    filter: brightness(2.5) drop-shadow(0 0 14px #ff5267);
}

.player.hit { translate: -7px 0; }
.enemy.hit { transform: scaleX(-1) translateX(-7px); }

.player.attack { animation: recoil .22s ease; }

@keyframes recoil {
    0% { translate: 0 0; }
    40% { translate: -7px 0; }
    100% { translate: 0 0; }
}

.projectile {
    position: absolute;
    z-index: 7;
    display: none;
    width: 28px;
    height: 4px;
    border-radius: 4px;
    background: #80d5ff;
    box-shadow: 0 0 13px 4px #318dff;
    pointer-events: none;
}

.projectile.grenade {
    width: 14px;
    height: 14px;
    border: 1px solid #ffd09a;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 25%, #fff0bf, #ff9b55 45%, #a64029);
    box-shadow: 0 0 20px 8px #ff5c3588;
}

.projectile.heavy {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: radial-gradient(circle, #fff, #ffb65a 45%, #fa4856);
    box-shadow: 0 0 25px 12px #ff653c99;
}

.blast {
    position: absolute;
    z-index: 8;
    display: none;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #ffd7a1;
    box-shadow: 0 0 25px 18px #ff603b, 0 0 65px 35px #ffb34d88;
    pointer-events: none;
}

.bottom {
    position: relative;
    z-index: 4;
    display: grid;
    grid-template-columns: 190px minmax(0, 1fr);
    gap: 13px;
    padding: 13px;
}

.player-panel {
    padding: 13px;
    border: 1px solid #2a4056;
    background: #101b28;
}

.panel-title {
    margin-bottom: 12px;
    color: #9cc9ee;
    font-size: 11px;
    letter-spacing: 1.5px;
}

.small-label {
    margin: 12px 0 6px;
    color: #91a4b8;
    font-size: 10px;
}

.hp-track, .energy-track {
    display: flex;
    gap: 4px;
    height: 9px;
    padding: 1px;
    background: #253243;
}

.hp-unit {
    flex: 1;
    background: #62baff;
    box-shadow: 0 0 5px #45a6ff77;
}

.hp-unit.lost {
    background: #3b2029;
    box-shadow: none;
}

.energy-fill {
    width: 0%;
    height: 100%;
    background: #65d8db;
    transition: width .2s;
}

.weapon {
    margin-top: 6px;
    padding: 8px;
    border: 1px solid #344a60;
    background: #142131;
    color: #91a4b8;
    font-size: 10px;
}

.weapon.active {
    border-color: #65baff;
    background: #1b344a;
    color: white;
    box-shadow: inset 3px 0 #65baff;
}

.weapon.grenade-active {
    border-color: #ffad61;
    background: #3b2a20;
    color: #ffe0b8;
    box-shadow: inset 3px 0 #ffad61;
}

.weapon.heavy-active {
    border-color: #ff7180;
    background: #3a2029;
    color: #ffd4d9;
    box-shadow: inset 3px 0 #ff7180;
}

.weapon-hint {
    margin-top: 8px;
    color: #8da7bf;
    font-size: 9px;
    line-height: 1.6;
}

.question-panel {
    min-width: 0;
    padding: 16px;
    border: 1px solid #30475e;
    background: #0b121d;
}

.question-meta {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    color: #8ebce7;
    font-size: 10px;
    letter-spacing: 1px;
}

.question {
    margin: 13px 0 15px;
    font-size: 16px;
    line-height: 1.6;
    font-weight: 700;
}

.answers {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}

.answer {
    min-height: 43px;
    padding: 10px 12px;
    border: 1px solid #34475d;
    background: #101b29;
    color: #d4dfeb;
    text-align: left;
    font-size: 12px;
    cursor: pointer;
}

.answer:hover:not(:disabled) {
    border-color: #76bfff;
    background: #1b3044;
}

.answer:disabled { cursor: default; opacity: .8; }

.answer.correct {
    border-color: #61d5a0;
    background: #15372f;
    color: #b7f4d8;
}

.answer.wrong {
    border-color: #f16b78;
    background: #3a1c27;
    color: #ffc3c8;
}

.feedback {
    min-height: 35px;
    margin-top: 12px;
    color: #b2c3d5;
    font-size: 11px;
    line-height: 1.7;
}

.action-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
}

.action {
    padding: 10px 13px;
    border: 1px solid #52728e;
    background: #17293a;
    color: #e8f4ff;
    font-size: 11px;
    font-weight: 700;
    cursor: pointer;
}

.action:hover:not(:disabled) { background: #244664; }
.action:disabled { opacity: .35; cursor: not-allowed; }

.status {
    margin-top: 10px;
    color: #9eb3c9;
    font-size: 10px;
    line-height: 1.6;
}

.overlay {
    position: absolute;
    z-index: 20;
    inset: 0;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
    background: #03070df2;
    text-align: center;
}

.overlay.show { display: flex; }

.result-box {
    width: min(500px, 100%);
    padding: 30px 20px;
    border: 1px solid #536c85;
    background: #101a27;
    box-shadow: 0 0 60px #1a5b8a33;
}

.result-title {
    margin-bottom: 12px;
    font-size: clamp(25px, 5vw, 39px);
    font-weight: 900;
    letter-spacing: 2px;
}

.fail { color: #ff6a79; }
.win { color: #7bc9ff; }

.result-desc {
    margin-bottom: 22px;
    color: #c1cfde;
    font-size: 13px;
    line-height: 1.9;
}

.result-actions {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
}

.retry, .base-button {
    padding: 13px 18px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .7px;
    cursor: pointer;
}

.retry {
    border: 1px solid #6abaff;
    background: #193b57;
    color: #f2f8ff;
}

.base-button {
    border: 1px solid #75869a;
    background: #17212d;
    color: #e3ebf4;
}

.retry:hover { background: #255a80; }
.base-button:hover { background: #2a3a4b; }

@media (max-width: 680px) {
    .game { min-height: 760px; }
    .topbar { align-items: flex-start; padding: 14px; }
    .top-actions { flex-direction: column; align-items: flex-end; }
    .enemy-hud { width: 145px; max-width: 42vw; }
    .exit-button { padding: 8px; font-size: 9px; }
    .arena { height: 255px; }
    .machine { width: 140px; height: 155px; }
    .machine::before { width: 65px; height: 110px; }
    .fighter { scale: .8; transform-origin: bottom center; }
    .player { left: 1%; }
    .enemy { right: 1%; transform: scaleX(-.8); }
    .bottom { grid-template-columns: 1fr; padding: 9px; }
    .player-panel { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
    .panel-title { grid-column: 1 / -1; margin-bottom: 0; }
    .small-label { margin-top: 4px; }
    .question { font-size: 14px; }
    .answers { grid-template-columns: 1fr; }
}
</style>
</head>

<body>
<div class="game" id="game">
    <div class="grid"></div>

    <div class="topbar">
        <div>
            <div class="kicker">CELL VISION / OPERATION CELL SHIELD</div>
            <div class="heading">BLACK VEIL INTERCEPTION</div>
            <div class="sub">BIOLOGICAL THREAT ELIMINATION</div>
        </div>

        <div class="top-actions">
            <div class="enemy-hud">
                <div class="hud-label">
                    <span>ENEMY INTEGRITY</span>
                    <span id="enemyCount">10 / 10</span>
                </div>
                <div class="bar-track" id="enemyBars"></div>
            </div>
            <button class="exit-button" id="exitButton" type="button">
                EXIT TO BASE
            </button>
        </div>
    </div>

    <div class="arena" id="arena">
        <div class="machine"></div>
        <div class="unit-label player-label">PLAYER / OPERATIVE</div>
        <div class="unit-label enemy-label">BLACK VEIL / ELITE</div>

        <div class="fighter player" id="player">
            <div class="helmet"></div>
            <div class="body-shape"></div>
            <div class="shoulder left"></div>
            <div class="shoulder right"></div>
            <div class="arm left"></div>
            <div class="arm right"></div>
            <div class="belt"></div>
            <div class="leg left"></div>
            <div class="leg right"></div>
            <div class="boot left"></div>
            <div class="boot right"></div>
            <div class="pouch"></div>
            <div class="weapon-model" id="playerWeapon">
                <div class="weapon-stock"></div>
                <div class="weapon-body"></div>
                <div class="weapon-barrel"></div>
                <div class="weapon-scope"></div>
                <div class="weapon-grip"></div>
            </div>
        </div>

        <div class="fighter enemy" id="enemy">
            <div class="helmet"></div>
            <div class="body-shape"></div>
            <div class="shoulder left"></div>
            <div class="shoulder right"></div>
            <div class="arm left"></div>
            <div class="arm right"></div>
            <div class="belt"></div>
            <div class="leg left"></div>
            <div class="leg right"></div>
            <div class="boot left"></div>
            <div class="boot right"></div>
            <div class="pouch"></div>
            <div class="weapon-model">
                <div class="weapon-stock"></div>
                <div class="weapon-body"></div>
                <div class="weapon-barrel"></div>
                <div class="weapon-scope"></div>
                <div class="weapon-grip"></div>
            </div>
        </div>

        <div class="projectile" id="projectile"></div>
        <div class="blast" id="blast"></div>
        <div class="floor"></div>
    </div>

    <div class="bottom">
        <div class="player-panel">
            <div class="panel-title">OPERATIVE STATUS</div>

            <div>
                <div class="small-label">
                    PLAYER HP <span id="hpCount">4 / 4</span>
                </div>
                <div class="hp-track" id="hpBars"></div>
            </div>

            <div>
                <div class="small-label">
                    COMBO <span id="comboCount">0</span> / 2
                </div>
                <div class="energy-track">
                    <div class="energy-fill" id="energyFill"></div>
                </div>
            </div>

            <div style="grid-column:1 / -1;">
                <div class="small-label">EQUIPPED WEAPONS</div>
                <div class="weapon active" id="rifleSlot">1 — PULSE RIFLE</div>
                <div class="weapon" id="grenadeSlot">2 — GRENADE / 2 COMBO</div>
                <div class="weapon" id="heavySlot">3 — HEAVY BOMB / PERFECT</div>
                <div class="weapon-hint" id="weaponHint">
                    PULSE RIFLE 장착 중
                </div>
            </div>
        </div>

        <div class="question-panel">
            <div class="question-meta">
                <span id="questionNumber">MISSION QUESTION 01</span>
                <span id="accuracy">CORRECT 0 · WRONG 0</span>
            </div>
            <div class="question" id="questionText"></div>
            <div class="answers" id="answers"></div>
            <div class="feedback" id="feedback">
                문제를 풀어 작전을 진행하십시오.
            </div>
            <div class="action-row">
                <button class="action" id="nextButton" disabled>
                    NEXT QUESTION
                </button>
            </div>
            <div class="status" id="status">
                연속 2정답: 수류탄 공격 / 체력 소진: 임무 실패
            </div>
        </div>
    </div>

    <div class="overlay" id="overlay">
        <div class="result-box">
            <div class="result-title" id="resultTitle">MISSION FAILED</div>
            <div class="result-desc" id="resultDesc"></div>
            <div class="result-actions">
                <button class="retry" id="retryButton">RETRY MISSION</button>
                <button class="base-button" id="baseButton">RETURN TO BASE</button>
            </div>
        </div>
    </div>
</div>

<script>
"use strict";

const questionBank = [
    {
        q: "세포에서 ATP 생성과 밀접한 관련이 있는 소기관은 무엇인가요?",
        a: ["리보솜", "미토콘드리아", "골지체", "리소좀"],
        correct: 1,
        explain: "미토콘드리아는 세포 호흡을 통해 ATP를 생성하는 데 중요한 역할을 합니다."
    },
    {
        q: "단백질 합성이 일어나는 주요 장소는 어디인가요?",
        a: ["리보솜", "핵", "리소좀", "세포막"],
        correct: 0,
        explain: "리보솜은 유전 정보를 바탕으로 단백질을 합성합니다."
    },
    {
        q: "세포의 유전 정보가 주로 저장되는 곳은 어디인가요?",
        a: ["골지체", "세포질", "핵", "액포"],
        correct: 2,
        explain: "핵에는 DNA가 들어 있으며 세포의 활동을 조절하는 데 중요한 역할을 합니다."
    },
    {
        q: "세포 안팎의 물질 이동을 조절하는 구조는 무엇인가요?",
        a: ["리보솜", "세포막", "핵소체", "미토콘드리아"],
        correct: 1,
        explain: "세포막은 세포 내부와 외부 사이의 물질 이동을 선택적으로 조절합니다."
    },
    {
        q: "단백질의 가공과 분류, 포장에 관여하는 소기관은 무엇인가요?",
        a: ["골지체", "핵", "리소좀", "세포골격"],
        correct: 0,
        explain: "골지체는 단백질과 지질을 가공하고 분류해 목적지로 보내는 데 관여합니다."
    },
    {
        q: "세포 내 물질을 분해하는 효소를 포함하는 소기관은 무엇인가요?",
        a: ["리보솜", "골지체", "리소좀", "핵"],
        correct: 2,
        explain: "리소좀은 여러 분해 효소를 이용해 세포 내 물질을 분해합니다."
    },
    {
        q: "세포질에서 다양한 대사 반응이 일어나는 영역은 무엇인가요?",
        a: ["세포질", "핵막", "세포벽", "염색체"],
        correct: 0,
        explain: "세포질은 세포막 안쪽에서 핵을 제외한 영역으로, 다양한 대사 반응이 일어납니다."
    },
    {
        q: "세포의 형태 유지와 세포 내 구조물 이동에 관여하는 것은 무엇인가요?",
        a: ["세포골격", "리소좀", "핵소체", "골지체"],
        correct: 0,
        explain: "세포골격은 세포의 형태를 유지하고 세포 내 구조물의 이동에도 관여합니다."
    },
    {
        q: "단백질 합성에 필요한 정보를 담고 있는 분자는 무엇인가요?",
        a: ["DNA", "지방산", "포도당", "물"],
        correct: 0,
        explain: "DNA의 유전 정보는 RNA를 거쳐 단백질 합성에 이용됩니다."
    },
    {
        q: "세포 호흡에 사용되는 대표적인 에너지원은 무엇인가요?",
        a: ["포도당", "산소만", "핵산", "셀룰로스만"],
        correct: 0,
        explain: "포도당은 세포 호흡에서 분해되어 ATP 생성에 필요한 에너지를 제공합니다."
    },
    {
        q: "거친면 소포체 표면에 리보솜이 붙어 있는 이유는 무엇인가요?",
        a: ["단백질 합성", "DNA 복제만", "ATP 직접 저장", "세포 분열 중단"],
        correct: 0,
        explain: "거친면 소포체의 리보솜은 주로 막 단백질이나 분비 단백질 합성에 관여합니다."
    },
    {
        q: "농도 기울기를 따라 에너지 투입 없이 일어나는 물질 이동은 무엇인가요?",
        a: ["능동 수송", "확산", "소낭 수송만", "DNA 복제"],
        correct: 1,
        explain: "확산은 입자가 농도가 높은 곳에서 낮은 곳으로 순이동하는 현상입니다."
    }
];

const $ = (id) => document.getElementById(id);

let questions = [];
let questionIndex = 0;
let playerHP = 4;
let enemyHP = 10;
let combo = 0;
let correctTotal = 0;
let wrongTotal = 0;
let locked = false;
let finished = false;
let perfectRun = true;
let actionToken = 0;
let timers = [];

function later(callback, delay) {
    const timer = window.setTimeout(() => {
        timers = timers.filter((item) => item !== timer);
        callback();
    }, delay);

    timers.push(timer);
    return timer;
}

function clearTimers() {
    timers.forEach((timer) => window.clearTimeout(timer));
    timers = [];
}

function shuffle(array) {
    const result = [...array];

    for (let i = result.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [result[i], result[j]] = [result[j], result[i]];
    }

    return result;
}

function setWeapon(type) {
    const model = $("playerWeapon");

    model.classList.remove("grenade-mode", "heavy-mode");
    $("rifleSlot").className = "weapon";
    $("grenadeSlot").className = "weapon";
    $("heavySlot").className = "weapon";

    if (type === "grenade") {
        model.classList.add("grenade-mode");
        $("grenadeSlot").classList.add("grenade-active");
        $("weaponHint").textContent =
            "GRENADE 장착 · 연속 2정답 공격";
    } else if (type === "heavy") {
        model.classList.add("heavy-mode");
        $("heavySlot").classList.add("heavy-active");
        $("weaponHint").textContent =
            "HEAVY BOMB 발동 · 완벽 작전";
    } else {
        $("rifleSlot").classList.add("active");
        $("weaponHint").textContent = "PULSE RIFLE 장착 중";
    }
}

function renderBars() {
    $("enemyBars").innerHTML = "";

    for (let i = 0; i < 10; i++) {
        const cell = document.createElement("div");
        cell.className =
            "enemy-cell" + (i >= enemyHP ? " empty" : "");
        $("enemyBars").appendChild(cell);
    }

    $("enemyCount").textContent = `${enemyHP} / 10`;
    $("hpBars").innerHTML = "";

    for (let i = 0; i < 4; i++) {
        const cell = document.createElement("div");
        cell.className =
            "hp-unit" + (i >= playerHP ? " lost" : "");
        $("hpBars").appendChild(cell);
    }

    $("hpCount").textContent = `${playerHP} / 4`;
    $("comboCount").textContent = combo;
    $("energyFill").style.width = `${combo * 50}%`;
    $("accuracy").textContent =
        `CORRECT ${correctTotal} · WRONG ${wrongTotal}`;
}

function loadQuestion() {
    if (finished) return;

    locked = false;
    $("nextButton").disabled = true;

    const item = questions[questionIndex];

    $("questionNumber").textContent =
        `MISSION QUESTION ${String(questionIndex + 1).padStart(2, "0")}`;

    $("questionText").textContent = item.q;
    $("feedback").textContent = "정답을 선택하십시오.";
    $("answers").innerHTML = "";

    item.a.forEach((answer, index) => {
        const button = document.createElement("button");
        button.className = "answer";
        button.textContent =
            `${String.fromCharCode(65 + index)}. ${answer}`;

        button.addEventListener("click", () => submitAnswer(index));
        $("answers").appendChild(button);
    });
}

function animateShot(type, token) {
    if (finished || token !== actionToken) return;

    const projectile = $("projectile");
    const arena = $("arena");
    const player = $("player");
    const enemy = $("enemy");

    const startX = player.offsetLeft + player.offsetWidth * 0.8;
    const startY = arena.clientHeight - 105;
    const endX = enemy.offsetLeft + enemy.offsetWidth * 0.2;

    projectile.className = "projectile";

    if (type === "grenade") {
        projectile.classList.add("grenade");
    } else if (type === "heavy") {
        projectile.classList.add("heavy");
    }

    projectile.style.display = "block";
    projectile.style.left = `${startX}px`;
    projectile.style.top = `${startY}px`;

    player.classList.remove("attack");
    void player.offsetWidth;
    player.classList.add("attack");

    const duration = type === "heavy" ? 650 :
                     type === "grenade" ? 480 : 300;

    const start = performance.now();

    function step(now) {
        if (finished || token !== actionToken) {
            projectile.style.display = "none";
            return;
        }

        const progress = Math.min((now - start) / duration, 1);
        let curve = 0;

        if (type === "grenade") {
            curve = Math.sin(progress * Math.PI) * -65;
        } else if (type === "heavy") {
            curve = Math.sin(progress * Math.PI) * -25;
        }

        projectile.style.left =
            `${startX + (endX - startX) * progress}px`;
        projectile.style.top = `${startY + curve}px`;

        if (progress < 1) {
            requestAnimationFrame(step);
        } else {
            projectile.style.display = "none";

            if (type === "heavy" || type === "grenade") {
                showBlast(endX, startY, type, token);
            } else {
                hitEnemy(1);
                finishAnswerAction();
            }
        }
    }

    requestAnimationFrame(step);
}

function showBlast(x, y, type, token) {
    if (finished || token !== actionToken) return;

    const blast = $("blast");
    blast.style.left = `${x - 10}px`;
    blast.style.top = `${y - 10}px`;
    blast.style.display = "block";

    blast.animate(
        [
            { transform: "scale(.2)", opacity: 1 },
            { transform: "scale(3.8)", opacity: .95 },
            { transform: "scale(6)", opacity: 0 }
        ],
        {
            duration: type === "heavy" ? 900 : 650,
            easing: "ease-out"
        }
    );

    if (type === "heavy") {
        $("feedback").textContent =
            "HEAVY BOMB IMPACT! 완벽한 작전 수행.";
    }

    later(() => {
        if (finished || token !== actionToken) return;

        blast.style.display = "none";

        if (type === "heavy") {
            enemyHP = 0;
            renderBars();
            endGame(true);
        } else {
            hitEnemy(2);
            finishAnswerAction();
        }
    }, type === "heavy" ? 650 : 420);
}

function hitEnemy(damage) {
    if (finished) return;

    $("enemy").classList.add("hit");

    later(() => {
        $("enemy").classList.remove("hit");
    }, 220);

    enemyHP = Math.max(0, enemyHP - damage);
    renderBars();

    if (enemyHP <= 0) {
        endGame(true);
    }
}

function finishAnswerAction() {
    if (finished) return;

    // 공격이 끝나면 답변 처리를 해제하고 다음 질문 버튼을 활성화합니다.
    locked = false;
    $("nextButton").disabled = false;
}

function submitAnswer(selected) {
    if (locked || finished) return;

    locked = true;
    const token = ++actionToken;
    const item = questions[questionIndex];
    const buttons = [...$("answers").querySelectorAll("button")];

    buttons.forEach((button) => {
        button.disabled = true;
    });

    if (selected === item.correct) {
        correctTotal++;
        combo++;
        buttons[selected].classList.add("correct");

        // 첫 10문제를 모두 맞히면 대형 폭탄을 발동합니다.
        if (
            questionIndex === 9 &&
            correctTotal === 10 &&
            wrongTotal === 0 &&
            perfectRun
        ) {
            combo = 0;
            setWeapon("heavy");
            renderBars();

            $("feedback").textContent =
                `PERFECT CLEAR! 대형 폭탄을 발동합니다. ${item.explain}`;

            $("nextButton").disabled = true;

            later(() => {
                if (!finished && token === actionToken) {
                    animateShot("heavy", token);
                }
            }, 350);

            return;
        }

        if (combo >= 2) {
            combo = 0;
            setWeapon("grenade");
            renderBars();

            $("feedback").textContent =
                `연속 2정답! GRENADE 발사 · 적 체력 2칸 감소. ${item.explain}`;

            $("nextButton").disabled = true;
            animateShot("grenade", token);
        } else {
            setWeapon("rifle");
            renderBars();

            $("feedback").textContent =
                `정답입니다. PULSE RIFLE 발사 · 적 체력 1칸 감소. ${item.explain}`;

            $("nextButton").disabled = true;
            animateShot("rifle", token);
        }
    } else {
        wrongTotal++;
        combo = 0;
        perfectRun = false;
        playerHP = Math.max(0, playerHP - 1);

        buttons[selected].classList.add("wrong");
        buttons[item.correct].classList.add("correct");

        setWeapon("rifle");
        renderBars();

        $("player").classList.add("hit");

        later(() => {
            $("player").classList.remove("hit");
        }, 250);

        $("feedback").textContent =
            `오답입니다. 플레이어 HP -1, 콤보 초기화. ${item.explain}`;

        if (playerHP <= 0) {
            $("nextButton").disabled = true;
            later(() => endGame(false), 300);
            return;
        }

        // 오답이어도 체력이 남아 있으면 다음 질문으로 이동할 수 있습니다.
        $("nextButton").disabled = false;
    }
}

function endGame(victory) {
    if (finished) return;

    finished = true;
    locked = true;
    actionToken++;
    clearTimers();

    $("overlay").classList.add("show");

    $("resultTitle").textContent =
        victory ? "MISSION COMPLETE" : "MISSION FAILED";

    $("resultTitle").className =
        "result-title " + (victory ? "win" : "fail");

    $("resultDesc").innerHTML = victory
        ? `BLACK VEIL의 적을 제압했습니다.<br>
           정답: ${correctTotal} / 오답: ${wrongTotal}<br>
           임무를 성공적으로 완료했습니다.`
        : `플레이어의 체력이 모두 소진되었습니다.<br>
           정답: ${correctTotal} / 오답: ${wrongTotal}<br>
           재정비 후 다시 작전을 시작하십시오.`;

    $("nextButton").disabled = true;
    $("projectile").style.display = "none";
    $("blast").style.display = "none";

    [...$("answers").querySelectorAll("button")].forEach((button) => {
        button.disabled = true;
    });
}

function restartGame() {
    actionToken++;
    clearTimers();

    questionIndex = 0;
    playerHP = 4;
    enemyHP = 10;
    combo = 0;
    correctTotal = 0;
    wrongTotal = 0;
    locked = false;
    finished = false;
    perfectRun = true;

    questions = shuffle(questionBank);

    $("overlay").classList.remove("show");
    $("projectile").style.display = "none";
    $("blast").style.display = "none";

    $("player").classList.remove("hit", "attack");
    $("enemy").classList.remove("hit", "attack");

    setWeapon("rifle");
    renderBars();
    loadQuestion();
}

function returnToBase() {
    // 앱이 도메인 루트에 배포된 경우 본부 화면으로 돌아갑니다.
    window.parent.location.assign(window.parent.location.origin + "/");
}

$("nextButton").addEventListener("click", () => {
    // locked 값에 막혀 버튼이 작동하지 않던 문제를 수정했습니다.
    if (finished || $("nextButton").disabled) return;

    questionIndex++;

    if (questionIndex >= questions.length) {
        questions = questions.concat(shuffle(questionBank));
    }

    loadQuestion();
});

$("retryButton").addEventListener("click", restartGame);
$("baseButton").addEventListener("click", returnToBase);
$("exitButton").addEventListener("click", returnToBase);

restartGame();
</script>
</body>
</html>
"""

components.html(game_html, height=900, scrolling=True)
