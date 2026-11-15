# -*- coding: utf-8 -*-
# Outils gratuits de Ma liste bébé
# TOOLS : liste de dict(slug, title, h1, desc, short, emoji, tint, tool, body, faq)

TOOLS = []

def t(**k):
    TOOLS.append(k)

t(slug='calcul-date-accouchement/',
  title="Calcul de la date d'accouchement (DPA) et calendrier",
  h1="Calcul de la date d'accouchement",
  short="Calcul date d'accouchement",
  desc="Calcule ta date prévue d'accouchement selon la convention française (41 SA), ton nombre de semaines d'aménorrhée et ton calendrier de préparation.",
  emoji='📅', tint='lilas',
  tool="""<form id="t-dpa" class="accf tool-form">
<label>Je connais<select id="t-mode"><option value="ddr">la date de mes dernières règles</option><option value="conc">la date de conception</option></select></label>
<label><span id="t-date-label">Premier jour des dernières règles</span><input type="date" id="t-date" required></label>
<label id="t-cycle-row">Durée habituelle de ton cycle (en jours)<input type="number" id="t-cycle" value="28" min="21" max="45" inputmode="numeric"></label>
<button class="btn" type="submit">Calculer ma date</button>
</form>
<div id="t-out" class="tool-res" hidden aria-live="polite"></div>""",
  body="""
<h2>Comment le calcul fonctionne</h2>
<p>En France, la date prévue d'accouchement (DPA) est fixée par convention à <strong>41 semaines d'aménorrhée</strong> (SA) après le premier jour des dernières règles, soit 287 jours. Ailleurs, on compte souvent 40 semaines : c'est pour cela que certains calculateurs étrangers donnent une date une semaine plus tôt.</p>
<p>Les semaines d'aménorrhée se comptent depuis le premier jour des dernières règles. Les semaines de grossesse se comptent depuis la fécondation, environ deux semaines plus tard. 41 SA correspondent donc à 39 semaines de grossesse.</p>
<h2>Si ton cycle n'est pas de 28 jours</h2>
<p>Le calcul de base suppose une ovulation au 14e jour d'un cycle de 28 jours. Avec un cycle plus long, l'ovulation arrive plus tard, et la date d'accouchement aussi. L'outil décale la date d'autant de jours que ton cycle dépasse 28 jours (ou l'avance s'il est plus court). Si tes cycles sont très irréguliers, la date des règles est peu fiable : l'échographie de datation sera plus précise.</p>
<h2>SA, mois et trimestres</h2>
<table><thead><tr><th>Repère</th><th>Semaines d'aménorrhée</th></tr></thead><tbody>
<tr><td>1er trimestre</td><td>jusqu'à 14 SA environ</td></tr>
<tr><td>2e trimestre</td><td>de 14 à 28 SA environ</td></tr>
<tr><td>3e trimestre</td><td>à partir de 28 SA</td></tr>
<tr><td>Date prévue d'accouchement</td><td>41 SA</td></tr>
</tbody></table>
<h2>Ton calendrier de préparation</h2>
<p>L'outil te propose aussi des repères pour préparer l'arrivée de bébé : créer ta liste vers le 5e mois, la partager au 6e, préparer la <a href="{R}valise-maternite/">valise de maternité</a> vers le 7e mois et avoir l'essentiel à la maison au 8e. Pour savoir quoi mettre dans ta liste, ouvre notre <a href="{R}checklist/">checklist</a> ou lis <a href="{R}quand-faire-sa-liste-de-naissance/">quand faire sa liste de naissance</a>.</p>
<h2>Une date indicative</h2>
<p>Peu de bébés naissent pile le jour prévu : la naissance arrive souvent dans les jours ou semaines autour de cette date. C'est ton médecin ou ta sage-femme qui fixe la date officielle, en général après l'échographie du premier trimestre. Cet outil ne remplace pas un avis médical.</p>
""",
  faq=[("Pourquoi ma date est différente d'un autre calculateur ?", "En France, on compte 41 semaines d'aménorrhée (287 jours) après les dernières règles. Beaucoup de calculateurs étrangers comptent 40 semaines, soit une semaine de moins."),
       ("Quelle date garder : celle du calcul ou celle de l'échographie ?", "Celle de ton médecin ou de ta sage-femme, souvent ajustée après l'échographie de datation. Le calcul en ligne reste une estimation."),
       ("Combien de semaines de grossesse font 41 SA ?", "41 semaines d'aménorrhée correspondent à environ 39 semaines de grossesse, car la fécondation a lieu environ deux semaines après le début des règles.")])

t(slug='calculateur-trousseau-bebe/',
  title="Calculateur de trousseau bébé : combien de bodies ?",
  h1="Calculateur de trousseau bébé",
  short="Calculateur de trousseau",
  desc="Combien de bodies, pyjamas, bavoirs et langes acheter pour bébé ? Calcule ton trousseau selon la fréquence de tes lessives et la saison de naissance.",
  emoji='🧺', tint='ciel',
  tool="""<form id="t-trousseau" class="accf tool-form">
<label>Tu fais une lessive tous les<select id="t-wash"><option value="1">jours</option><option value="2">2 jours</option><option value="3" selected>3 jours</option><option value="4">4 jours</option><option value="5">5 jours</option><option value="7">7 jours</option></select></label>
<label>Bébé naît en<select id="t-season"><option value="hiver">automne ou hiver</option><option value="mi">printemps</option><option value="ete">été</option></select></label>
<button class="btn" type="submit">Calculer mon trousseau</button>
</form>
<div id="t-out" class="tool-res" hidden aria-live="polite"></div>""",
  body="""
<h2>Comment le calcul fonctionne</h2>
<p>Un nouveau-né se change souvent : couche qui déborde, régurgitation, bavoir trempé. Le calculateur part d'une consommation moyenne par jour (environ 2 bodies, 1 à 2 pyjamas, 2 bavoirs) et la multiplie par le nombre de jours entre deux lessives, plus un jour pour le séchage. Résultat : tu ne te retrouves jamais à court, sans acheter des piles de vêtements trop petits dans un mois.</p>
<h2>Ne pas acheter trop de taille naissance</h2>
<p>C'est l'erreur la plus fréquente. Beaucoup de bébés portent la taille naissance quelques semaines seulement, et certains passent directement à la taille 1 mois. Prends environ la moitié des quantités en naissance, et le reste en 1 mois et 3 mois. Notre guide <a href="{R}combien-de-bodies-et-pyjamas-pour-bebe/">combien de bodies et de pyjamas</a> détaille les quantités taille par taille.</p>
<h2>Selon la saison</h2>
<table><thead><tr><th>Saison</th><th>À ajouter</th></tr></thead><tbody>
<tr><td>Automne, hiver</td><td>Gilet supplémentaire, bonnet chaud, combinaison pilote, chancelière</td></tr>
<tr><td>Printemps</td><td>Gilets légers, une tenue plus chaude pour les soirées</td></tr>
<tr><td>Été</td><td>Bodies à manches courtes, voile léger pour la poussette</td></tr>
</tbody></table>
<p>Pour aller plus loin, lis nos guides <a href="{R}liste-de-naissance-bebe-ne-en-hiver/">bébé né en hiver</a> et <a href="{R}liste-de-naissance-bebe-ne-en-ete/">bébé né en été</a>, puis ajoute le trousseau à ta liste avec notre <a href="{R}checklist/">checklist</a>.</p>
<h2>Les vêtements, un cadeau facile pour les proches</h2>
<p>Les vêtements sont parmi les cadeaux les plus offerts, souvent sans être sur la liste. Pour éviter de recevoir dix tenues taille naissance, indique dans ta liste les tailles qui te manquent vraiment, surtout 3 et 6 mois.</p>
""",
  faq=[("Combien de bodies pour un nouveau-né ?", "Avec une lessive tous les 2 ou 3 jours, compte 6 à 8 bodies par taille, et environ la moitié en taille naissance."),
       ("Faut-il laver les vêtements de bébé avant de les mettre ?", "Oui, c'est conseillé pour retirer les apprêts du neuf. Utilise une lessive douce.")])
