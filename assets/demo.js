// BarkZone members area demo: small interactions so the pages feel real on the call.
(function () {
  var toastEl = document.createElement('div');
  toastEl.className = 'toast';
  document.body.appendChild(toastEl);
  var th;
  function toast(m) {
    toastEl.textContent = m;
    toastEl.classList.add('on');
    clearTimeout(th);
    th = setTimeout(function () { toastEl.classList.remove('on'); }, 2800);
  }
  window.demoToast = toast;

  document.addEventListener('click', function (e) {
    var d = e.target.closest('[data-demo]');
    if (d) { e.preventDefault(); toast(d.getAttribute('data-demo')); }
    var m = e.target.closest('[data-menu]');
    if (m) { e.preventDefault(); document.body.classList.toggle('menu-open'); }
  });

  // Skill page filters
  var filters = document.querySelectorAll('[data-filter]');
  filters.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      filters.forEach(function (x) { x.classList.toggle('on', x === b); });
      document.querySelectorAll('[data-state]').forEach(function (c) {
        var s = c.getAttribute('data-state');
        c.hidden = !(f === 'all' || s === f || (f === 'todo' && s !== 'done'));
      });
    });
  });

  // Lesson player: switch parts, mark as watched
  var parts = Array.prototype.slice.call(document.querySelectorAll('[data-part]'));
  if (parts.length) {
    var cur = parts.findIndex(function (p) { return p.classList.contains('current'); });
    if (cur < 0) cur = 0;
    var total = parts.length;
    var $ = function (id) { return document.getElementById(id); };
    function render() {
      var watched = 0;
      parts.forEach(function (p, i) {
        p.classList.toggle('current', i === cur);
        if (p.classList.contains('watched')) watched++;
        var st = p.querySelector('.st');
        if (st) st.textContent = i === cur ? 'Now playing' : (p.classList.contains('watched') ? '✓ Watched' : 'Part ' + (i + 1));
      });
      var p = parts[cur];
      if ($('pl-thumb')) $('pl-thumb').src = p.getAttribute('data-thumb');
      if ($('pl-title')) $('pl-title').textContent = p.getAttribute('data-title');
      if ($('pl-num')) $('pl-num').textContent = 'Part ' + (cur + 1) + ' of ' + total;
      if ($('pl-prev')) $('pl-prev').style.visibility = cur === 0 ? 'hidden' : 'visible';
      if ($('pl-next')) $('pl-next').textContent = cur === total - 1 ? 'Next lesson ›' : 'Part ' + (cur + 2) + ' ›';
      if ($('pl-prev')) $('pl-prev').textContent = '‹ Part ' + cur;
      if ($('pl-count')) $('pl-count').textContent = watched + ' of ' + total + ' watched';
      if ($('pl-ring')) {
        $('pl-ring').style.setProperty('--p', Math.round(100 * watched / total));
        $('pl-ring').querySelector('b').textContent = watched + '/' + total;
      }
      if ($('pl-mark')) $('pl-mark').textContent = '✓ Mark part ' + (cur + 1) + ' as watched';
    }
    parts.forEach(function (p, i) {
      p.addEventListener('click', function () { cur = i; render(); window.scrollTo({ top: 0, behavior: 'smooth' }); });
    });
    if ($('pl-prev')) $('pl-prev').addEventListener('click', function (e) { e.preventDefault(); if (cur > 0) { cur--; render(); } });
    if ($('pl-next')) $('pl-next').addEventListener('click', function (e) {
      e.preventDefault();
      if (cur < total - 1) { cur++; render(); } else { toast('This would take you to the next lesson: Weave Entries on full set'); }
    });
    if ($('pl-mark')) $('pl-mark').addEventListener('click', function (e) {
      e.preventDefault();
      parts[cur].classList.add('watched');
      if (cur < total - 1) cur++;
      render();
      toast('Marked as watched. Progress saves to the member’s account.');
    });
    if ($('pl-done')) $('pl-done').addEventListener('click', function (e) {
      e.preventDefault();
      parts.forEach(function (p) { p.classList.add('watched'); });
      render();
      toast('Lesson marked as done. The Weaves progress bar moves to 4 of 7.');
    });
    render();
  }

  // Feedback video drop zone (demo only, nothing uploads)
  document.querySelectorAll('[data-drop]').forEach(function (z) {
    var input = z.querySelector('input[type=file]');
    var label = z.querySelector('.drop-msg');
    function picked(name) {
      z.classList.add('has-file');
      label.innerHTML = '<b>✓ ' + name.replace(/[<>&]/g, '') + '</b><br>ready to send to Iain and Livvi';
      var send = z.parentNode.querySelector('[data-send]');
      if (send) send.hidden = false;
    }
    if (input) input.addEventListener('change', function () { if (input.files[0]) picked(input.files[0].name); });
    ['dragenter', 'dragover'].forEach(function (ev) { z.addEventListener(ev, function (e) { e.preventDefault(); z.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { z.addEventListener(ev, function (e) { e.preventDefault(); z.classList.remove('over'); }); });
    z.addEventListener('drop', function (e) { if (e.dataTransfer.files[0]) picked(e.dataTransfer.files[0].name); });
  });
  document.querySelectorAll('[data-send]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      toast('Demo only, nothing was uploaded. In the real version Iain and Livvi get a notification and reply here.');
    });
  });

  // Add a lesson form with live preview
  var form = document.getElementById('add-lesson');
  if (form) {
    var rows = document.getElementById('vid-rows');
    var tpl = document.getElementById('vid-row-tpl');
    function ytId(u) {
      var m = (u || '').match(/(?:v=|youtu\.be\/|embed\/|shorts\/|live\/)([\w-]{11})/);
      return m ? m[1] : null;
    }
    function addRow() {
      var n = tpl.content.cloneNode(true);
      rows.appendChild(n);
      renumber(); update();
    }
    function renumber() {
      rows.querySelectorAll('.vid-row').forEach(function (r, i) {
        r.querySelector('.vid-n').textContent = 'Video ' + (i + 1);
      });
    }
    function update() {
      var title = form.querySelector('[name=title]').value.trim() || 'Your new lesson';
      var skill = form.querySelector('[name=skill]').value;
      var vids = Array.prototype.slice.call(rows.querySelectorAll('.vid-row'));
      var ids = [];
      vids.forEach(function (r) {
        var id = ytId(r.querySelector('[name=url]').value);
        var ok = r.querySelector('.vid-ok');
        ok.textContent = id ? '✓ Found' : '';
        if (id) ids.push(id);
      });
      document.getElementById('pv-title').textContent = title;
      document.getElementById('pv-skill').textContent = skill;
      document.getElementById('pv-count').textContent = vids.length + ' video' + (vids.length === 1 ? '' : 's');
      var img = document.getElementById('pv-thumb');
      if (ids.length) { img.src = 'https://img.youtube.com/vi/' + ids[0] + '/hqdefault.jpg'; img.parentNode.classList.add('has'); }
      else { img.removeAttribute('src'); img.parentNode.classList.remove('has'); }
    }
    form.addEventListener('input', update);
    form.addEventListener('change', update);
    document.getElementById('add-vid').addEventListener('click', function (e) { e.preventDefault(); addRow(); });
    rows.addEventListener('click', function (e) {
      var x = e.target.closest('.vid-x');
      if (x) { e.preventDefault(); if (rows.children.length > 1) { x.closest('.vid-row').remove(); renumber(); update(); } }
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var t = form.querySelector('[name=title]').value.trim();
      if (!t) { toast('Give the lesson a title first'); form.querySelector('[name=title]').focus(); return; }
      document.getElementById('done-msg').hidden = false;
      document.getElementById('done-title').textContent = t;
      document.getElementById('done-skill').textContent = form.querySelector('[name=skill]').value;
      document.getElementById('done-msg').scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    addRow();
  }
})();
