# -*- coding: utf-8 -*-
import os, json, html, re, shutil, sys
from urllib.parse import quote_plus
sys.path.insert(0, os.path.dirname(__file__))
from content import CHECKLIST, PRIO, GUIDES, MESSAGES, FAQ_HOME
from extra6 import EXTRA
from longtail import PRINTLIST
import neutre_b
from auto_articles import AUTO_META
from tools_b import TOOLS
import ogimg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'docs')
# Domaine : malistebebe.fr (sans domaine : LDN_BASE=https://jeremstyke.github.io/listedenaissance)
BASE = os.environ.get('LDN_BASE', 'https://malistebebe.fr')
CUSTOM = 'malistebebe.fr' in BASE
PATH0 = '/' + BASE.split('://', 1)[1].split('/', 1)[1] + '/' if BASE.count('/') > 2 else '/'
DOMAIN = 'malistebebe.fr' if CUSTOM else 'Ma liste bébé'
SITE = 'Ma liste bébé'
LLMS_INTRO = "Ma liste bébé aide les futurs parents à préparer l'arrivée de leur bébé : liste de naissance complète, guides pour bien choisir le matériel de puériculture (poussette, siège auto, lit, babyphone, tire-lait), comparatifs de produits vendus en France et outils pratiques. Les liens vers Amazon sont des liens d'affiliation."
TAG = 'malistebebe-21'   # identifiant Amazon Partenaires
CONTACT = 'contact@cvlibre.com'
YEAR = 2026
AMZ_LIST = 'https://www.amazon.fr/baby-reg/homepage?tag=' + TAG
AMZ_WEDDING = 'https://www.amazon.fr/wedding?tag=' + TAG   # prime liste de mariage
DISCLOSURE = "En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises."

def amz(q):
    return 'https://www.amazon.fr/s?k=' + quote_plus(q) + '&tag=' + TAG

def esc(s): return html.escape(s, quote=True)

# Couleur et emoji de chaque guide
META = {
  'liste-de-naissance-amazon/': ('🎁', 'peche'),
  'quoi-mettre-dans-une-liste-de-naissance/': ('📝', 'ciel'),
  'liste-de-naissance-petit-budget/': ('🪙', 'menthe'),
  'liste-de-naissance-jumeaux/': ('👣', 'lilas'),
  'liste-de-naissance-petit-appartement/': ('🏠', 'ciel'),
  'liste-de-naissance-deuxieme-enfant/': ('🧒', 'peche'),
  'quand-faire-sa-liste-de-naissance/': ('📅', 'menthe'),
  'message-liste-de-naissance/': ('💌', 'lilas'),
  'valise-maternite/': ('🧳', 'peche'),
  'idees-cadeau-de-naissance/': ('🎀', 'lilas'),
  'trousseau-de-naissance/': ('🧦', 'ciel'),
  'liste-de-naissance-bebe-ne-en-hiver/': ('❄️', 'ciel'),
  'liste-de-naissance-bebe-ne-en-ete/': ('☀️', 'miel'),
  'comment-choisir-sa-poussette/': ('🚼', 'menthe'),
  'comment-choisir-son-siege-auto-bebe/': ('🚗', 'peche'),
  'liste-de-naissance-allaitement/': ('🍼', 'lilas'),
  'liste-de-naissance-originale/': ('✨', 'miel'),
  'reduction-liste-de-naissance-amazon-ne-fonctionne-pas/': ('🔧', 'peche'),
  'code-liste15-amazon/': ('🏷️', 'miel'),
  'liste-de-naissance-minimaliste/': ('🌿', 'menthe'),
  'liste-de-naissance-a-imprimer/': ('🖨️', 'ciel'),
  'materiel-bebe-chez-les-grands-parents/': ('👵', 'lilas'),
  'liste-de-naissance-bebe-premature/': ('🤍', 'peche'),
  'combien-de-bodies-et-pyjamas-pour-bebe/': ('👕', 'ciel'),
  'liste-de-naissance-ecologique/': ('♻️', 'menthe'),
  'cadeau-futur-papa/': ('👨', 'lilas'),
}
META.update(AUTO_META)
CAT_TINT = ['lilas', 'ciel', 'peche', 'menthe', 'miel', 'lilas', 'ciel']

CTA = ('<aside class="tag"><span class="tag-hole" aria-hidden="true"></span><div class="tag-tx">'
       '<strong>Prête à créer ta liste en ligne ?</strong>'
       '<span>Notre choix : la liste Amazon, gratuite et simple pour tes proches. <a href="{R}ou-faire-sa-liste-de-naissance/">Comparer les solutions</a></span></div>'
       '<a class="btn" href="' + AMZ_LIST + '" rel="sponsored nofollow noopener" target="_blank">Créer ma liste</a></aside>')

NAV = [('checklist/', 'Checklist'), ('ou-faire-sa-liste-de-naissance/', 'Où faire sa liste'),
       ('outils/', 'Outils'), ('guides/', 'Guides')]

FONTS = ('<link rel="preload" href="@R@assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>'
         '<link rel="preload" href="@R@assets/fonts/figtree-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>')

AUTHOR_NAME = 'Jérémy Dacier-Jury'
AUTHOR_LD = {"@type": "Person", "name": AUTHOR_NAME, "url": BASE + '/a-propos/'}
PUBLISHER_LD = {"@type": "Organization", "name": SITE, "url": BASE + '/', "logo": {"@type": "ImageObject", "url": BASE + '/assets/apple-touch-icon.png'}}



# Boutons de partage (22 nov 2026, demande de Jeremy)
SHARE_SKIP = ('', 'a-propos/', 'mentions-legales/', 'confidentialite/', 'contact/', 'publicite/', 'partenariats/', '404-tmp/')
def share_html(url, title):
    from urllib.parse import quote
    import json as _j
    t = title.split(' | ')[0]
    u, tq = quote(url, safe=''), quote(t, safe='')
    return ('<style>.share{margin:28px 0 8px;padding:14px 0 0;border-top:1px solid var(--line,var(--trait,#ddd))}'
      '.share-t{font-weight:700;margin:0 0 8px}.share-b{display:flex;flex-wrap:wrap;gap:8px}'
      '.sh{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;border:1.5px solid var(--brand,var(--framboise,#2F6B57));'
      'background:#fff;color:var(--brand,var(--framboise,#2F6B57));font:inherit;font-size:.92em;font-weight:700;text-decoration:none;cursor:pointer}'
      '.sh:hover,.sh:focus-visible{background:var(--brand,var(--framboise,#2F6B57));color:#fff}.sh[hidden]{display:none}</style>'
      '<div class="share"><p class="share-t">Partager cette page</p><div class="share-b">'
      '<button type="button" class="sh sh-n" hidden>Partager</button>'
      f'<a class="sh" href="https://wa.me/?text={tq}%20{u}" target="_blank" rel="noopener nofollow">WhatsApp</a>'
      f'<a class="sh" href="https://www.facebook.com/sharer/sharer.php?u={u}" target="_blank" rel="noopener nofollow">Facebook</a>'
      f'<a class="sh" href="mailto:?subject={tq}&amp;body={u}">E-mail</a>'
      '<button type="button" class="sh sh-c">Copier le lien</button></div></div>'
      '<script>(function(){var s=document.currentScript.previousElementSibling,u=' + _j.dumps(url) + ',t=' + _j.dumps(t) + ';'
      'var n=s.querySelector(".sh-n");if(navigator.share){n.hidden=false;n.onclick=function(){navigator.share({title:t,url:u}).catch(function(){})}}'
      'var c=s.querySelector(".sh-c");c.onclick=function(){var ok=function(){c.textContent="Lien copié"};'
      'if(navigator.clipboard){navigator.clipboard.writeText(u).then(ok,function(){})}else{var i=document.createElement("input");i.value=u;document.body.appendChild(i);i.select();try{document.execCommand("copy");ok()}catch(e){}i.remove()}}})()</script>')

def page(path, title, desc, body, schema=None, crumbs=None, extra_head='', cls='', noindex=False, og=None):
    depth = path.count('/')
    R = '../' * depth
    url = BASE + '/' + path
    if path not in SHARE_SKIP and body.count('</article>') == 1: body = body.replace('</article>', share_html(url, title) + '</article>')
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE + '/', "inLanguage": "fr", "publisher": PUBLISHER_LD}]
    if path == '': ld.append(dict({"@context": "https://schema.org"}, **PUBLISHER_LD))
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + '/'}]
        for i, (n, p) in enumerate(crumbs):
            items.append({"@type": "ListItem", "position": i + 2, "name": n, "item": BASE + '/' + p})
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if schema: ld += schema
    nav = ''.join('<a href="%s%s"%s>%s</a>' % (R, p, ' aria-current="page"' if p == path else '', n) for p, n in NAV)
    bc = ''
    if crumbs:
        bc = '<nav class="bc" aria-label="Fil d\'Ariane"><a href="%s">Accueil</a>' % R + ''.join(
            ' / <a href="%s%s">%s</a>' % (R, p, esc(n)) for n, p in crumbs[:-1]) + ' / <span>%s</span></nav>' % esc(crumbs[-1][0])
    doc = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/{og or "assets/og.png"}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(title)}">
<meta property="og:site_name" content="Ma liste bébé">
<meta name="twitter:image" content="{BASE}/{og or "assets/og.png"}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3F7F6">
<meta name="google-site-verification" content="vZRYCBHYca7nlt0R-OhpmTUbDuUdi15H0e80qVRcmIw" />
<link rel="icon" href="{R}assets/favicon.ico" sizes="32x32"><link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
{FONTS.replace('@R@', R)}
<link rel="stylesheet" href="{R}assets/style.css?v=28">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_head}</head>
<body class="{cls}">
<a class="skip" href="#main">Aller au contenu</a>
<header class="top"><div class="wrap top-in">
<a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">🍼</span>Ma liste bébé</a>
<nav class="menu" aria-label="Menu">{nav}</nav>
</div></header>
<main id="main">
{('<div class="wrap">' + bc + '</div>') if bc else ''}
{body.replace('{R}', R)}
</main>
<div class="wave-foot"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div><footer class="foot"><div class="wrap foot-in">
<div><a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">🍼</span>Ma liste bébé</a>
<p>La checklist gratuite pour préparer l'arrivée de bébé, sans rien oublier.</p></div>
<nav aria-label="Pied de page"><a href="{R}checklist/">Checklist</a><a href="{R}guides/">Guides</a><a href="{R}outils/">Outils</a><a href="{R}a-propos/">À propos</a><a href="{R}mentions-legales/">Mentions légales</a><a href="{R}confidentialite/">Confidentialité</a><a href="mailto:{CONTACT}">Contact</a></nav>
<p class="wed">💍 Tu te maries aussi ? Prépare ta liste avec <a href="https://malistedemariage.fr/">Ma liste mariage</a> ou <a href="{AMZ_WEDDING}" rel="sponsored nofollow noopener" target="_blank">crée ta liste de mariage Amazon</a></p>
<nav class="sites" aria-label="Nos autres sites"><p class="sites-t">Découvrez aussi nos autres sites</p><div class="sites-g"><a href="https://vieillir-chez-soi.fr/"><img src="https://vieillir-chez-soi.fr/assets/favicon.svg" alt="" width="40" height="40" loading="lazy"><span><strong>Vieillir chez soi</strong><small>Rester autonome à la maison</small></span></a><a href="https://lesoiseauxdujardin.fr/"><img src="https://lesoiseauxdujardin.fr/assets/favicon.svg" alt="" width="40" height="40" loading="lazy"><span><strong>Les oiseaux du jardin</strong><small>Nourrir et observer les oiseaux</small></span></a><a href="https://malistedemariage.fr/"><img src="https://malistedemariage.fr/assets/favicon.svg" alt="" width="40" height="40" loading="lazy"><span><strong>Ma liste mariage</strong><small>La liste de mariage simple</small></span></a></div></nav>
<p class="disc">{DISCLOSURE} Les prix et les conditions d'Amazon peuvent changer : vérifie-les avant d'acheter. © {YEAR} {DOMAIN}</p>
</div></footer>
<script src="{R}assets/track.js?v=1" defer></script>
</body>
</html>
'''
    if '—' in doc:
        raise SystemExit('Tiret long interdit dans ' + path)
    d = os.path.join(OUT, path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(doc)
    if len(title) > 65: print('Titre long :', path, len(title))
    if not noindex: PAGES.append(path)

PAGES = []

def ogfor(name, title, kicker, emoji, tint):
    rel = 'og/' + name + '.png'
    ogimg.make(os.path.join(OUT, rel), title, kicker, emoji, tint)
    return rel

def faq_block(faq):
    if not faq: return '', []
    h = '<h2 id="faq">Questions fréquentes</h2><div class="faq">' + ''.join(
        '<details><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq) + '</div>'
    s = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    return h, s

def gcard(x, long=False):
    e, t = META.get(x['slug'], ('📄', 'ciel'))
    d = x['desc'] if long else x['desc'][:96].rsplit(' ', 1)[0] + '...'
    return ('<a class="gcard t-%s" href="{R}%s"><span class="gcard-e" aria-hidden="true">%s</span>'
            '<strong>%s</strong><span class="gcard-d">%s</span></a>') % (t, x['slug'], e, esc(x['short'] if not long else x['h1']), esc(d))

def related(cur):
    i = [x['slug'] for x in GUIDES].index(cur)
    links = [GUIDES[(i + k) % len(GUIDES)] for k in range(1, 4)]
    return '<section class="wrap rel"><h2>À lire ensuite</h2><div class="grid3">' + ''.join(gcard(x) for x in links) + '</div></section>'

def slugify(t):
    import unicodedata
    t = unicodedata.normalize('NFD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:50]

def top_price_buttons(body):
    # Tops : le bouton Amazon de chaque fiche produit (h2 « 1. Modèle ») passe juste sous le nom du produit,
    # avec le texte « Voir le prix sur Amazon ». Un seul lien Amazon par fiche.
    parts = re.split(r'(?=<h2>)', body)
    for i, p in enumerate(parts):
        if not re.match(r'<h2>\d+\.\s', p):
            continue
        m = re.search(r'\s*<p class="amz-p"><a class="btn-amz" ([^>]*)>[^<]*</a></p>', p)
        if not m:
            continue
        p = p[:m.start()] + p[m.end():]
        btn = '\n<p class="amz-p amz-top"><a class="btn-amz" %s>Voir le prix sur Amazon</a></p>' % m.group(1)
        parts[i] = re.sub(r'(<h2>[^<]*(?:<[^/][^>]*>[^<]*</[^>]+>[^<]*)*</h2>)', lambda h: h.group(1) + btn, p, count=1)
    return ''.join(parts)


def add_toc(body):
    heads = []
    def rep(m):
        txt = re.sub('<[^>]+>', '', m.group(1)); sid = slugify(txt); heads.append((sid, txt))
        return '<h2 id="%s">%s</h2>' % (sid, m.group(1))
    body = re.sub(r'<h2>(.*?)</h2>', rep, body)
    if len(heads) < 3: return body, ''
    toc = '<nav class="toc" aria-label="Sommaire"><strong>Dans ce guide</strong><ol>' + ''.join(
        '<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in heads) + '</ol></nav>'
    return body, toc

def messages_html():
    out = '<div class="msgs">'
    for i, (t, m) in enumerate(MESSAGES):
        m = m.replace('\\n', '\n')
        out += '<div class="msg"><h3>%s</h3><p class="mtext" id="m%d">%s</p><button class="btn ghost sm copy" data-t="m%d">Copier le message</button></div>' % (
            esc(t), i, esc(m).replace('\n', '<br>'), i)
    out += '</div><script src="{R}assets/msg.js?v=2" defer></script>'
    return out

HERO_TAG = """<div class="hero-tag" aria-hidden="true"><span class="tag-hole"></span>
<p class="ht-title">Ma liste de naissance</p>
<ul>
<li class="on" style="--d:.2s">Siège auto i-Size</li>
<li class="on" style="--d:.6s">Lit et matelas</li>
<li class="on" style="--d:1s">Gigoteuses</li>
<li style="--d:1.4s">Porte-bébé</li>
<li style="--d:1.8s">Tapis d'éveil</li>
</ul>
<p class="ht-foot">3 sur 53 cochés</p></div>"""
# Guide « comment choisir » associé à un article de la checklist (affiché seulement si le guide existe)
GUIDE_MAP = [('Poussette', 'comment-choisir-sa-poussette/'), ('Siège auto', 'comment-choisir-son-siege-auto-bebe/'), ('Lit bébé', 'comment-choisir-lit-bebe/'), ('Matelas', 'comment-choisir-matelas-bebe/'), ('Babyphone', 'comment-choisir-son-babyphone/'), ('Chaise haute', 'comment-choisir-chaise-haute/'), ('Tire-lait', 'comment-choisir-tire-lait/'), ('Transat', 'comment-choisir-transat-bebe/'), ('Sac à langer', 'comment-choisir-sac-a-langer/'), ('Biberons', 'comment-choisir-biberon/'), ('Lit parapluie', 'comment-choisir-lit-parapluie/'), ("Tapis d'éveil", 'comment-choisir-tapis-d-eveil/'), ("Coussin d'allaitement", 'comment-choisir-coussin-allaitement/'), ('Thermomètre médical', 'comment-choisir-thermometre-bebe/'), ('Gigoteuses', 'gigoteuse-quel-tog/'), ('Porte-bébé', 'porte-bebe-ou-echarpe-de-portage/'), ('Lit cododo', 'lit-cododo-utile/'), ('Stérilisateur', 'sterilisateur-biberon-utile/'), ('Chauffe-biberon', 'chauffe-biberon-utile/'), ('Baignoire', 'baignoire-bebe-ou-transat-de-bain/'), ('Bodies', 'combien-de-bodies-et-pyjamas-pour-bebe/'), ('Pyjamas', 'combien-de-bodies-et-pyjamas-pour-bebe/'), ('Mouche-bébé', 'mouche-bebe-lequel-choisir/'), ('Veilleuse', 'veilleuse-bebe-utile/')]
def guide_for(name):
    have = {x['slug'] for x in GUIDES}
    for key, slug in GUIDE_MAP:
        if name.startswith(key) and slug in have:
            return slug
    return None

REL = 'rel="sponsored nofollow noopener" target="_blank"'
def top_pick(body):
    """Produit n°1 d'un top : (nom, raison, ancre, requête Amazon) ou None.
    Premier intertitre (« 1. » en priorité) suivi, avant l'intertitre suivant, d'un lien « Voir ... Amazon »."""
    if not re.search(r'Comment (?:nous avons|on a) fait cette sélection', body): return None
    heads = list(re.finditer(r'<h([23])(?: id="([^"]*)")?>\s*(.+?)</h\1>', body))
    order = [h for h in heads if re.match(r'1\.\s', h.group(3))] + heads
    for k, h in enumerate(order):
        nxt = next((x.start() for x in heads if x.start() > h.start()), len(body))
        a = re.search(r'href="\{AMZ:([^}]+)\}"[^>]*>\s*Voir[^<]*Amazon', body[h.end():nxt])
        if not a: continue
        title = re.sub(r'^1\.\s*', '', re.sub('<[^>]+>', '', h.group(3)))
        name, _, why = title.partition(' : ')
        why = re.sub(r'\s*\((?:notre|mon) choix[^)]*\)\s*$', '', why.strip(), flags=re.I)
        return name.strip(), (why[:1].upper() + why[1:]) if why else '', h.group(2), a.group(1)
    return None

def pick_box(body):
    """Encadré « Notre choix » juste après l'intro : produit n°1 des tops, ou n°1 du comparatif lié pour les guides."""
    if '{CTA}' not in body or 'class="pick"' in body: return body
    p = top_pick(body)
    if p:
        name, why, anchor, q = p
        more = ('<a class="pick-more" href="#%s">Pourquoi ce choix</a>' % anchor) if anchor else ''
        box = ('<aside class="pick"><div><span class="pick-tag">⭐ Notre choix n°1</span><strong>%s</strong><span>%s</span>%s</div>'
               '<a class="btn" href="{AMZ:%s}" %s>Voir sur Amazon</a></aside>') % (esc(name), esc(why or 'Notre recommandation n°1 dans ce comparatif.'), more, q, REL)
        return body.replace('{CTA}', box + '\n{CTA}', 1)
    return body

def pick_box_guide(body, slug):
    """Pour un guide : n°1 du comparatif lié qui parle du même produit (mots communs dans l'adresse)."""
    if '{CTA}' not in body or 'class="pick"' in body or slug.startswith('meilleur'): return body
    stop = {'a', 'd', 'l', 'au', 'aux', 'des', 'en', 'et', 'un', 'une', 'par', 'sa', 'son', 'ses', 'ma', 'mon', 'mes', 'ta', 'ton', 'tes', 'noces', 'annee', 'ans', 'bebe', 'mariage', 'liste', 'naissance', 'cadeau', 'livre', 'livres', 'meilleur', 'meilleure', 'meilleurs', 'comment', 'choisir', 'senior', 'personne', 'agee', 'de', 'du', 'la', 'le', 'les', 'pour', 'bien', 'quel', 'quelle'}
    if re.search(r'aide|rembours|prix|retraite', slug): return body
    words = [w for w in slug.strip('/').split('-') if w not in stop]
    if not words: return body
    mine = set(words)
    best, score = None, 0
    cands = list(dict.fromkeys(re.findall(r'href="\{R\}(meilleur[a-z0-9-]*/)"', body))) + [gd['slug'] for gd in GUIDES if gd['slug'].startswith('meilleur')]
    for cand in cands:
        cw = set(cand.strip('/').split('-')) - stop
        sc = len(mine & cw) if words[0] in cw else 0
        if sc > score: best, score = cand, sc
    if not best or score < min(2, len(mine)): return body
    top = next((gd for gd in GUIDES if gd['slug'] == best), None)
    p = top_pick(top['body']) if top else None
    if not p: return body
    name, why, anchor, q = p
    box = ('<aside class="pick"><div><span class="pick-tag">⭐ Notre n°1</span><strong>%s</strong><span>%s</span>'
           '<a class="pick-more" href="{R}%s">Voir tout le comparatif</a></div>'
           '<a class="btn" href="{AMZ:%s}" %s>Voir sur Amazon</a></aside>') % (esc(name), esc(why or ('Extrait de notre comparatif « %s ».' % top['short'])), best, q, REL)
    return body.replace('{CTA}', box + '\n{CTA}', 1)

def build():
    if os.path.exists(OUT):
        for n in os.listdir(OUT):
            p = os.path.join(OUT, n)
            if n == 'assets' or (n.endswith('.txt') and len(n) == 36): continue
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)

    # Image de partage par défaut
    ogimg.make(os.path.join(OUT, 'assets', 'og.png'), 'Ta liste de naissance, sans rien oublier', 'Checklist gratuite', '🍼', 'miel')
    # Données de la checklist
    data = []
    for cat, emo, items in CHECKLIST:
        data.append({"c": cat, "e": emo, "i": [dict({"n": n, "u": amz(q), "p": p, "t": t}, **({"g": guide_for(n)} if guide_for(n) else {})) for n, q, p, t in items]})
    total = sum(len(c['i']) for c in data)
    js = 'window.LDN_DATA=' + json.dumps(data, ensure_ascii=False) + ';window.LDN_PRIO=' + json.dumps({str(k): v for k, v in PRIO.items()}, ensure_ascii=False) + ';window.LDN_LIST=' + json.dumps(AMZ_LIST) + ';window.LDN_TAG=' + json.dumps(TAG) + ';'
    with open(os.path.join(OUT, 'assets', 'data.js'), 'w', encoding='utf-8') as f:
        f.write(js)

    tool = ('<div id="ck" class="ck"><noscript>Active JavaScript pour cocher les articles.</noscript></div>'
            '<script src="{R}assets/data.js?v=3"></script><script src="{R}assets/checklist.js?v=9b" defer></script>')

    # Accueil
    cats = ''.join('<a class="cat-chip t-%s" href="{R}checklist/#cat%d"><span aria-hidden="true">%s</span>%s<small>%d articles</small></a>' % (
        CAT_TINT[i % len(CAT_TINT)], i, e, esc(c), len(it)) for i, (c, e, it) in enumerate(CHECKLIST))
    fh, fs = faq_block(FAQ_HOME)
    home = f'''<section class="hero"><span class="blob b1" aria-hidden="true"></span><span class="blob b2" aria-hidden="true"></span><span class="spark s1" aria-hidden="true">✦</span><span class="spark s2" aria-hidden="true">✦</span><span class="spark s3" aria-hidden="true">✦</span><div class="wrap hero-in">
<div class="hero-tx">
<h1>Ta liste de naissance, sans rien oublier</h1>
<p class="hero-p">{total} articles triés par pièce, des vrais indispensables aux petits plus. Tu coches, tu compares les modèles en un clic, et tu remplis ta liste en ligne sans rien oublier.</p>
<div class="hbtn"><a class="btn big" href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Créer ma liste</a>
<a class="btn ghost big" href="{{R}}checklist/">Voir la checklist</a></div>
<p class="hero-note"><strong>1.</strong> Crée ta liste de naissance sur Amazon, c'est gratuit (<a href="{{R}}ou-faire-sa-liste-de-naissance/">pourquoi Amazon ?</a>). <strong>2.</strong> Remplis-la avec notre checklist, sans rien oublier.</p>
</div>
{HERO_TAG}
</div></section>
<section class="wrap block">
<h2>Pièce par pièce</h2>
<p class="sub">Ouvre une catégorie pour voir ce qu'il faut vraiment prévoir.</p>
<div class="chips">{cats}</div>
</section>
<div class="wave-top"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div><section class="band"><div class="wrap block">
<h2>Comment ça marche</h2>
<ol class="steps">
<li><strong>Crée ta liste</strong><span>sur Amazon, gratuitement : <a href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">créer ma liste</a>.</span></li>
<li><strong>Remplis-la</strong><span>avec la <a href="{{R}}checklist/">checklist</a> : pour chaque article, « Voir » te montre les modèles à ajouter.</span></li>
<li><strong>Partage-la</strong><span>avec tes proches grâce à nos <a href="{{R}}message-liste-de-naissance/">messages tout prêts</a>.</span></li>
</ol></div></section><div class="wave-bot"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div>
<section class="wrap block">
<h2>Les guides des futurs parents</h2>
<div class="grid3">{''.join(gcard(x) for x in GUIDES[:6])}</div>
<p class="more"><a href="{{R}}guides/">Voir les {len(GUIDES)} guides</a></p>
</section>
<section class="wrap block">
<h2>Nos outils gratuits</h2>
<div class="grid3">{''.join(('<a class="gcard t-%s" href="{R}%s"><span class="gcard-e" aria-hidden="true">%s</span><strong>%s</strong><span class="gcard-d">%s</span></a>') % (x['tint'], x['slug'], x['emoji'], esc(x['h1']), esc(x['desc'])) for x in TOOLS)}</div>
</section>
<section class="wrap block narrow"><div class="prose">
<h2>Préparer sa liste de naissance sans stress</h2>
<p>Une liste de naissance sert à deux choses : ne rien oublier pour l'arrivée de bébé, et aider tes proches qui veulent te faire un cadeau. La plupart des futurs parents la commencent au deuxième trimestre, quand l'énergie revient, et la partagent quelques semaines avant le terme. Notre <a href="{{R}}quand-faire-sa-liste-de-naissance/">calendrier détaillé</a> t'aide à caler les étapes.</p>
<p>Le plus difficile, c'est de faire le tri entre l'indispensable et le superflu. Dans la checklist, chaque article porte une priorité : <strong>Indispensable</strong> pour les premières semaines, <strong>Utile</strong> pour les cadeaux de la famille, <strong>En option</strong> pour plus tard. Tu évites ainsi les achats inutiles, un vrai plus si tu as un <a href="{{R}}liste-de-naissance-petit-budget/">petit budget</a> ou un <a href="{{R}}liste-de-naissance-petit-appartement/">petit appartement</a>.</p>
<p>Pour la liste en ligne, plusieurs solutions existent : site marchand, liste multi-boutiques, magasin, cagnotte. Notre comparatif <a href="{{R}}ou-faire-sa-liste-de-naissance/">où faire sa liste de naissance</a> t'aide à choisir. Tu attends des jumeaux, un deuxième enfant ou un bébé d'hiver ? Nos guides dédiés t'aident à adapter la liste à ta situation.</p>
</div></section>
<section class="wrap block narrow">{fh}</section>'''
    page('', 'Liste de naissance : checklist complète et idées (%d)' % YEAR,
         'Fais ta liste de naissance en 5 minutes : checklist gratuite de %d articles triés par pièce, conseils de parents et comparatif des listes en ligne.' % total,
         home, schema=fs, cls='home', og=ogfor('accueil', 'Ta liste de naissance, sans rien oublier', 'Checklist gratuite', '🍼', 'miel'))

    # Checklist
    ck = f'''<section class="wrap pagehead"><h1>Checklist liste de naissance</h1>
<p class="lead">{total} articles triés par usage. Coche ce que tu veux mettre dans ta liste : tes choix restent enregistrés sur cet appareil.</p></section>
<div class="wrap"><div class="ck-first"><strong>Comment ajouter un article à ta liste</strong><ol><li>Pas encore de liste ? <a href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Crée-la sur Amazon</a>, c'est gratuit.</li><li>Ici, clique sur <strong>« Voir »</strong> à côté d'un article : Amazon s'ouvre avec des modèles.</li><li>Choisis un modèle, puis appuie sur <strong>« Ajouter à la liste de naissance »</strong>, sous « Ajouter au panier ». Sur l'appli, il peut se trouver dans le menu « Ajouter à une liste ».</li><li>Reviens ici : l'article est déjà coché, passe au suivant.</li></ol></div></div>
<div class="wrap">{tool}
{CTA}
<div class="prose">
<h2>Comment utiliser cette checklist ?</h2>
<p>Commence par filtrer sur <strong>Indispensable</strong> : c'est ce dont tu as besoin dès le retour de la maternité. Ajoute ensuite les articles <strong>Utile</strong>, qui font de très bons cadeaux pour la famille. Les articles <strong>En option</strong> peuvent attendre les mois suivants.</p>
<p>Pour chaque article, le bouton « Voir » te montre des modèles : choisis celui qui te plaît et ajoute-le à ta liste en ligne. Une fois ta liste remplie, partage-la avec nos <a href="{{R}}message-liste-de-naissance/">messages tout prêts</a>.</p>
</div></div>'''
    schema = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "Checklist liste de naissance",
               "applicationCategory": "LifestyleApplication", "operatingSystem": "Tous", "url": BASE + '/checklist/',
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
    page('checklist/', 'Checklist liste de naissance gratuite (%d articles)' % total,
         'Checklist interactive pour ta liste de naissance : %d articles triés par pièce (sommeil, sorties, repas, toilette), avec les indispensables et des conseils.' % total,
         ck, schema=schema, crumbs=[('Checklist', 'checklist/')], cls='tool', og=ogfor('checklist', 'Checklist liste de naissance : %d articles' % total, 'Gratuit', '✅', 'menthe'))

    # Guides
    for x in GUIDES:
        ex_html, ex_faq = EXTRA.get(x['slug'], ('', []))
        fh, fs = faq_block(x['faq'] + ex_faq)
        body = pick_box_guide(pick_box(x['body'] + ex_html), x['slug']).replace('{CTA}', CTA).replace('{PRINTLIST}', PRINTLIST).replace('{MSGS}', messages_html())
        body = re.sub(r'\{AMZ:([^}]+)\}', lambda m: amz(m.group(1)), body)
        body = re.sub(r'<p>\s*<a (href="https://www\.amazon\.fr[^"]*"[^>]*)>([^<]+)</a>\s*</p>', r'<p class="amz-p"><a class="btn-amz" \1>\2</a></p>', body)
        if x['slug'].startswith('meilleur'):
            body = top_price_buttons(body)
        body, toc = add_toc(body)
        words = len(re.sub('<[^>]+>', ' ', body).split())
        mins = max(2, round(words / 200))
        e, t = META.get(x['slug'], ('📄', 'ciel'))
        ogp = ogfor(x['slug'].strip('/'), x['h1'], 'Guide', e, t)
        art = [{"@context": "https://schema.org", "@type": "Article", "headline": x['h1'], "description": x['desc'],
                "inLanguage": "fr-FR", "datePublished": "2026-11-14", "dateModified": "2026-11-14",
                "author": AUTHOR_LD, "publisher": PUBLISHER_LD, "image": BASE + '/' + ogp, "mainEntityOfPage": BASE + '/' + x['slug']}]
        b = ('<header class="cover t-%s"><span class="cover-dots" aria-hidden="true"></span><div class="wrap cover-in"><span class="cover-e" aria-hidden="true">%s</span>'
             '<div><h1>%s</h1><p class="cover-d">%s</p><p class="cover-m">%d min de lecture, mis à jour en novembre %d, par <a href="/a-propos/" rel="author">Jérémy</a></p></div></div></header>'
             '<div class="wrap art-wrap"><article class="prose">%s%s%s%s</article></div>%s') % (
            t, e, esc(x['h1']), esc(x['desc']), mins, YEAR, toc, body, CTA, fh, related(x['slug']))
        page(x['slug'], x['title'], x['desc'], b, schema=art + fs,
             crumbs=[('Guides', 'guides/'), (x['short'], x['slug'])], cls='guide',
             og=ogp)

    idx = ('<section class="wrap pagehead"><h1>Guides liste de naissance</h1><p class="lead">Tout pour préparer l\'arrivée de bébé sereinement, du choix de la poussette à la valise maternité.</p></section>'
           '<section class="wrap block"><div class="grid3">' + ''.join(gcard(x, True) for x in GUIDES) + '</div></section>')
    page('guides/', 'Guides liste de naissance et préparation bébé',
         'Tous nos guides pour préparer ta liste de naissance : que mettre, petit budget, jumeaux, 2e enfant, valise maternité, messages et idées cadeaux.',
         idx, crumbs=[('Guides', 'guides/')], og=ogfor('guides', 'Tous les guides pour préparer l\'arrivée de bébé', 'Guides', '📚', 'ciel'))


    # Outils gratuits
    for x in TOOLS:
        fh, fs = faq_block(x['faq'])
        body, toc = add_toc(x['body'])
        app = [{"@context": "https://schema.org", "@type": "WebApplication", "name": x['h1'], "description": x['desc'],
                "applicationCategory": "UtilitiesApplication", "operatingSystem": "Tous", "url": BASE + '/' + x['slug'],
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
        ogp = ogfor(x['slug'].strip('/'), x['h1'], 'Outil gratuit', x['emoji'], x['tint'])
        b = ('<header class="cover t-%s"><span class="cover-dots" aria-hidden="true"></span><div class="wrap cover-in"><span class="cover-e" aria-hidden="true">%s</span>'
             '<div><h1>%s</h1><p class="cover-d">%s</p><p class="cover-m">Outil gratuit, sans inscription</p></div></div></header>'
             '<div class="wrap art-wrap"><div class="tool-box">%s</div><article class="prose">%s%s%s%s</article></div>'
             '<script src="{R}assets/tools.js?v=1" defer></script>') % (
            x['tint'], x['emoji'], esc(x['h1']), esc(x['desc']), x['tool'], toc, body, CTA, fh)
        page(x['slug'], x['title'], x['desc'], b, schema=app + fs,
             crumbs=[('Outils', 'outils/'), (x['short'], x['slug'])], cls='guide', og=ogp)
    tcards = ''.join(('<a class="gcard t-%s" href="{R}%s"><span class="gcard-e" aria-hidden="true">%s</span>'
                      '<strong>%s</strong><span class="gcard-d">%s</span></a>') % (x['tint'], x['slug'], x['emoji'], esc(x['h1']), esc(x['desc'])) for x in TOOLS)
    page('outils/', "Outils gratuits futurs parents : date d'accouchement, trousseau", "Outils gratuits pour préparer l'arrivée de bébé : calcul de la date d'accouchement, calendrier de préparation et calculateur de trousseau.",
         '<section class="wrap pagehead"><h1>Outils gratuits pour futurs parents</h1><p class="lead">Calcule ta date d\'accouchement, prépare ton trousseau et organise l\'arrivée de bébé.</p></section><section class="wrap block"><div class="grid3">' + tcards + '</div></section>',
         crumbs=[('Outils', 'outils/')], og=ogfor('outils', 'Outils gratuits pour futurs parents', 'Gratuit', '🧰', 'menthe'))

    # Compte


    # Pages légales
    ml = f'''<div class="wrap art-wrap"><article class="prose"><h1>Mentions légales</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, CA 94107, États-Unis.</p>
<h2>Affiliation</h2><p>{DISCLOSURE} Les liens vers Amazon.fr sont des liens d'affiliation : si tu achètes après avoir cliqué, nous touchons une commission, sans surcoût pour toi. Le choix des articles reste indépendant.</p>
<h2>Responsabilité</h2><p>Les conseils de ce site sont donnés à titre informatif. Ils ne remplacent pas l'avis d'un professionnel de santé (médecin, sage-femme, pédiatre). Les conditions des offres Amazon peuvent changer à tout moment.</p></article></div>'''
    page('a-propos/', 'À propos | ' + SITE, "Qui écrit " + SITE + ", d'où viennent nos conseils et comment le site est financé.", f'''<div class="wrap art-wrap"><article class="prose"><h1>À propos</h1>
<p>Ma liste bébé aide les futurs parents à préparer l'arrivée de bébé : liste de naissance, checklist, guides d'achat et outils gratuits. Le site est édité par Jérémy Dacier-Jury.</p>
<h2>Qui écrit</h2><p>Les guides sont rédigés et relus par Jérémy, avec l'aide d'outils de rédaction. Chaque page indique sa date de mise à jour.</p>
<h2>Notre méthode</h2><ul><li><strong>Des critères de choix expliqués</strong> pour chaque article : sécurité, normes, usage réel, entretien.</li>
<li><strong>Pas de faux tests</strong> : nous ne testons pas tous les produits nous-mêmes. Les sélections s'appuient sur les fiches des fabricants, les normes et les avis d'utilisateurs.</li>
<li><strong>Aucun prix inventé</strong> : les prix changent, nous renvoyons vers la fiche du produit.</li>
<li><strong>Des corrections rapides</strong> : une erreur ? Écris-nous à <a href="mailto:{CONTACT}">{CONTACT}</a>.</li></ul>
<h2>Comment le site est financé</h2><p>{DISCLOSURE} Si tu achètes après avoir cliqué sur un lien Amazon, nous touchons une commission, sans surcoût pour toi. Le choix des articles reste indépendant.</p></article></div>''', crumbs=[('À propos', 'a-propos/')])
    page('mentions-legales/', 'Mentions légales | Ma liste bébé', 'Mentions légales du site Ma liste bébé.', ml, crumbs=[('Mentions légales', 'mentions-legales/')])
    cf = f'''<div class="wrap art-wrap"><article class="prose"><h1>Confidentialité</h1>
<p>La checklist fonctionne sans inscription. Aucun compte n'est nécessaire.</p>
<h2>Ta checklist</h2><p>Les articles que tu coches sont enregistrés uniquement dans ton navigateur (stockage local). Rien n'est envoyé sur un serveur. Vider les données du navigateur efface ta checklist.</p>
<h2>Mesure d'audience</h2><p>Nous comptons les pages vues et les clics vers Amazon de façon anonyme (page visitée, site d'origine, type d'appareil et un identifiant aléatoire stocké dans ton navigateur). Ces données ne sont ni vendues ni utilisées pour de la publicité, et sont hébergées par Supabase dans l'Union européenne.</p>
<h2>Amazon</h2><p>Quand tu cliques sur un lien vers Amazon.fr, Amazon peut déposer des cookies pour attribuer la commission. Consulte la politique de confidentialité d'Amazon pour en savoir plus.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p></article></div>'''
    page('confidentialite/', 'Confidentialité | Ma liste bébé', 'Politique de confidentialité de Ma liste bébé : checklist sans inscription, sans inscription ni compte.', cf, crumbs=[('Confidentialité', 'confidentialite/')])

    # 404
    page('404-tmp/', 'Page introuvable | Ma liste bébé', 'Page introuvable.',
         '<div class="wrap art-wrap prose"><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a changé d\'adresse. <a href="/checklist/">Ouvre la checklist</a> ou retourne à <a href="/">l\'accueil</a>.</p></div>')
    shutil.move(os.path.join(OUT, '404-tmp', 'index.html'), os.path.join(OUT, '404.html'))
    shutil.rmtree(os.path.join(OUT, '404-tmp')); PAGES.remove('404-tmp/')
    with open(os.path.join(OUT, '404.html'), encoding='utf-8') as f: t = f.read()
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(t.replace('href="../', 'href="' + PATH0).replace('src="../', 'src="' + PATH0).replace('href="/checklist/', 'href="' + PATH0 + 'checklist/').replace('href="/">', 'href="' + PATH0 + '">').replace('<head>', '<head>\n<meta name="robots" content="noindex">')
            .replace('<link rel="canonical" href="' + BASE + '/404-tmp/">\n', ''))

    # sitemap, robots, CNAME
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        '<url><loc>%s/%s</loc><lastmod>2026-11-14</lastmod></url>\n' % (BASE, p) for p in PAGES) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % BASE)
    # llms.txt : résumé du site pour les IA (généré à chaque build)
    try:
        import html as _h
        _out = ['# ' + SITE, '', '> ' + LLMS_INTRO, '', 'Site : ' + BASE + '/', 'Langue : français', '', '## Pages']
        for _loc in re.findall(r'<loc>([^<]+)</loc>', sm):
            _rel = _loc[len(BASE):].strip('/')
            _f = os.path.join(OUT, _rel, 'index.html') if _rel else os.path.join(OUT, 'index.html')
            if not os.path.exists(_f): continue
            _t = open(_f, encoding='utf-8').read()
            _ti = re.search(r'<title>(.*?)</title>', _t, re.S)
            _de = re.search(r'<meta name="description" content="([^"]*)"', _t)
            if not _ti or 'http-equiv="refresh"' in _t: continue
            _out.append('- [%s](%s)%s' % (_h.unescape(_ti.group(1)).strip(), _loc, (': ' + _h.unescape(_de.group(1)).strip()) if _de else ''))
        open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(_out) + '\n')
    except Exception as _e:
        print('llms.txt non généré :', _e)
    cn = os.path.join(OUT, 'CNAME')
    if CUSTOM: open(cn, 'w').write(DOMAIN + '\n')
    elif os.path.exists(cn): os.remove(cn)
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print(len(PAGES), 'pages,', total, 'articles')

if __name__ == '__main__':
    build()
