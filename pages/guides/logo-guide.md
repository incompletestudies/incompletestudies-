---
layout: default
title: Logo & Branding Guide
permalink: /logo-guide/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Logo &amp; Branding Guide</span>
    <span class="col-head-meta">The Journal of Incomplete Studies · v1.0</span>
  </div>


  <div style="padding: 2rem 0; border-bottom: 1px solid var(--rule); margin-bottom: 2rem;">
      <img src="{{ '/assets/images/logo/logo_gold-dim.svg' | relative_url }}" 
          alt="Journal Logo Test" 
          style="width: 100%; max-width: 600px; height: auto;">
      <img src="{{ '/assets/images/logo/logo_sage.svg' | relative_url }}" 
          alt="Journal Logo Test" 
          style="width: 100%; max-width: 600px; height: auto;">
      <p style="font-size: 12px; color: var(--muted); margin-top: 0.5rem;">Logo test — remove this after checking</p>
  </div>

  <!-- ─── QUICK NAVIGATION ─── -->
  <div class="style-toc">
    <span class="style-toc-label">Jump to:</span>
    <a href="#logo-versions">Logo Versions</a>
    <a href="#sizes">Sizes</a>
    <a href="#colors">Colors</a>
    <a href="#css">CSS Filters</a>
    <a href="#examples">Examples</a>
    <a href="#dark-mode">Dark/Light Mode</a>
    <a href="#download">Download</a>
  </div>

  <div class="style-guide-body">

    <!-- ═══════════════════════════════════════════════ -->
    <!-- LOGO VERSIONS                                  -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="logo-versions">
      <h2 class="style-section-title">Logo Versions</h2>

      <div class="style-grid style-grid--logos">

        <div class="style-item style-item--logo">
          <span class="style-label">Primary (Dark on Light)</span>
          <div class="style-demo logo-demo" style="background: var(--paper);">
            <img src="{{ '/assets/images/logo/logo.svg' | relative_url }}" 
                 alt="Logo primary" 
                 class="logo-preview">
          </div>
          <div class="style-code">/assets/images/logo/logo.svg</div>
        </div>

        <div class="style-item style-item--logo">
          <span class="style-label">Negative (Light on Dark)</span>
          <div class="style-demo logo-demo" style="background: var(--void);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo negative" 
                 class="logo-preview">
          </div>
          <div class="style-code">/assets/images/logo/logo-negative.svg</div>
        </div>

        <div class="style-item style-item--logo">
          <span class="style-label">Gold Accent</span>
          <div class="style-demo logo-demo" style="background: var(--void);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo gold" 
                 class="logo-preview logo-gold">
          </div>
          <div class="style-code"><code>filter: sepia(1) saturate(4) hue-rotate(-15deg) brightness(0.9);</code></div>
        </div>

        <div class="style-item style-item--logo">
          <span class="style-label">Cream (for Dark Bg)</span>
          <div class="style-demo logo-demo" style="background: var(--void);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo cream" 
                 class="logo-preview logo-cream">
          </div>
          <div class="style-code"><code>filter: brightness(0) invert(1) saturate(0.8);</code></div>
        </div>

      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- LOGO SIZES                                     -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="sizes">
      <h2 class="style-section-title">Logo Sizes</h2>

      <div class="style-item style-item--full">
        <span class="style-label">Size Reference</span>
        <div class="style-demo" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 2rem; padding: 1.5rem; background: var(--void);">
          <div style="text-align: center;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo xs" 
                 width="32" 
                 height="32">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">32×32</p>
            <p style="font-size: 9px; color: var(--ash);">Favicon</p>
          </div>
          <div style="text-align: center;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo sm" 
                 width="48" 
                 height="48">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">48×48</p>
            <p style="font-size: 9px; color: var(--ash);">Small logo</p>
          </div>
          <div style="text-align: center;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo md" 
                 width="80" 
                 height="80">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">80×80</p>
            <p style="font-size: 9px; color: var(--ash);">Header</p>
          </div>
          <div style="text-align: center;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo lg" 
                 width="120" 
                 height="120">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">120×120</p>
            <p style="font-size: 9px; color: var(--ash);">Hero section</p>
          </div>
          <div style="text-align: center;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo xl" 
                 width="200" 
                 height="200">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">200×200</p>
            <p style="font-size: 9px; color: var(--ash);">Full-page</p>
          </div>
        </div>
        <div class="style-code">Recommended: <code>80×80</code> for header · <code>120×120</code> for hero · <code>32×32</code> for favicon</div>
      </div>

      <div class="style-item" style="margin-top: 1rem;">
        <span class="style-label">Usage Guide</span>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; font-size: 13px; color: var(--pale);">
          <div style="padding: 0.75rem; border: 1px solid var(--rule); border-radius: 4px; background: var(--void2);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
              <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="32" height="32">
              <div>
                <strong style="color: var(--cream);">Header</strong>
                <p style="font-size: 11px; color: var(--muted); margin: 0;">40–48px height</p>
              </div>
            </div>
          </div>
          <div style="padding: 0.75rem; border: 1px solid var(--rule); border-radius: 4px; background: var(--void2);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
              <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="24" height="24">
              <div>
                <strong style="color: var(--cream);">Favicon</strong>
                <p style="font-size: 11px; color: var(--muted); margin: 0;">16–32px square</p>
              </div>
            </div>
          </div>
          <div style="padding: 0.75rem; border: 1px solid var(--rule); border-radius: 4px; background: var(--void2);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
              <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="48" height="48">
              <div>
                <strong style="color: var(--cream);">Footer</strong>
                <p style="font-size: 11px; color: var(--muted); margin: 0;">32–40px height</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- COLORS                                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="colors">
      <h2 class="style-section-title">Brand Colors</h2>

      <div class="style-grid style-grid--colors">
        <div class="color-swatch" style="background: var(--cream); color: var(--void);">
          <span class="color-name">Cream</span>
          <span class="color-hex">#e8dfd0</span>
          <span class="color-usage">Primary text</span>
        </div>
        <div class="color-swatch" style="background: var(--paper); color: var(--void);">
          <span class="color-name">Paper</span>
          <span class="color-hex">#f2ede4</span>
          <span class="color-usage">Light background</span>
        </div>
        <div class="color-swatch" style="background: var(--bright); color: var(--void);">
          <span class="color-name">Bright</span>
          <span class="color-hex">#faf6ef</span>
          <span class="color-usage">Highlight</span>
        </div>
        <div class="color-swatch" style="background: var(--gold); color: var(--void);">
          <span class="color-name">Gold</span>
          <span class="color-hex">#d4b87a</span>
          <span class="color-usage">Accent, links</span>
        </div>
        <div class="color-swatch" style="background: var(--gold-dim); color: var(--cream);">
          <span class="color-name">Gold Dim</span>
          <span class="color-hex">#a68b5c</span>
          <span class="color-usage">Subtle accent</span>
        </div>
        <div class="color-swatch" style="background: var(--void); color: var(--cream);">
          <span class="color-name">Void</span>
          <span class="color-hex">#0c0b09</span>
          <span class="color-usage">Primary background</span>
        </div>
        <div class="color-swatch" style="background: var(--void2); color: var(--cream);">
          <span class="color-name">Void 2</span>
          <span class="color-hex">#1a1714</span>
          <span class="color-usage">Cards, secondary</span>
        </div>
        <div class="color-swatch" style="background: var(--void3); color: var(--cream);">
          <span class="color-name">Void 3</span>
          <span class="color-hex">#28231e</span>
          <span class="color-usage">Tertiary bg</span>
        </div>
        <div class="color-swatch" style="background: var(--surface); color: var(--cream);">
          <span class="color-name">Surface</span>
          <span class="color-hex">#342e28</span>
          <span class="color-usage">Elevated surfaces</span>
        </div>
        <div class="color-swatch" style="background: var(--muted); color: var(--void);">
          <span class="color-name">Muted</span>
          <span class="color-hex">#9e9282</span>
          <span class="color-usage">Secondary text</span>
        </div>
        <div class="color-swatch" style="background: var(--pale); color: var(--void);">
          <span class="color-name">Pale</span>
          <span class="color-hex">#c8bfae</span>
          <span class="color-usage">Body text</span>
        </div>
        <div class="color-swatch" style="background: var(--sage); color: var(--void);">
          <span class="color-name">Sage</span>
          <span class="color-hex">#8aaa7a</span>
          <span class="color-usage">Success states</span>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- CSS MANIPULATION                               -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="css">
      <h2 class="style-section-title">CSS Manipulation</h2>

      <div class="style-item style-item--full">
        <span class="style-label">CSS Filters Reference</span>
        <div class="style-demo" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 1rem; padding: 1rem; background: var(--void);">
          <div style="text-align: center; background: var(--void2); padding: 0.5rem; border-radius: 4px; border: 1px solid var(--rule);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="64" height="64">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">Original</p>
            <code style="font-size: 8px; color: var(--ash);">—</code>
          </div>
          <div style="text-align: center; background: var(--void2); padding: 0.5rem; border-radius: 4px; border: 1px solid var(--rule);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="64" height="64" style="filter: sepia(1) saturate(4) hue-rotate(-15deg) brightness(0.9);">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">Gold</p>
            <code style="font-size: 8px; color: var(--ash);">sepia(1) saturate(4) hue-rotate(-15deg) brightness(0.9)</code>
          </div>
          <div style="text-align: center; background: var(--void2); padding: 0.5rem; border-radius: 4px; border: 1px solid var(--rule);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="64" height="64" style="filter: brightness(0) invert(1) saturate(0.8);">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">Cream</p>
            <code style="font-size: 8px; color: var(--ash);">brightness(0) invert(1) saturate(0.8)</code>
          </div>
          <div style="text-align: center; background: var(--paper); padding: 0.5rem; border-radius: 4px; border: 1px solid var(--rule);">
            <img src="{{ '/assets/images/logo/logo.svg' | relative_url }}" width="64" height="64" style="filter: brightness(0);">
            <p style="font-size: 10px; color: var(--void); margin-top: 0.3rem;">Black</p>
            <code style="font-size: 8px; color: var(--ash);">brightness(0)</code>
          </div>
          <div style="text-align: center; background: var(--void2); padding: 0.5rem; border-radius: 4px; border: 1px solid var(--rule);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="64" height="64" style="filter: sepia(1) saturate(0.5) hue-rotate(0deg);">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">Greyscale</p>
            <code style="font-size: 8px; color: var(--ash);">sepia(1) saturate(0.5)</code>
          </div>
          <div style="text-align: center; background: var(--void2); padding: 0.5rem; border-radius: 4px; border: 1px solid var(--rule);">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="64" height="64" style="filter: brightness(1.5) saturate(0.8);">
            <p style="font-size: 10px; color: var(--muted); margin-top: 0.3rem;">Bright</p>
            <code style="font-size: 8px; color: var(--ash);">brightness(1.5) saturate(0.8)</code>
          </div>
        </div>
        <div class="style-code">Use CSS filters to adjust logo color without creating new files</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- EXAMPLES                                       -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="examples">
      <h2 class="style-section-title">Usage Examples</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Header</span>
          <div class="style-demo" style="background: var(--void); padding: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" alt="Logo" width="48" height="48">
              <span style="font-family: var(--display); font-size: 20px; font-style: italic; font-weight: 700; color: var(--cream);">The Journal of Incomplete Studies</span>
            </div>
          </div>
          <div class="style-code">
            <code>{% raw %}<img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="48" height="48">{% endraw %}</code>
          </div>
        </div>

        <div class="style-item">
          <span class="style-label">Hero / Landing Page</span>
          <div class="style-demo" style="background: var(--void); padding: 2rem; display: flex; flex-direction: column; align-items: center; gap: 1rem;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" alt="Logo" width="150" height="150">
            <h2 style="font-family: var(--display); font-size: 28px; font-style: italic; font-weight: 700; color: var(--cream); margin: 0;">The Journal of Incomplete Studies</h2>
            <p style="font-size: 14px; color: var(--muted); margin: 0;">A serial research publication for ideas still in motion</p>
          </div>
          <div class="style-code">
            <code>{% raw %}<img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="150" height="150">{% endraw %}</code>
          </div>
        </div>

        <div class="style-item">
          <span class="style-label">Footer</span>
          <div class="style-demo" style="background: var(--void2); padding: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
              <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" alt="Logo" width="32" height="32">
              <span style="font-family: var(--display); font-size: 16px; font-style: italic; font-weight: 700; color: var(--muted);">JIS</span>
              <span style="color: var(--ash); margin-left: 0.5rem; font-size: 12px;">© 2024</span>
            </div>
          </div>
          <div class="style-code">
            <code>{% raw %}<img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" width="32" height="32">{% endraw %}</code>
          </div>
        </div>

        <div class="style-item">
          <span class="style-label">Gold Accent (Hero)</span>
          <div class="style-demo" style="background: var(--void); padding: 2rem; display: flex; flex-direction: column; align-items: center;">
            <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" 
                 alt="Logo gold" 
                 width="120" 
                 height="120"
                 style="filter: sepia(1) saturate(4) hue-rotate(-15deg) brightness(0.9);">
            <p style="font-size: 12px; color: var(--gold); margin-top: 0.5rem; font-style: italic;">Scholarship in motion</p>
          </div>
          <div class="style-code">
            <code>style="filter: sepia(1) saturate(4) hue-rotate(-15deg) brightness(0.9);"</code>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- DARK / LIGHT MODE                             -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="dark-mode">
      <h2 class="style-section-title">Dark / Light Mode</h2>

      <div class="style-item style-item--full">
        <span class="style-label">Automatic Theme Switching</span>
        <div class="style-demo" style="background: var(--void); padding: 1rem;">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div style="text-align: center; background: var(--void); padding: 1rem; border-radius: 4px; border: 1px solid var(--rule);">
              <p style="font-size: 10px; color: var(--muted);">Light Logo (dark bg)</p>
              <img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" alt="Light logo" width="80" height="80">
              <p style="font-size: 9px; color: var(--ash); margin-top: 0.3rem;">.logo-light</p>
            </div>
            <div style="text-align: center; background: var(--paper); padding: 1rem; border-radius: 4px; border: 1px solid var(--rule);">
              <p style="font-size: 10px; color: var(--void);">Dark Logo (light bg)</p>
              <img src="{{ '/assets/images/logo/logo.svg' | relative_url }}" alt="Dark logo" width="80" height="80">
              <p style="font-size: 9px; color: var(--ash); margin-top: 0.3rem;">.logo-dark</p>
            </div>
          </div>
        </div>
        <div class="style-code" style="font-size: 11px; line-height: 1.8;">
          <strong>HTML:</strong><br>
          <code>{% raw %}<img src="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" class="logo-light">{% endraw %}</code><br>
          <code>{% raw %}<img src="{{ '/assets/images/logo/logo.svg' | relative_url }}" class="logo-dark">{% endraw %}</code><br><br>
          <strong>CSS:</strong><br>
          <code>.logo-dark { display: block; }</code><br>
          <code>.logo-light { display: none; }</code><br>
          <code>@media (prefers-color-scheme: dark) {</code><br>
          <code>&nbsp;&nbsp;.logo-dark { display: none; }</code><br>
          <code>&nbsp;&nbsp;.logo-light { display: block; }</code><br>
          <code>}</code>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- DOWNLOAD / REFERENCE                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="download">
      <h2 class="style-section-title">Download &amp; Reference</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Logo Files</span>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; color: var(--pale); line-height: 2.2;">
            <li>📄 <a href="{{ '/assets/images/logo/logo.svg' | relative_url }}" class="link-underline" target="_blank">Logo (Primary)</a></li>
            <li>📄 <a href="{{ '/assets/images/logo/logo-negative.svg' | relative_url }}" class="link-underline" target="_blank">Logo (Negative)</a></li>
          </ul>
          <div class="style-code">Right-click → Save As to download</div>
        </div>

        <div class="style-item">
          <span class="style-label">Quick Reference</span>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; color: var(--pale); line-height: 2.2;">
            <li><strong style="color: var(--cream);">Path:</strong> <code>/assets/images/logo/logo.svg</code></li>
            <li><strong style="color: var(--cream);">Format:</strong> SVG (Scalable Vector Graphics)</li>
            <li><strong style="color: var(--cream);">Colors:</strong> Cream · Gold · Void</li>
            <li><strong style="color: var(--cream);">License:</strong> All Rights Reserved</li>
          </ul>
        </div>
      </div>
    </section>

  </div>
</div>

<style>
/* ============================================
   LOGO & BRANDING GUIDE — IMPROVED UI/UX
   ============================================ */

/* ─── TABLE OF CONTENTS ─── */
.style-toc {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem 1.2rem;
  padding: 0.8rem 1.5rem;
  border: 1px solid var(--rule);
  border-radius: 6px;
  background: var(--void2);
  margin: 1.5rem 0 2rem;
}

.style-toc-label {
  font-family: var(--mono);
  font-size: 7px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ash);
  margin-right: 0.3rem;
}

.style-toc a {
  font-family: var(--mono);
  font-size: 8px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  padding-bottom: 2px;
  transition: all 0.2s ease;
}

.style-toc a:hover {
  color: var(--cream);
  border-color: var(--gold-dim);
}

/* ─── BODY ─── */
.style-guide-body {
  padding: 0 0 4rem;
  max-width: 1200px;
  margin: 0 auto;
}

.style-section {
  margin: 3rem 0 4rem 0;
  scroll-margin-top: 60px;
}

.style-section-title {
  font-family: var(--display);
  font-size: 28px;
  font-style: italic;
  font-weight: 700;
  color: var(--bright);
  margin-bottom: 1.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid var(--rule-mid);
}

/* ─── GRID LAYOUTS ─── */
.style-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.style-grid--logos {
  grid-template-columns: 1fr 1fr;
}

.style-grid--colors {
  grid-template-columns: repeat(4, 1fr);
}

.style-item--full {
  grid-column: 1 / -1;
}

/* ─── ITEMS ─── */
.style-item {
  padding: 1.25rem;
  border: 1px solid var(--rule);
  border-radius: 6px;
  background: var(--void2);
  transition: border-color 0.2s ease, background 0.2s ease;
}

.style-item:hover {
  border-color: var(--rule-mid);
  background: var(--void3);
}

.style-item--logo {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.style-label {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ash);
  margin-bottom: 0.75rem;
  display: block;
}

.style-demo {
  padding: 0.75rem;
  border-radius: 4px;
  border: 1px solid var(--rule);
  min-height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.logo-demo {
  min-height: 160px;
}

.logo-preview {
  width: 120px;
  height: 120px;
  object-fit: contain;
}

@media (max-width: 768px) {
  .logo-preview {
    width: 80px;
    height: 80px;
  }
}

/* ─── LOGO FILTERS ─── */
.logo-gold {
  filter: sepia(1) saturate(4) hue-rotate(-15deg) brightness(0.9);
}

.logo-cream {
  filter: brightness(0) invert(1) saturate(0.8);
}

/* ─── COLOR SWATCHES ─── */
.color-swatch {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  border-radius: 6px;
  border: 1px solid var(--rule);
  font-family: var(--mono);
  font-size: 9px;
  gap: 0.2rem;
  min-height: 80px;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.color-swatch:hover {
  transform: scale(1.03);
  border-color: var(--gold-dim);
}

.color-name {
  font-weight: 700;
}

.color-hex {
  opacity: 0.6;
  font-size: 8px;
}

.color-usage {
  font-size: 7px;
  opacity: 0.5;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-top: 0.2rem;
}

/* ─── CODE ─── */
.style-code {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--mid);
  margin-top: 0.75rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--rule);
  opacity: 0.8;
  line-height: 1.6;
  text-align: left;
  width: 100%;
}

.style-code code {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--gold-dim);
  background: var(--void);
  padding: 0.1rem 0.3rem;
  border-radius: 2px;
}

/* ─── RESPONSIVE ─── */
@media (max-width: 1024px) {
  .style-grid--colors {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .style-toc {
    padding: 0.75rem 1rem;
    gap: 0.3rem 1rem;
  }
  
  .style-toc a {
    font-size: 7px;
  }
  
  .style-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .style-grid--logos {
    grid-template-columns: 1fr;
  }
  
  .style-grid--colors {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .style-guide-body {
    padding: 0 0 3rem;
  }
  
  .style-section-title {
    font-size: 24px;
  }
  
  .style-item {
    padding: 1rem;
  }
  
  .logo-demo {
    min-height: 120px;
  }
}

@media (max-width: 480px) {
  .style-toc {
    padding: 0.5rem 0.75rem;
    gap: 0.2rem 0.75rem;
  }
  
  .style-toc a {
    font-size: 6px;
  }
  
  .style-toc-label {
    font-size: 6px;
    width: 100%;
    margin-bottom: 0.25rem;
  }
  
  .style-grid--colors {
    grid-template-columns: 1fr 1fr;
  }
  
  .style-section-title {
    font-size: 20px;
  }
}
</style>