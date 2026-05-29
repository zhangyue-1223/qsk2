(function () {
  var sidebar = document.getElementById('app-sidebar');
  var backdrop = document.getElementById('sidebar-backdrop');
  var toggle = document.getElementById('btn-sidebar-toggle');

  if (toggle && sidebar && backdrop) {
    function setSidebarDrawerOpen(open) {
      sidebar.classList.toggle('-translate-x-full', !open);
      sidebar.classList.toggle('translate-x-0', open);
      backdrop.classList.toggle('hidden', !open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    toggle.addEventListener('click', function () {
      setSidebarDrawerOpen(sidebar.classList.contains('-translate-x-full'));
    });
    backdrop.addEventListener('click', function () {
      setSidebarDrawerOpen(false);
    });
  }

  if (!sidebar) return;

  var nav = sidebar.querySelector('nav');
  if (!nav) return;

  var STORAGE_KEY = 'qsk-sidebar-open-groups';
  var currentFile = (location.pathname.split('/').pop() || 'index.html').split('?')[0].split('#')[0];
  if (!currentFile) currentFile = 'index.html';

  /** 详情页归属的一级菜单入口 */
  var DETAIL_PARENT = {
    'customer-detail.html': 'customer-management.html',
    'customer-edit.html': 'customer-management.html',
    'government-affairs-detail.html': 'government-affairs.html',
    'accounting-customer-detail.html': 'accounting-customer-management.html',
    'address-room-detail.html': 'address-management.html',
    'opportunity-detail.html': 'opportunity-management.html',
    'lead-follow-detail.html': 'lead-management.html',
    'employee-profile.html': 'department-employees.html',
    'employee-edit.html': 'department-employees.html'
  };

  function getGroupId(detailsEl) {
    var summary = detailsEl.querySelector('summary');
    if (!summary) return '';
    var label = summary.querySelector('span');
    return (label ? label.textContent : summary.textContent).replace(/\s+/g, ' ').trim();
  }

  function linkHrefFile(href) {
    if (!href || href === '#') return '';
    return href.split('?')[0].split('#')[0];
  }

  function isActiveNavLink(href) {
    var file = linkHrefFile(href);
    if (!file) return false;
    if (file === currentFile) return true;
    var parent = DETAIL_PARENT[currentFile];
    return !!(parent && file === parent);
  }

  function loadOpenGroups() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      var list = raw ? JSON.parse(raw) : [];
      return Array.isArray(list) ? list : [];
    } catch (e) {
      return [];
    }
  }

  function saveOpenGroups() {
    var ids = [];
    nav.querySelectorAll('details').forEach(function (detailsEl) {
      if (detailsEl.open) {
        var id = getGroupId(detailsEl);
        if (id && ids.indexOf(id) === -1) ids.push(id);
      }
    });
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(ids));
    } catch (e) { /* ignore */ }
  }

  function openDetailsByIds(ids) {
    if (!ids || !ids.length) return;
    nav.querySelectorAll('details').forEach(function (detailsEl) {
      var id = getGroupId(detailsEl);
      if (id && ids.indexOf(id) !== -1) detailsEl.open = true;
    });
  }

  function openDetailsForCurrentPage() {
    nav.querySelectorAll('details').forEach(function (detailsEl) {
      var links = detailsEl.querySelectorAll('a[href]');
      for (var i = 0; i < links.length; i++) {
        if (isActiveNavLink(links[i].getAttribute('href'))) {
          detailsEl.open = true;
          return;
        }
      }
    });
  }

  openDetailsForCurrentPage();
  openDetailsByIds(loadOpenGroups());

  nav.querySelectorAll('details').forEach(function (detailsEl) {
    detailsEl.addEventListener('toggle', saveOpenGroups);
  });

  nav.querySelectorAll('details a[href]').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href || href === '#') return;

    link.addEventListener('click', function () {
      var group = link.closest('details');
      if (group) group.open = true;
      saveOpenGroups();
    });
  });
})();
