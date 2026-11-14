# -*- coding: utf-8 -*-
import os, json, html, re, shutil, sys
from urllib.parse import quote_plus
sys.path.insert(0, os.path.dirname(__file__))
from content import CHECKLIST, PRIO, GUIDES, MESSAGES, FAQ_HOME
from extra5 import EXTRA

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'docs')
# Domaine : malistebebe.fr (pour tester sur GitHub Pages sans domaine : LDN_BASE=https://jeremstyke.github.io/listedenaissance)
BASE = os.environ.get('LDN_BASE', 'https://malistebebe.fr')
CUSTOM = 'malistebebe.fr' in BASE
PATH0 = '/' + BASE.split('://', 1)[1].split('/', 1)[1] + '/' if BASE.count('/') > 2 else '/'
DOMAIN = 'malistebebe.fr'
SITE = 'Ma liste bébé'
TAG = 'listedenaissance-21'   # identifiant Amazon Partenaires (a remplacer)
CONTACT = 'contact@cvlibre.com'
YEAR = 2026
AMZ_LIST = 'https://www.amazon.fr/baby-reg/homepage?tag=' + TAG
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
}
CAT_TINT = ['lilas', 'ciel', 'peche', 'menthe', 'miel', 'lilas', 'ciel']

CTA = ('<aside class="tag"><span class="tag-hole" aria-hidden="true"></span><div class="tag-tx">'
       '<strong>Crée ta liste de naissance Amazon</strong>'
       '<span>Gratuite, avec jusqu\'à 15 % de réduction sur ce qui reste à la fin.</span></div>'
       '<a class="btn" href="' + AMZ_LIST + '" rel="sponsored nofollow noopener" target="_blank">Créer ma liste</a></aside>')

NAV = [('checklist/', 'Checklist'), ('liste-de-naissance-amazon/', 'Liste Amazon'),
       ('quoi-mettre-dans-une-liste-de-naissance/', 'Que mettre ?'), ('guides/', 'Guides')]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">')

def page(path, title, desc, body, schema=None, crumbs=None, extra_head='', cls='', noindex=False):
    depth = path.count('/')
    R = '../' * depth
    url = BASE + '/' + path
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE + '/'}]
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
<meta property="og:image" content="{BASE}/assets/og.png">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3F7F6">
<link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{R}assets/style.css?v=6">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_head}</head>
<body class="{cls}">
<a class="skip" href="#main">Aller au contenu</a>
<header class="top"><div class="wrap top-in">
<a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">🍼</span>Ma liste bébé</a>
<nav class="menu" aria-label="Menu">{nav}<a id="nav-account" class="nav-acc" href="{R}compte/">Connexion</a></nav>
</div></header>
<main id="main">
{('<div class="wrap">' + bc + '</div>') if bc else ''}
{body.replace('{R}', R)}
</main>
<footer class="foot"><div class="wrap foot-in">
<div><a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">🍼</span>Ma liste bébé</a>
<p>La checklist gratuite pour préparer l'arrivée de bébé, sans rien oublier.</p></div>
<nav aria-label="Pied de page"><a href="{R}checklist/">Checklist</a><a href="{R}guides/">Guides</a><a href="{R}mentions-legales/">Mentions légales</a><a href="{R}confidentialite/">Confidentialité</a><a href="mailto:{CONTACT}">Contact</a></nav>
<p class="disc">{DISCLOSURE} Les prix et les conditions d'Amazon peuvent changer : vérifie-les avant d'acheter. © {YEAR} {DOMAIN}</p>
</div></footer>
<script src="{R}assets/account.js?v=1" defer></script>
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
def build():
    if os.path.exists(OUT):
        for n in os.listdir(OUT):
            p = os.path.join(OUT, n)
            if n == 'assets': continue
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)

    # Données de la checklist
    data = []
    for cat, emo, items in CHECKLIST:
        data.append({"c": cat, "e": emo, "i": [{"n": n, "u": amz(q), "p": p, "t": t} for n, q, p, t in items]})
    total = sum(len(c['i']) for c in data)
    js = 'window.LDN_DATA=' + json.dumps(data, ensure_ascii=False) + ';window.LDN_PRIO=' + json.dumps({str(k): v for k, v in PRIO.items()}, ensure_ascii=False) + ';window.LDN_LIST=' + json.dumps(AMZ_LIST) + ';'
    with open(os.path.join(OUT, 'assets', 'data.js'), 'w', encoding='utf-8') as f:
        f.write(js)

    tool = ('<div id="ck" class="ck"><noscript>Active JavaScript pour cocher les articles.</noscript></div>'
            '<script src="{R}assets/data.js?v=2"></script><script src="{R}assets/checklist.js?v=2" defer></script>')

    # Accueil
    cats = ''.join('<a class="cat-chip t-%s" href="{R}checklist/#cat%d"><span aria-hidden="true">%s</span>%s<small>%d articles</small></a>' % (
        CAT_TINT[i % len(CAT_TINT)], i, e, esc(c), len(it)) for i, (c, e, it) in enumerate(CHECKLIST))
    fh, fs = faq_block(FAQ_HOME)
    home = f'''<section class="hero"><div class="wrap hero-in">
<div class="hero-tx">
<h1>Ta liste de naissance, sans rien oublier</h1>
<p class="hero-p">{total} articles triés par pièce, des vrais indispensables aux petits plus. Tu coches, tu retrouves chaque article sur Amazon, et tu profites de la réduction de la liste de naissance.</p>
<div class="hbtn"><a class="btn big" href="{{R}}checklist/">Commencer ma checklist</a>
<a class="btn ghost big" href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Créer ma liste Amazon</a></div>
<p class="hero-note">Gratuit, sans inscription. Tes choix restent sur ton téléphone.</p>
</div>
{HERO_TAG}
</div></section>
<section class="wrap block">
<h2>Pièce par pièce</h2>
<p class="sub">Ouvre une catégorie pour voir ce qu'il faut vraiment prévoir.</p>
<div class="chips">{cats}</div>
</section>
<section class="band"><div class="wrap block">
<h2>En 4 étapes</h2>
<ol class="steps">
<li><strong>Coche</strong><span>les articles dont tu as besoin dans la <a href="{{R}}checklist/">checklist</a>.</span></li>
<li><strong>Ajoute</strong><span>chaque article à ta liste de naissance sur Amazon.</span></li>
<li><strong>Partage</strong><span>ta liste avec nos <a href="{{R}}message-liste-de-naissance/">messages tout prêts</a>.</span></li>
<li><strong>Économise</strong><span>sur ce qui reste grâce à la <a href="{{R}}liste-de-naissance-amazon/">réduction</a>.</span></li>
</ol></div></section>
<section class="wrap block">
<h2>Les guides des futurs parents</h2>
<div class="grid3">{''.join(gcard(x) for x in GUIDES[:6])}</div>
<p class="more"><a href="{{R}}guides/">Voir les {len(GUIDES)} guides</a></p>
</section>
<section class="wrap block narrow">{fh}</section>'''
    page('', 'Liste de naissance : checklist complète et idées (%d)' % YEAR,
         'Fais ta liste de naissance en 5 minutes : checklist gratuite de %d articles triés par pièce, conseils de parents et réduction de la liste Amazon.' % total,
         home, schema=fs, cls='home')

    # Checklist
    ck = f'''<section class="wrap pagehead"><h1>Checklist liste de naissance</h1>
<p class="lead">{total} articles triés par usage. Coche ce que tu veux mettre dans ta liste : tes choix restent enregistrés sur cet appareil.</p></section>
<div class="wrap">{tool}
{CTA}
<div class="prose">
<h2>Comment utiliser cette checklist ?</h2>
<p>Commence par filtrer sur <strong>Indispensable</strong> : c'est ce dont tu as besoin dès le retour de la maternité. Ajoute ensuite les articles <strong>Utile</strong>, qui font de très bons cadeaux pour la famille. Les articles <strong>En option</strong> peuvent attendre les mois suivants.</p>
<p>Pour chaque article, ouvre la recherche Amazon, choisis le modèle qui te plaît et clique sur « Ajouter à la liste de naissance ». Une fois ta liste remplie, partage-la avec nos <a href="{{R}}message-liste-de-naissance/">messages tout prêts</a>.</p>
</div></div>'''
    schema = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "Checklist liste de naissance",
               "applicationCategory": "LifestyleApplication", "operatingSystem": "Tous", "url": BASE + '/checklist/',
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
    page('checklist/', 'Checklist liste de naissance gratuite (%d articles)' % total,
         'Checklist interactive pour ta liste de naissance : %d articles triés par pièce (sommeil, sorties, repas, toilette), avec les indispensables et des conseils.' % total,
         ck, schema=schema, crumbs=[('Checklist', 'checklist/')], cls='tool')

    # Guides
    for x in GUIDES:
        ex_html, ex_faq = EXTRA.get(x['slug'], ('', []))
        fh, fs = faq_block(x['faq'] + ex_faq)
        body = (x['body'] + ex_html).replace('{CTA}', CTA).replace('{MSGS}', messages_html())
        body = re.sub(r'\{AMZ:([^}]+)\}', lambda m: amz(m.group(1)), body)
        body, toc = add_toc(body)
        words = len(re.sub('<[^>]+>', ' ', body).split())
        mins = max(2, round(words / 200))
        e, t = META.get(x['slug'], ('📄', 'ciel'))
        art = [{"@context": "https://schema.org", "@type": "Article", "headline": x['h1'], "description": x['desc'],
                "inLanguage": "fr-FR", "datePublished": "2026-11-14", "dateModified": "2026-11-14",
                "author": {"@type": "Organization", "name": SITE}, "mainEntityOfPage": BASE + '/' + x['slug']}]
        b = ('<header class="cover t-%s"><div class="wrap cover-in"><span class="cover-e" aria-hidden="true">%s</span>'
             '<div><h1>%s</h1><p class="cover-d">%s</p><p class="cover-m">%d min de lecture, mis à jour en novembre %d</p></div></div></header>'
             '<div class="wrap art-wrap"><article class="prose">%s%s%s</article></div>%s') % (
            t, e, esc(x['h1']), esc(x['desc']), mins, YEAR, toc, body, fh, related(x['slug']))
        page(x['slug'], x['title'], x['desc'], b, schema=art + fs,
             crumbs=[('Guides', 'guides/'), (x['short'], x['slug'])], cls='guide')

    idx = ('<section class="wrap pagehead"><h1>Guides liste de naissance</h1><p class="lead">Tout pour préparer l\'arrivée de bébé sereinement, du choix de la poussette à la valise maternité.</p></section>'
           '<section class="wrap block"><div class="grid3">' + ''.join(gcard(x, True) for x in GUIDES) + '</div></section>')
    page('guides/', 'Guides liste de naissance et préparation bébé',
         'Tous nos guides pour préparer ta liste de naissance : que mettre, petit budget, jumeaux, 2e enfant, valise maternité, messages et idées cadeaux.',
         idx, crumbs=[('Guides', 'guides/')])


    # Compte
    acc = """<div class="wrap art-wrap"><div class="prose" id="acc">
<h1>Mon compte</h1>
<div id="acc-out">
<p class="lead">Crée un compte gratuit pour retrouver ta checklist sur ton téléphone et ton ordinateur, et la partager avec ta famille.</p>
<div class="tabs" role="tablist"><button type="button" data-tab="login" class="on">Se connecter</button><button type="button" data-tab="signup">Créer un compte</button></div>
<form id="form-login" class="accf" data-pane="login">
<label>E-mail<input type="email" name="email" autocomplete="email" required></label>
<label>Mot de passe<input type="password" name="password" autocomplete="current-password" required></label>
<button class="btn" type="submit">Se connecter</button>
<button class="linkbtn" type="button" data-tab="forgot">Mot de passe oublié ?</button>
</form>
<form id="form-signup" class="accf" data-pane="signup" hidden>
<label>E-mail<input type="email" name="email" autocomplete="email" required></label>
<label>Mot de passe (8 caractères minimum)<input type="password" name="password" autocomplete="new-password" minlength="8" required></label>
<button class="btn" type="submit">Créer mon compte</button>
<p class="small">En créant un compte, tu acceptes notre <a href="{R}confidentialite/">politique de confidentialité</a>.</p>
</form>
<form id="form-forgot" class="accf" data-pane="forgot" hidden>
<label>E-mail du compte<input type="email" name="email" autocomplete="email" required></label>
<button class="btn" type="submit">Recevoir un lien</button>
<button class="linkbtn" type="button" data-tab="login">Retour à la connexion</button>
</form>
</div>
<div id="acc-newpw" hidden>
<h2>Choisis un nouveau mot de passe</h2>
<form id="form-newpw" class="accf"><label>Nouveau mot de passe<input type="password" name="password" autocomplete="new-password" minlength="8" required></label><button class="btn" type="submit">Enregistrer</button></form>
</div>
<div id="acc-in" hidden>
<p class="lead">Connecté avec <strong id="acc-email"></strong>. Ta checklist est sauvegardée : <strong id="acc-count"></strong>.</p>
<p><a class="btn" href="{R}checklist/">Ouvrir ma checklist</a></p>
<h2>Ma liste à partager</h2>
<form id="form-baby" class="accf">
<label>Prénom de bébé (facultatif)<input type="text" id="f-baby" maxlength="40"></label>
<label>Date prévue (facultatif)<input type="date" id="f-due"></label>
<label class="check"><input type="checkbox" id="f-public"> Rendre ma liste visible avec un lien privé</label>
<button class="btn" type="submit">Enregistrer</button>
</form>
<div id="acc-sharebox" hidden><p>Envoie ce lien à tes proches : ils voient les articles que tu as cochés, avec les liens pour les offrir.</p>
<div class="sharerow"><input id="acc-share" readonly><button class="btn ghost sm" type="button" id="acc-copy">Copier le lien</button></div></div>
<h2>Mon compte</h2>
<p><button class="btn ghost sm" type="button" id="acc-logout">Se déconnecter</button> <button class="btn ghost sm" type="button" id="acc-wipe">Supprimer mes données</button></p>
</div>
<p id="acc-msg" class="acc-msg" role="status" aria-live="polite"></p>
</div></div>"""
    page('compte/', 'Mon compte | Ma liste bébé', 'Crée ton compte gratuit pour sauvegarder ta checklist de naissance et la partager.', acc, noindex=True)

    pub = """<section class="wrap pagehead"><h1 id="pub-title">Une liste de naissance</h1>
<p class="lead">Voici les articles choisis par les parents. Clique sur un article pour l'offrir.</p></section>
<div class="wrap"><div id="pub" class="ck"><p>Chargement de la liste...</p></div>
<div class="prose"><p>Toi aussi tu prépares l'arrivée d'un bébé ? <a href="{R}checklist/">Fais ta checklist gratuite</a>.</p></div></div>
<script src="{R}assets/data.js?v=2"></script>"""
    page('ma-liste/', 'Liste de naissance partagée', 'Une liste de naissance partagée par des futurs parents.', pub, noindex=True, cls='tool')

    # Pages légales
    ml = f'''<div class="wrap art-wrap"><article class="prose"><h1>Mentions légales</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, CA 94107, États-Unis.</p>
<h2>Affiliation</h2><p>{DISCLOSURE} Les liens vers Amazon.fr sont des liens d'affiliation : si tu achètes après avoir cliqué, nous touchons une commission, sans surcoût pour toi. Le choix des articles reste indépendant.</p>
<h2>Responsabilité</h2><p>Les conseils de ce site sont donnés à titre informatif. Ils ne remplacent pas l'avis d'un professionnel de santé (médecin, sage-femme, pédiatre). Les conditions des offres Amazon peuvent changer à tout moment.</p></article></div>'''
    page('mentions-legales/', 'Mentions légales | Ma liste bébé', 'Mentions légales du site malistebebe.fr.', ml, crumbs=[('Mentions légales', 'mentions-legales/')])
    cf = f'''<div class="wrap art-wrap"><article class="prose"><h1>Confidentialité</h1>
<p>La checklist fonctionne sans inscription. Le compte est facultatif.</p>
<h2>Sans compte</h2><p>Les articles que tu coches sont enregistrés uniquement dans ton navigateur (stockage local). Rien n'est envoyé sur un serveur. Vider les données du navigateur efface ta checklist.</p>
<h2>Avec un compte</h2><p>Si tu crées un compte, nous enregistrons ton adresse e-mail, ton mot de passe (chiffré, nous ne le voyons jamais), les articles cochés et, si tu les indiques, le prénom de bébé et la date prévue. Ces données servent uniquement à faire fonctionner ton compte et le partage de ta liste. Elles sont hébergées par Supabase, sur des serveurs situés dans l'Union européenne (Paris). Nous ne les vendons pas et ne les utilisons pas pour de la publicité.</p>
<p>Ta liste n'est visible par d'autres personnes que si tu actives le partage : elle n'est alors accessible qu'avec son lien. Tu peux supprimer tes données à tout moment depuis la page Mon compte, et demander la suppression complète de ton compte en nous écrivant.</p>
<h2>Amazon</h2><p>Quand tu cliques sur un lien vers Amazon.fr, Amazon peut déposer des cookies pour attribuer la commission. Consulte la politique de confidentialité d'Amazon pour en savoir plus.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p></article></div>'''
    page('confidentialite/', 'Confidentialité | Ma liste bébé', 'Politique de confidentialité de malistebebe.fr : checklist sans inscription, compte facultatif.', cf, crumbs=[('Confidentialité', 'confidentialite/')])

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
    cn = os.path.join(OUT, 'CNAME')
    if CUSTOM: open(cn, 'w').write(DOMAIN + '\n')
    elif os.path.exists(cn): os.remove(cn)
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print(len(PAGES), 'pages,', total, 'articles')

if __name__ == '__main__':
    build()
