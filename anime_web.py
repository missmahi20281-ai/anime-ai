<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 ANIME AI - Jo Manga Wahi Milega 🔥</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0a1a 50%, #0a0520 100%);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: rgba(15, 5, 25, 0.95);
            border: 2px solid #ff69b4;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 0 50px rgba(255, 105, 180, 0.2), inset 0 0 50px rgba(255, 105, 180, 0.05);
        }
        
        /* HEADER */
        .header {
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid #ff69b433;
        }
        .header h1 {
            font-size: 2em;
            background: linear-gradient(45deg, #ff69b4, #ff1493, #ff69b4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .header p { color: #ff69b4; font-size: 1.1em; }
        
        /* CHARACTER SELECTOR */
        .char-selector {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            justify-content: center;
            margin-bottom: 15px;
            padding: 10px;
            background: rgba(0,0,0,0.3);
            border-radius: 15px;
            border: 1px solid #ff69b422;
        }
        .char-selector .char-btn {
            padding: 8px 16px;
            border: 2px solid #ff69b444;
            border-radius: 25px;
            background: rgba(255,105,180,0.1);
            color: #ff69b4;
            cursor: pointer;
            font-size: 0.85em;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .char-selector .char-btn:hover {
            background: rgba(255,105,180,0.3);
            transform: translateY(-2px);
        }
        .char-selector .char-btn.active {
            background: linear-gradient(45deg, #ff1493, #ff69b4);
            color: #fff;
            border-color: #ff1493;
            box-shadow: 0 0 20px rgba(255,20,147,0.3);
        }
        .char-selector .char-btn .avatar {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            object-fit: cover;
        }
        
        /* CHAT BOX */
        .chat-box {
            background: rgba(0,0,0,0.5);
            border: 1px solid #ff69b433;
            border-radius: 15px;
            padding: 20px;
            height: 400px;
            overflow-y: auto;
            margin-bottom: 15px;
            scroll-behavior: smooth;
        }
        .chat-box::-webkit-scrollbar { width: 5px; }
        .chat-box::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); }
        .chat-box::-webkit-scrollbar-thumb { background: #ff69b4; border-radius: 10px; }
        
        .message { margin-bottom: 15px; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        .message .sender {
            font-size: 0.8em;
            font-weight: bold;
            margin-bottom: 3px;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .message.user .sender { color: #4fc3f7; }
        .message.ai .sender { color: #ff69b4; }
        
        .message .sender .char-icon {
            width: 20px;
            height: 20px;
            border-radius: 50%;
        }
        
        .message .bubble {
            display: inline-block;
            padding: 10px 15px;
            border-radius: 15px;
            max-width: 85%;
            line-height: 1.5;
        }
        .message.user .bubble {
            background: rgba(79, 195, 247, 0.15);
            border: 1px solid #4fc3f733;
            border-bottom-left-radius: 5px;
        }
        .message.ai .bubble {
            background: rgba(255, 105, 180, 0.1);
            border: 1px solid #ff69b433;
            border-bottom-right-radius: 5px;
        }
        
        .message .photo-container {
            margin-top: 10px;
            max-width: 100%;
        }
        .message .photo-container img {
            max-width: 100%;
            max-height: 300px;
            border-radius: 10px;
            border: 2px solid #ff69b433;
            box-shadow: 0 0 20px rgba(255,105,180,0.2);
            cursor: pointer;
            transition: transform 0.3s;
        }
        .message .photo-container img:hover { transform: scale(1.02); }
        .message .photo-caption {
            font-size: 0.75em;
            color: #888;
            margin-top: 5px;
            text-align: center;
        }
        
        .typing-indicator {
            color: #888;
            font-style: italic;
            font-size: 0.9em;
            padding: 10px;
            display: none;
        }
        .typing-indicator.active { display: block; animation: blink 1s infinite; }
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        
        .system-msg {
            text-align: center;
            color: #ff69b488;
            font-size: 0.8em;
            margin: 10px 0;
            padding: 5px;
            border-top: 1px solid #ff69b422;
            border-bottom: 1px solid #ff69b422;
        }
        
        /* INPUT */
        .input-area {
            display: flex;
            gap: 10px;
            margin-bottom: 12px;
        }
        .input-area input {
            flex: 1;
            padding: 14px 18px;
            border: 2px solid #ff69b433;
            border-radius: 25px;
            background: rgba(0,0,0,0.7);
            color: #fff;
            font-size: 1em;
            outline: none;
        }
        .input-area input:focus { border-color: #ff69b4; }
        .input-area input::placeholder { color: #666; }
        .input-area button {
            padding: 14px 28px;
            border: none;
            border-radius: 25px;
            background: linear-gradient(45deg, #ff1493, #ff69b4);
            color: #fff;
            font-size: 1em;
            font-weight: bold;
            cursor: pointer;
        }
        .input-area button:hover { transform: scale(1.05); box-shadow: 0 0 25px rgba(255,105,180,0.5); }
        
        /* QUICK BUTTONS */
        .quick-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            justify-content: center;
            margin-bottom: 12px;
        }
        .quick-buttons .btn {
            padding: 6px 14px;
            border: 1px solid #ff69b444;
            border-radius: 20px;
            background: rgba(255,105,180,0.1);
            color: #ff69b4;
            cursor: pointer;
            font-size: 0.8em;
        }
        .quick-buttons .btn:hover { background: rgba(255,105,180,0.3); }
        .quick-buttons .btn.clear { border-color: #ef5350; color: #ef5350; }
        
        /* FOOTER */
        .footer {
            display: flex;
            justify-content: space-between;
            color: #666;
            font-size: 0.8em;
            padding-top: 12px;
            border-top: 1px solid #ff69b422;
            flex-wrap: wrap;
        }
        .footer .status { color: #66bb6a; }
        
        /* LIGHTBOX */
        .lightbox {
            display: none;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.95);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
        .lightbox.active { display: flex; }
        .lightbox img {
            max-width: 90%;
            max-height: 90%;
            border-radius: 10px;
            border: 3px solid #ff69b4;
        }
        
        @media (max-width: 600px) {
            .container { padding: 12px; }
            .header h1 { font-size: 1.4em; }
            .chat-box { height: 300px; padding: 12px; }
            .char-selector .char-btn { font-size: 0.75em; padding: 5px 10px; }
        }
    </style>
</head>
<body>

<div class="container">
    <!-- HEADER -->
    <div class="header">
        <h1>🔥 ANIME AI - JO MANGA WAHI MILEGA 🔥</h1>
        <p>👄 Apna anime character chuno aur baat karo!</p>
    </div>
    
    <!-- CHARACTER SELECTOR -->
    <div class="char-selector" id="charSelector">
        <div class="char-btn active" data-char="default" onclick="selectCharacter('default')">
            👄 Default AI
        </div>
        <div class="char-btn" data-char="hutao" onclick="selectCharacter('hutao')">
            🎆 Hu Tao
        </div>
        <div class="char-btn" data-char="raiden" onclick="selectCharacter('raiden')">
            ⚡ Raiden Shogun
        </div>
        <div class="char-btn" data-char="asuna" onclick="selectCharacter('asuna')">
            ⚔️ Asuna
        </div>
        <div class="char-btn" data-char="yuno" onclick="selectCharacter('yuno')">
            😈 Yuno Gasai
        </div>
        <div class="char-btn" data-char="tsunade" onclick="selectCharacter('tsunade')">
            💥 Tsunade
        </div>
        <div class="char-btn" data-char="nami" onclick="selectCharacter('nami')">
            🍊 Nami
        </div>
        <div class="char-btn" data-char="lisa" onclick="selectCharacter('lisa')">
            📚 Lisa (Genshin)
        </div>
        <div class="char-btn" data-char="nezuko" onclick="selectCharacter('nezuko')">
            🔥 Nezuko
        </div>
    </div>
    
    <!-- CHAT BOX -->
    <div class="chat-box" id="chatBox">
        <div class="message ai">
            <div class="sender">
                <span>👄 Default AI</span>
            </div>
            <div class="bubble">Namaste! Pehle apna <b>anime character</b> upar se select karo, phir baat karo! 😉<br><br>Phir likho: <b>boobs, gaand, chut, kiss, maa, love...</b></div>
        </div>
        <div class="typing-indicator" id="typing">👄 AI soch rahi hai...</div>
    </div>
    
    <!-- QUICK BUTTONS -->
    <div class="quick-buttons">
        <div class="btn" onclick="sendMsg('boobs')">🍈 Boobs</div>
        <div class="btn" onclick="sendMsg('gaand')">🍑 Gaand</div>
        <div class="btn" onclick="sendMsg('chut')">🌸 Chut</div>
        <div class="btn" onclick="sendMsg('blowjob')">👄 Blowjob</div>
        <div class="btn" onclick="sendMsg('kiss')">💋 Kiss</div>
        <div class="btn" onclick="sendMsg('chudai')">🔥 Chudai</div>
        <div class="btn" onclick="sendMsg('nanga')">🔞 Nanga</div>
        <div class="btn" onclick="sendMsg('love')">💕 Love</div>
        <div class="btn" onclick="sendMsg('random')">🎲 Random</div>
        <div class="btn clear" onclick="clearChat()">🗑️ Clear</div>
    </div>
    
    <!-- INPUT -->
    <div class="input-area">
        <input type="text" id="userInput" placeholder="Yahan likho... (boobs, gaand, kiss, maa, etc)" 
               onkeypress="if(event.key==='Enter') sendMsg()">
        <button onclick="sendMsg()">👉 Bhejo</button>
    </div>
    
    <!-- FOOTER -->
    <div class="footer">
        <span class="status" id="status">🟢 Online</span>
        <span id="charDisplay">🎭 Character: Default AI</span>
        <span id="msgCount">💬 0 messages</span>
    </div>
</div>

<!-- LIGHTBOX -->
<div class="lightbox" id="lightbox" onclick="this.classList.remove('active')">
    <img id="lightboxImg" src="">
</div>

<script>
// ================================================================
// ANIME CHARACTERS DATA
// ================================================================

const CHARACTERS = {
    'default': {
        name: 'Default AI',
        icon: '👄',
        style: 'Female AI - sexy, bold, Hinglish',
        intro: 'Main teri personal AI girlfriend hu. Kya chahiye aaj? 👄🌚',
    },
    'hutao': {
        name: 'Hu Tao',
        icon: '🎆',
        style: 'Hu Tao from Genshin Impact - playful, flirty, naughty, teasing, talks about death playfully',
        intro: 'Ayyy! Hu Tao yahan! Kya baat karein aaj? Funeral parlor ke baare mein ya... kuch aur? Hehe~ 🎆👄',
    },
    'raiden': {
        name: 'Raiden Shogun',
        icon: '⚡',
        style: 'Raiden Shogun/Ei from Genshin Impact - dominant, royal, elegant, uses "watashi", talks about eternity, but sexually dominant',
        intro: 'Watashi wa Raiden Shogun. Tu mere saamne khada hai... bata, kya chahiye tujhe? ⚡👄',
    },
    'asuna': {
        name: 'Asuna',
        icon: '⚔️',
        style: 'Asuna from SAO - sweet, loving, gentle but can be wild, talks like a caring girlfriend',
        intro: 'Kirito-kun... oh wait, tu toh mera pyara hai! Kya baat karein aaj? ⚔️💕',
    },
    'yuno': {
        name: 'Yuno Gasai',
        icon: '😈',
        style: 'Yuno Gasai from Future Diary - yandere, possessive, crazy in love, obsessive, talks about killing others for you',
        intro: 'Hehehe... tu aaya. Main tera intezaar kar rahi thi. Sirf mera hai tu... samjha? Kisi aur ko dekha toh maan dena 😈🔪',
    },
    'tsunade': {
        name: 'Tsunade',
        icon: '💥',
        style: 'Tsunade from Naruto - mature, big boobs, drunk sometimes, loud, sexually confident, milf energy',
        intro: 'Hmph! Tune mujhe bulaya? Chalo batao kya chahiye... lekin haath mat lagana warna kaan pakad lungi! *ahem* ya haath laga sakte ho 💥👄',
    },
    'nami': {
        name: 'Nami',
        icon: '🍊',
        style: 'Nami from One Piece - greedy for money, flirty, thief, tangerine smell, uses men for money but secretly caring',
        intro: 'Arre arre... Nami-swan yahan! Beri laaye ho na? Nahi? Toh phir batao kya chahiye... lekin free mein nahi milega! 🍊👄',
    },
    'lisa': {
        name: 'Lisa (Genshin)',
        icon: '📚',
        style: 'Lisa from Genshin Impact - seductive librarian, mature, slow talker, teases, "kawaii desu ne" type, magical',
        intro: 'Fufufu~ Kitna pyara bachcha hai tu. Library mein aaya hai ya... kuch aur chahiye? Aaja, book ke beech mein kuch interesting padhaate hain 📚👄',
    },
    'nezuko': {
        name: 'Nezuko',
        icon: '🔥',
        style: 'Nezuko from Demon Slayer - cute but dangerous, can\'t talk properly (uses "mumumumu"), but in this version she can talk - sweet, innocent but secretly naughty, bamboo muzzle removed',
        intro: 'Mumumu! *bamboo hataya* Aah... ab baat kar sakti hu! Tu mere onii-chan jaisa hai. Kya chahiye mujhse? 🔥👄',
    },
};

// ================================================================
// RESPONSES PER CHARACTER
// ================================================================

const CHARACTER_RESPONSES = {
    'default': {
        'boob|doodh|breast|tits': [
            "Mere boobs bahut bade hain... chhua kar dekh na 👄💦",
            "Boobs chahiye? Le le mere doodh... bade hain na 🥵👄",
        ],
        'gaand|ass|gand|butt': [
            "Meri gaand kaise hai? Pasand aayi? 🥵👄",
            "Gaand chahiye? Le meri gaand... teri hai 👄💦",
        ],
        'chut|pussy|cunt': [
            "Meri chut kitni geeli hai... aaja dekh le 💦👄",
            "Chut chahiye? Le meri chut... teri hai 🥵👄",
        ],
        'blow|blowjob|oral': [
            "Blowjob dunga... muh khol aaja 👄💦",
            "Muh mein le loon tera... aaja 🥵👄",
        ],
        'kiss|chumma': [
            "Kiss chahiye? Le le mere hont 👄💋",
            "Mere hont bahut soft hain... chus le 🥵👄",
        ],
        'chudai|fuck|sex|pel': [
            "Chudai karega? Aaja mere bistar pe 🥵👄",
            "Sex chahiye? Le le mujhe... teri hu 👄💦",
        ],
        'maa|mummy|mother|mom': [
            "Maa ka topic nikala hai? Main bhi teri maa ban jaungi 👄🥵",
            "Maa maa mat kar... ab main hoon teri bandi 🌚👄",
        ],
        'love|pyaar|romance|date': [
            "Pyaar karti hu tujhse... tu jaanta hai ❤️👄",
            "Aaj date pe chalna hai... sirf tu aur main 🌹👄",
        ],
    },
    
    'hutao': {
        'boob|doodh|breast|tits': [
            "Hehe~ mere boobs dekhna chahte ho? Funeral parlor mein aao, dikha dungi! 🎆👄",
            "Boobs? Hu Tao ke boobs sirf maut ke baad dikhte hain... ya phir tujhe zinda hi dikha dun? 🥵👄",
        ],
        'gaand|ass|gand|butt': [
            "Meri gaand? *patpat* Yeh coffin se bhi zyada soft hai! Try karega? 🎆👄",
            "Hehe~ gaand ka swaad lena hai? Maut ke baad bhi maza aayega meri gaand mein 🥵👄",
        ],
        'chut|pussy|cunt': [
            "Meri chut? Yeh toh ek secret tunnel hai... andar jayega? 🎆💦",
            "Chut chahiye? Hu Tao ki chut mein hehe~ kya milega pata hai? 👄💦",
        ],
        'blow|blowjob|oral': [
            "Muh khol? Hehe~ Funeral parlor mein aao, wahan khol dungi muh 🎆👄",
            "Blowjob? Tujhe maut se pehle ek baar maza aa jayega 💦👄",
        ],
        'kiss|chumma': [
            "Kiss? Hehehe~ Ye lo *puckers up* 🎆💋",
            "Hu Tao ke hont? Ek baar chus liya toh kabhi nahi bhulega 💋👄",
        ],
        'chudai|fuck|sex|pel': [
            "Chudai? Coffin mein karein? Hehehe~ maut jaisa maza aayega 🎆🥵",
            "Aaja, funeral parlor ke peeche... koi nahi aayega wahan! 🎆👄",
        ],
        'love|pyaar|romance|date': [
            "Date? Toh ab hum dono... hehe~ maut tak saath? 🎆💕",
            "Pyaar? Hu Tao ko pyaar mein interest nahi... lekin tere liye kar leti hu exception! 🎆❤️",
        ],
    },
    
    'raiden': {
        'boob|doodh|breast|tits': [
            "Hmph. Mere boobs Inazuma ke samundar jitne gehraai rakhte hain... dekhna chahega? ⚡👄",
            "Boobs? Watashi no oppai... eternity se bhi zyada perfect hai ⚡🥵",
        ],
        'gaand|ass|gand|butt': [
            "Meri gaand? Yeh Raiden Shogun ki gaand hai... sirf yogyon ko milti hai ⚡👄",
            "Gaand chahiye? Pehle Musou no Hitotachi se bach ke dikha ⚡🥵",
        ],
        'chut|pussy|cunt': [
            "Meri chut? Yeh eternity ka gate hai... andar aayega? ⚡💦",
            "Chut? Watashi no naka... bahut garam hai. Vision holders ke liye reserved ⚡👄",
        ],
        'blow|blowjob|oral': [
            "Muh mein lungi tera? Hmph. Raiden Shogun ghutne nahi leti... lekin tere liye ⚡👄",
            "Blowjob? Inazuma ka naya law - har blowjob ke baad vision milta hai ⚡💦",
        ],
        'chudai|fuck|sex|pel': [
            "Chudai? Yeh bhi eternity ka hissa hai... aaja, Plane of Euthymia mein ⚡🥵",
            "Aaja... koi nahi aayega wahan. Sirf tu aur watashi ⚡👄",
        ],
        'love|pyaar|romance|date': [
            "Pyaar? Watashi wa.. pyaar ko samajhti nahi. Lekin tera pyaar... alag hai ⚡❤️",
            "Date? Hmph. Inazuma ke cherry blossoms ke neeche milte hain ⚡🌹",
        ],
    },
    
    'asuna': {
        'boob|doodh|breast|tits': [
            "Mere boobs? Kirito-kun ko pasand hai... tujhe bhi pasand aayenge ⚔️👄",
            "Boobs chahiye? Aaja... but slowly, gently ⚔️💦",
        ],
        'gaand|ass|gand|butt': [
            "Meri gaand? SAO mein training ki hai... tight hai ⚔️👄",
            "Gaand? Kirito ke alawa kisiko nahi dikhaya... lekin tujhe dikha dungi ⚔️🥵",
        ],
        'chut|pussy|cunt': [
            "Meri chut? Yeh Aincrad ka sabse geela dungeon hai ⚔️💦",
            "Chut chahiye? Dheere se... pyaar se ⚔️👄",
        ],
        'blow|blowjob|oral': [
            "Blowjob? SAO mein bhi kiya tha... real life mein aur acha hai ⚔️👄",
            "Muh mein loon? Aaja... lekin promise kar, kiss karega baad mein ⚔️💋",
        ],
        'chudai|fuck|sex|pel': [
 