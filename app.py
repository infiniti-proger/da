import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="Для Даши ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
html, body, #root, .stApp {
    margin: 0 !important; padding: 0 !important;
    width: 100% !important; height: 100% !important;
    overflow: hidden !important; background: #3b0717 !important;
}
header, [data-testid="stHeader"], #MainMenu, footer { display: none !important; }
iframe {
    display: block !important;
    width: 100vw !important; height: 100vh !important;
    border: 0 !important;
}
</style>
""", unsafe_allow_html=True)


def to_b64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


music_b64 = to_b64("romantic.mp3")

photos_b64 = {}
for i in range(1, 11):
    for ext in ("jpg", "JPG", "jpeg", "JPEG", "png", "PNG"):
        p = f"static/photo{i}.{ext}"
        if os.path.exists(p):
            photos_b64[i] = to_b64(p)
            break


def ph(n):
    if n in photos_b64:
        return "data:image/jpeg;base64," + photos_b64[n]
    return ""


html = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
html, body { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background: #3b0717; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
body { color: #fff; }
#app { position: fixed; inset: 0; width: 100%; height: 100%; overflow: hidden; background: radial-gradient(circle at 50% 45%, rgba(145,20,62,.22), transparent 48%), #3b0717; }
.scene { position: absolute; inset: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; padding: 30px; opacity: 0; visibility: hidden; transform: scale(1.035); transition: opacity .75s ease, transform .9s cubic-bezier(.22,.61,.36,1); z-index: 1; }
.scene.active { opacity: 1; visibility: visible; transform: scale(1); z-index: 5; }
.scene-inner { width: min(900px, 92vw); text-align: center; position: relative; z-index: 3; }
h1, h2, p { margin: 0; }
.title { font-family: Georgia, "Times New Roman", serif; font-size: clamp(34px, 6vw, 66px); font-weight: 400; letter-spacing: -1px; line-height: 1.05; }
.subtitle { margin-top: 20px; font-size: clamp(15px, 2vw, 19px); line-height: 1.75; color: rgba(255,255,255,.72); }
.date { font-family: Georgia, "Times New Roman", serif; font-size: clamp(34px, 7vw, 75px); letter-spacing: 4px; font-weight: 400; }
button { border: 0; outline: none; cursor: pointer; font-family: inherit; }
.main-button { margin-top: 35px; padding: 14px 28px; border-radius: 100px; color: #fff; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.18); font-size: 14px; letter-spacing: .5px; }
.main-button:hover { background: rgba(255,255,255,.14); border-color: rgba(255,255,255,.3); transform: translateY(-2px); }
.main-button:active { transform: scale(.97); }
.envelope-scene { background: radial-gradient(circle at 50% 48%, rgba(170,35,75,.14), transparent 43%); }
.envelope-wrap { position: relative; width: min(520px, 90vw); height: min(420px, 70vh); display: flex; align-items: center; justify-content: center; perspective: 1400px; }
.envelope { position: relative; width: min(430px, 82vw); aspect-ratio: 1.62 / 1; cursor: pointer; transform-style: preserve-3d; filter: drop-shadow(0 25px 45px rgba(0,0,0,.5)); transition: transform .3s ease; }
.envelope:hover { transform: translateY(-3px); }
.envelope:active { transform: scale(.985); }
.envelope-shadow { position: absolute; left: 50%; bottom: 22px; width: min(400px, 75vw); height: 25px; transform: translateX(-50%); background: rgba(0,0,0,.42); filter: blur(16px); border-radius: 50%; }
.envelope-back { position: absolute; inset: 0; border-radius: 7px; overflow: hidden; background: linear-gradient(145deg, #8f2742 0%, #741c35 50%, #5d152b 100%); }
.envelope-paper { position: absolute; left: 8%; right: 8%; bottom: 0; height: 76%; border-radius: 4px 4px 1px 1px; background: linear-gradient(145deg, #fffdf9 0%, #f7eee5 100%); z-index: 2; transform: translateY(0); transform-origin: bottom center; transition: transform .85s cubic-bezier(.22,.61,.36,1); }
.envelope-paper::before { content: "❤️"; position: absolute; left: 0; right: 0; top: 24%; text-align: center; font-size: clamp(20px, 4vw, 28px); }
.envelope-paper::after { content: "для тебя"; position: absolute; left: 0; right: 0; top: 40%; text-align: center; font-family: Georgia, serif; font-size: clamp(19px, 4vw, 29px); color: #711d34; }
.envelope-front { position: absolute; inset: 0; z-index: 5; border-radius: 7px; overflow: hidden; background: #741c35; clip-path: polygon(0 0, 50% 57%, 100% 0, 100% 100%, 0 100%); }
.envelope-left { position: absolute; inset: 0; z-index: 6; background: linear-gradient(145deg, #711a32, #64162d); clip-path: polygon(0 0, 50% 57%, 0 100%); }
.envelope-right { position: absolute; inset: 0; z-index: 6; background: linear-gradient(215deg, #68172e, #5e152b); clip-path: polygon(100% 0, 50% 57%, 100% 100%); }
.envelope-flap { position: absolute; left: 0; top: 0; width: 100%; height: 58%; z-index: 10; transform-origin: top center; background: linear-gradient(145deg, #9b2946 0%, #812039 50%, #6b182f 100%); clip-path: polygon(0 0, 100% 0, 50% 100%); transition: transform .9s cubic-bezier(.22,.61,.36,1); }
.envelope-seal { position: absolute; left: 50%; top: 47%; width: 58px; height: 58px; transform: translate(-50%,-50%); z-index: 15; display: flex; align-items: center; justify-content: center; border-radius: 50%; background: radial-gradient(circle, #c54b68 0%, #96263f 58%, #72192f 100%); border: 1px solid rgba(255,255,255,.12); font-size: 22px; transition: opacity .25s ease, transform .45s ease; }
.envelope-open .envelope-flap { transform: rotateX(180deg); }
.envelope-open .envelope-seal { opacity: 0; transform: translate(-50%,-50%) scale(.65); }
.envelope-open .envelope-paper { transform: translateY(-38%); }
.letter { max-width: 720px; margin: auto; }
.letter-title { font-family: Georgia, serif; font-size: clamp(34px, 6vw, 62px); font-weight: 400; }
.letter-text { margin-top: 28px; color: rgba(255,255,255,.72); font-size: clamp(15px, 2vw, 18px); line-height: 1.9; }
.photo-scene { padding: 0 !important; }
.photo-scene .scene-inner { position: absolute; inset: 0; width: 100%; height: 100%; max-width: none; display: block; }
.photo-wrapper { position: absolute; inset: 0; width: 100%; height: 100%; overflow: hidden; background: #080808; }
.photo-wrapper::after { content: ""; position: absolute; inset: 0; z-index: 2; pointer-events: none; background: linear-gradient(to top, rgba(0,0,0,.88) 0%, rgba(0,0,0,.62) 17%, rgba(0,0,0,.25) 38%, rgba(0,0,0,.05) 65%, rgba(0,0,0,.12) 100%); }
.photo { position: absolute; inset: 0; width: 100%; height: 100%; display: block; object-fit: cover; transform: translateZ(0) scale(1.02); transition: transform 8s cubic-bezier(.22,.61,.36,1); }
.scene.active .photo { transform: translateZ(0) scale(1.08); }
.photo-caption { position: absolute; left: 7vw; right: 7vw; bottom: 8vh; z-index: 5; text-align: left; pointer-events: none; }
.photo-number { font-size: 11px; letter-spacing: 5px; color: rgba(255,255,255,.65); margin-bottom: 12px; }
.photo-title { font-family: Georgia, serif; font-size: clamp(32px, 5vw, 64px); line-height: 1.05; font-weight: 400; color: #fff; text-shadow: 0 4px 25px rgba(0,0,0,.55); }
.photo-text { margin-top: 14px; max-width: 650px; font-size: clamp(13px, 1.5vw, 17px); line-height: 1.65; color: rgba(255,255,255,.72); text-shadow: 0 2px 12px rgba(0,0,0,.6); }
.big-heart { font-size: clamp(100px, 20vw, 190px); line-height: 1; animation: heartBeat 2s ease-in-out infinite; }
@keyframes heartBeat { 0%,100% { transform: scale(1); } 50% { transform: scale(1.08); } }
.gift { position: relative; width: 170px; height: 150px; margin: 0 auto; cursor: pointer; animation: giftFloat 3s ease-in-out infinite; }
@keyframes giftFloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-7px); } }
.gift-box { position: absolute; left: 15px; right: 15px; bottom: 0; height: 105px; border-radius: 5px; background: linear-gradient(135deg, #8d243e, #63172d); }
.gift-lid { position: absolute; left: 5px; right: 5px; top: 25px; height: 32px; border-radius: 5px; background: linear-gradient(135deg, #a82c4b, #751b34); z-index: 3; }
.gift-ribbon-v { position: absolute; top: 25px; bottom: 0; left: 50%; width: 27px; transform: translateX(-50%); background: rgba(240,184,195,.75); z-index: 4; }
.gift-ribbon-h { position: absolute; left: 5px; right: 5px; top: 37px; height: 20px; background: rgba(240,184,195,.75); z-index: 4; }
.gift-bow { position: absolute; left: 50%; top: 2px; width: 65px; height: 40px; transform: translateX(-50%); z-index: 8; }
.bow-left, .bow-right { position: absolute; width: 34px; height: 25px; border-radius: 50%; background: #d68a9d; }
.bow-left { left: 0; transform: rotate(-25deg); }
.bow-right { right: 0; transform: rotate(25deg); }
.music { position: fixed; right: 22px; top: 20px; width: 42px; height: 42px; border-radius: 50%; background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.12); color: rgba(255,255,255,.7); z-index: 100; font-size: 19px; }
.hearts { position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 0; }
.bg-heart { position: absolute; bottom: -50px; color: rgba(230,65,105,.28); animation: floatHeart linear infinite; }
@keyframes floatHeart { from { transform: translateY(0) rotate(0deg); } to { transform: translateY(-115vh) rotate(35deg); } }
.quest-scene { padding: 25px; }
.quest-box { width: min(700px, 92vw); margin: auto; }
.quest-number { font-size: 12px; text-transform: uppercase; letter-spacing: 3px; color: rgba(255,255,255,.38); margin-bottom: 20px; }
.quest-title { font-family: Georgia, serif; font-size: clamp(30px, 5vw, 52px); font-weight: 400; margin-bottom: 22px; }
.quest-text { color: rgba(255,255,255,.72); font-size: clamp(15px, 2vw, 18px); line-height: 1.75; min-height: 60px; white-space: pre-line; }
.answer-box { display: flex; justify-content: center; gap: 10px; margin-top: 30px; }
.answer-input { width: min(350px, 65vw); padding: 14px 18px; border-radius: 100px; border: 1px solid rgba(255,255,255,.16); outline: none; background: rgba(255,255,255,.06); color: white; font-size: 15px; text-align: center; }
.answer-button { padding: 14px 22px; border-radius: 100px; color: white; background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.16); }
.answer-message { min-height: 25px; margin-top: 16px; font-size: 13px; color: rgba(255,255,255,.55); }
.finish { position: fixed; inset: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% 45%, rgba(150,25,65,.18), transparent 45%), #3b0717; display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; z-index: 20; transition: opacity .8s ease; }
.finish.show { opacity: 1; visibility: visible; }
.finish-title { font-family: Georgia, serif; font-size: clamp(40px, 7vw, 78px); font-weight: 400; }
.finish-text { margin-top: 20px; color: rgba(255,255,255,.7); font-size: clamp(15px, 2vw, 18px); }
.explosion-heart { position: fixed; pointer-events: none; z-index: 200; font-size: 22px; animation: explodeHeart 1.2s ease-out forwards; }
@keyframes explodeHeart { 0% { opacity: 1; transform: translate(-50%,-50%) scale(.5) rotate(0deg); } 100% { opacity: 0; transform: translate(calc(-50% + var(--x)), calc(-50% + var(--y))) scale(1.4) rotate(var(--r)); } }
@media (max-width: 700px) { .scene { padding: 20px; } .photo-caption { left: 25px; right: 25px; bottom: 55px; } .photo-title { font-size: 34px; } }
</style>
</head>
<body>
<div id="app">

<div class="hearts">
    <span class="bg-heart" style="left:8%;font-size:20px;animation-duration:17s;">♥</span>
    <span class="bg-heart" style="left:43%;font-size:24px;animation-duration:19s;">♥</span>
    <span class="bg-heart" style="left:84%;font-size:27px;animation-duration:20s;">♥</span>
</div>

<section class="scene active envelope-scene" id="scene0">
    <div class="envelope-wrap">
        <div class="envelope-shadow"></div>
        <div class="envelope" id="envelope" onclick="openEnvelope()">
            <div class="envelope-back"></div>
            <div class="envelope-paper"></div>
            <div class="envelope-left"></div>
            <div class="envelope-right"></div>
            <div class="envelope-front"></div>
            <div class="envelope-flap"></div>
            <div class="envelope-seal">❤️</div>
        </div>
    </div>
</section>

<section class="scene" id="scene1">
    <div class="scene-inner letter">
        <h1 class="letter-title">Моя любимая Даша</h1>
        <p class="letter-text">Спасибо тебе за каждый день, который мы прожили вместе. За смех, за объятия, за маленькие моменты, которые со временем становятся самыми дорогими воспоминаниями. Я очень тебя люблю.</p>
        <button class="main-button" onclick="nextScene(event)">дальше →</button>
    </div>
</section>

<section class="scene photo-scene" id="scene2"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_1__" alt="">
    <div class="photo-caption"><div class="photo-number">01 / 10</div><div class="photo-title">Всё началось с нас</div><div class="photo-text">И я даже представить не мог, сколько всего прекрасного ещё будет впереди.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene3"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_2__" alt="">
    <div class="photo-caption"><div class="photo-number">02 / 10</div><div class="photo-title">Наши моменты</div><div class="photo-text">Именно из таких маленьких моментов и складывается что-то настоящее.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene4"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_3__" alt="">
    <div class="photo-caption"><div class="photo-number">03 / 10</div><div class="photo-title">Ты и я</div><div class="photo-text">Два человека. Одна история. И столько всего, что ещё предстоит прожить.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene5"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_4__" alt="">
    <div class="photo-caption"><div class="photo-number">04 / 10</div><div class="photo-title">Моё самое дорогое</div><div class="photo-text">Когда рядом есть человек, с которым хочется делить не только праздники, но и обычные дни.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene6"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_5__" alt="">
    <div class="photo-caption"><div class="photo-number">05 / 10</div><div class="photo-title">С тобой всё по-другому</div><div class="photo-text">Даже самые обычные дни становятся особенными.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene7"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_6__" alt="">
    <div class="photo-caption"><div class="photo-number">06 / 10</div><div class="photo-title">Ещё один момент</div><div class="photo-text">Ещё одна фотография, которую хочется сохранить не только в телефоне, но и в памяти.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene8"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_7__" alt="">
    <div class="photo-caption"><div class="photo-number">07 / 10</div><div class="photo-title">Счастье в мелочах</div><div class="photo-text">Иногда для счастья нужно совсем немного. Просто быть рядом.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene9"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_8__" alt="">
    <div class="photo-caption"><div class="photo-number">08 / 10</div><div class="photo-title">Вот за что я люблю нас</div><div class="photo-text">За смех, за тепло и за те моменты, которые хочется проживать снова и снова.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene10"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_9__" alt="">
    <div class="photo-caption"><div class="photo-number">09 / 10</div><div class="photo-title">Просто мы</div><div class="photo-text">Без лишних слов и всего остального. Только ты, я и наше маленькое счастье.</div></div>
</div></div></section>

<section class="scene photo-scene" id="scene11"><div class="scene-inner"><div class="photo-wrapper">
    <img class="photo" src="__PHOTO_10__" alt="">
    <div class="photo-caption"><div class="photo-number">10 / 10</div><div class="photo-title">И это только начало</div><div class="photo-text">Десять фотографий — и впереди ещё целая жизнь, которую я хочу прожить с тобой.</div></div>
</div></div></section>

<section class="scene" id="scene12">
    <div class="scene-inner">
        <div class="date">21.09.2024</div>
        <h1 class="title" style="margin-top:28px;">Наша дата</h1>
        <p class="subtitle">День, когда мы стали семьёй.</p>
        <button class="main-button" onclick="nextScene(event)">дальше →</button>
    </div>
</section>

<section class="scene" id="scene13">
    <div class="scene-inner">
        <div class="big-heart">❤️</div>
        <p class="subtitle">Я не знаю, каким будет наше будущее через 10, 20 или 50 лет.<br>Но я хочу встретить его рядом с тобой.</p>
        <button class="main-button" onclick="nextScene(event)">дальше →</button>
    </div>
</section>

<section class="scene" id="scene14">
    <div class="scene-inner">
        <h1 class="title" style="margin-bottom: 30px;">Для тебя подарочек</h1>
        <div class="gift" onclick="openGift(event)">
            <div class="gift-bow"><div class="bow-left"></div><div class="bow-right"></div></div>
            <div class="gift-lid"></div>
            <div class="gift-box"></div>
            <div class="gift-ribbon-v"></div>
            <div class="gift-ribbon-h"></div>
        </div>
    </div>
</section>

<section class="scene quest-scene" id="scene15">
    <div class="scene-inner quest-box">
        <div class="quest-number" id="questNumber">Пасхалка №1</div>
        <h1 class="quest-title" id="questTitle">Вспомни...</h1>
        <p class="quest-text" id="questText">...</p>
        <div class="answer-box">
            <input id="answerInput" class="answer-input" type="text" autocomplete="off" placeholder="твой ответ">
            <button class="answer-button" onclick="checkAnswer(event)">ответить</button>
        </div>
        <div class="answer-message" id="answerMessage"></div>
    </div>
</section>

<div class="finish" id="finish">
    <div class="finish-content">
        <h1 class="finish-title">Ты справилась ❤️</h1>
        <p class="finish-text">А теперь загляни в свою тумбочку.</p>
    </div>
</div>

<audio id="music" loop preload="auto"><source src="__MUSIC__" type="audio/mpeg"></audio>
<button class="music" id="musicButton" onclick="toggleMusic(event)">♪</button>

</div>

<script>
let currentScene = 0;
let musicStarted = false;
let envelopeOpened = false;
const music = document.getElementById("music");
const musicButton = document.getElementById("musicButton");

const quests = [
    { title: "", text: "Ищи там, где вещи иногда находят свой временный дом.\nТы точно знаешь это место.\nВозможно, сегодня среди них спряталось кое-что ещё… ❤️", answer: "твой" },
    { title: "", text: "Теперь отправляйся туда,\nгде живут маленькие флакончики,\nспособные оставить после тебя\nслед даже тогда, когда тебя уже нет рядом.\nТуда, где начинается твой любимый аромат. 🌸", answer: "подарок" },
    { title: "", text: "Следующая подсказка находится\nв самом холодном мире нашей квартиры.\nТам всегда что-нибудь ждёт своего часа,\nа за дверцей никогда не бывает слишком тепло. ❄️", answer: "уже" },
    { title: "", text: "Ты ведь так сильно любишь читать,\nчто среди всех этих историй\nвполне могла потеряться ещё одна.\nПерелистай взглядом свои любимые книги —\nкажется, одна из них знает продолжение этой игры. 📖❤️", answer: "совсем" },
    { title: "", text: "Вспомни место, которое обычно вспоминают\nтолько тогда, когда в квартире становится\nслишком много пыли.", answer: "рядом" }
];

let questIndex = 0;

function playMusic() {
    if (musicStarted) return;
    musicStarted = true;
    music.volume = 0.45;
    const p = music.play();
    if (p) p.catch(function() { musicStarted = false; });
    musicButton.innerHTML = "♫";
}

function toggleMusic(e) {
    if (e) e.stopPropagation();
    if (music.paused) {
        music.play().then(function() { musicButton.innerHTML = "♫"; });
    } else {
        music.pause();
        musicButton.innerHTML = "♪";
    }
}

function openEnvelope() {
    if (envelopeOpened) return;
    envelopeOpened = true;
    playMusic();
    document.getElementById("envelope").classList.add("envelope-open");
    setTimeout(function() { setScene(1); }, 1350);
}

function setScene(n) {
    document.querySelectorAll(".scene").forEach(function(s) { s.classList.remove("active"); });
    const t = document.getElementById("scene" + n);
    if (t) t.classList.add("active");
    currentScene = n;
    if (n === 15) startQuest();
}

function nextScene(e) {
    if (e) e.stopPropagation();
    if (currentScene >= 1 && currentScene < 14) setScene(currentScene + 1);
}

function openGift(e) {
    if (e) e.stopPropagation();
    createHeartExplosion();
    setTimeout(function() { setScene(15); }, 650);
}

function startQuest() {
    questIndex = 0;
    showQuest();
    setTimeout(function() {
        const i = document.getElementById("answerInput");
        if (i) i.focus();
    }, 300);
}

function showQuest() {
    const q = quests[questIndex];
    document.getElementById("questNumber").innerText = "Пасхалка №" + (questIndex + 1);
    document.getElementById("questTitle").innerText = q.title;
    document.getElementById("questText").innerText = q.text;
    document.getElementById("answerMessage").innerText = "";
    document.getElementById("answerInput").value = "";
}

function normalizeAnswer(v) {
    return v.toLowerCase().trim().replace(/ё/g, "е");
}

function checkAnswer(e) {
    if (e) e.stopPropagation();
    const inp = document.getElementById("answerInput");
    const msg = document.getElementById("answerMessage");
    const a = normalizeAnswer(inp.value);
    const c = normalizeAnswer(quests[questIndex].answer);
    if (!a) { msg.innerText = "Напиши ответ ❤️"; return; }
    if (a === c) {
        createHeartExplosion();
        questIndex++;
        if (questIndex >= quests.length) {
            setTimeout(function() {
                document.getElementById("finish").classList.add("show");
                setTimeout(function() { window.close(); }, 5000);
            }, 500);
            return;
        }
        msg.innerText = "Правильно ❤️";
        setTimeout(function() {
            showQuest();
            document.getElementById("answerInput").focus();
        }, 500);
    } else {
        msg.innerText = "Не совсем... попробуй ещё ❤️";
        inp.value = "";
        inp.focus();
    }
}

function createHeartExplosion() {
    const s = ["❤️", "♥", "♡"];
    for (let i = 0; i < 18; i++) {
        const h = document.createElement("div");
        h.className = "explosion-heart";
        h.innerText = s[Math.floor(Math.random() * s.length)];
        const x = (Math.random() - .5) * 500;
        const y = (Math.random() - .5) * 400;
        const r = (Math.random() - .5) * 160;
        h.style.left = "50%";
        h.style.top = "50%";
        h.style.setProperty("--x", x + "px");
        h.style.setProperty("--y", y + "px");
        h.style.setProperty("--r", r + "deg");
        h.style.animationDelay = (Math.random() * .15) + "s";
        document.body.appendChild(h);
        setTimeout(function() { h.remove(); }, 1500);
    }
}

document.addEventListener("keydown", function(e) {
    if (e.code === "Space") {
        if (document.activeElement && document.activeElement.tagName === "INPUT") return;
        e.preventDefault();
        toggleMusic();
        return;
    }
    if (e.key === "Enter" && currentScene === 15) checkAnswer(e);
    if (currentScene === 12 || currentScene === 13) return;
    if (e.key === "ArrowRight" || e.key === "ArrowDown") {
        if (currentScene >= 1 && currentScene < 14) nextScene(e);
    }
    if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
        if (currentScene > 1 && currentScene <= 14) setScene(currentScene - 1);
    }
});

let touchStartX = 0, touchStartY = 0;
document.addEventListener("touchstart", function(e) {
    if (!e.touches || !e.touches.length) return;
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
}, { passive: true });

document.addEventListener("touchend", function(e) {
    if (!e.changedTouches || !e.changedTouches.length) return;
    if (currentScene === 12 || currentScene === 13) return;
    const touch = e.changedTouches[0];
    const dx = touch.clientX - touchStartX;
    const dy = touch.clientY - touchStartY;
    if (Math.abs(dx) < 60) return;
    if (Math.abs(dx) < Math.abs(dy)) return;
    if (currentScene >= 1 && currentScene < 14) {
        if (dx < 0) setScene(currentScene + 1);
        else setScene(currentScene - 1);
    }
}, { passive: true });

document.addEventListener("click", function(e) {
    if (currentScene < 1 || currentScene >= 14) return;
    if (currentScene === 12 || currentScene === 13) return;
    if (e.target.closest("button") || e.target.closest("input") ||
        e.target.closest(".music") || e.target.closest(".gift") ||
        e.target.closest(".answer-box")) return;
    nextScene(e);
});
</script>

</body>
</html>
"""

# Подставляем фото 1..10
html = html.replace("__PHOTO_1__",  ph(1))
html = html.replace("__PHOTO_2__",  ph(2))
html = html.replace("__PHOTO_3__",  ph(3))
html = html.replace("__PHOTO_4__",  ph(4))
html = html.replace("__PHOTO_5__",  ph(5))
html = html.replace("__PHOTO_6__",  ph(6))
html = html.replace("__PHOTO_7__",  ph(7))
html = html.replace("__PHOTO_8__",  ph(8))
html = html.replace("__PHOTO_9__",  ph(9))
html = html.replace("__PHOTO_10__", ph(10))

# Подставляем музыку
if music_b64:
    html = html.replace("__MUSIC__", "data:audio/mpeg;base64," + music_b64)
else:
    html = html.replace("__MUSIC__", "")

import streamlit as st

if hasattr(st, "iframe"):
    st.iframe(html, height=900)
else:
    components.html(html, height=900, scrolling=False)
