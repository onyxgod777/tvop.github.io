// Back to Top button
(function() {
  var btn = document.createElement('button');
  btn.innerHTML = '&#8593;';
  btn.title = 'Back to top';
  btn.style.cssText = 'position:fixed;bottom:60px;right:20px;z-index:99;width:40px;height:40px;border:none;outline:none;background:#2077dd;color:gold;cursor:pointer;border-radius:50%;font-size:20px;display:none;box-shadow:0 2px 8px rgba(0,0,0,0.3);';
  document.body.appendChild(btn);
  window.onscroll = function() {
    btn.style.display = document.documentElement.scrollTop > 300 ? 'block' : 'none';
  };
  btn.onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };
})();
