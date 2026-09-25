/* Click-to-load YouTube facades for the Videos page.
   Nothing contacts YouTube until the reader presses play; the frame is then
   swapped in from youtube-nocookie.com. Delegated listeners, so it keeps
   working under Material's instant navigation. */
(function () {
  'use strict';

  function activate(btn) {
    var id = btn.getAttribute('data-video');
    if (!id || !/^[A-Za-z0-9_-]{11}$/.test(id)) return;
    var frame = document.createElement('div');
    frame.className = 'gp-yt__frame';
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&modestbranding=1';
    iframe.title = btn.getAttribute('aria-label') || 'Video';
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
    iframe.setAttribute('allowfullscreen', '');
    frame.appendChild(iframe);
    btn.replaceWith(frame);
  }

  function handler(e) {
    if (!e.target || !e.target.closest) return;
    var btn = e.target.closest('.gp-yt__btn');
    if (!btn) return;
    e.preventDefault();
    activate(btn);
  }

  document.addEventListener('click', handler);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') handler(e);
  });
})();
