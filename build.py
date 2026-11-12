"""Builds the BarkZone members area demo (Option A and Option B) as static pages.
Run: python3 build.py   (writes index.html, a/*.html, b/*.html, a/a.css, b/b.css)
"""
import os, html

R = os.path.dirname(os.path.abspath(__file__))
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Anton&display=swap" rel="stylesheet">'

SKILLS = [  # (name, img, lessons, done)
    ('Foundations', 'foundations', 22, 22), ('Life Skills', 'life-skills', 10, 7),
    ('Weaves', 'weaves', 7, 3), ('Jumps', 'jumps', 9, 2), ('Tunnels', 'tunnels', 2, 0),
    ('Dog Walk', 'dog-walk', 5, 0), ('Seesaw', 'seesaw', 1, 0), ('A-Frame', 'aframe', 1, 0),
]
VIDS = [  # parts of the Weave Entries lesson
    ('Weave Entries Part 1', 'yt_9ighu9ilb5g'), ('Weave Entries Part 2', 'yt_9ighu9ilb5g'),
    ('Weave Entries Part 3', 'yt_k_3itnoujyc'), ('Weave Entries Part 4', 'yt_vkrzkg9vomm'),
    ('Weave Entries Part 5', 'yt_hanzt6bwepe'), ('Hokey 2x2 Weaves, 2 gates', 'yt_jdhagjetawy'),
    ('Troubleshooting weave entries', 'yt_yffzsbw73ei'),
]
WEAVES = [  # lessons on the Weaves skill page
    ('Weave Entries Explanation', 1, 'yt_yffzsbw73ei', 'done'), ('Weave Entries', 7, 'yt_k_3itnoujyc', 'progress'),
    ('Weave Entries on full set', 1, 'yt_vkrzkg9vomm', 'todo'), ('Bugs Weaves', 18, 'yt_hanzt6bwepe', 'done'),
    ("Heck's Weaves 2x2", 4, 'yt_jdhagjetawy', 'done'), ("Ferdi's Weaves 2x2", None, 'yt_9ighu9ilb5g', 'todo'),
    ('Weave Challenges', 1, 'yt_k_3itnoujyc', 'todo'),
]
OTHER = 'This preview only has the Weaves skill built. In the real version every skill gets a page like it.'
NOTBUILT = 'Not part of this preview. This page gets the same new look in the real build.'
PLAY = 'In the real members area the YouTube video plays here.'
def img(n): return f'../img/{n}.jpg'
def e(s): return html.escape(s, quote=True)
def vids_label(c): return f'{c} video{"s" if c != 1 else ""}' if c else 'Video lesson'

PAGES = [('index', 'Members home'), ('weaves', 'Skill page'), ('weave-entries', 'Lesson page'), ('add-lesson', 'Add a lesson')]

def strip(opt, page):
    other = 'b' if opt == 'a' else 'a'
    name = 'Option A: Your look, refined' if opt == 'a' else 'Option B: The Training Zone'
    links = ''.join(f'<a href="{p}.html" class="{"on" if p == page else ""}">{t}</a>' for p, t in PAGES)
    return (f'<div class="pv"><a href="../index.html"><b>BarkZone members area preview</b></a><span>{name}</span><nav>{links}</nav>'
            f'<a class="sw" href="../{other}/{page}.html">View Option {other.upper()} ›</a></div>')

def page(opt, pg, title, body, extra_body_class=''):
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)} | BarkZone members preview</title>{FONTS}
<link rel="stylesheet" href="../assets/demo.css"><link rel="stylesheet" href="{opt}.css">
</head><body class="{extra_body_class}">{strip(opt, pg)}{body}<script src="../assets/demo.js"></script></body></html>'''

# ======================================================================= OPTION A
A_CSS = '''
body{background:#f7f5f9;color:var(--ink)}
.obar{background:var(--obar);color:#fff;font-size:13px;padding:8px 0}
.obar .w{display:flex;gap:26px}
.w{max-width:1180px;margin:0 auto;padding:0 32px}
.nav{background:#fff;border-bottom:1px solid #eee;position:relative}
.nav .w{display:flex;align-items:center;gap:30px;padding-top:10px;padding-bottom:10px}
.nav .logo{height:58px;width:auto}
.links{display:flex;gap:24px;font-size:14px;font-weight:500;flex:1;justify-content:center}
.links a{padding:6px 0;border-bottom:2px solid transparent}
.links a:hover{color:var(--purple)}
.links a.on{color:var(--purple);font-weight:600;border-color:var(--purple)}
.adm{font-size:10px;font-weight:700;background:#f1e3f8;color:var(--purple);padding:2px 6px;border-radius:5px;margin-left:4px;vertical-align:2px}
.me{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600}
.me i{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--purple),var(--pink));display:inline-block}
.burger{display:none;font-size:26px;line-height:1;padding:4px 8px}
.band{background:var(--purple);color:#fff;padding:34px 0}
.band h1{font-size:clamp(26px,4vw,34px);font-weight:700;line-height:1.2}
.band p{opacity:.92;margin-top:6px;font-size:15px}
.crumb{font-size:13px;opacity:.85;margin-bottom:6px}.crumb a:hover{text-decoration:underline}
.chip{display:inline-block;background:#fff;color:var(--purple);font-weight:700;font-size:12px;padding:5px 12px;border-radius:99px;margin-left:10px;vertical-align:middle;letter-spacing:.04em}
.card{background:#fff;border-radius:16px;box-shadow:0 2px 12px rgba(40,10,60,.07)}
a.card{transition:transform .2s,box-shadow .2s}a.card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(40,10,60,.12)}
.btn{display:inline-block;background:var(--orange);color:#fff;font-weight:600;font-size:14px;padding:11px 22px;border-radius:10px;text-align:center;transition:filter .2s}
.btn:hover{filter:brightness(1.07)}
.btn.ghost{background:#fff;color:var(--ink);border:1.5px solid #ddd}
.btn.pink{background:var(--pink)}.btn.green{background:var(--green)}
.btn.sm{padding:8px 16px;font-size:13px}
.bar{height:8px;background:#eee;border-radius:99px;overflow:hidden}.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--purple),var(--pink))}
h2.sec{font-size:22px;font-weight:700;margin:42px 0 16px}
.muted{color:var(--muted)}
.slimfoot{background:var(--lime);margin-top:56px;padding:22px 0}
.slimfoot .w{display:flex;justify-content:space-between;align-items:center;gap:16px;font-weight:600;flex-wrap:wrap}
.slimfoot .wa{display:flex;gap:12px}.slimfoot .wa a{background:#fff;padding:9px 16px;border-radius:10px;font-size:14px}
/* hub */
.hero{display:grid;grid-template-columns:1.6fr 1fr;gap:24px;padding-top:34px}
.cont{display:flex;overflow:hidden}
.cont .thumb{width:46%;min-height:220px;flex:none}
.cont .txt{padding:26px 28px;flex:1}
.eyebrow{color:var(--pink);font-weight:700;font-size:12px;letter-spacing:.08em}
.acts{display:grid;gap:14px}
.act{padding:18px 20px;display:flex;justify-content:space-between;align-items:center;gap:12px}
.act b{display:block}.act small{color:var(--muted);font-size:13px}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.tile{overflow:hidden}.tile img{width:100%;aspect-ratio:1;object-fit:cover}
.tile .tx{padding:14px 16px 16px}.tile .row{display:flex;justify-content:space-between;font-weight:700;gap:8px}
.tile .row span{font-weight:500;color:var(--muted);font-size:13px;white-space:nowrap}
.more{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.more a{display:flex;overflow:hidden;align-items:center}.more img{width:110px;height:110px;object-fit:cover;flex:none}.more div{padding:0 20px}
/* skill page */
.skill-head{display:flex;align-items:center;gap:28px}
.skill-head img{width:120px;height:120px;border-radius:14px;object-fit:cover;border:4px solid #fff;flex:none}
.prog{display:flex;align-items:center;gap:14px;margin-top:12px}
.tools{display:flex;justify-content:space-between;align-items:center;margin:34px 0 18px;gap:16px;flex-wrap:wrap}
.filt{display:flex;gap:8px}
.filt button{padding:8px 16px;border-radius:10px;font-size:13px;font-weight:600;background:#fff;border:1.5px solid #ddd}
.filt button.on{background:var(--orange);border-color:var(--orange);color:#fff}
.lessons{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.lessons .thumb{aspect-ratio:16/9}
.num{position:absolute;top:12px;left:12px;background:#fff;border-radius:99px;font-weight:700;font-size:12px;padding:4px 10px}
.lessons .tx{padding:16px 18px}
.lessons .meta{display:flex;justify-content:space-between;margin-top:8px;font-size:13px}
.s-done{color:var(--green);font-weight:700}.s-progress{color:var(--pink);font-weight:700}.s-todo{color:var(--muted)}
/* lesson page */
.lesson{display:grid;grid-template-columns:minmax(0,1.85fr) minmax(0,1fr);gap:26px;margin-top:34px}
.player{aspect-ratio:16/9}
.ph{padding:20px 24px;display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.ph h2{font-size:22px;font-weight:700}
.navbtns{display:flex;gap:10px}
.notes{padding:22px 24px;margin-top:22px}
.notes p{color:var(--muted);font-size:14px;line-height:1.7}
.pl{padding:16px}
.pl-h{display:flex;justify-content:space-between;font-weight:700;padding:4px 6px 12px}
.part{display:flex;gap:12px;align-items:center;padding:10px;border-radius:10px;cursor:pointer;width:100%;text-align:left}
.part:hover{background:#f6f0fa}
.part.current{background:#fbeef6}
.part .thumb{width:96px;height:54px;border-radius:6px;flex:none}
.part b{display:block;font-size:13px;font-weight:600;line-height:1.35}
.part .st{font-size:12px;color:var(--muted)}
.part.watched .st{color:var(--green)}.part.current .st{color:var(--pink)}
.fin{padding:20px;margin-top:22px;text-align:center}
.fin .btn{display:block;margin-top:14px}
/* add lesson */
.add{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:26px;margin-top:34px;align-items:start}
.form{padding:26px 28px}
.form h2{font-size:19px;margin-bottom:4px}
.fld{margin-top:18px}
.fld label,.lab{display:block;font-weight:600;font-size:14px;margin-bottom:6px}
.fld small{display:block;color:var(--muted);font-size:12px;margin-top:4px}
input[type=text],input[type=url],select,textarea{width:100%;font:inherit;font-size:14px;padding:11px 14px;border:1.5px solid #ddd;border-radius:10px;background:#fff;color:var(--ink)}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--purple);box-shadow:0 0 0 3px rgba(190,66,225,.15)}
textarea{min-height:110px;resize:vertical}
.vid-row{background:#faf7fc;border:1px solid #eee5f3;border-radius:12px;padding:14px;margin-bottom:10px}
.vid-top{display:flex;justify-content:space-between;align-items:center;font-size:13px;font-weight:700;margin-bottom:8px}
.vid-ok{color:var(--green);font-weight:700;margin-left:8px}
.vid-x{color:var(--muted);font-size:13px}
.vid-row .two{display:grid;grid-template-columns:1.3fr 1fr;gap:10px}
.checks{display:flex;gap:18px;flex-wrap:wrap;font-size:14px}
.checks label{display:flex;gap:6px;align-items:center;font-weight:500}
.checks input{accent-color:var(--purple);width:17px;height:17px}
.file{display:block;border:1.5px dashed #ccc;border-radius:10px;padding:14px;font-size:13px;color:var(--muted);text-align:center}
.form .go{display:flex;gap:10px;margin-top:24px;flex-wrap:wrap}
.preview{position:sticky;top:20px}
.preview .pv-thumb{background:#ece6f0;color:var(--muted);border-radius:16px 16px 0 0}
.done-msg{margin-top:18px;padding:16px 18px;border-radius:12px;background:#eaf6ec;color:#1d6b2f;font-size:14px}
@media (max-width:980px){
 .tiles{grid-template-columns:repeat(2,1fr)}.more,.lessons{grid-template-columns:repeat(2,1fr)}
 .hero,.lesson,.add{grid-template-columns:1fr}
 .preview{position:static}
}
@media (max-width:860px){
 .obar{display:none}
 .burger{display:block}
 .links{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;flex-direction:column;gap:0;padding:8px 16px 16px;box-shadow:0 12px 20px rgba(0,0,0,.08);z-index:50}
 .links a{padding:12px 4px;border-bottom:1px solid #f0f0f0}
 .links a.on{border-color:#f0f0f0}
 .menu-open .links{display:flex}
 .nav .w{justify-content:space-between}
 .me span{display:none}
}
@media (max-width:620px){
 .w{padding:0 16px}
 .nav .logo{height:46px}
 .band{padding:22px 0}
 .chip{margin:8px 0 0;display:table}
 .cont{flex-direction:column}.cont .thumb{width:100%;min-height:0;aspect-ratio:16/9}
 .cont .txt{padding:20px}
 .tiles{gap:14px}.tile .tx{padding:10px 12px 12px}.tile .row{flex-direction:column;gap:0;font-size:14px}
 .more,.lessons{grid-template-columns:1fr}
 .skill-head{gap:16px}.skill-head img{width:84px;height:84px}
 .prog .bar{width:140px!important}
 .ph{padding:16px}.navbtns{width:100%}.navbtns .btn{flex:1}
 .form{padding:20px}
 .vid-row .two{grid-template-columns:1fr}
 .slimfoot .w{justify-content:center;text-align:center}
}
'''

def a_shell(pg, title, band, body):
    links = [('index.html', 'Members Home', pg in ('index',)), ('index.html#skills', 'Skills', pg in ('weaves', 'weave-entries')),
             ('#', 'Course Plans', False), ('#', 'Wednesday Classes', False), ('#', 'Training Days', False), ('#', 'Feedback', False)]
    nav = ''.join(f'<a href="{h}" class="{"on" if on else ""}"{" data-demo=" + chr(34) + NOTBUILT + chr(34) if h == "#" else ""}>{t}</a>' for h, t, on in links)
    nav += f'<a href="add-lesson.html" class="{"on" if pg == "add-lesson" else ""}">Add a lesson<span class="adm">ADMIN</span></a>'
    wa = f'<a href="#" data-demo="Opens WhatsApp to message Iain">Message Iain</a><a href="#" data-demo="Opens WhatsApp to message Livvi">Message Livvi</a>'
    body = (f'<div class="obar"><div class="w">{wa}</div></div>'
            f'<header class="nav"><div class="w"><a href="index.html"><img class="logo" src="../img/logo.png" alt="BarkZone Agility"></a>'
            f'<nav class="links">{nav}</nav><div class="me"><i></i><span>Sam</span></div><button class="burger" data-menu aria-label="Menu">☰</button></div></header>'
            f'<section class="band"><div class="w">{band}</div></section><main>{body}</main>'
            f'<footer class="slimfoot"><div class="w"><span>Stuck on something? We are a message away.</span><div class="wa">{wa}</div></div></footer>')
    return page('a', pg, title, body)

def a_hub():
    tiles = ''.join(
        f'<a class="card tile" href="{"weaves.html" if n == "Weaves" else "#"}"{"" if n == "Weaves" else f" data-demo={chr(34)}{OTHER}{chr(34)}"}>'
        f'<img src="{img(i)}" alt="{n}" loading="lazy"><div class="tx"><div class="row">{n}<span>{d}/{l} lesson{"s" if l != 1 else ""}</span></div>'
        f'<div class="bar" style="margin-top:10px"><i style="width:{int(100 * d / l)}%"></i></div></div></a>'
        for n, i, l, d in SKILLS)
    more = ''.join(f'<a class="card" href="#" data-demo="{NOTBUILT}"><img src="{img(a)}" alt="" loading="lazy"><div><b>{t}</b><div class="muted" style="font-size:13px">{s}</div></div></a>'
                   for t, s, a in [('Course Plans', 'Show courses to practise at home', 'course'), ('Wednesday Classes', 'Catch up on class videos', 'wed'), ('Stop Contacts', 'Seesaw and dog walk foundation', 'stop')])
    body = f'''<div class="w">
<div class="hero">
 <div class="card cont"><a class="thumb" href="weave-entries.html"><img src="{img('yt_k_3itnoujyc')}" alt=""><span class="play"><i></i></span></a>
  <div class="txt"><div class="eyebrow">PICK UP WHERE YOU LEFT OFF</div>
   <div style="font-size:24px;font-weight:700;margin:8px 0 2px">Weave Entries</div><div class="muted" style="font-size:14px">Weaves · Part 3 of 7</div>
   <div class="bar" style="margin:18px 0 20px"><i style="width:43%"></i></div><a class="btn" href="weave-entries.html">Continue lesson</a></div></div>
 <div class="acts">
  <div class="card act"><div><b>Send this week's video</b><small>Guided: 1 feedback video a week</small></div><a class="btn pink sm" href="#" data-demo="Opens your feedback video form">Upload</a></div>
  <div class="card act"><div><b>Training Days, early access</b><small>Members book first</small></div><a class="btn ghost sm" href="#" data-demo="Opens Training Days booking (Amelia)">Book</a></div>
  <div class="card act"><div><b>My bookings and membership</b><small>Change plan, invoices, sessions</small></div><a class="btn ghost sm" href="#" data-demo="Opens the SureCart customer dashboard">Manage</a></div>
 </div>
</div>
<h2 class="sec" id="skills">Your skills</h2>
<div class="tiles">{tiles}</div>
<h2 class="sec">More for members</h2>
<div class="more">{more}</div></div>'''
    band = '<h1>Welcome back, Sam <span class="chip">GUIDED MEMBER</span></h1><p>Pip has finished 34 lessons so far. Keep going!</p>'
    return a_shell('index', 'Members home', band, body)

def a_skill():
    st = {'done': ('s-done', '✓ Done'), 'progress': ('s-progress', 'In progress'), 'todo': ('s-todo', 'Not started')}
    cards = ''.join(
        f'<a class="card" href="{"weave-entries.html" if n == "Weave Entries" else "#"}" data-state="{s}"{"" if n == "Weave Entries" else " data-demo=" + chr(34) + "This preview has the Weave Entries lesson built. Every lesson gets the same page." + chr(34)}>'
        f'<span class="thumb" style="aspect-ratio:16/9"><img src="{img(t)}" alt="" loading="lazy"><span class="play"><i></i></span><span class="num">{i}</span></span>'
        f'<div class="tx"><div style="font-weight:700;font-size:16px">{e(n)}</div><div class="meta"><span class="muted">{vids_label(c)}</span><span class="{st[s][0]}">{st[s][1]}</span></div></div></a>'
        for i, (n, c, t, s) in enumerate(WEAVES, 1))
    body = f'''<div class="w"><div class="tools">
<div class="muted" style="font-size:15px">Work through the lessons in order, or jump to the one you need.</div>
<div class="filt"><button class="on" data-filter="all">All</button><button data-filter="todo">Not done</button><button data-filter="done">Done</button></div></div>
<div class="lessons">{cards}</div></div>'''
    band = (f'<div class="skill-head"><img src="{img("weaves")}" alt="Weaves">'
            '<div><div class="crumb"><a href="index.html">Members Home</a> › Skills › Weaves</div><h1>Weaves</h1><p>7 lessons · 33+ videos</p>'
            '<div class="prog"><div class="bar" style="width:260px;background:rgba(255,255,255,.3)"><i style="width:43%;background:#fff"></i></div><span style="font-size:14px;font-weight:600">3 of 7 done</span></div></div></div>')
    return a_shell('weaves', 'Weaves', band, body)

def a_lesson():
    pl = ''.join(
        f'<button class="part{" watched" if i < 2 else ""}{" current" if i == 2 else ""}" data-part data-title="{e(n)}" data-thumb="{img(t)}">'
        f'<span class="thumb"><img src="{img(t)}" alt="" loading="lazy"></span><span><b>{e(n)}</b><span class="st"></span></span></button>'
        for i, (n, t) in enumerate(VIDS))
    body = f'''<div class="w"><div class="lesson">
<div><div class="card" style="overflow:hidden"><a class="thumb player" href="#" data-demo="{PLAY}"><img id="pl-thumb" src="{img('yt_k_3itnoujyc')}" alt=""><span class="play lg"><i></i></span></a>
<div class="ph"><div><div class="muted" style="font-size:13px" id="pl-num">Part 3 of 7</div><h2 id="pl-title">Weave Entries Part 3</h2></div>
<div class="navbtns"><a class="btn ghost" href="#" id="pl-prev">‹ Part 2</a><a class="btn" href="#" id="pl-next">Part 4 ›</a></div></div></div>
<div class="card notes"><div style="font-weight:700;font-size:17px;margin-bottom:8px">Lesson notes</div>
<p>Space for a short write-up from Iain or Livvi under each lesson: the set-up, what to reward, and the common mistakes to watch for. Members can also download a printable plan here.</p>
<div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap"><a class="btn ghost sm" href="#" data-demo="Downloads the session plan PDF">⬇ Session plan (PDF)</a><a class="btn ghost sm" href="#" data-demo="Saved to My saved lessons">♡ Save lesson</a></div></div></div>
<div><div class="card pl"><div class="pl-h">In this lesson<span class="muted" style="font-weight:500;font-size:13px" id="pl-count">2 of 7 watched</span></div>{pl}</div>
<div class="card fin"><div style="font-weight:700">Finished this lesson?</div><div class="muted" style="font-size:13px;margin-top:4px">Mark it done to track Pip's progress</div><a class="btn green" href="#" id="pl-done">✓ Mark lesson as done</a>
<div class="muted" style="font-size:13px;margin-top:12px">Next lesson: <b style="color:var(--ink)">Weave Entries on full set</b></div></div></div>
</div></div>'''
    band = '<div class="crumb"><a href="index.html">Members Home</a> › <a href="weaves.html">Weaves</a></div><h1>Weave Entries</h1><p>Weaves · 7 videos</p>'
    return a_shell('weave-entries', 'Weave Entries', band, body)

def add_form(dark=False):
    skills = ''.join(f'<option{" selected" if n == "Weaves" else ""}>{n}</option>' for n, *_ in SKILLS) + '<option>Course Plans</option><option>Wednesday Classes</option>'
    return f'''<form id="add-lesson" class="{"panel" if dark else "card"} form" novalidate>
<h2>Add a new lesson</h2><div class="muted" style="font-size:14px">Fill this in and the lesson appears in the members area with the new design. No page builder needed.</div>
<div class="fld"><label for="f-skill">Which skill is it for?</label><select id="f-skill" name="skill">{skills}</select></div>
<div class="fld"><label for="f-title">Lesson title</label><input id="f-title" type="text" name="title" placeholder="e.g. Weave Entries on full set"></div>
<div class="fld"><span class="lab">Videos</span><div id="vid-rows"></div>
<button class="btn {"g" if dark else "ghost"} sm" id="add-vid" type="button">+ Add another video</button>
<small>Paste the YouTube link. The thumbnail and video player are added for you.</small></div>
<div class="fld"><label for="f-notes">Lesson notes (optional)</label><textarea id="f-notes" name="notes" placeholder="Set-up, what to reward, common mistakes..."></textarea></div>
<div class="fld"><span class="lab">Session plan PDF (optional)</span><label class="file"><input type="file" accept="application/pdf" style="display:none">Choose a PDF</label></div>
<div class="fld"><span class="lab">Who can see it?</span><div class="checks"><label><input type="checkbox" checked> Online</label><label><input type="checkbox" checked> Guided</label><label><input type="checkbox" checked> Coached</label></div></div>
<div class="go"><button class="btn" type="submit">Publish lesson</button><a class="btn {"g" if dark else "ghost"}" href="#" data-demo="Saved as a draft. Only admins can see it.">Save as draft</a></div>
<div class="done-msg" id="done-msg" hidden>✓ <b id="done-title"></b> has been added to <b id="done-skill"></b>. Members will see it straight away. <span style="opacity:.75">(Demo only, nothing was saved.)</span></div>
</form>
<template id="vid-row-tpl"><div class="vid-row"><div class="vid-top"><span><span class="vid-n">Video 1</span><span class="vid-ok"></span></span><a href="#" class="vid-x">Remove</a></div>
<div class="two"><input type="url" name="url" placeholder="YouTube link"><input type="text" name="vtitle" placeholder="Part title (optional)"></div></div></template>'''

def a_add():
    body = f'''<div class="w"><div class="add">{add_form()}
<div class="preview"><div style="font-weight:700;margin-bottom:10px">How it will look</div>
<div class="card" style="overflow:hidden"><div class="pv-thumb"><img id="pv-thumb" alt=""><span>Paste a YouTube link to see the thumbnail</span></div>
<div style="padding:16px 18px"><div style="font-weight:700;font-size:16px" id="pv-title">Your new lesson</div>
<div style="display:flex;justify-content:space-between;margin-top:8px;font-size:13px"><span class="muted"><span id="pv-skill">Weaves</span> · <span id="pv-count">1 video</span></span><span class="s-todo">Not started</span></div></div></div>
<div class="muted" style="font-size:13px;margin-top:12px">Try it: paste any YouTube link into the Videos box.</div></div>
</div></div>'''
    band = '<div class="crumb">Admin</div><h1>Add a lesson</h1><p>Only Iain and Livvi see this page.</p>'
    return a_shell('add-lesson', 'Add a lesson', band, body)

# ======================================================================= OPTION B
B_CSS = '''
body{background:#0f0f13;color:#f2f2f5}
.app{display:grid;grid-template-columns:250px minmax(0,1fr);min-height:100vh}
.side{background:#17171d;padding:24px 18px;display:flex;flex-direction:column;gap:4px;border-right:1px solid #24242c;position:sticky;top:0;height:100vh;overflow-y:auto}
.side .logo{height:64px;width:auto;margin:0 0 24px 6px;background:#fff;border-radius:10px;padding:4px 8px;align-self:flex-start}
.side a{display:flex;gap:12px;align-items:center;padding:11px 14px;border-radius:10px;font-size:14px;font-weight:500;color:#b9b9c4;transition:.15s}
.side a:hover{background:#202028;color:#fff}
.side a.on{background:linear-gradient(90deg,rgba(190,66,225,.35),rgba(226,69,122,.15));color:#fff;font-weight:600}
.side a i{width:18px;height:18px;border-radius:5px;border:2px solid currentColor;opacity:.8;flex:none}
.side .sep{height:1px;background:#26262f;margin:10px 4px}
.adm{font-size:10px;font-weight:700;background:#2c2236;color:#d79bf0;padding:2px 6px;border-radius:5px;margin-left:auto}
.tier{margin-top:auto;background:#22222b;border-radius:14px;padding:16px}
.main{padding:30px 40px 60px;min-width:0}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:26px;gap:16px}
.mtop{display:none}
.big{font-family:Anton,sans-serif;font-size:clamp(34px,5vw,52px);letter-spacing:.01em;line-height:1.05;text-transform:uppercase}
.grad{background:linear-gradient(90deg,#ff6b2c,#e2457a,#be42e1,#4fc3f7);-webkit-background-clip:text;background-clip:text;color:transparent}
.panel{background:#1a1a21;border:1px solid #26262f;border-radius:18px}
a.panel{transition:transform .2s,border-color .2s}a.panel:hover{transform:translateY(-3px);border-color:#3a3a46}
.btn{display:inline-block;background:linear-gradient(90deg,#ff6b2c,#e2457a);color:#fff;font-weight:600;font-size:14px;padding:11px 22px;border-radius:10px;text-align:center;transition:filter .2s}
.btn:hover{filter:brightness(1.1)}
.btn.g{background:#2a2a33}.btn.lime{background:#b5d043;color:#111}
.btn.sm{padding:8px 14px;font-size:13px}
.lbl{font-size:12px;font-weight:700;letter-spacing:.1em;color:#9a9aa8;text-transform:uppercase}
.muted{color:#9a9aa8}
.ring{--p:50;width:58px;height:58px;border-radius:50%;background:conic-gradient(#b5d043 calc(var(--p)*1%),#2c2c36 0);display:grid;place-items:center;flex:none;transition:background .4s}
.ring b{width:76%;height:76%;border-radius:50%;background:#1a1a21;display:grid;place-items:center;font-size:12px}
.me{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:600}.me i{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#be42e1,#ff6b2c)}
.tabs{display:none}
/* hub */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.stat{padding:18px 20px}.stat .v{font-size:30px;font-weight:800;margin-top:6px;line-height:1.2}
.duo{display:grid;grid-template-columns:1.5fr 1fr;gap:18px;margin-top:18px}
.focus{overflow:hidden;display:grid;grid-template-columns:1.1fr 1fr}
.focus .thumb{min-height:260px}
.track{height:8px;background:#2c2c36;border-radius:99px;margin:18px 0 22px}.track i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,#ff6b2c,#be42e1)}
.pill{background:#b5d043;color:#111;font-weight:700;font-size:11px;padding:3px 9px;border-radius:99px}
.rail{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.rail a{overflow:hidden}.rail img{width:100%;aspect-ratio:1;object-fit:cover}
.rail .tx{padding:14px 16px;display:flex;justify-content:space-between;align-items:center;gap:8px}
.sec{display:flex;justify-content:space-between;align-items:end;margin:34px 0 16px}
/* skill */
.shead{display:grid;grid-template-columns:220px 1fr auto;gap:30px;align-items:center;padding:22px;margin-bottom:30px;background:linear-gradient(120deg,#2a1633,#1a1a21 60%)}
.shead>img{width:220px;height:220px;border-radius:14px;object-fit:cover}
.shead .ring{width:120px;height:120px;margin-right:20px}.shead .ring b{font-size:22px;font-weight:800}
.btns{display:flex;gap:10px;margin-top:20px;flex-wrap:wrap}
.filt{display:flex;gap:8px;margin-bottom:20px}
.filt button{padding:8px 16px;border-radius:10px;font-size:13px;font-weight:600;background:#22222b;color:#b9b9c4}
.filt button.on{background:#f2f2f5;color:#111}
.path{max-width:980px}
.step{display:grid;grid-template-columns:54px minmax(0,1fr);gap:18px}
.step .dot{display:flex;flex-direction:column;align-items:center}
.step .dot b{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-weight:800;background:#3a3a46}
.step[data-state=done] .dot b{background:#b5d043;color:#111}.step[data-state=progress] .dot b{background:#e2457a}
.step .line{flex:1;width:3px;background:#2c2c36;margin:4px 0}
.step:last-child .line{display:none}
.step .panel{display:flex;gap:18px;align-items:center;padding:12px;margin-bottom:14px}
.step[data-state=progress] .panel{border-color:#e2457a}
.step .thumb{width:170px;height:96px;border-radius:10px;flex:none}
.step .play i{width:40px;height:40px}.step .play i:after{border-left-width:13px;border-top-width:8px;border-bottom-width:8px;margin-left:3px}
.step .tx{flex:1;min-width:0}
.step .btn{margin-right:10px;flex:none}
/* lesson */
.lesson{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:22px}
.player{aspect-ratio:16/9;border-radius:18px}
.lh{display:flex;justify-content:space-between;align-items:center;margin:20px 0;gap:16px;flex-wrap:wrap}
.lh h1{font-size:26px;font-weight:700;margin-top:4px;line-height:1.25}
.chips{display:flex;gap:14px;overflow-x:auto;padding:4px 4px 10px;scrollbar-width:thin}
.part{flex:none;width:200px;text-align:left}
.part .thumb{height:112px;border-radius:10px}
.part.current .thumb{outline:3px solid #e2457a;outline-offset:2px}
.part .tick{display:none;position:absolute;top:8px;left:8px;background:#b5d043;color:#111;font-size:11px;font-weight:800;padding:2px 8px;border-radius:99px}
.part.watched .tick{display:block}
.part b{display:block;font-size:13px;font-weight:600;margin-top:8px}
.part .st{font-size:12px;color:#9a9aa8}.part.current .st{color:#e2457a}.part.watched .st{color:#b5d043}
.aside{display:grid;gap:18px;align-content:start}
.aside .panel{padding:20px}
.drop{color:#3a3a46;margin-top:14px}.drop .drop-msg{color:#9a9aa8}.drop .drop-msg b{color:#fff}
.drop:hover,.drop.over{color:#e2457a}.drop.has-file{color:#b5d043}
/* add lesson */
.add{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:22px;align-items:start}
.form{padding:26px 28px}
.form h2{font-size:19px;margin-bottom:4px}
.fld{margin-top:18px}
.fld label,.lab{display:block;font-weight:600;font-size:14px;margin-bottom:6px}
.fld small{display:block;color:#9a9aa8;font-size:12px;margin-top:6px}
input[type=text],input[type=url],select,textarea{width:100%;font:inherit;font-size:14px;padding:11px 14px;border:1.5px solid #30303a;border-radius:10px;background:#121217;color:#f2f2f5}
input::placeholder,textarea::placeholder{color:#6a6a76}
input:focus,select:focus,textarea:focus{outline:none;border-color:#e2457a;box-shadow:0 0 0 3px rgba(226,69,122,.2)}
textarea{min-height:110px;resize:vertical}
.vid-row{background:#15151b;border:1px solid #2a2a33;border-radius:12px;padding:14px;margin-bottom:10px}
.vid-top{display:flex;justify-content:space-between;align-items:center;font-size:13px;font-weight:700;margin-bottom:8px}
.vid-ok{color:#b5d043;margin-left:8px}.vid-x{color:#9a9aa8;font-size:13px}
.vid-row .two{display:grid;grid-template-columns:1.3fr 1fr;gap:10px}
.checks{display:flex;gap:18px;flex-wrap:wrap;font-size:14px}.checks label{display:flex;gap:6px;align-items:center;font-weight:500}
.checks input{accent-color:#e2457a;width:17px;height:17px}
.file{display:block;border:1.5px dashed #3a3a46;border-radius:10px;padding:14px;font-size:13px;color:#9a9aa8;text-align:center;cursor:pointer}
.go{display:flex;gap:10px;margin-top:24px;flex-wrap:wrap}
.preview{position:sticky;top:20px}
.preview .pv-thumb{background:#22222b;color:#9a9aa8;border-radius:18px 18px 0 0}
.done-msg{margin-top:18px;padding:16px 18px;border-radius:12px;background:#24301a;color:#cfe68a;font-size:14px}
@media (max-width:1180px){.stats,.rail{grid-template-columns:repeat(2,1fr)}.duo,.lesson,.add{grid-template-columns:1fr}.preview{position:static}}
@media (max-width:900px){
 .app{display:block}
 .side{display:none}
 .main{padding:16px 16px 96px}
 .top{display:none}
 .mtop{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
 .mtop .logo{height:42px;width:auto;background:#fff;border-radius:8px;padding:3px 6px}
 .tabs{display:flex;position:fixed;left:0;right:0;bottom:0;background:#17171d;border-top:1px solid #26262f;justify-content:space-around;padding:10px 0 calc(10px + env(safe-area-inset-bottom));z-index:40}
 .tabs a{font-size:11px;color:#9a9aa8;display:flex;flex-direction:column;align-items:center;gap:4px}
 .tabs a i{width:20px;height:20px;border-radius:6px;border:2px solid currentColor}
 .tabs a.on{color:#fff;font-weight:700}
 .toast{bottom:84px}
 .shead{grid-template-columns:1fr;text-align:left;gap:16px}
 .shead>img{width:120px;height:120px}
 .shead .ring{display:none}
}
@media (max-width:620px){
 .stats{gap:12px}.stat{padding:14px}.stat .v{font-size:22px}
 .focus{grid-template-columns:1fr}.focus .thumb{min-height:0;aspect-ratio:16/9}
 .rail{gap:12px}.rail .tx{padding:10px 12px}.rail .ring{width:44px;height:44px}.rail .ring b{font-size:10px}
 .step{grid-template-columns:34px minmax(0,1fr);gap:10px}.step .dot b{width:30px;height:30px;font-size:13px}
 .step .panel{flex-wrap:wrap;gap:12px}.step .thumb{width:100%;height:auto;aspect-ratio:16/9}.step .btn{margin:0;width:100%}
 .part{width:150px}.part .thumb{height:84px}
 .lh h1{font-size:21px}.lh .btns{width:100%;margin:0}.lh .btns .btn{flex:1}
 .form{padding:20px}.vid-row .two{grid-template-columns:1fr}
}
'''
B_NAV = [('index.html', 'Home', ('index',)), ('index.html#skills', 'Skills', ('weaves', 'weave-entries')), ('#', 'Course Plans', ()),
         ('#', 'Wednesday Classes', ()), ('#', 'Training Days', ()), ('#', 'My Feedback', ()), ('#', 'My Membership', ())]

def b_shell(pg, title, crumb, main):
    nav = ''.join(f'<a href="{h}" class="{"on" if pg in pgs else ""}"{" data-demo=" + chr(34) + NOTBUILT + chr(34) if h == "#" else ""}><i></i>{t}</a>' for h, t, pgs in B_NAV)
    nav += f'<div class="sep"></div><a href="add-lesson.html" class="{"on" if pg == "add-lesson" else ""}"><i></i>Add a lesson<span class="adm">ADMIN</span></a>'
    tabs = [('index.html', 'Home', pg == 'index'), ('weaves.html', 'Skills', pg in ('weaves', 'weave-entries')), ('#', 'Plans', False), ('#', 'Feedback', False), ('add-lesson.html', 'Admin', pg == 'add-lesson')]
    tabs = ''.join(f'<a href="{h}" class="{"on" if on else ""}"{" data-demo=" + chr(34) + NOTBUILT + chr(34) if h == "#" else ""}><i></i>{t}</a>' for h, t, on in tabs)
    body = (f'<div class="app"><aside class="side"><a href="index.html" style="padding:0;background:none"><img class="logo" src="../img/logo.png" alt="BarkZone Agility"></a>{nav}'
            '<div class="tier"><div class="lbl" style="color:#b5d043">Guided member</div><div style="font-size:13px;color:#b9b9c4;margin:6px 0 12px">1 feedback video a week. Upgrade to Coached for 1:1 support.</div>'
            '<a class="btn g sm" href="#" data-demo="Opens the SureCart customer dashboard">Manage plan</a></div></aside>'
            f'<main class="main"><div class="mtop"><a href="index.html"><img class="logo" src="../img/logo.png" alt="BarkZone Agility"></a><div class="me"><i style="width:34px;height:34px"></i></div></div>'
            f'<div class="top"><div class="lbl">{crumb}</div><div class="me"><i></i>Sam</div></div>{main}</main></div><nav class="tabs">{tabs}</nav>')
    return page('b', pg, title, body)

def b_hub():
    rail = ''.join(
        f'<a class="panel" href="{"weaves.html" if n == "Weaves" else "#"}"{"" if n == "Weaves" else f" data-demo={chr(34)}{OTHER}{chr(34)}"}>'
        f'<img src="{img(i)}" alt="{n}" loading="lazy"><div class="tx"><div><div style="font-weight:700">{n}</div><div class="muted" style="font-size:12px">{d} of {l} lesson{"s" if l != 1 else ""}</div></div>'
        f'<div class="ring" style="--p:{int(100 * d / l)}"><b>{int(100 * d / l)}%</b></div></div></a>'
        for n, i, l, d in SKILLS)
    stats = ''.join(f'<div class="panel stat"><div class="lbl">{a}</div><div class="v">{b}</div><div class="muted" style="font-size:13px">{c}</div></div>'
                    for a, b, c in [('Lessons done', '34', 'of 57 in the library'), ('Training streak', '5 weeks', 'keep it going'), ('Feedback video', '1 left', 'this week (Guided)'), ('Next training day', 'Sat 22 Nov', 'early access open')])
    main = f'''<div style="margin-bottom:24px"><div class="big">Welcome back, <span class="grad">Sam &amp; Pip</span></div></div>
<div class="stats">{stats}</div>
<div class="duo">
 <div class="panel focus"><a class="thumb" href="weave-entries.html"><img src="{img('yt_k_3itnoujyc')}" alt=""><span class="play"><i></i></span></a>
  <div style="padding:24px"><div class="lbl" style="color:#e2457a">This week's focus · set by Iain</div><div style="font-size:24px;font-weight:700;margin:8px 0 4px">Weave Entries</div><div class="muted" style="font-size:14px">Part 3 of 7 · Weaves</div>
  <div class="track"><i style="width:43%"></i></div><a class="btn" href="weave-entries.html">Continue</a></div></div>
 <div class="panel" style="padding:22px"><div style="display:flex;justify-content:space-between;align-items:center"><div class="lbl">My feedback</div><span class="pill">NEW REPLY</span></div>
  <div style="display:flex;gap:14px;margin:16px 0;align-items:center"><span class="thumb" style="width:120px;height:68px;border-radius:8px;flex:none"><img src="{img('yt_jdhagjetawy')}" alt=""></span><div style="font-size:14px"><b>Weave entry, left side</b><div class="muted" style="font-size:13px">Sent Monday · Iain replied</div></div></div>
  <div style="background:#22222b;border-radius:12px;padding:14px;font-size:13px;color:#c9c9d2;line-height:1.6">“Lovely drive into the entry. Next session, try the same from the right side and reward the moment he finds the gap.” <span class="muted">Iain</span></div>
  <a class="btn" style="display:block;margin-top:16px" href="weave-entries.html#upload">Upload this week's video</a></div>
</div>
<div class="sec" id="skills"><div class="big" style="font-size:34px">Your skills</div><span class="muted" style="font-size:14px">8 skills · 57 lessons</span></div>
<div class="rail">{rail}</div>'''
    return b_shell('index', 'Members home', 'Members home', main)

def b_skill():
    steps = ''.join(
        f'<div class="step" data-state="{s}"><div class="dot"><b>{"✓" if s == "done" else ("▶" if s == "progress" else i)}</b><div class="line"></div></div>'
        f'<div class="panel"><a class="thumb" href="{"weave-entries.html" if n == "Weave Entries" else "#"}"{"" if n == "Weave Entries" else " data-demo=" + chr(34) + "This preview has the Weave Entries lesson built. Every lesson gets the same page." + chr(34)}><img src="{img(t)}" alt="" loading="lazy"><span class="play"><i></i></span></a>'
        f'<div class="tx"><div class="lbl">Step {i}</div><div style="font-size:18px;font-weight:700;margin-top:2px">{e(n)}</div><div class="muted" style="font-size:13px;margin-top:2px">{vids_label(c)}</div></div>'
        f'<a class="btn {"" if s == "progress" else "g"}" href="{"weave-entries.html" if n == "Weave Entries" else "#"}"{"" if n == "Weave Entries" else " data-demo=" + chr(34) + "This preview has the Weave Entries lesson built. Every lesson gets the same page." + chr(34)}>{"Continue" if s == "progress" else ("Watch again" if s == "done" else "Start")}</a></div></div>'
        for i, (n, c, t, s) in enumerate(WEAVES, 1))
    main = f'''<div class="panel shead"><img src="{img('weaves')}" alt="Weaves">
<div><div class="big">Weaves</div><div style="color:#c9c9d2;margin-top:10px;font-size:15px">7 lessons · 33+ videos · follow the path from top to bottom</div>
<div class="btns"><a class="btn" href="weave-entries.html">Continue: Weave Entries</a><a class="btn g" href="weave-entries.html#upload">Send a weaves clip for feedback</a></div></div>
<div class="ring" style="--p:43"><b>3/7</b></div></div>
<div class="filt"><button class="on" data-filter="all">All</button><button data-filter="todo">Not done</button><button data-filter="done">Done</button></div>
<div class="path">{steps}</div>'''
    return b_shell('weaves', 'Weaves', '<a href="index.html">Skills</a> › Weaves', main)

def b_lesson():
    chips = ''.join(
        f'<button class="part{" watched" if i < 2 else ""}{" current" if i == 2 else ""}" data-part data-title="{e(n)}" data-thumb="{img(t)}">'
        f'<span class="thumb"><img src="{img(t)}" alt="" loading="lazy"><span class="tick">✓</span></span><b>{i + 1}. {e(n)}</b><span class="st"></span></button>'
        for i, (n, t) in enumerate(VIDS))
    main = f'''<div class="lesson">
<div style="min-width:0"><a class="thumb player" href="#" data-demo="{PLAY}"><img id="pl-thumb" src="{img('yt_k_3itnoujyc')}" alt=""><span class="play lg"><i></i></span></a>
<div class="lh"><div><div class="lbl" id="pl-num">Part 3 of 7</div><h1 id="pl-title">Weave Entries Part 3</h1></div>
<div class="btns" style="margin:0"><a class="btn g" href="#" id="pl-prev">‹ Part 2</a><a class="btn" href="#" id="pl-next">Part 4 ›</a></div></div>
<div class="lbl" style="margin-bottom:10px">All parts in this lesson</div>
<div class="chips">{chips}</div></div>
<div class="aside">
<div class="panel" id="upload"><div class="lbl" style="color:#b5d043">Your turn</div><div style="font-weight:700;font-size:17px;margin:6px 0 6px">Film your attempt</div><div class="muted" style="font-size:13px;line-height:1.6">Upload a short clip of this exercise and Iain or Livvi will reply with feedback. Guided: 1 a week. Coached: unlimited.</div>
<label class="drop" data-drop><input type="file" accept="video/*"><span class="drop-msg">Drop a video here<br><b>or choose from your phone</b></span></label>
<a class="btn" href="#" style="display:block;margin-top:12px" data-send hidden>Send for feedback</a></div>
<div class="panel"><div class="lbl">Coach notes</div><div style="color:#c9c9d2;font-size:13px;line-height:1.7;margin-top:8px">Short written notes from Iain under each lesson: set-up, what to reward and common mistakes, with a printable session plan.</div><a class="btn g sm" style="margin-top:14px" href="#" data-demo="Downloads the session plan PDF">⬇ Session plan</a></div>
<div class="panel" style="text-align:center"><div class="ring" id="pl-ring" style="--p:28;margin:0 auto 10px;width:74px;height:74px"><b>2/7</b></div><div class="muted" style="font-size:13px;margin-bottom:12px" id="pl-count">2 of 7 watched</div><a class="btn lime" style="display:block" href="#" id="pl-mark">✓ Mark part 3 as watched</a></div>
</div></div>'''
    return b_shell('weave-entries', 'Weave Entries', '<a href="index.html">Skills</a> › <a href="weaves.html">Weaves</a> › Weave Entries', main)

def b_add():
    main = f'''<div style="margin-bottom:24px"><div class="lbl">Admin · only Iain and Livvi see this</div><div class="big" style="margin-top:6px;font-size:clamp(30px,4vw,42px)">Add a lesson</div></div>
<div class="add">{add_form(dark=True)}
<div class="preview"><div class="lbl" style="margin-bottom:10px">How it will look</div>
<div class="panel" style="overflow:hidden"><div class="pv-thumb"><img id="pv-thumb" alt=""><span>Paste a YouTube link to see the thumbnail</span></div>
<div style="padding:16px 18px"><div class="lbl" id="pv-skill">Weaves</div><div style="font-size:18px;font-weight:700;margin-top:2px" id="pv-title">Your new lesson</div><div class="muted" style="font-size:13px;margin-top:2px" id="pv-count">1 video</div></div></div>
<div class="muted" style="font-size:13px;margin-top:12px">Try it: paste any YouTube link into the Videos box.</div></div></div>'''
    return b_shell('add-lesson', 'Add a lesson', 'Admin', main)

# ======================================================================= landing
def landing():
    card = lambda o, t, d, href: f'''<a class="opt" href="{href}"><img src="img/preview-{o}-hub.jpg" alt="Option {o.upper()} preview"><div class="ot"><div class="k">Option {o.upper()}</div><h2>{t}</h2><p>{d}</p><span>Open Option {o.upper()} ›</span></div></a>'''
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>BarkZone members area preview</title>{FONTS}<link rel="stylesheet" href="assets/demo.css">
<style>body{{background:#f7f5f9;color:var(--ink)}}.w{{max-width:1120px;margin:0 auto;padding:48px 24px 64px}}
.hd{{display:flex;align-items:center;gap:20px}}.hd img{{height:72px}}h1{{font-size:clamp(28px,4vw,40px);line-height:1.15;margin-top:28px}}
.lead{{color:var(--muted);font-size:17px;max-width:680px;margin-top:10px}}
.opts{{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:36px}}
.opt{{background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 20px rgba(40,10,60,.08);transition:transform .2s,box-shadow .2s}}
.opt:hover{{transform:translateY(-4px);box-shadow:0 12px 32px rgba(40,10,60,.14)}}
.opt img{{width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top;border-bottom:1px solid #eee}}
.ot{{padding:22px 24px 26px}}.k{{font-size:12px;font-weight:700;letter-spacing:.1em;color:var(--pink)}}.ot h2{{font-size:22px;margin:4px 0 6px}}.ot p{{color:var(--muted);font-size:14px}}
.ot span{{display:inline-block;margin-top:16px;background:var(--orange);color:#fff;font-weight:600;font-size:14px;padding:10px 20px;border-radius:10px}}
.pages{{margin-top:36px;background:#fff;border-radius:16px;padding:22px 24px;font-size:14px;color:var(--muted)}}.pages b{{color:var(--ink)}}
.foot{{margin-top:40px;display:flex;align-items:center;gap:12px;font-size:13px;color:var(--muted)}}.foot img{{height:28px}}
@media (max-width:760px){{.opts{{grid-template-columns:1fr}}.w{{padding:28px 16px 48px}}.hd img{{height:56px}}}}</style></head><body><div class="w">
<div class="hd"><img src="img/logo.png" alt="BarkZone Agility"></div>
<h1>A new look for your members area</h1>
<p class="lead">Two working previews for Iain and Livvi. Click around each one: the members home, a skill page, a lesson page and the new "Add a lesson" form. Both work on phones too.</p>
<div class="opts">{card("a", "Your look, refined", "Light pages in your purple, orange and lime. Familiar for members, with progress tracking and proper lesson pages.", "a/index.html")}
{card("b", "The Training Zone", "A bold, dark training hub with side menu, progress rings, this week's focus and a feedback video upload on every lesson.", "b/index.html")}</div>
<div class="pages"><b>In each preview:</b> Members home · Weaves skill page · Weave Entries lesson page · Add a lesson (admin). Other skills and pages are not built in the preview but get the same design in the real build. Videos don't play in the preview.</div>
<div class="foot"><img src="img/bbm-logo.png" alt="">Preview by Big Bark Media</div>
</div></body></html>'''

if __name__ == '__main__':
    open(os.path.join(R, 'a', 'a.css'), 'w').write(A_CSS)
    open(os.path.join(R, 'b', 'b.css'), 'w').write(B_CSS)
    out = {'index.html': landing(),
           'a/index.html': a_hub(), 'a/weaves.html': a_skill(), 'a/weave-entries.html': a_lesson(), 'a/add-lesson.html': a_add(),
           'b/index.html': b_hub(), 'b/weaves.html': b_skill(), 'b/weave-entries.html': b_lesson(), 'b/add-lesson.html': b_add()}
    for p, h in out.items():
        open(os.path.join(R, p), 'w').write(h)
        print('wrote', p)
