/* Translation widget for thealpha-secret.xyz network - Google Translate with dark theme */
(function() {
  'use strict';

  // Don't load if already present
  if (document.getElementById('google_translate_element')) return;

  // Create the widget container
  var container = document.createElement('div');
  container.id = 'google_translate_element';
  container.setAttribute('aria-label', 'Translate this page');
  document.body.appendChild(container);

  // Inject dark-theme styles for the dropdown
  var style = document.createElement('style');
  style.textContent =
    '#google_translate_element{position:fixed;top:12px;right:12px;z-index:99999;}' +
    '.goog-te-gadget{font-family:inherit!important;font-size:0!important;}' +
    '.goog-te-gadget span{display:none!important;}' +
    '.goog-te-combo{' +
      'background:#13131f!important;color:#e0dcc7!important;' +
      'border:1px solid #2a2a3e!important;border-radius:6px!important;' +
      'padding:5px 10px!important;font-size:0.85rem!important;font-family:inherit!important;' +
      'cursor:pointer!important;outline:none!important;min-width:160px;' +
    '}' +
    '.goog-te-combo:hover{border-color:#d4a843!important;}' +
    '.goog-te-combo:focus{border-color:#d4a843!important;box-shadow:0 0 0 2px rgba(212,168,67,0.3)!important;}' +
    '.goog-te-banner-frame.skiptranslate{display:none!important;}' +
    'body{top:0!important;}' +
    /* Hide Google's attribution text */
    '.goog-logo-link,.goog-te-gadget .goog-logo-link{display:none!important;}' +
    /* Ensure translated text is readable */
    '.translated-ltr .container,.translated-rtl .container{width:auto!important;}';
  document.head.appendChild(style);

  // Initialize Google Translate
  window.googleTranslateElementInit = function() {
    new google.translate.TranslateElement({
      pageLanguage: 'en',
      includedLanguages: 'en,fr,es,pt,de,it,ru,ja,zh-CN,ar,hi,ko,nl,tr,vi,th,pl,sv,da,fi,el,he,ro,cs,hu,no,id,ms,fil,uk',
      layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
      autoDisplay: false
    }, 'google_translate_element');
  };

  // Load the Google Translate script
  var gs = document.createElement('script');
  gs.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
  gs.async = true;
  document.body.appendChild(gs);
})();
