(function () {
  var sidebar = document.getElementById('app-sidebar');
  var backdrop = document.getElementById('sidebar-backdrop');
  var toggle = document.getElementById('btn-sidebar-toggle');
  if (!sidebar || !backdrop || !toggle) return;

  function setOpen(open) {
    sidebar.classList.toggle('-translate-x-full', !open);
    sidebar.classList.toggle('translate-x-0', open);
    backdrop.classList.toggle('hidden', !open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  toggle.addEventListener('click', function () {
    setOpen(sidebar.classList.contains('-translate-x-full'));
  });
  backdrop.addEventListener('click', function () {
    setOpen(false);
  });
})();
