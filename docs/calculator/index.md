# Golden π Calculator

<link rel="stylesheet" href="/css/styles.css">

<div id="calc-root">
<noscript>
<p style="text-align:center;padding:2rem;color:#a07830;">The interactive calculator requires JavaScript.</p>
</noscript>
</div>

<script>
// Load the calculator in an iframe
document.addEventListener('DOMContentLoaded', function() {
    var div = document.getElementById('calc-root');
    var iframe = document.createElement('iframe');
    iframe.src = '/calculator.html';
    iframe.style.width = '100%';
    iframe.style.height = '800px';
    iframe.style.border = 'none';
    iframe.style.overflow = 'hidden';
    div.appendChild(iframe);
});
</script>

Alternatively, visit the [full-page calculator](/calculator.html) directly.

## About

This interactive calculator uses golden π = 4/√φ = 3.144605511030 as its circle constant. It includes a full expression evaluator, trigonometric functions, and a comparison mode to see how results differ from conventional π.
