/**
 * 企税康平台 — 侧栏菜单默认配置（与当前项目页面一致）
 */
(function (global) {
  var STORAGE_KEY = 'qsk-menu-config-v1';

  var DEFAULT_MENUS = [
    { id: 'workbench', type: 'link', name: '工作台', icon: 'fa-table-columns', href: 'index.html', enabled: true, sort: 1 },
    {
      id: 'sales', type: 'group', name: '销售管理', icon: 'fa-chart-line', enabled: true, sort: 2,
      children: [
        { id: 'sales-target', type: 'link', name: '销售目标', icon: '', href: 'sales-target.html', enabled: true, sort: 1 },
        { id: 'lead-mgmt', type: 'link', name: '线索管理', icon: '', href: 'lead-management.html', enabled: true, sort: 2 },
        { id: 'opp-mgmt', type: 'link', name: '商机管理', icon: '', href: 'opportunity-management.html', enabled: true, sort: 3 },
        { id: 'sales-perf', type: 'link', name: '销售业绩', icon: '', href: 'sales-performance.html', enabled: true, sort: 4 }
      ]
    },
    {
      id: 'customer-center', type: 'group', name: '客户中心', icon: 'fa-building-user', enabled: true, sort: 3,
      children: [
        { id: 'customer-mgmt', type: 'link', name: '客户管理', icon: '', href: 'customer-management.html', enabled: true, sort: 1 },
        { id: 'gov-affairs', type: 'link', name: '政务服务', icon: '', href: 'government-affairs.html', enabled: true, sort: 2 },
        { id: 'accounting-svc', type: 'link', name: '代账服务', icon: '', href: 'accounting-customer-management.html', enabled: true, sort: 3 },
        { id: 'address-mgmt', type: 'link', name: '地址管理', icon: '', href: 'address-management.html', enabled: true, sort: 4 },
        { id: 'customer-items', type: 'link', name: '客户物品', icon: '', href: 'customer-items.html', enabled: true, sort: 5 }
      ]
    },
    { id: 'knowledge', type: 'link', name: '知识库', icon: 'fa-book-open', href: 'knowledge-base.html', enabled: true, sort: 4 },
    {
      id: 'contract-order', type: 'group', name: '合同订单', icon: 'fa-file-signature', enabled: true, sort: 5,
      children: [
        { id: 'contract-mgmt', type: 'link', name: '合同管理', icon: '', href: 'contract-management.html', enabled: true, sort: 1 },
        { id: 'order-mgmt', type: 'link', name: '订单管理', icon: '', href: 'order-management.html', enabled: true, sort: 2 }
      ]
    },
    {
      id: 'operations', type: 'group', name: '运营管理', icon: 'fa-wallet', enabled: true, sort: 6,
      children: [
        { id: 'payment-request', type: 'link', name: '财务报销', icon: '', href: 'payment-request.html', enabled: true, sort: 1 },
        { id: 'hr-request', type: 'link', name: '人事申请', icon: '', href: 'hr-request.html', enabled: true, sort: 2 },
        { id: 'financial-reports', type: 'link', name: '经营报表', icon: '', href: 'financial-reports.html', enabled: true, sort: 3 },
        { id: 'salary-mgmt', type: 'link', name: '薪资管理', icon: '', href: 'salary-management.html', enabled: true, sort: 4 },
        { id: 'employee-mgmt', type: 'link', name: '员工管理', icon: '', href: 'department-employees.html', enabled: true, sort: 5 }
      ]
    },
    {
      id: 'system', type: 'group', name: '系统管理', icon: 'fa-gear', enabled: true, sort: 7,
      children: [
        { id: 'role-perm', type: 'link', name: '角色权限', icon: '', href: 'role-permissions.html', enabled: true, sort: 1 },
        { id: 'dict-mgmt', type: 'link', name: '字典管理', icon: '', href: 'dictionary-management.html', enabled: true, sort: 2 },
        { id: 'menu-mgmt', type: 'link', name: '菜单管理', icon: '', href: 'menu-management.html', enabled: true, sort: 3 }
      ]
    }
  ];

  function deepClone(obj) {
    return JSON.parse(JSON.stringify(obj));
  }

  function normalizeSort(list) {
    list.sort(function (a, b) { return a.sort - b.sort; });
    list.forEach(function (item, i) { item.sort = i + 1; });
  }

  function getMenus() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) { /* ignore */ }
    return deepClone(DEFAULT_MENUS);
  }

  function saveMenus(menus) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(menus));
  }

  function resetMenus() {
    localStorage.removeItem(STORAGE_KEY);
    return deepClone(DEFAULT_MENUS);
  }

  function findParentList(menus, id, parentList) {
    parentList = parentList || menus;
    for (var i = 0; i < parentList.length; i++) {
      if (parentList[i].id === id) return { list: parentList, index: i, item: parentList[i] };
      if (parentList[i].children) {
        var found = findParentList(menus, id, parentList[i].children);
        if (found) return found;
      }
    }
    return null;
  }

  global.MenuData = {
    STORAGE_KEY: STORAGE_KEY,
    DEFAULT_MENUS: DEFAULT_MENUS,
    getMenus: getMenus,
    saveMenus: saveMenus,
    resetMenus: resetMenus,
    deepClone: deepClone,
    normalizeSort: normalizeSort,
    findParentList: findParentList
  };
})(typeof window !== 'undefined' ? window : global);
