// Auto-update copyright year
(function() {
  var year = new Date().getFullYear();
  var els = document.querySelectorAll('footer h6');
  for (var i = 0; i < els.length; i++) {
    els[i].innerHTML = els[i].innerHTML.replace(/\d{4}/, year);
  }
})();
