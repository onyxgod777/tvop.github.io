/* Click-to-load Desmos graphs.
 *
 * Why this exists: a bare <iframe> of the Desmos calculator leaves a large blank
 * box while Desmos's application bundle downloads and boots - measured at 97.5%
 * white / 0.0% coloured pixels eight seconds after page load on the live site.
 * A poster image paints immediately, and the calculator is fetched only when the
 * reader actually asks for it, so no page pays for 144 third-party app loads.
 */
(function () {
  'use strict';

  function activate(facade) {
    var src = facade.getAttribute('data-embed');
    if (!src) return;
    var label = facade.getAttribute('data-label') || 'Interactive Desmos graph';

    var frame = document.createElement('iframe');
    frame.className = 'gp-live__frame';
    frame.src = src;
    frame.width = '100%';
    frame.height = '470';
    frame.setAttribute('title', label);
    frame.setAttribute('allowfullscreen', '');
    frame.setAttribute('frameborder', '0');
    frame.style.border = '0';
    frame.style.borderRadius = '10px';
    frame.style.display = 'block';

    facade.replaceWith(frame);
  }

  document.addEventListener('click', function (event) {
    var target = event.target;
    var facade = target && target.closest ? target.closest('.gp-live__facade') : null;
    if (facade) {
      event.preventDefault();
      activate(facade);
    }
  });

  /* The facade is a <button>, so Enter/Space must work too. */
  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    var el = document.activeElement;
    if (el && el.classList && el.classList.contains('gp-live__facade')) {
      event.preventDefault();
      activate(el);
    }
  });
})();
