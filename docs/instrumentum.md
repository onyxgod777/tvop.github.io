# ⚙️ Instrumentum

A precision tool that reveals golden π **(4/√φ = 3.144606...)** through the identity **4y²x / ((y²+x²)√(y²-x²))** — exact only when **y/x = √φ**. Explores the relativistic spacetime interval **√(y²−x²)** and the Lorentz factor **γ = φ** at the golden ratio.

<div id="instrumentum-root">
<noscript>
<p style="text-align:center;padding:2rem;color:#d4a843;">The interactive instrument requires JavaScript.</p>
</noscript>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    var div = document.getElementById('instrumentum-root');
    var iframe = document.createElement('iframe');
    iframe.src = '/instrumentum.html';
    iframe.style.width = '100%';
    iframe.style.height = '1050px';
    iframe.style.border = 'none';
    iframe.style.overflow = 'hidden';
    div.appendChild(iframe);
});
</script>

[Open full-screen instrument ⚙️](/instrumentum.html){ .md-button .md-button--primary }

## About the Instrument

Adjust the **r = y/x** slider to see how the computed value of π changes:

- Slide toward **√φ ≈ 1.27202** — the computation converges on **π = 4/√φ = 3.144606**
- At any other ratio, the result diverges from both golden π and conventional π
- The **green target** marks √φ — the exact golden ratio root
- The **red dashed line** marks the light cone (r=1) — below it, the value becomes complex
- **Relativity readouts** show β = v/c, γ (Lorentz factor), τ/t (proper time ratio), and ψ (rapidity)
- At r = √φ, γ = **φ** exactly — proper time dilates to τ = t/φ

Includes a geometric visualization canvas with light cone boundaries, real-time readouts comparing golden π vs conventional π, relativistic quantity displays, and a complete algebraic proof.
