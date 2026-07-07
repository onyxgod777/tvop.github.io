/* ═══════════════════════════════════════════════════════════════
   Golden Pi Wiki — Custom JavaScript Enhancements
   ═══════════════════════════════════════════════════════════════ */

(function() {
  'use strict';

  // ── Update Copyright Year ──
  function updateCopyrightYear() {
    var yearEls = document.querySelectorAll('.md-footer-copyright');
    var currentYear = new Date().getFullYear();
    yearEls.forEach(function(el) {
      el.innerHTML = el.innerHTML.replace(/\d{4}/g, function(match) {
        return parseInt(match) > 1900 && parseInt(match) < 2100 ? currentYear : match;
      });
    });
  }

  // ── Smooth Scroll for Anchor Links ──
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
      anchor.addEventListener('click', function(e) {
        var target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  // ── Hero Formula Typing Effect (for the golden pi value) ──
  function initFormulaHighlight() {
    var formulaEls = document.querySelectorAll('.gp-hero-formula');
    formulaEls.forEach(function(el) {
      el.innerHTML = el.innerHTML.replace(
        /3\.144605511029693/g,
        '<span style="color: #f0d080; text-shadow: 0 0 20px rgba(212,168,67,0.4);">3.144605511029693</span>'
      );
    });
  }

  // ── Add .blog-card class to blog grid cards ──
  function initBlogCards() {
    var blogLists = document.querySelectorAll('.md-content .grid.cards ul');
    blogLists.forEach(function(list) {
      if (list.closest('[data-page="blog/index.md"]') || 
          window.location.pathname.includes('/blog/')) {
        list.querySelectorAll('li').forEach(function(li) {
          li.classList.add('blog-card');
          // Try to extract date from content
          var dateMatch = li.textContent.match(/(\d{4}-\d{2}-\d{2})/);
          if (dateMatch) {
            var dateEl = document.createElement('div');
            dateEl.className = 'blog-date';
            dateEl.textContent = dateMatch[1];
            li.insertBefore(dateEl, li.firstChild);
          }
        });
      }
    });
  }

  // ── Add gold top border animation observer ──
  function initCardAnimations() {
    var cards = document.querySelectorAll('.md-typeset .grid.cards > ul > li');
    if (cards.length === 0) return;

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, { threshold: 0.1, rootMargin: '50px' });

    cards.forEach(function(card) {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
      observer.observe(card);
    });
  }

  // ── Add active state tracking to nav tabs ──
  function initActiveNavTracking() {
    var currentPath = window.location.pathname;
    var tabs = document.querySelectorAll('.md-tabs__link');
    tabs.forEach(function(tab) {
      tab.classList.remove('md-tabs__link--active');
      if (tab.getAttribute('href') === currentPath || 
          (currentPath.startsWith(tab.getAttribute('href')) && tab.getAttribute('href') !== '/')) {
        tab.classList.add('md-tabs__link--active');
      }
    });
  }

  // ── Initialize all on DOM ready ──
  function init() {
    updateCopyrightYear();
    initSmoothScroll();
    initFormulaHighlight();
    initBlogCards();
    initActiveNavTracking();

    // Delay card animations slightly to let layout settle
    setTimeout(initCardAnimations, 300);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // ── Re-run on dynamic content changes (e.g., search) ──
  var observer = new MutationObserver(function() {
    updateCopyrightYear();
    initActiveNavTracking();
  });
  observer.observe(document.body, { childList: true, subtree: true });

})();
