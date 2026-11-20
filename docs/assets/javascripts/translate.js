/* Translation widget for thealpha-secret.xyz network - Google Translate with dark theme */
(function() {
  'use strict';

  // Don't load if already present
  if (document.getElementById('google_translate_element')) return;

  // Wait for DOM ready (script runs in <head> before <body> exists)
  function domReady(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  domReady(function() {

    // Don't load if already present (double-check after DOM ready)
    if (document.getElementById('google_translate_element')) return;

    // Create the widget container
    var container = document.createElement('div');
    container.id = 'google_translate_element';
    container.setAttribute('aria-label', 'Translate this page');
    document.body.appendChild(container);

    // Inject light (Vector 2022) styles for the dropdown
    var style = document.createElement('style');
    style.textContent =
      '#google_translate_element{position:fixed;bottom:14px;right:14px;z-index:99999;}' +
      '.goog-te-gadget{font-family:inherit!important;font-size:0!important;}' +
      '.goog-te-gadget span{display:none!important;}' +
      '.goog-te-combo{' +
        'background:#fff!important;color:#202122!important;' +
        'border:1px solid #a2a9b1!important;border-radius:2px!important;' +
        'padding:4px 8px!important;font-size:13px!important;font-family:inherit!important;' +
        'cursor:pointer!important;outline:none!important;min-width:150px;' +
      '}' +
      '.goog-te-combo:hover{border-color:#72777d!important;}' +
      '.goog-te-combo:focus{border-color:#36c!important;box-shadow:0 0 0 2px rgba(51,102,204,0.25)!important;}' +
      '.goog-te-banner-frame.skiptranslate{display:none!important;}' +
      'body{top:0!important;}' +
      /* Hide Google's attribution text */
      '.goog-logo-link,.goog-te-gadget .goog-logo-link{display:none!important;}' +
      /* Ensure translated text is readable */
      '.translated-ltr .container,.translated-rtl .container{width:auto!important;}' +
      /* Loading indicator while Google's script loads */
      '#google_translate_element:empty::after{content:"🌐";position:absolute;top:5px;right:5px;font-size:16px;animation:pulse 1.5s infinite;}@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}' +
      '#google_translate_element:not(:empty)::after{display:none;}';
    document.head.appendChild(style);

    // Initialize Google Translate
    window.googleTranslateElementInit = function() {
      try {
        new google.translate.TranslateElement({
          pageLanguage: 'en',
          includedLanguages: 'en,fr,es,pt,de,it,ru,ja,zh-CN,ar,hi,ko,nl,tr,vi,th,pl,sv,da,fi,el,he,ro,cs,hu,no,id,ms,fil,uk',
          layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
          autoDisplay: false
        }, 'google_translate_element');
      } catch(e) {
        // Google Translate blocked or unavailable — fail silently
      }
    };

    // Load the Google Translate script
    var gs = document.createElement('script');
    gs.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    gs.async = true;
    document.body.appendChild(gs);

  });
})();
