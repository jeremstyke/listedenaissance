# -*- coding: utf-8 -*-
import os, json, html, re, shutil, sys
from urllib.parse import quote_plus
sys.path.insert(0, os.path.dirname(__file__))
from content import CHECKLIST, PRIO, GUIDES, MESSAGES, FAQ_HOME

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'docs')
BASE = 'https://listedenaissance.xyz'
DOMAIN = 'listedenaissance.xyz'
SITE = 'Liste de Naissance'
TAG = 'listedenaissance-21'   # identifiant Amazon Partenaires (a remplacer)
CONTACT = 'contact@cvlibre.com'
YEAR = 2026
AMZ_LIST = 'https://www.amazon.fr/baby-reg/homepage?tag=' + TAG
DISCLOSURE = "En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises."

def amz(q):
    return 'https://www.amazon.fr/s?k=' + quote_plus(q) + '&tag=' + TAG

def esc(s): return html.escape(s, quote=True)

CTA = ('<div class="cta"><div><strong>Crée ta liste de naissance Amazon</strong>'
       '<span>Gratuite, et jusqu\'à 15 % de réduction sur les articles restants.</span></div>'
       '<a class="btn" href="' + AMZ_LIST + '" rel="sponsored nofollow noopener" target="_blank">Créer ma liste ↗</a></div>')

NAV = [('checklist/', 'Checklist'), ('liste-de-naissance-amazon/', 'Liste Amazon'),
       ('quoi-mettre-dans-une-liste-de-naissance/', 'Que mettre ?'), ('guides/', 'Guides')]

def page(path, title, desc, body, schema=None, crumbs=None, extra_head=''):
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
    nav = ''.join('<a href="%s%s">%s</a>' % (R, p, n) for p, n in NAV)
    bc = ''
    if crumbs:
        bc = '<nav class="bc"><a href="%s">Accueil</a>' % R + ''.join(
            ' › <a href="%s%s">%s</a>' % (R, p, esc(n)) for n, p in crumbs[:-1]) + ' › <span>%s</span></nav>' % esc(crumbs[-1][0])
    doc = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og.png">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f6a5b5">
<link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{R}assets/style.css?v=2">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_head}</head>
<body>
<header class="top"><div class="wrap">
<a class="logo" href="{R}">🍼 <span>Liste de Naissance</span></a>
<nav class="menu">{nav}</nav>
</div></header>
<main class="wrap">
{bc}
{body.replace('{R}', R)}
</main>
<footer class="foot"><div class="wrap">
<p class="disc">{DISCLOSURE} Les prix et conditions affichés sur Amazon peuvent changer : vérifie-les avant d'acheter.</p>
<p><a href="{R}checklist/">Checklist</a> · <a href="{R}guides/">Guides</a> · <a href="{R}mentions-legales/">Mentions légales</a> · <a href="{R}confidentialite/">Confidentialité</a> · <a href="mailto:{CONTACT}">Contact</a></p>
<p class="small">© {YEAR} {DOMAIN}. Site indépendant, non affilié à Amazon autrement que par le programme Partenaires.</p>
</div></footer>
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
    PAGES.append(path)

PAGES = []

def faq_block(faq):
    if not faq: return '', []
    h = '<h2>Questions fréquentes</h2><div class="faq">' + ''.join(
        '<details><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq) + '</div>'
    s = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    return h, s

def related(cur):
    i = [x['slug'] for x in GUIDES].index(cur)
    links = [GUIDES[(i + k) % len(GUIDES)] for k in range(1, 6)]
    return '<aside class="rel"><h2>À lire aussi</h2><ul>' + ''.join(
        '<li><a href="{R}%s">%s</a></li>' % (x['slug'], esc(x['short'])) for x in links) + '</ul></aside>'

def messages_html():
    out = '<div class="msgs">'
    for i, (t, m) in enumerate(MESSAGES):
        m = m.replace('\\n', '\n')
        out += '<div class="msg"><h3>%s</h3><p class="mtext" id="m%d">%s</p><button class="btn ghost copy" data-t="m%d">📋 Copier</button></div>' % (
            esc(t), i, esc(m).replace('\n', '<br>'), i)
    out += '</div><script src="{R}assets/msg.js?v=1" defer></script>'
    return out

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
            '<script src="{R}assets/data.js?v=1"></script><script src="{R}assets/checklist.js?v=1" defer></script>')

    # Accueil
    guides_cards = ''.join('<a class="card" href="{R}%s"><strong>%s</strong><span>%s</span></a>' % (x['slug'], esc(x['short']), esc(x['desc'][:110].rsplit(' ', 1)[0] + '...')) for x in GUIDES[:6])
    fh, fs = faq_block(FAQ_HOME)
    home = f'''<section class="hero">
<h1>Ta liste de naissance, prête en 5 minutes</h1>
<p>{total} articles triés par pièce, les vrais indispensables d'abord. Coche ce que tu veux, retrouve chaque article sur Amazon, et profite de la réduction de la liste de naissance.</p>
<div class="hbtn"><a class="btn big" href="{{R}}checklist/">✅ Commencer ma checklist</a>
<a class="btn ghost big" href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Créer ma liste Amazon ↗</a></div>
<ul class="pts"><li>Gratuit, sans inscription</li><li>Enregistré sur ton téléphone</li><li>Conseils de parents</li></ul>
</section>
<h2>Les guides pour bien préparer l'arrivée de bébé</h2>
<div class="cards">{guides_cards}</div>
<p><a href="{{R}}guides/">Voir tous les guides →</a></p>
<h2>Comment ça marche ?</h2>
<ol class="steps"><li><strong>Coche</strong> les articles dans la <a href="{{R}}checklist/">checklist</a>.</li>
<li><strong>Ouvre</strong> chaque article sur Amazon et ajoute-le à ta liste de naissance.</li>
<li><strong>Partage</strong> ta liste avec nos <a href="{{R}}message-liste-de-naissance/">messages tout prêts</a>.</li>
<li><strong>Achète</strong> ce qui reste avec la réduction (<a href="{{R}}liste-de-naissance-amazon/">conditions</a>).</li></ol>
{fh}'''
    page('', 'Liste de naissance : checklist complète et idées (%d)' % YEAR,
         'Fais ta liste de naissance en 5 minutes : checklist gratuite de %d articles triés par pièce, conseils de parents et réduction de la liste Amazon.' % total,
         home, schema=fs)

    # Checklist
    ck = f'''<h1>Checklist liste de naissance</h1>
<p class="lead">{total} articles triés par usage. Coche ce que tu veux mettre dans ta liste : tes choix restent enregistrés sur cet appareil. Chaque article s'ouvre sur Amazon.</p>
{CTA}
{tool}
<h2>Comment utiliser cette checklist ?</h2>
<p>Commence par filtrer sur <strong>Indispensable</strong> : c'est ce dont tu as besoin dès le retour de la maternité. Ajoute ensuite les articles <strong>Utile</strong>, qui font de très bons cadeaux pour la famille. Les articles <strong>En option</strong> peuvent attendre les mois suivants.</p>
<p>Pour chaque article, ouvre la recherche Amazon, choisis le modèle qui te plaît et clique sur « Ajouter à la liste de naissance ». Une fois ta liste remplie, partage-la avec nos <a href="{{R}}message-liste-de-naissance/">messages tout prêts</a>.</p>'''
    schema = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "Checklist liste de naissance",
               "applicationCategory": "LifestyleApplication", "operatingSystem": "Tous", "url": BASE + '/checklist/',
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
    page('checklist/', 'Checklist liste de naissance gratuite (%d articles)' % total,
         'Checklist interactive pour ta liste de naissance : %d articles triés par pièce (sommeil, sorties, repas, toilette), avec les indispensables et des conseils.' % total,
         ck, schema=schema, crumbs=[('Checklist', 'checklist/')])

    # Guides
    for x in GUIDES:
        fh, fs = faq_block(x['faq'])
        body = x['body'].replace('{CTA}', CTA).replace('{MSGS}', messages_html())
        body = re.sub(r'\{AMZ:([^}]+)\}', lambda m: amz(m.group(1)), body)
        art = [{"@context": "https://schema.org", "@type": "Article", "headline": x['h1'], "description": x['desc'],
                "inLanguage": "fr-FR", "datePublished": "2026-11-14", "dateModified": "2026-11-14",
                "author": {"@type": "Organization", "name": SITE}, "mainEntityOfPage": BASE + '/' + x['slug']}]
        b = '<article><h1>%s</h1>%s%s</article>%s' % (esc(x['h1']), body, fh, related(x['slug']))
        page(x['slug'], x['title'], x['desc'], b, schema=art + fs,
             crumbs=[('Guides', 'guides/'), (x['short'], x['slug'])])

    idx = '<h1>Guides liste de naissance</h1><p class="lead">Tout pour préparer l\'arrivée de bébé sans stress.</p><div class="cards">' + ''.join(
        '<a class="card" href="{R}%s"><strong>%s</strong><span>%s</span></a>' % (x['slug'], esc(x['h1']), esc(x['desc'])) for x in GUIDES) + '</div>'
    page('guides/', 'Guides liste de naissance et préparation bébé',
         'Tous nos guides pour préparer ta liste de naissance : que mettre, petit budget, jumeaux, 2e enfant, valise maternité, messages et idées cadeaux.',
         idx, crumbs=[('Guides', 'guides/')])

    # Pages légales
    ml = f'''<h1>Mentions légales</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, CA 94107, États-Unis.</p>
<h2>Affiliation</h2><p>{DISCLOSURE} Les liens vers Amazon.fr sont des liens d'affiliation : si tu achètes après avoir cliqué, nous touchons une commission, sans surcoût pour toi. Le choix des articles reste indépendant.</p>
<h2>Responsabilité</h2><p>Les conseils de ce site sont donnés à titre informatif. Ils ne remplacent pas l'avis d'un professionnel de santé (médecin, sage-femme, pédiatre). Les conditions des offres Amazon peuvent changer à tout moment.</p>'''
    page('mentions-legales/', 'Mentions légales | Liste de Naissance', 'Mentions légales du site listedenaissance.xyz.', ml, crumbs=[('Mentions légales', 'mentions-legales/')])
    cf = f'''<h1>Confidentialité</h1>
<p>Ce site ne demande aucune inscription et ne collecte aucune donnée personnelle.</p>
<h2>Ta checklist</h2><p>Les articles que tu coches sont enregistrés uniquement dans ton navigateur (stockage local). Rien n'est envoyé sur un serveur. Vider les données du navigateur efface ta checklist.</p>
<h2>Amazon</h2><p>Quand tu cliques sur un lien vers Amazon.fr, Amazon peut déposer des cookies pour attribuer la commission. Consulte la politique de confidentialité d'Amazon pour en savoir plus.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p>'''
    page('confidentialite/', 'Confidentialité | Liste de Naissance', 'Politique de confidentialité de listedenaissance.xyz : aucune donnée collectée.', cf, crumbs=[('Confidentialité', 'confidentialite/')])

    # 404
    page('404-tmp/', 'Page introuvable | Liste de Naissance', 'Page introuvable.',
         '<h1>Page introuvable</h1><p><a href="/checklist/">Va plutôt voir la checklist</a> ou <a href="/">l\'accueil</a>.</p>')
    shutil.move(os.path.join(OUT, '404-tmp', 'index.html'), os.path.join(OUT, '404.html'))
    shutil.rmtree(os.path.join(OUT, '404-tmp')); PAGES.remove('404-tmp/')
    with open(os.path.join(OUT, '404.html'), encoding='utf-8') as f: t = f.read()
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(t.replace('href="../', 'href="/').replace('src="../', 'src="/').replace('<head>', '<head>\n<meta name="robots" content="noindex">'))

    # sitemap, robots, CNAME
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        '<url><loc>%s/%s</loc><lastmod>2026-11-14</lastmod></url>\n' % (BASE, p) for p in PAGES) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % BASE)
    open(os.path.join(OUT, 'CNAME'), 'w').write(DOMAIN + '\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print(len(PAGES), 'pages,', total, 'articles')

if __name__ == '__main__':
    build()
