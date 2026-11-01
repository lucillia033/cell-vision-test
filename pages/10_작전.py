
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
    <div style="
        color:#8ABCE8;
        font-size:12px;
        letter-spacing:3px;
        margin-bottom:4px;
    ">CELL VISION / BIOLOGICAL OPERATIONS UNIT</div>

    <div style="
        color:#F0F5FA;
        font-size:30px;
        font-weight:800;
        letter-spacing:2px;
    ">OPERATION CELL SHIELD</div>

    <div style="
        color:#8598AD;
        font-size:13px;
        margin-top:5px;
        margin-bottom:16px;
    ">BLACK VEIL INTERCEPTION PROTOCOL</div>
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
    background: #070c13;
    color: #edf4fc;
    font-family: Arial, "Malgun Gothic", sans-serif;
}

.game {
    position: relative;
    width: 100%;
    min-height: 710px;
    overflow: hidden;
    background:
        radial-gradient(ellipse at 50% 34%, #183653 0%, transparent 43%),
        linear-gradient(180deg, #111e2d 0%, #101927 52%, #070b11 100%);
    border: 1px solid #293d51;
    border-radius: 10px;
}

.grid {
    position: absolute;
    inset: 0;
    opacity: .18;
    background-image:
        linear-gradient(#5c8cb1 1px, transparent 1px),
        linear-gradient(90deg, #5c8cb1 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: linear-gradient(to bottom, black, transparent 90%);
    pointer-events: none;
}

.light {
    position: absolute;
    top: 0;
    left: 50%;
    width: 3px;
    height: 60%;
    background: #5aa7ed;
    box-shadow: 0 0 35px 10px #2374ba;
    opacity: .35;
}

.topbar {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    padding: 20px 24px 12px;
}

.kicker {
    color: #8dbce9;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 6px;
}

.heading {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.sub {
    color: #8194aa;
    font-size: 11px;
    margin-top: 5px;
    letter-spacing: 1px;
}

.enemy-hud {
    width: min(340px, 43%);
}

.hud-label {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    font-size: 11px;
    color: #d6e0eb;
    margin-bottom: 8px;
    letter-spacing: 1px;
}

.bar-track {
    height: 12px;
    padding: 2px;
    background: #281b24;
    border: 1px solid #85414b;
    display: flex;
    gap: 3px;
}

.enemy-cell {
    flex: 1;
    min-width: 0;
    background: #e24e5d;
    box-shadow: 0 0 7px #a72c3b66;
    transition: opacity .3s, background .3s, transform .3s;
}

.enemy-cell.empty {
    background: #241b25;
    box-shadow: none;
}

.arena {
    height: 310px;
    position: relative;
    overflow: hidden;
    border-top: 1px solid #233548;
    border-bottom: 1px solid #314358;
    background:
        radial-gradient(ellipse at 50% 100%, #27445c77, transparent 55%),
        linear-gradient(180deg, transparent 65%, #070c13 100%);
}

.machine {
    position: absolute;
    left: 50%;
    top: 16px;
    transform: translateX(-50%);
    width: 230px;
    height: 200px;
    border: 2px solid #32648c88;
    border-radius: 48% 48% 12% 12%;
    background: linear-gradient(180deg, #214b6c33, #07111d99);
    box-shadow: 0 0 50px #1678ba22, inset 0 0 35px #287db322;
}

.machine::before {
    content: "";
    position: absolute;
    left: 50%;
    top: 12px;
    transform: translateX(-50%);
    width: 100px;
    height: 165px;
    border: 3px solid #69baf2;
    border-radius: 50%;
    box-shadow: 0 0 20px #4ba9ff66, inset 0 0 20px #4ba9ff44;
}

.machine::after {
    content: "BIOLOGICAL CORE";
    position: absolute;
    left: 0;
    right: 0;
    bottom: 12px;
    text-align: center;
    color: #8bc8f2;
    font-size: 9px;
    letter-spacing: 2px;
}

.floor {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 50px;
    background: linear-gradient(180deg, #1c2b3b, #070b11);
    border-top: 2px solid #476580;
}

.floor::after {
    content: "";
    position: absolute;
    top: 12px;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #54a9ec, transparent);
    opacity: .6;
}

.fighter {
    position: absolute;
    bottom: 39px;
    width: 96px;
    height: 148px;
    transition: left .25s ease, right .25s ease, filter .15s;
    z-index: 3;
}

.player { left: 12%; }
.enemy { right: 12%; }

.body-shape {
    position: absolute;
    left: 24px;
    top: 47px;
    width: 49px;
    height: 67px;
    background: linear-gradient(110deg, #35475a, #101722 65%);
    border: 1px solid #63758a;
    clip-path: polygon(18% 0, 80% 0, 100% 35%, 83% 100%, 17% 100%, 0 35%);
}

.helmet {
    position: absolute;
    top: 9px;
    left: 25px;
    width: 48px;
    height: 49px;
    background: linear-gradient(135deg, #45576b, #0b1018 72%);
    border: 2px solid #7a8b9b;
    border-radius: 42% 42% 26% 26%;
    z-index: 2;
}

.helmet::before {
    content: "";
    position: absolute;
    left: 6px;
    right: 6px;
    top: 19px;
    height: 7px;
    background: #8bcfff;
    box-shadow: 0 0 12px #4bb6ff;
}

.enemy .helmet {
    background: linear-gradient(135deg, #382e35, #090b10 70%);
    border-color: #a34b56;
}

.enemy .helmet::before {
    background: #fa4856;
    box-shadow: 0 0 12px #fa3349;
}

.leg {
    position: absolute;
    top: 104px;
    width: 17px;
    height: 36px;
    background: #182330;
    border: 1px solid #4a5c70;
}

.leg.left { left: 31px; transform: rotate(5deg); }
.leg.right { left: 52px; transform: rotate(-5deg); }

.gun {
    position: absolute;
    top: 63px;
    width: 53px;
    height: 10px;
    background: #8796a5;
    border: 1px solid #d0d9e1;
    z-index: 4;
}

.player .gun { left: 52px; }
.enemy .gun { left: -9px; transform: scaleX(-1); background: #9b5a62; }

.player.hit, .enemy.hit {
    filter: brightness(2.8) drop-shadow(0 0 14px #ff5267);
    transform: translateX(-7px);
}

.enemy.hit { transform: translateX(7px); }

.projectile {
    position: absolute;
    width: 28px;
    height: 4px;
    background: #80d5ff;
    box-shadow: 0 0 13px 4px #318dff;
    border-radius: 4px;
    z-index: 5;
    display: none;
}

.projectile.grenade {
    width: 14px;
    height: 14px;
    background: #ff9b55;
    border-radius: 50%;
    box-shadow: 0 0 20px 8px #ff5c35;
}

.blast {
    position: absolute;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #ffd7a1;
    box-shadow: 0 0 25px 18px #ff603b, 0 0 65px 35px #ffb34d88;
    z-index: 6;
    display: none;
}

.enemy-name {
    position: absolute;
    bottom: 190px;
    right: 9%;
    color: #ee8790;
    font-size: 10px;
    letter-spacing: 2px;
}

.player-name {
    position: absolute;
    bottom: 190px;
    left: 10%;
    color: #8dcaff;
    font-size: 10px;
    letter-spacing: 2px;
}

.bottom {
    display: grid;
    grid-template-columns: 190px minmax(0, 1fr);
    gap: 14px;
    padding: 14px;
    position: relative;
    z-index: 4;
}

.player-panel {
    background: #101b28;
    border: 1px solid #2a4056;
    padding: 14px;
}

.panel-title {
    font-size: 11px;
    color: #9cc9ee;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.small-label {
    color: #91a4b8;
    font-size: 10px;
    margin: 12px 0 6px;
}

.hp-track, .energy-track {
    height: 9px;
    background: #253243;
    display: flex;
    gap: 4px;
    padding: 1px;
}

.hp-unit {
    flex: 1;
    background: #62baff;
    box-shadow: 0 0 5px #45a6ff77;
    transition: background .2s;
}

.hp-unit.lost { background: #3b2029; box-shadow: none; }

.energy-fill {
    height: 100%;
    background: #65d8db;
    width: 0%;
    transition: width .25s;
}

.weapon {
    border: 1px solid #344a60;
    padding: 8px;
    color: #c9d8e7;
    font-size: 11px;
    margin-top: 6px;
    background: #142131;
}

.weapon.active {
    border-color: #65baff;
    color: #ffffff;
    box-shadow: inset 3px 0 #65baff;
}

.question-panel {
    background: #0b121d;
    border: 1px solid #30475e;
    padding: 17px;
    min-width: 0;
}

.question-meta {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    color: #8ebce7;
    font-size: 10px;
    letter-spacing: 1.2px;
}

.question {
    margin: 13px 0 15px;
    font-size: 17px;
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
    text-align: left;
    padding: 10px 12px;
    color: #d4dfeb;
    background: #101b29;
    border: 1px solid #34475d;
    cursor: pointer;
    font-size: 13px;
    transition: .15s;
}

.answer:hover:not(:disabled) {
    border-color: #76bfff;
    background: #1b3044;
}

.answer:disabled { cursor: default; opacity: .7; }

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
    min-height: 25px;
    color: #b2c3d5;
    font-size: 12px;
    margin-top: 12px;
    line-height: 1.5;
}

.action-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 10px;
}

.action {
    background: #17293a;
    color: #e8f4ff;
    border: 1px solid #52728e;
    padding: 10px 13px;
    cursor: pointer;
    font-weight: 700;
    font-size: 11px;
    letter-spacing: .5px;
}

.action:hover:not(:disabled) { background: #244664; }
.action:disabled { opacity: .35; cursor: not-allowed; }

.status {
    color: #9eb3c9;
    font-size: 11px;
    margin-top: 10px;
}

.overlay {
    position: absolute;
    inset: 0;
    z-index: 20;
    background: #03070deF;
    display: none;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
}

.overlay.show { display: flex; }

.result-box {
    width: min(500px, 100%);
    padding: 30px 20px;
    background: #101a27;
    border: 1px solid #536c85;
    box-shadow: 0 0 60px #1a5b8a33;
}

.result-title {
    font-size: clamp(25px, 5vw, 39px);
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.fail { color: #ff6a79; }
.win { color: #7bc9ff; }

.result-desc {
    color: #c1cfde;
    font-size: 13px;
    line-height: 1.8;
    margin-bottom: 22px;
}

.retry {
    background: #193b57;
    border: 1px solid #6abaff;
    color: #f2f8ff;
    padding: 13px 22px;
    cursor: pointer;
    font-weight: 800;
    letter-spacing: 1px;
}

.retry:hover { background: #255a80; }

@media (max-width: 680px) {
    .game { min-height: 760px; }
    .topbar { padding: 15px; }
    .heading { font-size: 17px; }
    .arena { height: 270px; }
    .machine { width: 150px; height: 155px; }
    .machine::before { height: 120px; width: 70px; }
    .fighter { transform: scale(.8); transform-origin: bottom center; }
    .player { left: 4%; }
    .enemy { right: 4%; }
    .bottom { grid-template-columns: 1fr; padding: 9px; }
    .player-panel { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
    .panel-title { grid-column: 1 / -1; margin-bottom: 0; }
    .small-label { margin-top: 4px; }
    .question { font-size: 15px; }
    .answers { grid-template-columns: 1fr; }
    .enemy-hud { width: 45%; }
}
</style>
</head>
<body>
<div class="game" id="game">
    <div class="grid"></div>
    <div class="light"></div>

    <div class="topbar">
        <div>
            <div class="kicker">CELL VISION / OPERATION CELL SHIELD</div>
            <div class="heading">BLACK VEIL INTERCEPTION</div>
            <div class="sub">BIOLOGICAL THREAT ELIMINATION</div>
        </div>
        <div class="enemy-hud">
            <div class="hud-label">
                <span>ENEMY INTEGRITY</span>
                <span id="enemyCount">10 / 10</span>
            </div>
            <div class="bar-track" id="enemyBars"></div>
        </div>
    </div>

    <div class="arena" id="arena">
        <div class="machine"></div>
        <div class="player-name">PLAYER / OPERATIVE</div>
        <div class="enemy-name">BLACK VEIL / ELITE</div>

        <div class="fighter player" id="player">
            <div class="helmet"></div>
            <div class="body-shape"></div>
            <div class="leg left"></div>
            <div class="leg right"></div>
            <div class="gun"></div>
        </div>

        <div class="fighter enemy" id="enemy">
            <div class="helmet"></div>
            <div class="body-shape"></div>
            <div class="leg left"></div>
            <div class="leg right"></div>
            <div class="gun"></div>
        </div>

        <div class="projectile" id="projectile"></div>
        <div class="blast" id="blast"></div>
        <div class="floor"></div>
    </div>

    <div class="bottom">
        <div class="player-panel">
            <div class="panel-title">OPERATIVE STATUS</div>

            <div>
                <div class="small-label">PLAYER HP <span id="hpCount">4 / 4</span></div>
                <div class="hp-track" id="hpBars"></div>
            </div>

            <div>
                <div class="small-label">COMBO <span id="comboCount">0</span> / 2</div>
                <div class="energy-track">
                    <div class="energy-fill" id="energyFill"></div>
                </div>
            </div>

            <div style="grid-column:1 / -1;">
                <div class="small-label">EQUIPPED WEAPONS</div>
                <div class="weapon active">1 — PULSE RIFLE</div>
                <div class="weapon">2 — GRENADE / 2 COMBO</div>
                <div class="weapon">3 — HEAVY BOMB / ALL CORRECT</div>
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
                연속 2정답: 적 체력 2칸 감소 / 오답 4개: 임무 실패
            </div>
        </div>
    </div>

    <div class="overlay" id="overlay">
        <div class="result-box">
            <div class="result-title" id="resultTitle">MISSION FAILED</div>
            <div class="result-desc" id="resultDesc"></div>
            <button class="retry" onclick="restartGame()">RETRY MISSION</button>
        </div>
    </div>
</div>

<script>
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
        q: "세포질에서 물질이 이동하고 여러 반응이 일어나는 바탕이 되는 것은 무엇인가요?",
        a: ["세포질", "핵막", "세포벽", "염색체"],
        correct: 0,
        explain: "세포질은 세포막 안쪽에서 핵을 제외한 영역으로, 다양한 대사 반응이 일어납니다."
    },
    {
        q: "세포 안에서 물질의 이동과 세포 형태 유지에 관여하는 구조는 무엇인가요?",
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
        q: "거친면 소포체 표면에 리보솜이 붙어 있는 이유와 가장 관련이 깊은 것은 무엇인가요?",
        a: ["단백질 합성", "DNA 복제만", "ATP 직접 저장", "세포 분열 중단"],
        correct: 0,
        explain: "거친면 소포체의 리보솜은 주로 막 단백질이나 분비 단백질 합성에 관여합니다."
    },
    {
        q: "세포막을 통한 물질 이동 중 농도 기울기를 따라 에너지 투입 없이 이동하는 것은 무엇인가요?",
        a: ["능동 수송", "확산", "소낭 수송만", "DNA 복제"],
        correct: 1,
        explain: "확산은 입자가 농도가 높은 곳에서 낮은 곳으로 순이동하는 현상입니다."
    }
];

let questions = [];
let questionIndex = 0;
let playerHP = 4;
let enemyHP = 10;
let combo = 0;
let correctTotal = 0;
let wrongTotal = 0;
let locked = false;
let finished = false;
let grenadeReady = false;
let heavyBombReady = false;

const $ = id => document.getElementById(id);

function shuffle(array) {
    const result = [...array];
    for (let i = result.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
}

function renderBars() {
    $("enemyBars").innerHTML = "";
    for (let i = 0; i < 10; i++) {
        const cell = document.createElement("div");
        cell.className = "enemy-cell" + (i >= enemyHP ? " empty" : "");
        $("enemyBars").appendChild(cell);
    }

    $("enemyCount").textContent = `${enemyHP} / 10`;

    $("hpBars").innerHTML = "";
    for (let i = 0; i < 4; i++) {
        const cell = document.createElement("div");
        cell.className = "hp-unit" + (i >= playerHP ? " lost" : "");
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

    if (questionIndex >= questions.length) {
        questions = questions.concat(shuffle(questionBank));
    }

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
        button.textContent = `${String.fromCharCode(65 + index)}. ${answer}`;
        button.onclick = () => submitAnswer(index);
        $("answers").appendChild(button);
    });
}

function animateShot(isGrenade, heavy = false) {
    const projectile = $("projectile");
    const arena = $("arena");
    const player = $("player");
    const enemy = $("enemy");

    const startX = player.offsetLeft + player.offsetWidth * 0.8;
    const startY = arena.clientHeight - 105;
    const endX = enemy.offsetLeft + enemy.offsetWidth * 0.2;

    projectile.className = "projectile" + (isGrenade ? " grenade" : "");
    projectile.style.display = "block";
    projectile.style.left = `${startX}px`;
    projectile.style.top = `${startY}px`;

    const duration = heavy ? 520 : 340;
    const start = performance.now();

    function step(now) {
        const progress = Math.min((now - start) / duration, 1);
        const curve = isGrenade ? Math.sin(progress * Math.PI) * -45 : 0;

        projectile.style.left =
            `${startX + (endX - startX) * progress}px`;
        projectile.style.top =
            `${startY + curve * (isGrenade ? 1 : 0)}px`;

        if (progress < 1) {
            requestAnimationFrame(step);
        } else {
            projectile.style.display = "none";
            if (heavy) {
                showBlast(endX, startY);
            } else if (isGrenade) {
                showBlast(endX, startY);
            } else {
                hitEnemy();
            }
        }
    }

    requestAnimationFrame(step);
}

function showBlast(x, y) {
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
        { duration: 650, easing: "ease-out" }
    );

    setTimeout(() => {
        blast.style.display = "none";
        hitEnemy();
    }, 420);
}

function hitEnemy() {
    if (finished) return;
    $("enemy").classList.add("hit");
    setTimeout(() => $("enemy").classList.remove("hit"), 220);

    enemyHP = Math.max(0, enemyHP - 2);
    renderBars();

    if (enemyHP <= 0) {
        endGame(true);
    }
}

function submitAnswer(selected) {
    if (locked || finished) return;
    locked = true;

    const item = questions[questionIndex];
    const buttons = [...$("answers").querySelectorAll("button")];
    buttons.forEach(button => button.disabled = true);

    if (selected === item.correct) {
        correctTotal++;
        combo++;
        buttons[selected].classList.add("correct");

        if (combo >= 2) {
            combo = 0;
            grenadeReady = true;
            $("feedback").textContent =
                `연속 정답 성공! 수류탄 발사. ${item.explain}`;
            renderBars();
            animateShot(true);
        } else {
            $("feedback").textContent =
                `정답입니다. PULSE RIFLE 발사! ${item.explain}`;
            renderBars();
            animateShot(false);
        }

        // 대형 폭탄은 모든 문항을 한 번씩 풀고 모두 정답일 때 발동
        // 최초 10문제에 대해 한 번도 오답이 없으면 최종 폭탄 공격
        if (
            questionIndex === 9 &&
            wrongTotal === 0 &&
            correctTotal === 10
        ) {
            heavyBombReady = true;
            $("feedback").textContent =
                "PERFECT CLEAR! 대형 폭탄 발동!";
            setTimeout(() => {
                if (!finished) {
                    enemyHP = 0;
                    renderBars();
                    showBlast(
                        $("enemy").offsetLeft + 35,
                        $("arena").clientHeight - 105
                    );
                }
            }, 700);
        }
    } else {
        wrongTotal++;
        combo = 0;
        playerHP = Math.max(0, playerHP - 1);

        buttons[selected].classList.add("wrong");
        buttons[item.correct].classList.add("correct");

        $("player").classList.add("hit");
        setTimeout(() => $("player").classList.remove("hit"), 250);

        $("feedback").textContent =
            `오답입니다. 플레이어 HP -1. ${item.explain}`;
        renderBars();

        if (playerHP <= 0) {
            setTimeout(() => endGame(false), 450);
            return;
        }
    }

    $("nextButton").disabled = false;
}

function endGame(victory) {
    if (finished) return;
    finished = true;

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
    [...$("answers").querySelectorAll("button")].forEach(b => b.disabled = true);
}

function restartGame() {
    questionIndex = 0;
    playerHP = 4;
    enemyHP = 10;
    combo = 0;
    correctTotal = 0;
    wrongTotal = 0;
    locked = false;
    finished = false;
    grenadeReady = false;
    heavyBombReady = false;

    questions = shuffle(questionBank);
    $("overlay").classList.remove("show");
    $("projectile").style.display = "none";
    $("blast").style.display = "none";

    renderBars();
    loadQuestion();
}

$("nextButton").addEventListener("click", () => {
    if (finished) return;
    questionIndex++;
    loadQuestion();
});

restartGame();
</script>
</body>
</html>
"""

components.html(game_html, height=735, scrolling=False)
