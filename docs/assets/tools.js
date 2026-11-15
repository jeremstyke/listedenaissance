/* Outils gratuits : calcul de la date d'accouchement, calculateur de trousseau */
(function () {
  function $(s) { return document.querySelector(s); }
  var MOIS = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'];
  var JOURS = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi'];
  function fmt(d) { return JOURS[d.getDay()] + ' ' + d.getDate() + ' ' + MOIS[d.getMonth()] + ' ' + d.getFullYear(); }
  function add(d, n) { var x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; }
  function parse(v) { if (!v) return null; var p = v.split('-'); return new Date(+p[0], +p[1] - 1, +p[2], 12); }
  function today() { var t = new Date(); t.setHours(12, 0, 0, 0); return t; }

  /* Date d'accouchement (convention française : 41 SA après le premier jour des dernières règles) */
  var dpa = $('#t-dpa');
  if (dpa) {
    var modeSel = $('#t-mode');
    function syncMode() {
      var m = modeSel.value;
      $('#t-cycle-row').hidden = m !== 'ddr';
      $('#t-date-label').textContent = m === 'ddr' ? 'Premier jour des dernières règles' : 'Date de conception (estimée)';
    }
    modeSel.addEventListener('change', syncMode); syncMode();
    dpa.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = parse($('#t-date').value), out = $('#t-out');
      if (!d) { out.innerHTML = '<p>Indique une date.</p>'; out.hidden = false; return; }
      var ddr;
      if (modeSel.value === 'ddr') {
        var cyc = parseInt($('#t-cycle').value, 10) || 28;
        cyc = Math.min(45, Math.max(21, cyc));
        ddr = add(d, cyc - 28); // ovulation décalée si le cycle n'est pas de 28 jours
      } else {
        ddr = add(d, -14);
      }
      var term = add(ddr, 287);
      var t = today(), days = Math.round((t - ddr) / 864e5);
      var h = '<p class="res-big">Date prévue d\'accouchement : <strong>' + fmt(term) + '</strong></p>';
      if (days >= 0 && days <= 300) {
        var sa = Math.floor(days / 7), j = days % 7, tri = sa < 14 ? '1er' : (sa < 28 ? '2e' : '3e');
        h += '<p>Aujourd\'hui, tu es à <strong>' + sa + ' SA' + (j ? ' et ' + j + ' jour' + (j > 1 ? 's' : '') : '') + '</strong> (semaines d\'aménorrhée), soit ' + Math.max(0, sa - 2) + ' semaines de grossesse, au ' + tri + ' trimestre.</p>';
      }
      var steps = [
        [15, 'Repérer le matériel, demander ce qu\'on peut te prêter'],
        [20, 'Créer la liste de naissance et la remplir'],
        [25, 'Partager la liste avec tes proches'],
        [31, 'Préparer la valise de maternité'],
        [34, 'Avoir l\'essentiel à la maison : siège auto installé, lit prêt'],
        [37, 'Début de la période dite « à terme »'],
        [41, 'Date prévue d\'accouchement']
      ];
      h += '<h3>Ton calendrier</h3><ol class="res-cal">';
      steps.forEach(function (s) {
        var dt = add(ddr, s[0] * 7), past = dt < t;
        h += '<li class="' + (past ? 'past' : '') + '"><span>' + fmt(dt) + ' <small>(' + s[0] + ' SA)</small></span>' + s[1] + '</li>';
      });
      h += '</ol><p class="small">Estimation indicative. Seul ton médecin ou ta sage-femme fixe la date de terme, souvent ajustée après l\'échographie de datation.</p>';
      out.innerHTML = h; out.hidden = false;
      out.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  /* Calculateur de trousseau */
  var tr = $('#t-trousseau');
  if (tr) {
    tr.addEventListener('submit', function (e) {
      e.preventDefault();
      var every = parseInt($('#t-wash').value, 10) || 3;
      var season = $('#t-season').value;
      var cover = every + 1; // jours couverts : entre deux lessives, plus un jour de séchage
      function q(perDay, min) { return Math.max(min, Math.ceil(perDay * cover)); }
      var rows = [
        ['Bodies', q(2, 6)],
        ['Pyjamas', q(1.5, 4)],
        ['Bavoirs', q(2, 4)],
        ['Langes en coton', q(1, 4)],
        ['Gigoteuses', 2],
        ['Gilets', season === 'hiver' ? 3 : 2],
        ['Bonnets', season === 'hiver' ? 2 : 1],
        ['Paires de chaussettes ou chaussons', season === 'ete' ? 2 : 4]
      ];
      var h = '<p class="res-big">Ton trousseau pour une lessive tous les <strong>' + every + ' jours</strong></p><table><thead><tr><th>Article</th><th>Quantité par taille</th></tr></thead><tbody>';
      rows.forEach(function (r) { h += '<tr><td>' + r[0] + '</td><td>' + r[1] + '</td></tr>'; });
      h += '</tbody></table><p>En taille naissance, prends environ la moitié de ces quantités pour les bodies et les pyjamas : bébé la porte souvent quelques semaines seulement, et certains bébés passent directement à la taille 1 mois.</p>';
      if (season === 'hiver') h += '<p>Bébé d\'hiver : ajoute une combinaison pilote ou une chancelière pour les sorties.</p>';
      if (season === 'ete') h += '<p>Bébé d\'été : privilégie les bodies à manches courtes et un voile léger pour la poussette.</p>';
      h += '<p class="small">Estimation indicative, à adapter à ton bébé (reflux, couches qui débordent...).</p>';
      var out = $('#t-out'); out.innerHTML = h; out.hidden = false;
      out.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }
})();
