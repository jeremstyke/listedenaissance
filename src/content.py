# -*- coding: utf-8 -*-
# Contenu du site malistebebe.fr

# Checklist : (categorie, emoji, [(article, recherche Amazon, priorite, conseil)])
# priorite : 1 = indispensable, 2 = utile, 3 = en option
CHECKLIST = [
  ("Sommeil", "🌙", [
    ("Lit bébé ou berceau", "lit bebe 60x120", 1, "Un lit à barreaux 60x120 sert jusqu'à 2 ou 3 ans, un berceau seulement 4 à 6 mois."),
    ("Matelas bébé ferme", "matelas bebe 60x120", 1, "Ferme, à la taille exacte du lit, sans espace sur les côtés."),
    ("Alèses imperméables (x2)", "alese bebe 60x120", 1, "Toujours en avoir une de rechange pour les nuits agitées."),
    ("Draps housses (x3)", "drap housse bebe 60x120", 1, "Pas de couette ni d'oreiller avant 1 an."),
    ("Gigoteuses ou turbulettes (x2)", "gigoteuse naissance 0-6 mois", 1, "Choisis l'indice TOG selon la saison et la chambre."),
    ("Babyphone", "babyphone", 2, "Audio suffit souvent, la vidéo rassure dans un grand logement."),
    ("Veilleuse", "veilleuse bebe", 2, "Pratique pour les tétées de nuit sans réveiller tout le monde."),
    ("Lit cododo", "lit cododo", 3, "Utile si tu allaites et veux bébé près de toi les premiers mois."),
    ("Mobile musical", "mobile musical bebe", 3, "Un joli cadeau à proposer à la famille."),
  ]),
  ("Sorties", "🚼", [
    ("Poussette", "poussette", 1, "Plie-la en magasin ou regarde les vidéos : le pliage compte plus que le look."),
    ("Siège auto i-Size (groupe 0+)", "siege auto i-size naissance", 1, "Obligatoire pour sortir de la maternité en voiture."),
    ("Base Isofix", "base isofix i-size", 2, "Le siège se clipse en 2 secondes, plus sûr qu'une ceinture mal passée."),
    ("Porte-bébé physiologique", "porte bebe physiologique", 2, "Mains libres, bébé contre toi : souvent le meilleur achat des 6 premiers mois."),
    ("Sac à langer", "sac a langer", 1, "Un modèle sac à dos se porte plus facilement avec une poussette."),
    ("Chancelière ou nid d'ange", "chanceliere poussette", 2, "Indispensable pour un bébé d'hiver."),
    ("Ombrelle ou voile de poussette", "voile anti uv poussette", 3, "Pour un bébé d'été."),
    ("Lit parapluie", "lit parapluie", 3, "Pour dormir chez les grands-parents ou en vacances."),
  ]),
  ("Repas", "🍼", [
    ("Biberons (x4 à 6)", "biberon naissance", 1, "Même si tu allaites, 1 ou 2 biberons dépannent."),
    ("Goupillon", "goupillon biberon", 1, "Pour laver les tétines sans les abîmer."),
    ("Stérilisateur", "sterilisateur biberon", 2, "Utile surtout les premiers mois."),
    ("Chauffe-biberon", "chauffe biberon", 2, "Pratique la nuit et en voiture avec un modèle nomade."),
    ("Tire-lait", "tire lait electrique", 2, "Souvent remboursé en location en pharmacie : vérifie avant d'acheter."),
    ("Coussin d'allaitement", "coussin allaitement", 2, "Sert aussi de coussin de grossesse avant la naissance."),
    ("Coussinets d'allaitement", "coussinets allaitement lavables", 2, "Les lavables reviennent moins cher."),
    ("Bavoirs (x6)", "bavoir bebe lot", 1, "Les bavoirs bandana servent aussi pour les dents."),
    ("Chaise haute", "chaise haute evolutive", 3, "Pas avant 6 mois, mais c'est un beau cadeau de groupe."),
  ]),
  ("Toilette et soins", "🛁", [
    ("Baignoire bébé ou transat de bain", "baignoire bebe", 1, "Un modèle pliable si tu manques de place."),
    ("Thermomètre de bain", "thermometre bain bebe", 1, "L'eau doit être autour de 37 °C."),
    ("Matelas à langer", "matelas a langer", 1, "Sur une commode, il évite d'acheter une table à langer."),
    ("Capes de bain (x2)", "cape de bain bebe", 1, "Avec capuche, pour ne pas refroidir bébé."),
    ("Thermomètre médical", "thermometre bebe", 1, "Un modèle rectal reste la référence pour les bébés."),
    ("Mouche-bébé", "mouche bebe", 1, "Le premier rhume arrive toujours plus vite que prévu."),
    ("Coupe-ongles ou ciseaux bébé", "ciseaux ongles bebe", 1, "Bout arrondi obligatoire."),
    ("Brosse à cheveux douce", "brosse cheveux bebe", 2, "Pratique contre les croûtes de lait."),
    ("Table à langer", "table a langer", 3, "Seulement si tu n'as pas de commode à la bonne hauteur."),
    ("Poubelle à couches", "poubelle a couches", 3, "Limite les odeurs, mais les recharges coûtent cher."),
  ]),
  ("Vêtements", "👶", [
    ("Bodies naissance et 1 mois (x8)", "body bebe naissance lot", 1, "Ne prends pas trop de taille naissance : bébé grandit vite."),
    ("Pyjamas (x6)", "pyjama bebe naissance lot", 1, "Avec pressions devant, plus faciles à mettre."),
    ("Gilets (x2)", "gilet bebe naissance", 1, "Plus pratiques qu'un pull pour un nouveau-né."),
    ("Bonnet naissance", "bonnet naissance", 1, "Pour les premiers jours, même en été."),
    ("Chaussettes et chaussons", "chaussettes bebe naissance", 1, "Les chaussons tiennent mieux que les chaussettes."),
    ("Combinaison pilote", "combinaison pilote bebe", 2, "Pour un bébé né en automne ou en hiver."),
    ("Lange en coton (x4)", "langes coton bebe", 1, "Le couteau suisse des parents : bavoir, ombre, plaid..."),
  ]),
  ("Éveil", "🧸", [
    ("Tapis d'éveil", "tapis d'eveil bebe", 2, "Bébé y passe beaucoup de temps dès les premières semaines."),
    ("Transat", "transat bebe", 2, "Pour garder bébé près de toi pendant que tu cuisines."),
    ("Doudou", "doudou bebe", 2, "Achète-le en double, le jour où il se perd tu nous remercieras."),
    ("Hochets et anneaux de dentition", "hochet bebe", 3, "Petits cadeaux faciles à proposer."),
    ("Livres en tissu", "livre tissu bebe", 3, "Pour les premiers mois."),
    ("Parc bébé", "parc bebe", 3, "Plutôt vers 6 mois, quand bébé commence à bouger."),
  ]),
  ("Sécurité et maison", "🏠", [
    ("Détecteur de fumée", "detecteur de fumee", 1, "Obligatoire dans chaque logement, vérifie qu'il fonctionne."),
    ("Barrière de sécurité", "barriere securite bebe", 3, "Pour plus tard, quand bébé marche à quatre pattes."),
    ("Cache-prises", "cache prise bebe", 3, "Pareil, vers 6 à 8 mois."),
    ("Humidificateur", "humidificateur bebe", 3, "Utile si la chambre est très sèche l'hiver."),
  ]),
]

PRIO = {1: "Indispensable", 2: "Utile", 3: "En option"}

# Guides : slug -> dict
GUIDES = []

def g(slug, title, h1, desc, body, faq=None, short=None):
    GUIDES.append(dict(slug=slug, title=title, h1=h1, desc=desc, body=body, faq=faq or [], short=short or h1))

g("liste-de-naissance-amazon/",
  "Liste de naissance Amazon : réduction, cadeau, avis (2026)",
  "Liste de naissance Amazon : comment ça marche ?",
  "Réduction jusqu'à 15 %, cadeau offert, délai de 14 jours, articles exclus : tout ce qu'il faut savoir avant de créer ta liste de naissance Amazon.",
  """
<p>La liste de naissance Amazon est gratuite et se crée en quelques minutes. Tes proches voient la liste, achètent un article, et il disparaît de la liste pour éviter les doublons. Le vrai intérêt, c'est la <strong>réduction sur les articles qui restent</strong> à la fin.</p>
{CTA}
<h2>La réduction de la liste de naissance</h2>
<p>Amazon propose une remise allant jusqu'à <strong>15 %</strong> sur une sélection d'articles bébé ajoutés à ta liste. Les conditions affichées en 2026 sont les suivantes :</p>
<ul>
<li>la réduction s'utilise de <strong>180 jours avant</strong> la date prévue d'arrivée de bébé jusqu'à <strong>90 jours après</strong> ;</li>
<li>la liste doit être <strong>active depuis au moins 14 jours</strong> ;</li>
<li>il faut ajouter l'article au panier <strong>depuis ta liste</strong>, sinon la remise ne s'applique pas ;</li>
<li>seuls les articles éligibles comptent, en général ceux vendus et expédiés par Amazon. Les couches, le lait infantile et l'alimentation bébé sont souvent exclus.</li>
</ul>
<p>Le taux exact (10 ou 15 %) et le plafond peuvent changer selon que tu es membre Prime ou non. Amazon affiche les conditions à jour directement dans ta liste : vérifie-les avant une grosse commande comme une poussette.</p>
<h2>Le cadeau de bienvenue</h2>
<p>Amazon offre aussi un petit cadeau (une box d'échantillons ou un article au choix selon les périodes) quand tu passes une première commande depuis ta liste. Cette offre est en général réservée aux membres Prime, ou à ceux qui activent l'essai gratuit.</p>
<h2>Créer sa liste en 4 étapes</h2>
<ol>
<li><strong>Crée la liste</strong> avec ton compte Amazon : nom, date prévue d'arrivée, et éventuellement un cotitulaire.</li>
<li><strong>Remplis-la</strong> avec notre <a href="{R}checklist/">checklist interactive</a> pour ne rien oublier.</li>
<li><strong>Partage le lien</strong> par SMS, e-mail ou WhatsApp. On te donne des <a href="{R}message-liste-de-naissance/">messages tout prêts</a>.</li>
<li><strong>Attends 14 jours</strong>, puis achète toi-même ce qui reste avec la réduction.</li>
</ol>
<h2>Notre avis</h2>
<p>Pour la plupart des parents, c'est la liste la plus simple : le catalogue est immense, la livraison rapide, et les proches éloignés participent en deux clics. Ses limites : pas d'articles de petits créateurs, pas de cagnotte libre comme sur certaines listes multi-boutiques, et une réduction qui ne marche que sur les articles éligibles. Beaucoup de parents combinent une liste Amazon pour le matériel et une cagnotte pour le reste.</p>
<h2>Astuce : mets les gros articles dans ta liste</h2>
<p>Même si tu comptes acheter la poussette ou le siège auto toi-même, ajoute-les à ta liste. Si personne ne les offre, tu les achètes avec la réduction. Sur un siège auto à 300 €, 15 % font 45 € d'économie.</p>
""",
  faq=[
    ("La liste de naissance Amazon est-elle gratuite ?", "Oui. La création et le partage sont gratuits, et l'abonnement Prime n'est pas obligatoire pour créer la liste."),
    ("Quand la réduction de la liste de naissance commence-t-elle ?", "La liste doit être active depuis au moins 14 jours. La remise s'utilise ensuite de 180 jours avant à 90 jours après la date prévue d'arrivée."),
    ("Les couches sont-elles concernées par la réduction ?", "En général non : les couches, le lait infantile et l'alimentation bébé sont exclus. Amazon indique dans ta liste quels articles sont éligibles."),
    ("Mes proches voient-ils mon adresse ?", "Tes proches peuvent faire livrer le cadeau chez toi. Vérifie dans les paramètres de ta liste ce qui est affiché avant de la partager."),
  ],
  short="Liste de naissance Amazon : le guide")

g("quoi-mettre-dans-une-liste-de-naissance/",
  "Quoi mettre dans une liste de naissance ? La liste complète",
  "Quoi mettre dans une liste de naissance ?",
  "Les indispensables, les articles utiles et ceux dont tu peux te passer : la liste de naissance complète, triée par pièce, avec des conseils de parents.",
  """
<p>Une bonne liste de naissance contient <strong>40 à 60 articles</strong>, avec des prix variés pour que chacun puisse participer : des bodies à 15 € jusqu'à la poussette pour un cadeau de groupe. Voici l'essentiel, trié par usage.</p>
{CTA}
<h2>Les vrais indispensables</h2>
<p>Ce sont les articles dont tu as besoin dès le retour de la maternité :</p>
<ul>
<li><strong>pour dormir</strong> : un lit ou un berceau, un matelas ferme, deux alèses, trois draps housses, deux gigoteuses ;</li>
<li><strong>pour sortir</strong> : un siège auto i-Size (obligatoire en voiture), une poussette, un sac à langer ;</li>
<li><strong>pour la toilette</strong> : une baignoire, un thermomètre de bain, un matelas à langer, deux capes de bain, un thermomètre médical et un mouche-bébé ;</li>
<li><strong>pour manger</strong> : quelques biberons et un goupillon, même si tu allaites ;</li>
<li><strong>pour s'habiller</strong> : bodies, pyjamas, gilets, un bonnet et des chaussons, surtout en taille 1 mois.</li>
</ul>
<h2>Les articles utiles</h2>
<p>Babyphone, porte-bébé, base Isofix, chauffe-biberon, tapis d'éveil, transat : tu peux vivre sans, mais ils simplifient vraiment les premiers mois. Ce sont de très bons cadeaux à proposer à la famille.</p>
<h2>Ce que tu peux éviter</h2>
<ul>
<li><strong>trop de vêtements taille naissance</strong> : beaucoup de bébés ne les portent que 2 ou 3 semaines ;</li>
<li><strong>le tour de lit, la couette et l'oreiller</strong> : déconseillés avant 1 an pour la sécurité du sommeil ;</li>
<li><strong>la table à langer</strong> si tu as une commode à la bonne hauteur ;</li>
<li><strong>les gadgets</strong> (chauffe-lingettes, presse-purée électrique...) qui finissent souvent dans un placard.</li>
</ul>
<h2>Fais ta liste en 5 minutes</h2>
<p>Notre <a href="{R}checklist/">checklist interactive</a> reprend tous ces articles. Tu coches ce que tu veux, chaque article mène vers Amazon, et ta sélection reste enregistrée sur ton téléphone.</p>
""",
  faq=[
    ("Combien d'articles mettre dans une liste de naissance ?", "Entre 40 et 60 articles en général, avec des prix variés pour que chaque proche trouve un cadeau à son budget."),
    ("Faut-il mettre des vêtements dans sa liste de naissance ?", "Oui, mais surtout en taille 1 et 3 mois. Les vêtements taille naissance sont portés très peu de temps."),
  ],
  short="Quoi mettre dans sa liste")

g("liste-de-naissance-petit-budget/",
  "Liste de naissance petit budget : l'essentiel sans se ruiner",
  "Liste de naissance petit budget",
  "Comment faire une liste de naissance utile avec un petit budget : les vrais indispensables, ce qu'on peut acheter d'occasion et les astuces pour payer moins cher.",
  """
<p>Un bébé n'a pas besoin de grand-chose les premiers mois : dormir en sécurité, être nourri, propre et au chaud. Avec un petit budget, l'idée est de <strong>mettre l'essentiel sur la liste</strong> et de ne rien acheter en double.</p>
{CTA}
<h2>Ce qui doit être neuf</h2>
<ul>
<li><strong>le siège auto</strong> : un siège d'occasion a pu subir un choc invisible ;</li>
<li><strong>le matelas</strong> : pour l'hygiène et la fermeté ;</li>
<li><strong>les tétines et biberons</strong>.</li>
</ul>
<h2>Ce qui se trouve facilement d'occasion</h2>
<p>Le lit à barreaux, la baignoire, le transat, le tapis d'éveil, les vêtements et même la poussette (si le pliage et les freins fonctionnent bien). Garde ta liste pour le neuf et demande à ton entourage ce qu'il peut prêter.</p>
<h2>Les 5 astuces qui font vraiment économiser</h2>
<ol>
<li><strong>Utilise la réduction de ta liste</strong> sur les articles restants : jusqu'à 15 % sur Amazon (voir <a href="{R}liste-de-naissance-amazon/">notre guide</a>).</li>
<li><strong>Choisis du matériel évolutif</strong> : un lit 60x120 plutôt qu'un berceau, une chaise haute évolutive.</li>
<li><strong>Remplace la table à langer</strong> par un matelas posé sur une commode.</li>
<li><strong>Loue le tire-lait</strong> en pharmacie : il est souvent remboursé sur prescription.</li>
<li><strong>Propose des cadeaux de groupe</strong> pour les gros articles : poussette, siège auto.</li>
</ol>
<p>Dans notre <a href="{R}checklist/">checklist</a>, filtre sur « Indispensable » : il te reste une trentaine d'articles, pas plus.</p>
""",
  short="Petit budget")

g("liste-de-naissance-jumeaux/",
  "Liste de naissance jumeaux : quoi prendre en double ?",
  "Liste de naissance pour des jumeaux",
  "Liste de naissance jumeaux : ce qu'il faut acheter en double, ce qu'un seul exemplaire suffit, et le matériel spécial (poussette double, coussin d'allaitement jumeaux).",
  """
<p>Avec des jumeaux, tout ne se double pas. Le secret d'une bonne liste, c'est de savoir <strong>ce qui doit être en double</strong>, ce qui se partage, et le matériel spécial jumeaux.</p>
{CTA}
<h2>À prendre en double</h2>
<ul>
<li><strong>2 sièges auto</strong> (obligatoire) et idéalement 2 bases Isofix ;</li>
<li><strong>2 lits</strong> à terme, même si les bébés peuvent partager un lit les premières semaines selon l'avis de ta sage-femme ;</li>
<li>gigoteuses, draps, bodies et pyjamas : <strong>deux fois plus</strong> ;</li>
<li><strong>2 transats</strong> : c'est ce qui te libère les mains quand les deux bébés sont réveillés.</li>
</ul>
<h2>Un seul exemplaire suffit</h2>
<p>Baignoire, matelas à langer, thermomètres, babyphone, stérilisateur, tapis d'éveil : un seul suffit, les bébés y passent à tour de rôle.</p>
<h2>Le matériel spécial jumeaux</h2>
<ul>
<li><strong>une poussette double</strong> : côte à côte (plus large) ou l'un derrière l'autre (plus étroite mais plus longue). Mesure tes portes avant !</li>
<li><strong>un coussin d'allaitement jumeaux</strong> pour nourrir les deux en même temps ;</li>
<li><strong>un grand sac à langer</strong>.</li>
</ul>
<p>Pense aux cadeaux de groupe : une poussette double coûte vite plus de 500 €. Notre <a href="{R}checklist/">checklist</a> t'aide à ne rien oublier.</p>
""",
  short="Jumeaux")

g("liste-de-naissance-petit-appartement/",
  "Liste de naissance petit appartement : le matériel compact",
  "Liste de naissance pour un petit appartement",
  "Bébé dans un petit appartement : quel matériel choisir pour gagner de la place (poussette compacte, baignoire pliable, lit cododo) et ce qu'il vaut mieux éviter.",
  """
<p>Dans 40 m², chaque meuble compte. Bonne nouvelle : un bébé peut très bien vivre dans un petit logement, à condition de choisir du <strong>matériel pliable ou multifonction</strong>.</p>
{CTA}
<h2>Les bons choix pour gagner de la place</h2>
<ul>
<li><strong>une poussette compacte</strong> qui se plie d'une main et se range dans un placard ;</li>
<li><strong>une baignoire pliable</strong> qui se glisse derrière une porte ;</li>
<li><strong>un lit cododo</strong> collé à ton lit les premiers mois, au lieu d'une chambre bébé complète ;</li>
<li><strong>un matelas à langer sur une commode</strong>, pas de table à langer ;</li>
<li><strong>un porte-bébé</strong> qui remplace souvent la poussette en ville.</li>
</ul>
<h2>Ce qu'il vaut mieux éviter</h2>
<p>Le parc, la grande chaise haute, le trio poussette et nacelle encombrant, et les doublons (deux transats, deux baignoires...). Si tu vis en étage sans ascenseur, pense aussi au poids de la poussette.</p>
<p>Dans notre <a href="{R}checklist/">checklist</a>, garde les « Indispensable » et choisis les modèles compacts.</p>
""",
  short="Petit appartement")

g("liste-de-naissance-deuxieme-enfant/",
  "Liste de naissance 2e enfant : quoi demander ?",
  "Liste de naissance pour un deuxième enfant",
  "Pour un deuxième bébé, on a déjà presque tout. Voici quoi mettre dans une liste de naissance pour un 2e enfant : ce qu'il faut remplacer et les idées utiles.",
  """
<p>Pour un deuxième enfant, la question n'est plus « qu'est-ce qu'il nous faut ? » mais « <strong>qu'est-ce qu'il faut remplacer ou compléter ?</strong> ». Une liste reste utile : ta famille voudra offrir quelque chose.</p>
{CTA}
<h2>Ce qu'il faut souvent remplacer</h2>
<ul>
<li><strong>le siège auto</strong> s'il est périmé ou a subi un choc (regarde la date sur l'étiquette) ;</li>
<li><strong>le matelas</strong>, pour l'hygiène ;</li>
<li><strong>les tétines et biberons</strong> ;</li>
<li>les vêtements, si le sexe ou la saison de naissance sont différents.</li>
</ul>
<h2>Ce qu'il faut ajouter</h2>
<ul>
<li><strong>une planche à roulettes ou une poussette double</strong> selon l'âge de l'aîné ;</li>
<li><strong>un deuxième lit</strong> si l'aîné n'est pas encore passé dans un grand lit ;</li>
<li><strong>un porte-bébé</strong> pour garder les mains libres avec l'aîné ;</li>
<li><strong>un cadeau pour l'aîné</strong> « de la part du bébé » : ça aide beaucoup à accueillir le petit frère ou la petite sœur.</li>
</ul>
<p>Coche dans notre <a href="{R}checklist/">checklist</a> ce que tu as déjà : il ne te restera que les manques.</p>
""",
  short="2e enfant")

g("quand-faire-sa-liste-de-naissance/",
  "Quand faire sa liste de naissance ? Le bon moment",
  "Quand faire sa liste de naissance ?",
  "À quel mois de grossesse créer et partager sa liste de naissance, et pourquoi il vaut mieux ne pas attendre le dernier moment pour profiter de la réduction.",
  """
<p>Le bon moment, c'est <strong>vers le 5e ou 6e mois de grossesse</strong>. Tu connais souvent le sexe du bébé, tu as encore de l'énergie, et tes proches ont le temps d'acheter avant la naissance.</p>
{CTA}
<h2>Le calendrier idéal</h2>
<ul>
<li><strong>4e mois</strong> : tu repères le matériel, tu lis des avis, tu demandes ce qu'on peut te prêter ;</li>
<li><strong>5e et 6e mois</strong> : tu crées la liste et tu la remplis ;</li>
<li><strong>6e mois</strong> : tu la partages, idéalement avant une baby shower ou un repas de famille ;</li>
<li><strong>8e mois</strong> : tu achètes ce qui reste avec la réduction, pour avoir le siège auto et le lit avant la maternité.</li>
</ul>
<h2>Pourquoi ne pas attendre</h2>
<p>Sur Amazon, la réduction ne marche que si ta liste est active depuis au moins 14 jours (voir <a href="{R}liste-de-naissance-amazon/">notre guide</a>). Et un bébé peut arriver en avance : mieux vaut avoir l'essentiel à la maison dès le 8e mois.</p>
<h2>Et après la naissance ?</h2>
<p>Ta liste reste utile : beaucoup de proches offrent un cadeau à la naissance ou à la première visite. Garde-la à jour avec les articles des mois suivants (chaise haute, parc, vêtements 6 mois).</p>
""",
  short="Quand la faire")

g("message-liste-de-naissance/",
  "Message pour partager sa liste de naissance : 10 exemples",
  "Message pour partager sa liste de naissance",
  "10 exemples de messages pour partager ta liste de naissance par SMS, WhatsApp ou e-mail, sans gêne : famille, amis, collègues. À copier en un clic.",
  """
<p>Partager sa liste de naissance peut sembler gênant. En réalité, la plupart des proches sont <strong>contents d'avoir des idées</strong> : ça leur évite d'offrir le cinquième doudou. Voici des messages à copier.</p>
{MSGS}
<h2>Nos conseils</h2>
<ul>
<li><strong>envoie la liste à ceux qui la demandent</strong>, ou en même temps que l'annonce d'une baby shower ;</li>
<li><strong>pour les collègues</strong>, passe par la personne qui organise le cadeau commun ;</li>
<li><strong>remercie toujours</strong>, même pour un cadeau hors liste.</li>
</ul>
<p>Pas encore de liste ? Commence avec notre <a href="{R}checklist/">checklist</a>.</p>
""",
  short="Messages à copier")

g("valise-maternite/",
  "Valise maternité : la liste complète pour maman et bébé",
  "Valise maternité : la liste complète",
  "Que mettre dans la valise maternité ? La liste complète pour maman, pour bébé et pour le papa ou le co-parent, à préparer dès le 7e mois.",
  """
<p>Prépare la valise <strong>vers le 7e mois</strong> (et un peu avant si on attend des jumeaux). La maternité te donne souvent une liste : compare-la avec celle-ci.</p>
{CTA}
<h2>Pour bébé</h2>
<ul>
<li>6 bodies et 6 pyjamas (taille naissance et 1 mois) ;</li>
<li>2 gilets, 1 bonnet, des chaussons ;</li>
<li>2 gigoteuses, 2 capes de bain, quelques langes ;</li>
<li>une tenue de sortie et la combinaison si c'est l'hiver ;</li>
<li><strong>le siège auto</strong>, déjà installé dans la voiture.</li>
</ul>
<h2>Pour maman</h2>
<ul>
<li>tes papiers : carte Vitale, mutuelle, carnet de maternité, résultats d'examens ;</li>
<li>2 chemises de nuit ou t-shirts amples (qui s'ouvrent devant si tu allaites) ;</li>
<li>2 soutiens-gorge d'allaitement et des coussinets ;</li>
<li>des culottes jetables ou en coton et des serviettes de maternité ;</li>
<li>trousse de toilette, chaussons, peignoir ;</li>
<li>une tenue confortable pour la sortie.</li>
</ul>
<h2>Pour le co-parent</h2>
<p>Un chargeur long, des en-cas, une bouteille d'eau, de la monnaie pour le parking et une tenue de rechange. Les nuits à la maternité sont longues.</p>
<p>La valise est prête ? Vérifie que le reste est à la maison avec notre <a href="{R}checklist/">checklist</a>.</p>
""",
  short="Valise maternité")

g("idees-cadeau-de-naissance/",
  "Idées cadeau de naissance : utiles, originales, par budget",
  "Idées cadeau de naissance",
  "Tu cherches un cadeau de naissance ? Des idées utiles par budget (moins de 20 €, 50 €, 100 €, cadeau de groupe) qui feront vraiment plaisir aux jeunes parents.",
  """
<p>Le meilleur cadeau de naissance, c'est <strong>celui qui est sur la liste</strong>. Demande-la aux parents ! Si tu ne l'as pas, voici des idées qui servent vraiment.</p>
<h2>Moins de 20 €</h2>
<ul>
<li>des bodies en taille 3 ou 6 mois (on en reçoit trop en taille naissance) ;</li>
<li>un lot de langes en coton ;</li>
<li>un livre en tissu ou un hochet ;</li>
<li>un thermomètre de bain.</li>
</ul>
<h2>Autour de 50 €</h2>
<ul>
<li>une gigoteuse de qualité ;</li>
<li>un tapis d'éveil ;</li>
<li>un sac à langer ;</li>
<li>une veilleuse ou un mobile.</li>
</ul>
<h2>Autour de 100 €</h2>
<ul>
<li>un porte-bébé physiologique ;</li>
<li>un babyphone ;</li>
<li>un transat.</li>
</ul>
<h2>Cadeau de groupe</h2>
<p>Entre collègues ou en famille : la poussette, le siège auto et sa base, la chaise haute évolutive. Ce sont les plus gros postes de dépense pour les parents.</p>
<h2>Le cadeau qu'on oublie</h2>
<p>Un repas livré, une séance de ménage, ou garder l'aîné une après-midi. Les jeunes parents adorent.</p>
<p>Tu veux voir tout le matériel utile ? Regarde notre <a href="{R}checklist/">checklist complète</a>.</p>
""",
  short="Idées cadeau")

MESSAGES = [
  ("Famille, simple", "Coucou ! Plusieurs d'entre vous nous ont demandé ce qui nous ferait plaisir pour bébé. On a préparé une petite liste : {LIEN}. Aucune obligation bien sûr, votre présence est le plus beau des cadeaux ❤️"),
  ("Amis, détendu", "Hello la team ! Comme certains nous ont demandé des idées pour l'arrivée de bébé, voici notre liste : {LIEN}. Merci d'avance, on a hâte de vous le présenter 😊"),
  ("Grands-parents", "Bonjour Mamie, bonjour Papi, voici la liste de naissance dont on vous a parlé : {LIEN}. Vous cliquez sur l'article et vous le faites livrer chez nous, c'est tout simple. On vous embrasse !"),
  ("Collègues", "Bonjour à tous, merci beaucoup pour votre attention. Pour ceux qui ont demandé, voici notre liste de naissance : {LIEN}. Encore merci, à très vite avec des photos !"),
  ("Avec baby shower", "Vous êtes invités à notre baby shower le [date] à [lieu] 🍼 Si vous souhaitez nous offrir quelque chose, voici notre liste : {LIEN}. Le plus important, c'est que vous soyez là !"),
  ("Après la naissance", "Bébé est arrivé ! [Prénom] est né(e) le [date], tout le monde va bien ❤️ Pour ceux qui nous ont demandé des idées, notre liste est toujours ici : {LIEN}."),
  ("Court, par SMS", "Comme promis, notre liste de naissance : {LIEN} Merci !"),
  ("Deuxième enfant", "Pour l'arrivée du petit frère ou de la petite sœur, on a fait une petite liste avec ce qui nous manque encore : {LIEN}. Merci pour votre gentillesse !"),
  ("E-mail formel", "Bonjour,\\n\\nNous sommes heureux de vous annoncer l'arrivée prochaine de notre enfant. Plusieurs personnes nous ayant demandé des idées de cadeaux, nous avons créé une liste de naissance : {LIEN}\\n\\nMerci pour votre attention.\\n\\nBien à vous,"),
  ("Avec humour", "Bébé n'est pas encore là mais il a déjà une liste de souhaits plus longue que la nôtre 😅 La voici : {LIEN}. Merci d'avance de la part du futur boss de la maison !"),
]

FAQ_HOME = [
  ("C'est gratuit ?", "Oui, entièrement. La checklist marche même sans compte : tes choix restent alors sur ton appareil."),
  ("Est-ce que je peux sauvegarder ma liste ?", "Oui : tes cases cochées restent enregistrées sur ton appareil, tant que tu ne vides pas les données du navigateur. Tu peux aussi imprimer ta checklist ou copier ta liste avec le bouton « Partager ma liste ». Pour tes proches, partage directement ta liste Amazon : elle évite les doublons toute seule."),
  ("Est-ce que vous vendez les produits ?", "Non. Les articles mènent vers Amazon.fr. Si tu achètes après avoir cliqué, Amazon nous verse une petite commission, sans aucun surcoût pour toi."),
  ("Où créer ma liste en ligne ?", "Plusieurs solutions existent : site marchand, liste multi-boutiques, magasin de puériculture ou cagnotte. Notre comparatif t'aide à choisir. Le bouton « Créer ma liste en ligne » ouvre la liste de naissance Amazon, notre choix pour sa simplicité."),
]

g("trousseau-de-naissance/",
  "Trousseau de naissance : combien de vêtements par taille ?",
  "Trousseau de naissance : la liste des vêtements",
  "Combien de bodies, pyjamas et gilets prévoir pour bébé ? Le trousseau de naissance complet, taille par taille, pour ne pas acheter trop de taille naissance.",
  """
<p>L'erreur classique : acheter 20 bodies taille naissance que bébé ne portera que 2 semaines. Voici un trousseau raisonnable, avec une machine tous les 2 ou 3 jours.</p>
{CTA}
<h2>Les quantités conseillées</h2>
<ul>
<li><strong>bodies</strong> : 4 en naissance, 8 en 1 mois, 8 en 3 mois ;</li>
<li><strong>pyjamas</strong> : 3 en naissance, 6 en 1 mois, 6 en 3 mois ;</li>
<li><strong>gilets</strong> : 2 à 3 ;</li>
<li><strong>bonnets</strong> : 2 (un fin, un chaud selon la saison) ;</li>
<li><strong>chaussons ou chaussettes</strong> : 4 paires ;</li>
<li><strong>gigoteuses</strong> : 2 ;</li>
<li><strong>bavoirs</strong> : 6 ;</li>
<li><strong>langes en coton</strong> : 4 à 6.</li>
</ul>
<h2>Nos conseils</h2>
<ul>
<li><strong>privilégie les pressions devant</strong> et les bodies croisés : on ne passe rien par la tête d'un nouveau-né ;</li>
<li><strong>lave tout avant la naissance</strong> avec une lessive douce ;</li>
<li><strong>mets les tailles 3 et 6 mois dans ta liste</strong> : on t'offrira de toute façon beaucoup de petites tailles.</li>
</ul>
<p>Le reste du matériel est dans notre <a href="{R}checklist/">checklist</a>.</p>
""",
  short="Trousseau de naissance")

g("liste-de-naissance-bebe-ne-en-hiver/",
  "Bébé né en hiver : quoi mettre dans sa liste de naissance ?",
  "Bébé né en hiver : la liste de naissance adaptée",
  "Bébé arrive entre novembre et mars ? Les articles à ajouter à ta liste de naissance pour l'hiver : combinaison, chancelière, gigoteuse chaude, humidificateur.",
  """
<p>Un bébé d'hiver a besoin de la même base que les autres, avec quelques <strong>articles en plus pour le froid</strong>.</p>
{CTA}
<h2>À ajouter pour l'hiver</h2>
<ul>
<li><strong>une combinaison pilote</strong> pour les sorties ;</li>
<li><strong>une chancelière ou un nid d'ange</strong> pour la poussette ;</li>
<li><strong>des gigoteuses plus chaudes</strong> (indice TOG 2,5) selon la température de la chambre ;</li>
<li><strong>des bonnets</strong> et des moufles de naissance ;</li>
<li><strong>un humidificateur</strong> si l'air est très sec avec le chauffage ;</li>
<li><strong>un mouche-bébé</strong> efficace : la saison des rhumes arrive vite.</li>
</ul>
<h2>Attention au siège auto</h2>
<p>Ne mets jamais bébé en combinaison épaisse dans le siège auto : le harnais serait trop lâche en cas de choc. Attache-le en tenue normale et couvre-le par-dessus avec une couverture.</p>
<h2>La bonne température</h2>
<p>La chambre de bébé doit rester autour de 18 à 20 °C. Pas besoin de surchauffer : c'est la gigoteuse qui fait le travail.</p>
<p>Retrouve toute la liste dans notre <a href="{R}checklist/">checklist</a>.</p>
""",
  short="Bébé né en hiver")

g("liste-de-naissance-bebe-ne-en-ete/",
  "Bébé né en été : la liste de naissance adaptée à la chaleur",
  "Bébé né en été : la liste de naissance adaptée",
  "Bébé arrive entre mai et septembre ? Les articles à prévoir pour la chaleur : voile de poussette, gigoteuse légère, ventilateur, bodies manches courtes.",
  """
<p>Pour un bébé d'été, l'enjeu est de <strong>le protéger de la chaleur et du soleil</strong>.</p>
{CTA}
<h2>À ajouter pour l'été</h2>
<ul>
<li><strong>un voile anti-UV ou une ombrelle</strong> pour la poussette ;</li>
<li><strong>des gigoteuses légères</strong> (indice TOG 0,5 ou 1) ;</li>
<li><strong>des bodies à manches courtes</strong> et des langes en coton fin ;</li>
<li><strong>un chapeau</strong> à large bord ;</li>
<li><strong>un ventilateur silencieux</strong> pour la chambre, jamais dirigé directement vers bébé.</li>
</ul>
<h2>Les bons réflexes</h2>
<ul>
<li>ne couvre jamais la poussette avec un lange ou une couverture : la chaleur s'y accumule très vite ;</li>
<li>pas d'exposition directe au soleil avant 1 an ;</li>
<li>propose plus souvent le sein ou le biberon quand il fait chaud.</li>
</ul>
<p>Le reste est dans notre <a href="{R}checklist/">checklist</a>.</p>
""",
  short="Bébé né en été")

g("comment-choisir-sa-poussette/",
  "Comment choisir sa poussette ? Les 6 critères qui comptent",
  "Comment choisir sa poussette ?",
  "Poussette compacte, trio, tout-terrain ou double : les 6 critères pour bien choisir sa poussette (pliage, poids, coffre, nacelle) avant de l'ajouter à ta liste.",
  """
<p>La poussette est souvent l'achat le plus cher de la liste. Avant de choisir un modèle, réponds à <strong>6 questions</strong>.</p>
{CTA}
<h2>1. Où vas-tu rouler ?</h2>
<p>Trottoirs en ville : une poussette compacte suffit. Chemins et campagne : prends de grandes roues et des suspensions.</p>
<h2>2. Comment se plie-t-elle ?</h2>
<p>C'est le critère numéro un au quotidien. Idéalement d'une main, en tenant bébé dans l'autre bras. Regarde des vidéos de pliage avant d'acheter.</p>
<h2>3. Rentre-t-elle dans ton coffre ?</h2>
<p>Mesure ton coffre et compare avec les dimensions pliée. Pense aussi aux courses qui doivent rentrer à côté.</p>
<h2>4. Combien pèse-t-elle ?</h2>
<p>En étage sans ascenseur ou en transports, chaque kilo compte. Une poussette compacte pèse souvent moins de 8 kg.</p>
<h2>5. Nacelle ou pas ?</h2>
<p>La nacelle permet à un nouveau-né d'être allongé à plat pour les longues balades. Certains hamacs s'inclinent complètement dès la naissance et peuvent la remplacer.</p>
<h2>6. Trio, duo ou seule ?</h2>
<p>Un trio comprend la poussette, une nacelle et un siège auto. C'est pratique, mais vérifie que le siège auto est bien homologué i-Size et qu'il rentre dans ta voiture.</p>
<h2>Nos raccourcis par profil</h2>
<ul>
<li><strong>ville et petit logement</strong> : poussette compacte ultra-pliable (voir <a href="{R}liste-de-naissance-petit-appartement/">petit appartement</a>) ;</li>
<li><strong>campagne</strong> : poussette tout-terrain à grandes roues ;</li>
<li><strong>deux enfants</strong> : poussette double ou planche à roulettes (voir <a href="{R}liste-de-naissance-jumeaux/">jumeaux</a>).</li>
</ul>
<p><a class="btn" href="{AMZ:poussette}" rel="sponsored nofollow noopener" target="_blank">Voir les poussettes sur Amazon</a></p>
""",
  short="Choisir sa poussette")

g("comment-choisir-son-siege-auto-bebe/",
  "Siège auto bébé : comment bien le choisir (i-Size, Isofix)",
  "Comment choisir son siège auto bébé ?",
  "i-Size, Isofix, dos à la route, coque ou siège évolutif : comment choisir le siège auto de bébé pour sortir de la maternité en sécurité.",
  """
<p>Le siège auto est le seul article <strong>vraiment obligatoire</strong> dès la sortie de la maternité si tu rentres en voiture. C'est aussi celui qu'il faut choisir avec le plus de soin.</p>
{CTA}
<h2>Choisis un siège homologué i-Size</h2>
<p>La norme i-Size (R129) est la plus récente. Elle impose notamment de transporter l'enfant <strong>dos à la route jusqu'à 15 mois au minimum</strong>, la position la plus protectrice pour la tête et la nuque.</p>
<h2>Coque ou siège évolutif ?</h2>
<ul>
<li><strong>la coque (cosy)</strong> : légère, elle se clipse sur la poussette et se porte à la main. Elle sert environ jusqu'à 12 à 15 mois ;</li>
<li><strong>le siège évolutif</strong> : il reste dans la voiture et suit l'enfant plus longtemps, souvent pivotant pour l'installer facilement.</li>
</ul>
<h2>Isofix : vraiment utile ?</h2>
<p>Oui. Les points d'ancrage Isofix limitent les erreurs d'installation, qui sont très fréquentes avec une ceinture. Vérifie que ta voiture en est équipée (presque toutes les voitures récentes).</p>
<h2>Neuf ou d'occasion ?</h2>
<p>Neuf de préférence : un siège qui a subi un accident peut être abîmé sans que ça se voie. Si on te le prête, demande son histoire et vérifie la date de fabrication.</p>
<h2>Pour aller plus loin</h2>
<p>Les tests indépendants de sièges auto (crash-tests de l'ADAC, repris par les associations de consommateurs) sont une bonne référence pour comparer les modèles.</p>
<p><a class="btn" href="{AMZ:siege auto i-size naissance}" rel="sponsored nofollow noopener" target="_blank">Voir les sièges auto i-Size sur Amazon</a></p>
""",
  short="Choisir son siège auto")

g("liste-de-naissance-allaitement/",
  "Liste de naissance allaitement : le matériel utile",
  "Liste de naissance : le matériel pour l'allaitement",
  "Tu prévois d'allaiter ? Le matériel utile à mettre sur ta liste de naissance : coussin, coussinets, soutiens-gorge, tire-lait, et ce dont tu peux te passer.",
  """
<p>L'allaitement demande peu de matériel. Mais quelques articles rendent les premières semaines <strong>beaucoup plus confortables</strong>.</p>
{CTA}
<h2>Vraiment utile</h2>
<ul>
<li><strong>un coussin d'allaitement</strong> : il soulage le dos et les bras, et sert de coussin de grossesse avant ;</li>
<li><strong>2 ou 3 soutiens-gorge d'allaitement</strong>, à acheter plutôt en fin de grossesse ;</li>
<li><strong>des coussinets</strong>, lavables ou jetables ;</li>
<li><strong>1 ou 2 biberons</strong> pour dépanner, même en allaitement exclusif ;</li>
<li><strong>une gourde</strong> : l'allaitement donne très soif.</li>
</ul>
<h2>Le tire-lait</h2>
<p>Avant de l'acheter, sache qu'un tire-lait peut être <strong>loué en pharmacie sur prescription</strong>, avec une prise en charge. Achète-le seulement si tu en auras besoin longtemps, par exemple pour la reprise du travail.</p>
<h2>Pas indispensable</h2>
<p>Le stérilisateur électrique (une casserole d'eau bouillante suffit pour quelques biberons), le chauffe-biberon et le cache-allaitement.</p>
<p>Pour toute question sur l'allaitement, une sage-femme ou une consultante en lactation peut t'aider. Le reste du matériel est dans notre <a href="{R}checklist/">checklist</a>.</p>
""",
  short="Allaitement")

g("liste-de-naissance-originale/",
  "Liste de naissance originale : 15 idées qui changent",
  "Liste de naissance originale : 15 idées",
  "Envie d'une liste de naissance qui sort de l'ordinaire ? 15 idées originales et utiles à ajouter : séances photo, livres, repas, objets personnalisés.",
  """
<p>Une liste originale, ce n'est pas une liste de gadgets. C'est une liste qui ajoute <strong>quelques idées inattendues</strong> à la base indispensable.</p>
{CTA}
<h2>Des objets qui durent</h2>
<ul>
<li>un livre de naissance à remplir (premiers mots, premiers pas) ;</li>
<li>une boîte à souvenirs pour le bracelet de maternité et les premières chaussures ;</li>
<li>un kit d'empreintes en argile ;</li>
<li>une veilleuse projecteur d'étoiles ;</li>
<li>une bibliothèque de livres pour bébé, à compléter au fil des années.</li>
</ul>
<h2>Des cadeaux pour les parents</h2>
<ul>
<li>un porte-bébé de qualité ;</li>
<li>un bon thermos ou une gourde isotherme pour les nuits ;</li>
<li>une machine à café ou à thé rapide (si, si) ;</li>
<li>un plaid tout doux pour les tétées sur le canapé ;</li>
<li>un abonnement à un service de streaming pour les nuits blanches.</li>
</ul>
<h2>Des expériences</h2>
<ul>
<li>une séance photo de naissance ;</li>
<li>des repas livrés la première semaine ;</li>
<li>quelques heures de ménage ;</li>
<li>une soirée de baby-sitting offerte par la famille ;</li>
<li>un massage pour la maman.</li>
</ul>
<p>Pour la base indispensable, utilise notre <a href="{R}checklist/">checklist</a>, puis ajoute 3 ou 4 idées originales.</p>
""",
  short="Liste originale")
