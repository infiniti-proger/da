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

# Скрываем интерфейс Streamlit
st.markdown("""
<style>
html, body, #root, .stApp {
    margin: 0 !important; padding: 0 !important;
    width: 100% !important; height: 100% !important;
    min-height: 100% !important;
    overflow: hidden !important; background: #3b0717 !important;
}
header, [data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stDeployButton"],
#MainMenu, footer {
    display: none !important; visibility: hidden !important; height: 0 !important;
}
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stAppViewContainer"] > .main,
section.main, .main, .block-container {
    margin: 0 !important; padding: 0 !important;
    width: 100% !important; max-width: none !important;
    height: 100% !important; min-height: 100% !important;
    overflow: hidden !important;
}
[data-testid="stVerticalBlock"],
[data-testid="stElementContainer"] {
    gap: 0 !important; margin: 0 !important;
    padding: 0 !important; width: 100% !important;
    max-width: none !important; overflow: hidden !important;
}
iframe {
    display: block !important;
    width: 100vw !important; height: 100vh !important;
    min-height: 100vh !important; max-height: 100vh !important;
    margin: 0 !important; padding: 0 !important;
    border: 0 !important; overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================
# ЧТЕНИЕ ФАЙЛОВ -> BASE64
# =========================================

def file_to_base64(filename):
    if not os.path.exists(filename):
        return ""
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


# Музыка
music = file_to_base64("romantic.mp3")

# Фото 1..10 — ищем в static/ с любым расширением
photos = {}
for i in range(1, 11):
    for ext in ("jpg", "JPG", "jpeg", "JPEG", "png", "PNG"):
        p = f"static/photo{i}.{ext}"
        if os.path.exists(p):
            photos[i] = file_to_base64(p)
            break


# =========================================
# HTML
# =========================================

html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
* {{ box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
html, body {{
    margin: 0; padding: 0; width: 100%; height: 100%;
    overflow: hidden; background: #3b0717;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}
body {{ color: #fff; }}
#app {{
    position: fixed; inset: 0; width: 100%; height: 100%; overflow: hidden;
    background:
        radial-gradient(circle at 50% 45%, rgba(145,20,62,0.22), transparent 48%),
        #3b0717;
}}

.scene {{
    position: absolute; inset: 0; width: 100%; height: 100%;
    display: flex; align-items: center; justify-content: center;
    padding: 30px;
    opacity: 0; visibility: hidden; transform: scale(1.035);
    transition: opacity 0.75s ease, transform 0.9s cubic-bezier(.22,.61,.36,1);
    z-index: 1; will-change: opacity, transform; backface-visibility: hidden;
}}
.scene.active {{ opacity: 1; visibility: visible; transform: scale(1); z-index: 5; }}
.scene-inner {{ width: min(900px, 92vw); text-align: center; position: relative; z-index: 3; }}

h1, h2, p {{ margin: 0; }}

.title {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(34px, 6vw, 66px); font-weight: 400;
    letter-spacing: -1px; line-height: 1.05;
}}
.subtitle {{
    margin-top: 20px; font-size: clamp(15px, 2vw, 19px);
    line-height: 1.75; color: rgba(255,255,255,.72);
}}
.date {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(34px, 7vw, 75px); letter-spacing: 4px; font-weight: 400;
}}
button {{ border: 0; outline: none; cursor: pointer; font-family: inherit; }}
.main-button {{
    margin-top: 35px; padding: 14px 28px; border-radius: 100px;
    color: #fff; background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.18);
    font-size: 14px; letter-spacing: .5px;
    transition: background .25s ease, transform .25s ease, border-color .25s ease;
}}
.main-button:hover {{
    background: rgba(255,255,255,.14);
    border-color: rgba(255,255,255,.3);
    transform: translateY(-2px);
}}
.main-button:active {{ transform: scale(.97); }}

/* КОНВЕРТ */
.envelope-scene {{
    background: radial-gradient(circle at 50% 48%, rgba(170,35,75,.14), transparent 43%);
}}
.envelope-wrap {{
    position: relative; width: min(520px, 90vw); height: min(420px, 70vh);
    display: flex; align-items: center; justify-content: center;
    perspective: 1400px;
}}
.envelope {{
    position: relative; width: min(430px, 82vw);
    aspect-ratio: 1.62 / 1; cursor: pointer;
    transform-style: preserve-3d;
    filter: drop-shadow(0 25px 45px rgba(0,0,0,.5));
    transition: transform .3s ease;
}}
.envelope:hover {{ transform: translateY(-3px); }}
.envelope:active {{ transform: scale(.985); }}
.envelope-shadow {{
    position: absolute; left: 50%; bottom: 22px;
    width: min(400px, 75vw); height: 25px;
    transform: translateX(-50%); background: rgba(0,0,0,.42);
    filter: blur(16px); border-radius: 50%;
}}
.envelope-back {{
    position: absolute; inset: 0; border-radius: 7px; overflow: hidden;
    background: linear-gradient(145deg, #8f2742 0%, #741c35 50%, #5d152b 100%);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.1), inset 0 -2px 5px rgba(0,0,0,.12);
}}
.envelope-paper {{
    position: absolute; left: 8%; right: 8%; bottom: 0; height: 76%;
    border-radius: 4px 4px 1px 1px;
    background: linear-gradient(145deg, #fffdf9 0%, #f7eee5 100%);
    z-index: 2; transform: translateY(0); transform-origin: bottom center;
    transition: transform .85s cubic-bezier(.22,.61,.36,1), box-shadow .5s ease;
    box-shadow: 0 -3px 12px rgba(0,0,0,.12);
}}
.envelope-paper::before {{
    content: "❤️"; position: absolute; left: 0; right: 0; top: 24%;
    text-align: center; font-size: clamp(20px, 4vw, 28px);
}}
.envelope-paper::after {{
    content: "для тебя"; position: absolute; left: 0; right: 0; top: 40%;
    text-align: center; font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(19px, 4vw, 29px); color: #711d34;
}}
.envelope-front {{
    position: absolute; inset: 0; z-index: 5; border-radius: 7px; overflow: hidden;
    background: #741c35;
    clip-path: polygon(0 0, 50% 57%, 100% 0, 100% 100%, 0 100%);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.07);
}}
.envelope-left {{
    position: absolute; inset: 0; z-index: 6;
    background: linear-gradient(145deg, #711a32, #64162d);
    clip-path: polygon(0 0, 50% 57%, 0 100%);
}}
.envelope-right {{
    position: absolute; inset: 0; z-index: 6;
    background: linear-gradient(215deg, #68172e, #5e152b);
    clip-path: polygon(100% 0, 50% 57%, 100% 100%);
}}
.envelope-flap {{
    position: absolute; left: 0; top: 0; width: 100%; height: 58%;
    z-index: 10; transform-origin: top center; transform-style: preserve-3d;
    background: linear-gradient(145deg, #9b2946 0%, #812039 50%, #6b182f 100%);
    clip-path: polygon(0 0, 100% 0, 50% 100%);
    transition: transform .9s cubic-bezier(.22,.61,.36,1);
    box-shadow: 0 4px 9px rgba(0,0,0,.15);
}}
.envelope-seal {{
    position: absolute; left: 50%; top: 47%; width: 58px; height: 58px;
    transform: translate(-50%, -50%); z-index: 15;
    display: flex; align-items: center; justify-content: center;
    border-radius: 50%;
    background: radial-gradient(circle, #c54b68 0%, #96263f 58%, #72192f 100%);
    border: 1px solid rgba(255,255,255,.12);
    box-shadow: 0 5px 18px rgba(0,0,0,.35), inset 0 1px 2px rgba(255,255,255,.22);
    font-size: 22px;
    transition: opacity .25s ease, transform .45s ease;
}}
.envelope-open .envelope-flap {{ transform: rotateX(180deg); }}
.envelope-open .envelope-seal {{ opacity: 0; transform: translate(-50%,-50%) scale(.65); }}
.envelope-open .envelope-paper {{
    transform: translateY(-38%);
    box-shadow: 0 -8px 25px rgba(0,0,0,.16);
}}

/* ПИСЬМО */
.letter {{ max-width: 720px; margin: auto; }}
.letter-title {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(34px, 6vw, 62px); font-weight: 400;
}}
.letter-text {{
    margin-top: 28px; color: rgba(255,255,255,.72);
    font-size: clamp(15px, 2vw, 18px); line-height: 1.9;
}}

/* ФОТО */
.photo-scene {{ padding: 0 !important; width: 100%; height: 100%; }}
.photo-scene .scene-inner {{
    position: absolute; inset: 0; width: 100%; height: 100%;
    max-width: none; display: block;
}}
.photo-wrapper {{
    position: absolute; inset: 0; width: 100%; height: 100%;
    max-width: none; max-height: none; margin: 0;
    overflow: hidden; border-radius: 0; background: #080808;
}}
.photo-wrapper::after {{
    content: ""; position: absolute; inset: 0; z-index: 2;
    pointer-events: none;
    background: linear-gradient(to top,
        rgba(0,0,0,.88) 0%, rgba(0,0,0,.62) 17%,
        rgba(0,0,0,.25) 38%, rgba(0,0,0,.05) 65%, rgba(0,0,0,.12) 100%);
}}
.photo {{
    position: absolute; inset: 0; width: 100%; height: 100%;
    max-width: none; max-height: none; display: block;
    object-fit: cover; image-rendering: auto;
    transform: translateZ(0) scale(1.02);
    transform-origin: center center;
    transition: transform 8s cubic-bezier(.22,.61,.36,1);
    will-change: transform; backface-visibility: hidden;
}}
.scene.active .photo {{ transform: translateZ(0) scale(1.08); }}
.photo-caption {{
    position: absolute; left: 7vw; right: 7vw; bottom: 8vh;
    z-index: 5; text-align: left; pointer-events: none;
}}
.photo-number {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 11px; letter-spacing: 5px;
    color: rgba(255,255,255,.65); margin-bottom: 12px;
}}
.photo-title {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(32px, 5vw, 64px); line-height: 1.05;
    font-weight: 400; color: #fff;
    text-shadow: 0 4px 25px rgba(0,0,0,.55);
}}
.photo-text {{
    margin-top: 14px; max-width: 650px;
    font-size: clamp(13px, 1.5vw, 17px); line-height: 1.65;
    color: rgba(255,255,255,.72); text-shadow: 0 2px 12px rgba(0,0,0,.6);
}}

/* СЕРДЦЕ */
.big-heart {{
    font-size: clamp(100px, 20vw, 190px); line-height: 1;
    animation: heartBeat 2s ease-in-out infinite;
    filter: drop-shadow(0 15px 35px rgba(150,20,60,.35));
}}
@keyframes heartBeat {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.08); }}
}}

/* ПОДАРОК */
.gift {{
    position: relative; width: 170px; height: 150px;
    margin: 0 auto; cursor: pointer;
    animation: giftFloat 3s ease-in-out infinite;
}}
@keyframes giftFloat {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-7px); }}
}}
.gift-box {{
    position: absolute; left: 15px; right: 15px; bottom: 0; height: 105px;
    border-radius: 5px;
    background: linear-gradient(135deg, #8d243e, #63172d);
    box-shadow: 0 20px 35px rgba(0,0,0,.35);
}}
.gift-lid {{
    position: absolute; left: 5px; right: 5px; top: 25px; height: 32px;
    border-radius: 5px;
    background: linear-gradient(135deg, #a82c4b, #751b34);
    z-index: 3;
}}
.gift-ribbon-v {{
    position: absolute; top: 25px; bottom: 0; left: 50%; width: 27px;
    transform: translateX(-50%);
    background: rgba(240,184,195,.75); z-index: 4;
}}
.gift-ribbon-h {{
    position: absolute; left: 5px; right: 5px; top: 37px; height: 20px;
    background: rgba(240,184,195,.75); z-index: 4;
}}
.gift-bow {{
    position: absolute; left: 50%; top: 2px; width: 65px; height: 40px;
    transform: translateX(-50%); z-index: 8;
}}
.bow-left, .bow-right {{
    position: absolute; width: 34px; height: 25px;
    border-radius: 50%; background: #d68a9d;
}}
.bow-left {{ left: 0; transform: rotate(-25deg); }}
.bow-right {{ right: 0; transform: rotate(25deg); }}

/* МУЗЫКА */
.music {{
    position: fixed; right: 22px; top: 20px; width: 42px; height: 42px;
    border-radius: 50%;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.12);
    color: rgba(255,255,255,.7);
    z-index: 100; font-size: 19px; transition: .25s ease;
}}
.music:hover {{ background: rgba(255,255,255,.14); }}

/* ФОНОВЫЕ СЕРДЦА */
.hearts {{
    position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 0;
}}
.bg-heart {{
    position: absolute; bottom: -50px;
    color: rgba(230,65,105,.28);
    text-shadow: 0 0 22px rgba(230,65,105,.18);
    animation: floatHeart linear infinite; will-change: transform;
}}
@keyframes floatHeart {{
    from {{ transform: translateY(0) rotate(0deg); }}
    to   {{ transform: translateY(-115vh) rotate(35deg); }}
}}

/* КВЕСТ */
.quest-scene {{ padding: 25px; }}
.quest-box {{ width: min(700px, 92vw); margin: auto; }}
.quest-number {{
    font-size: 12px; text-transform: uppercase; letter-spacing: 3px;
    color: rgba(255,255,255,.38); margin-bottom: 20px;
}}
.quest-title {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(30px, 5vw, 52px); font-weight: 400; margin-bottom: 22px;
}}
.quest-text {{
    color: rgba(255,255,255,.72);
    font-size: clamp(15px, 2vw, 18px); line-height: 1.75;
    min-height: 60px; white-space: pre-line;
}}
.answer-box {{
    display: flex; justify-content: center; gap: 10px; margin-top: 30px;
}}
.answer-input {{
    width: min(350px, 65vw); padding: 14px 18px;
    border-radius: 100px;
    border: 1px solid rgba(255,255,255,.16);
    outline: none;
    background: rgba(255,255,255,.06);
    color: white; font-size: 15px; text-align: center;
}}
.answer-input:focus {{ border-color: rgba(255,255,255,.35); }}
.answer-button {{
    padding: 14px 22px; border-radius: 100px; color: white;
    background: rgba(255,255,255,.1);
    border: 1px solid rgba(255,255,255,.16);
}}
.answer-message {{
    min-height: 25px; margin-top: 16px; font-size: 13px;
    color: rgba(255,255,255,.55);
}}

/* ФИНАЛ */
.finish {{
    position: fixed; inset: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at 50% 45%, rgba(150,25,65,.18), transparent 45%), #3b0717;
    display: flex; align-items: center; justify-content: center;
    opacity: 0; visibility: hidden; z-index: 20;
    transition: opacity .8s ease;
}}
.finish.show {{ opacity: 1; visibility: visible; }}
.finish-content {{ text-align: center; position: relative; z-index: 22; }}
.finish-title {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(40px, 7vw, 78px); font-weight: 400;
}}
.finish-text {{
    margin-top: 20px; color: rgba(255,255,255,.7);
    font-size: clamp(15px, 2vw, 18px);
}}

/* ВЗРЫВ СЕРДЕЦ */
.explosion-heart {{
    position: fixed; pointer-events: none; z-index: 200; font-size: 22px;
    animation: explodeHeart 1.2s ease-out forwards;
    will-change: transform, opacity;
}}
@keyframes explodeHeart {{
    0%   {{ opacity: 1; transform: translate(-50%, -50%) scale(.5) rotate(0deg); }}
    100% {{ opacity: 0; transform: translate(calc(-50% + var(--x)), calc(-50% + var(--y))) scale(1.4) rotate(var(--r)); }}
}}

@media (max-width: 700px) {{
    .scene {{ padding: 20px; }}
    .envelope-wrap {{ width: 100%; height: 350px; }}
    .envelope {{ width: min(370px, 86vw); }}
    .envelope-shadow {{ width: 78vw; }}
    .envelope-open .envelope-paper {{ transform: translateY(-35%); }}
    .envelope-seal {{ width: 52px; height: 52px; font-size: 20px; }}
    .photo-scene {{ padding: 0 !important; }}
    .photo {{ width: 100%; height: 100%; object-fit: cover; }}
    .photo-caption {{ left: 25px; right: 25px; bottom: 55px; }}
    .photo-number {{ font-size: 9px; letter-spacing: 4px; margin-bottom: 10px; }}
    .photo-title {{ font-size: 34px; line-height: 1.08; }}
    .photo-text {{ margin-top: 12px; font-size: 13px; line-height: 1.55; }}
    .finish-content {{ padding: 25px; }}
    .answer-box {{ flex-direction: column; align-items: center; }}
    .answer-input {{ width: min(330px, 82vw); }}
    .answer-button {{ width: min(330px, 82vw); }}
}}
</style>
</head>

<body>
<div id="app">

<div class="hearts">
    <span class="bg-heart" style="left:8%;font-size:20px;animation-duration:17s;animation-delay:0s;">♥</span>
    <span class="bg-heart" style="left:22%;font-size:13px;animation-duration:21s;animation-delay:3s;">♥</span>
    <span class="bg-heart" style="left:43%;font-size:24px;animation-duration:19s;animation-delay:6s;">♥</span>
    <span class="bg-heart" style="left:67%;font-size:17px;animation-duration:24s;animation-delay:1s;">♥</span>
    <span class="bg-heart" style="left:84%;font-size:27px;animation-duration:20s;animation-delay:8s;">♥</span>
    <span class="bg-heart" style="left:93%;font-size:12px;animation-duration:18s;animation-delay:4s;">♥</span>
</div>

<!-- 0. КОНВЕРТ -->
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

<!-- 1. ПИСЬМО -->
<section class="scene" id="scene1">
    <div class="scene-inner letter">
        <h1 class="letter-title">Моя любимая Даша</h1>
        <p class="letter-text">
            Спасибо тебе за каждый день, который мы прожили вместе.
            За смех, за объятия, за маленькие моменты, которые
            со временем становятся самыми дорогими воспоминаниями.
            Я очень тебя люблю.
        </p>
        <button class="main-button" onclick="nextScene(event)">дальше →</button>
    </div>
</section>

<!-- PHOTO 1 -->
<section class="scene photo-scene" id="scene2">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(1,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">01 / 10</div>
            <div class="photo-title">Всё началось с нас</div>
            <div class="photo-text">И я даже представить не мог, сколько всего прекрасного ещё будет впереди.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 2 -->
<section class="scene photo-scene" id="scene3">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(2,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">02 / 10</div>
            <div class="photo-title">Наши моменты</div>
            <div class="photo-text">Именно из таких маленьких моментов и складывается что-то настоящее.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 3 -->
<section class="scene photo-scene" id="scene4">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(3,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">03 / 10</div>
            <div class="photo-title">Ты и я</div>
            <div class="photo-text">Два человека. Одна история. И столько всего, что ещё предстоит прожить.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 4 -->
<section class="scene photo-scene" id="scene5">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(4,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">04 / 10</div>
            <div class="photo-title">Моё самое дорогое</div>
            <div class="photo-text">Когда рядом есть человек, с которым хочется делить не только праздники, но и обычные дни.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 5 -->
<section class="scene photo-scene" id="scene6">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(5,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">05 / 10</div>
            <div class="photo-title">С тобой всё по-другому</div>
            <div class="photo-text">Даже самые обычные дни становятся особенными.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 6 -->
<section class="scene photo-scene" id="scene7">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(6,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">06 / 10</div>
            <div class="photo-title">Ещё один момент</div>
            <div class="photo-text">Ещё одна фотография, которую хочется сохранить не только в телефоне, но и в памяти.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 7 -->
<section class="scene photo-scene" id="scene8">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(7,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">07 / 10</div>
            <div class="photo-title">Счастье в мелочах</div>
            <div class="photo-text">Иногда для счастья нужно совсем немного. Просто быть рядом.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 8 -->
<section class="scene photo-scene" id="scene9">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(8,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">08 / 10</div>
            <div class="photo-title">Вот за что я люблю нас</div>
            <div class="photo-text">За смех, за тепло и за те моменты, которые хочется проживать снова и снова.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 9 -->
<section class="scene photo-scene" id="scene10">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(9,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">09 / 10</div>
            <div class="photo-title">Просто мы</div>
            <div class="photo-text">Без лишних слов и всего остального. Только ты, я и наше маленькое счастье.</div>
        </div>
    </div></div>
</section>

<!-- PHOTO 10 -->
<section class="scene photo-scene" id="scene11">
    <div class="scene-inner"><div class="photo-wrapper">
        <img class="photo" src="data:image/jpeg;base64,{photos.get(10,'')}" alt="Наш момент">
        <div class="photo-caption">
            <div class="photo-number">10 / 10</div>
            <div class="photo-title">И это только начало</div>
            <div class="photo-text">Десять фотографий — и впереди ещё целая жизнь, которую я хочу прожить с тобой.</div>
        </div>
    </div></div>
</section>

<!-- 12. ДАТА -->
<section class="scene" id="scene12">
    <div class="scene-inner">
        <div class="date">21.09.2024</div>
        <h1 class="title" style="margin-top:28px;">Наша дата</h1>
        <p class="subtitle">День, когда мы стали семьёй.</p>
        <button class="main-button" onclick="nextScene(event)">дальше →</button>
    </div>
</section>

<!-- 13. ДАША -->
<section class="scene" id="scene13">
    <div class="scene-inner">
        <div class="big-heart">❤️</div>
        <p class="subtitle">
            Я не знаю, каким будет наше будущее
            через 10, 20 или 50 лет.<br>
            Но я хочу встретить его рядом с тобой.
        </p>
        <button class="main-button" onclick="nextScene(event)">дальше →</button>
    </div>
</section>

<!-- 14. ПОДАРОК -->
<section class="scene" id="scene14">
    <div class="scene-inner">
        <h1 class="title" style="margin-bottom: 30px;">Для тебя подарочек</h1>
        <div class="gift" onclick="openGift(event)">
            <div class="gift-bow">
                <div class="bow-left"></div>
                <div class="bow-right"></div>
            </div>
            <div class="gift-lid"></div>
            <div class="gift-box"></div>
            <div class="gift-ribbon-v"></div>
            <div class="gift-ribbon-h"></div>
        </div>
    </div>
</section>

<!-- 15. КВЕСТ -->
<section class="scene quest-scene" id="scene15">
    <div class="scene-inner quest-box">
        <div class="quest-number" id
