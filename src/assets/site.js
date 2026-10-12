// Copy-email buttons and the work hub filter. No dependencies.
document.querySelectorAll('[data-copy]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var toast = btn.parentElement.querySelector('.toast');
    function say(msg) { if (toast) { toast.textContent = msg; setTimeout(function () { toast.textContent = ''; }, 2500); } }
    try {
      navigator.clipboard.writeText(btn.getAttribute('data-copy')).then(
        function () { say('Copied'); },
        function () { say('Select the address to copy it'); });
    } catch (e) { say('Select the address to copy it'); }
  });
});

(function () {
  var bar = document.querySelector('.filters');
  if (!bar) return;
  var buttons = bar.querySelectorAll('button');
  var groups = document.querySelectorAll('.group');
  function show(key) {
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.f === key)); });
    groups.forEach(function (g) { g.hidden = !(key === 'all' || g.id === key); });
  }
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      show(b.dataset.f);
      try { history.replaceState(null, '', b.dataset.f === 'all' ? location.pathname : '#' + b.dataset.f); } catch (e) {}
    });
  });
  var start = (location.hash || '').slice(1);
  show(document.getElementById(start) && start !== '' ? start : 'all');
})();
