#!/usr/bin/env python3
"""Build a self-contained index.html from the guide's markdown files.

No dependencies. Reads the markdown, embeds it, and renders in-browser with
marked.js. Re-run after editing any .md file:  python3 site/build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "index.html"

# (path relative to guide root, sidebar label, section)
PAGES = [
    ("00-start-here.md", "Start here", "Guide"),
    ("01-cowork.md", "1 · Claude Cowork", "Guide"),
    ("02-claude-code.md", "2 · Claude Code", "Guide"),
    ("03-power-ups.md", "3 · Power-ups", "Guide"),
    ("04-now-what.md", "Now what", "Guide"),
    ("decisions/account.md", "Account & tier", "Decisions"),
    ("decisions/which-model.md", "Which model", "Decisions"),
    ("decisions/dictation.md", "Talking to Claude", "Decisions"),
    ("decisions/trust-and-permissions.md", "Trust & permissions", "Decisions"),
    ("decisions/connectors.md", "Which connectors", "Decisions"),
    ("decisions/cowork-vs-code.md", "Cowork vs Code", "Decisions"),
    ("decisions/interface.md", "How to run Code", "Decisions"),
    ("decisions/workspace-access.md", "Workspace access", "Decisions"),
]

content = {}
for rel, _, _ in PAGES:
    content[rel] = (ROOT / rel).read_text(encoding="utf-8")

nav = {}
for rel, label, section in PAGES:
    nav.setdefault(section, []).append({"path": rel, "label": label})

DATA = json.dumps({"content": content, "nav": nav}, ensure_ascii=False)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Claude On-Ramp</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  :root {
    --bg: #faf9f7; --fg: #201d1a; --muted: #6b645c; --line: #e7e2db;
    --accent: #b8532a; --card: #fff; --code: #f2efe9;
  }
  @media (prefers-color-scheme: dark) {
    :root { --bg:#1a1817; --fg:#e9e4dd; --muted:#a49b90; --line:#333029;
            --accent:#e07850; --card:#221f1d; --code:#2a2723; }
  }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--fg);
    font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; }
  .app { display:grid; grid-template-columns:250px minmax(0,1fr) 320px;
    min-height:100vh; }
  nav { border-right:1px solid var(--line); padding:24px 18px; position:sticky;
    top:0; height:100vh; overflow:auto; }
  nav h1 { font-size:15px; letter-spacing:.02em; margin:0 0 20px; }
  nav .sec { font-size:11px; text-transform:uppercase; letter-spacing:.08em;
    color:var(--muted); margin:22px 0 8px; }
  nav a { display:block; padding:5px 8px; margin:1px 0; border-radius:6px;
    color:var(--fg); text-decoration:none; font-size:14px; }
  nav a:hover { background:var(--code); }
  nav a.active { background:var(--accent); color:#fff; }
  main { padding:56px 64px; max-width:760px; }
  main h1 { font-size:30px; line-height:1.2; margin:0 0 24px; }
  main h2 { font-size:21px; margin:38px 0 12px; }
  main h3 { font-size:17px; margin:26px 0 8px; }
  main a { color:var(--accent); }
  main code { background:var(--code); padding:1px 6px; border-radius:5px;
    font-size:.9em; }
  main pre { background:var(--code); padding:14px 16px; border-radius:10px;
    overflow:auto; }
  main pre code { background:none; padding:0; }
  main table { border-collapse:collapse; width:100%; margin:16px 0; font-size:14px; }
  main th,main td { border:1px solid var(--line); padding:7px 10px; text-align:left; }
  main blockquote { border-left:3px solid var(--accent); margin:16px 0;
    padding:2px 18px; color:var(--muted); }
  details { background:var(--card); border:1px solid var(--line);
    border-radius:10px; padding:2px 16px; margin:14px 0; }
  details summary { cursor:pointer; padding:10px 0; font-weight:600;
    color:var(--accent); }
  details[open] summary { border-bottom:1px solid var(--line); margin-bottom:10px; }
  aside { border-left:1px solid var(--line); padding:24px 20px; position:sticky;
    top:0; height:100vh; display:flex; flex-direction:column; }
  aside h2 { font-size:14px; margin:0 0 4px; }
  aside .sub { font-size:12px; color:var(--muted); margin-bottom:14px; }
  .chat { flex:1; overflow:auto; background:var(--card); border:1px solid var(--line);
    border-radius:10px; padding:14px; font-size:13px; color:var(--muted); }
  .compose { margin-top:12px; display:flex; gap:8px; }
  .compose input { flex:1; padding:9px 11px; border:1px solid var(--line);
    border-radius:8px; background:var(--bg); color:var(--fg); font-size:13px; }
  .compose button { padding:9px 12px; border:none; border-radius:8px;
    background:var(--accent); color:#fff; font-size:13px; cursor:pointer; }
  .stub { font-size:11px; color:var(--muted); margin-top:10px; line-height:1.5; }
  .didntwork { margin:40px 0 0; padding-top:16px; border-top:1px solid var(--line);
    font-size:13px; color:var(--muted); }
  .didntwork button { background:none; border:1px solid var(--line);
    color:var(--muted); border-radius:20px; padding:5px 12px; cursor:pointer;
    font-size:12px; }
  @media (max-width:1100px){ .app{grid-template-columns:220px 1fr;} aside{display:none;} }
  @media (max-width:720px){ .app{grid-template-columns:1fr;} nav{display:none;} main{padding:28px 20px;} }
</style>
</head>
<body>
<div class="app">
  <nav id="nav"><h1>Claude On-Ramp</h1></nav>
  <main id="main"></main>
  <aside>
    <h2>Assistant</h2>
    <div class="sub">Stuck? Ask — this whole guide is loaded.</div>
    <div class="chat" id="chat">Hi — I have the full guide in front of me. Tell
      me what you're trying to do, or paste a screenshot of what you're seeing,
      and I'll get you to the next step.</div>
    <div class="compose">
      <input id="ask" placeholder="Describe what's happening…">
      <button onclick="stub()">Send</button>
    </div>
    <div class="stub">Preview only — the assistant isn't wired to a model yet.
      See <code>assistant/spec.md</code> for how it will work (full guide in
      context, screenshot-first, restricted web search, feedback log).</div>
  </aside>
</div>
<script>
const DATA = __DATA__;
const {content, nav} = DATA;

function resolve(from, href){
  // resolve a relative .md link against the current page's directory
  const dir = from.includes('/') ? from.slice(0, from.lastIndexOf('/')) : '';
  const parts = (dir ? dir.split('/') : []);
  href.split('/').forEach(p=>{
    if(p==='..') parts.pop();
    else if(p!=='.'&&p!=='') parts.push(p);
  });
  return parts.join('/');
}

function buildNav(){
  const n = document.getElementById('nav');
  for(const sec in nav){
    const h = document.createElement('div'); h.className='sec'; h.textContent=sec;
    n.appendChild(h);
    nav[sec].forEach(item=>{
      const a=document.createElement('a'); a.textContent=item.label;
      a.href='#'+item.path; a.dataset.path=item.path; n.appendChild(a);
    });
  }
}

function render(path){
  if(!content[path]) path='00-start-here.md';
  const main=document.getElementById('main');
  main.innerHTML = marked.parse(content[path]);
  // rewrite intra-guide .md links to hash routes
  main.querySelectorAll('a[href]').forEach(a=>{
    const href=a.getAttribute('href');
    if(href.endsWith('.md') || href.includes('.md#')){
      const clean=href.replace('#','');
      a.setAttribute('href', '#'+resolve(path, clean));
    }
  });
  const fb=document.createElement('div'); fb.className='didntwork';
  fb.innerHTML='<button onclick="stub()">This step didn\\'t work for me</button>';
  main.appendChild(fb);
  document.querySelectorAll('nav a').forEach(a=>
    a.classList.toggle('active', a.dataset.path===path));
  main.scrollTo?.(0,0); window.scrollTo(0,0);
}

function stub(){
  const c=document.getElementById('chat');
  c.innerHTML='<em>Preview build — not connected to a model yet. In the real '
    +'guide this logs your step + OS and either answers you or becomes a new '
    +'help note. See assistant/spec.md.</em>';
}

buildNav();
addEventListener('hashchange', ()=>render(location.hash.slice(1)));
render(location.hash.slice(1) || '00-start-here.md');
</script>
</body>
</html>
"""

OUT.write_text(HTML.replace("__DATA__", DATA), encoding="utf-8")
print(f"wrote {OUT} ({len(content)} pages)")
