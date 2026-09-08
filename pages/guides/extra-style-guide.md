---
layout: default
title: EXTRA Style Guide
permalink: /extra-style-guide/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Style Guide</span>
    <span class="col-head-meta">Component Library v1.0 — Extended</span>
  </div>

  <!-- ─── QUICK NAVIGATION ─── -->
  <div class="style-toc">
    <span class="style-toc-label">Jump to:</span>
    <a href="#forms">Forms & Inputs</a>
    <a href="#alerts">Alerts</a>
    <a href="#pagination">Pagination</a>
    <a href="#avatars">Avatars</a>
    <a href="#modals">Modals</a>
    <a href="#loading">Loading</a>
    <a href="#icons">Icons</a>
    <a href="#responsive">Responsive</a>
    <a href="#accessibility">Accessibility</a>
    <a href="#animations">Animations</a>
    <a href="#print">Print</a>
  </div>

  <div class="style-guide-body">

    <!-- ═══════════════════════════════════════════════ -->
    <!-- FORMS & INPUTS                                 -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="forms">
      <h2 class="style-section-title">Forms &amp; Inputs</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Text Input</span>
          <div class="style-demo">
            <input type="text" class="form-input" placeholder="Search projects..." value="Digital Archives">
          </div>
          <div class="style-code">.form-input · padding: 0.6rem 1rem · border: 1px solid var(--rule)</div>
        </div>

        <div class="style-item">
          <span class="style-label">Textarea</span>
          <div class="style-demo">
            <textarea class="form-textarea" placeholder="Write your response..." rows="3"></textarea>
          </div>
          <div class="style-code">.form-textarea · Resize: vertical · Font: var(--text)</div>
        </div>

        <div class="style-item">
          <span class="style-label">Select Dropdown</span>
          <div class="style-demo">
            <select class="form-select">
              <option>All projects</option>
              <option>Ongoing</option>
              <option>Archived</option>
              <option>On Hold</option>
            </select>
          </div>
          <div class="style-code">.form-select · Custom arrow · Background: var(--void2)</div>
        </div>

        <div class="style-item">
          <span class="style-label">Checkboxes &amp; Radio</span>
          <div class="style-demo" style="display: flex; gap: 2rem; flex-wrap: wrap;">
            <label class="form-check">
              <input type="checkbox" checked>
              <span>Checkbox</span>
            </label>
            <label class="form-check">
              <input type="checkbox">
              <span>Unchecked</span>
            </label>
            <label class="form-radio">
              <input type="radio" name="radio" checked>
              <span>Radio</span>
            </label>
            <label class="form-radio">
              <input type="radio" name="radio">
              <span>Radio</span>
            </label>
          </div>
          <div class="style-code">.form-check · .form-radio · Gold accent on checked</div>
        </div>

        <div class="style-item style-item--full">
          <span class="style-label">Search Bar</span>
          <div class="style-demo">
            <div class="search-bar">
              <span class="search-icon">⌕</span>
              <input type="search" class="search-input" placeholder="Search the archive...">
              <button class="search-btn">Search</button>
            </div>
          </div>
          <div class="style-code">.search-bar · .search-input · .search-btn</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- ALERTS & NOTIFICATIONS                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="alerts">
      <h2 class="style-section-title">Alerts &amp; Notifications</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Info</span>
          <div class="alert alert-info">This is an informational message.</div>
          <div class="style-code">.alert .alert-info</div>
        </div>

        <div class="style-item">
          <span class="style-label">Success</span>
          <div class="alert alert-success">✓ Your proposal has been submitted.</div>
          <div class="style-code">.alert .alert-success</div>
        </div>

        <div class="style-item">
          <span class="style-label">Warning</span>
          <div class="alert alert-warning">⚠️ This project will be archived soon.</div>
          <div class="style-code">.alert .alert-warning</div>
        </div>

        <div class="style-item">
          <span class="style-label">Error</span>
          <div class="alert alert-error">✕ There was a problem submitting your form.</div>
          <div class="style-code">.alert .alert-error</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- PAGINATION                                     -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="pagination">
      <h2 class="style-section-title">Pagination</h2>

      <div class="style-item">
        <nav class="pagination">
          <a href="#" class="pagination-prev">← Previous</a>
          <a href="#" class="pagination-link">1</a>
          <a href="#" class="pagination-link active">2</a>
          <a href="#" class="pagination-link">3</a>
          <span class="pagination-ellipsis">…</span>
          <a href="#" class="pagination-link">12</a>
          <a href="#" class="pagination-next">Next →</a>
        </nav>
        <div class="style-code">.pagination · .pagination-link · .pagination-link.active · .pagination-prev · .pagination-next</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- AVATARS                                        -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="avatars">
      <h2 class="style-section-title">Avatars</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Sizes</span>
          <div class="style-demo" style="display: flex; align-items: center; gap: 1rem;">
            <div class="avatar avatar-sm" style="background: var(--gold-dim);">JS</div>
            <div class="avatar avatar-md" style="background: var(--gold-dim);">JS</div>
            <div class="avatar avatar-lg" style="background: var(--gold-dim);">JS</div>
            <div class="avatar avatar-xl" style="background: var(--gold-dim);">JS</div>
          </div>
          <div class="style-code">.avatar · .avatar-sm · .avatar-md · .avatar-lg · .avatar-xl</div>
        </div>

        <div class="style-item">
          <span class="style-label">With Image</span>
          <div class="style-demo" style="display: flex; align-items: center; gap: 1rem;">
            <div class="avatar avatar-md" style="background: var(--void2); overflow: hidden;">
              <img src="/assets/images/avatar-placeholder.jpg" alt="Avatar" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div class="avatar avatar-md" style="background: var(--gold-dim);">JD</div>
            <div class="avatar avatar-md" style="background: var(--sage);">AK</div>
          </div>
          <div class="style-code">.avatar img · Initials as fallback</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- MODALS                                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="modals">
      <h2 class="style-section-title">Modals</h2>

      <div class="style-item">
        <span class="style-label">Modal Dialog</span>
        <div class="modal-demo">
          <div class="modal-overlay">
            <div class="modal">
              <div class="modal-header">
                <h3 class="modal-title">Confirm Action</h3>
                <button class="modal-close">✕</button>
              </div>
              <div class="modal-body">
                <p>Are you sure you want to archive this project?</p>
              </div>
              <div class="modal-footer">
                <button class="btn btn-secondary">Cancel</button>
                <button class="btn btn-primary">Confirm</button>
              </div>
            </div>
          </div>
        </div>
        <div class="style-code">.modal-overlay · .modal · .modal-header · .modal-body · .modal-footer</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- LOADING STATES                                 -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="loading">
      <h2 class="style-section-title">Loading States</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Spinner</span>
          <div class="style-demo" style="display: flex; gap: 1rem; align-items: center;">
            <div class="spinner"></div>
            <div class="spinner spinner-sm"></div>
            <div class="spinner spinner-lg"></div>
          </div>
          <div class="style-code">.spinner · .spinner-sm · .spinner-lg · Gold circular animation</div>
        </div>

        <div class="style-item">
          <span class="style-label">Skeleton</span>
          <div class="style-demo" style="display: flex; flex-direction: column; gap: 0.5rem; width: 100%;">
            <div class="skeleton" style="height: 20px; width: 60%;"></div>
            <div class="skeleton" style="height: 14px; width: 80%;"></div>
            <div class="skeleton" style="height: 14px; width: 70%;"></div>
            <div class="skeleton" style="height: 14px; width: 40%;"></div>
          </div>
          <div class="style-code">.skeleton · Pulsing background · Use for loading placeholders</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- ICONS                                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="icons">
      <h2 class="style-section-title">Icons</h2>

      <div class="style-item style-item--full">
        <span class="style-label">Common Icons</span>
        <div class="style-demo" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(80px, 1fr)); gap: 1rem; text-align: center;">
          <div><span class="icon" style="font-size: 24px;">⌕</span><br><span style="font-size: 10px; color: var(--muted);">search</span></div>
          <div><span class="icon" style="font-size: 24px;">✕</span><br><span style="font-size: 10px; color: var(--muted);">close</span></div>
          <div><span class="icon" style="font-size: 24px;">✓</span><br><span style="font-size: 10px; color: var(--muted);">check</span></div>
          <div><span class="icon" style="font-size: 24px;">←</span><br><span style="font-size: 10px; color: var(--muted);">back</span></div>
          <div><span class="icon" style="font-size: 24px;">→</span><br><span style="font-size: 10px; color: var(--muted);">forward</span></div>
          <div><span class="icon" style="font-size: 24px;">↑</span><br><span style="font-size: 10px; color: var(--muted);">up</span></div>
          <div><span class="icon" style="font-size: 24px;">↓</span><br><span style="font-size: 10px; color: var(--muted);">down</span></div>
          <div><span class="icon" style="font-size: 24px;">●</span><br><span style="font-size: 10px; color: var(--muted);">dot</span></div>
          <div><span class="icon" style="font-size: 24px;">✦</span><br><span style="font-size: 10px; color: var(--muted);">star</span></div>
          <div><span class="icon" style="font-size: 24px;">⟳</span><br><span style="font-size: 10px; color: var(--muted);">refresh</span></div>
          <div><span class="icon" style="font-size: 24px;">◈</span><br><span style="font-size: 10px; color: var(--muted);">diamond</span></div>
          <div><span class="icon" style="font-size: 24px;">◉</span><br><span style="font-size: 10px; color: var(--muted);">circle</span></div>
        </div>
        <div class="style-code">.icon · Use sparingly · Prefer text when possible</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- RESPONSIVE UTILITIES                           -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="responsive">
      <h2 class="style-section-title">Responsive Utilities</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Hide on Mobile</span>
          <div class="style-demo">
            <span class="hide-mobile">This is hidden on mobile</span>
            <span style="color: var(--muted); font-size: 12px; margin-left: 0.5rem;">(resize to test)</span>
          </div>
          <div class="style-code">.hide-mobile · display: none at &lt;768px</div>
        </div>

        <div class="style-item">
          <span class="style-label">Show on Mobile</span>
          <div class="style-demo">
            <span class="show-mobile">This is only visible on mobile</span>
            <span style="color: var(--muted); font-size: 12px; margin-left: 0.5rem;">(resize to test)</span>
          </div>
          <div class="style-code">.show-mobile · display: none at ≥768px</div>
        </div>

        <div class="style-item style-item--full">
          <span class="style-label">Breakpoints</span>
          <div class="style-demo" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; text-align: center;">
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">xs</span><br><span style="font-size: 12px; color: var(--muted);">0–480px</span></div>
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">sm</span><br><span style="font-size: 12px; color: var(--muted);">481–768px</span></div>
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">md</span><br><span style="font-size: 12px; color: var(--muted);">769–1024px</span></div>
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">lg</span><br><span style="font-size: 12px; color: var(--muted);">1025px+</span></div>
          </div>
          <div class="style-code">@media (max-width: 480px) · @media (max-width: 768px) · @media (max-width: 1024px)</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- ACCESSIBILITY                                  -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="accessibility">
      <h2 class="style-section-title">Accessibility</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Focus States</span>
          <div class="style-demo" style="display: flex; gap: 1rem; align-items: center;">
            <button class="btn btn-primary" style="outline: 2px solid var(--gold); outline-offset: 2px;">Focused</button>
            <a href="#" style="outline: 2px solid var(--gold); outline-offset: 2px; padding: 0.25rem 0.5rem;">Focused link</a>
          </div>
          <div class="style-code">:focus-visible · Gold outline · 2px offset</div>
        </div>

        <div class="style-item">
          <span class="style-label">Skip Link</span>
          <div class="style-demo">
            <a href="#main-content" class="skip-link">Skip to main content</a>
            <span style="color: var(--muted); font-size: 12px;">(hidden until focused)</span>
          </div>
          <div class="style-code">.skip-link · Position: absolute · Top: 0 · Left: 50%</div>
        </div>

        <div class="style-item style-item--full">
          <span class="style-label">Color Contrast Notes</span>
          <div class="style-demo" style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem;">
            <div style="background: var(--cream); color: var(--void); padding: 0.5rem; text-align: center; border-radius: 4px;">
              <span style="font-size: 13px; font-weight: 700;">AAA</span><br>
              <span style="font-size: 10px;">--cream on --void</span>
            </div>
            <div style="background: var(--gold); color: var(--void); padding: 0.5rem; text-align: center; border-radius: 4px;">
              <span style="font-size: 13px; font-weight: 700;">AA</span><br>
              <span style="font-size: 10px;">--gold on --void</span>
            </div>
            <div style="background: var(--muted); color: var(--void); padding: 0.5rem; text-align: center; border-radius: 4px;">
              <span style="font-size: 13px; font-weight: 700;">AA</span><br>
              <span style="font-size: 10px;">--muted on --void</span>
            </div>
          </div>
          <div class="style-code">All color combinations meet WCAG AA or AAA standards</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- ANIMATIONS                                     -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="animations">
      <h2 class="style-section-title">Animations</h2>

      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Fade In</span>
          <div class="style-demo">
            <div class="animate-fade" style="padding: 1rem; background: var(--void2); border: 1px solid var(--rule); border-radius: 4px;">
              This fades in on load
            </div>
          </div>
          <div class="style-code">.animate-fade · opacity: 0 → 1 · 0.5s ease</div>
        </div>

        <div class="style-item">
          <span class="style-label">Slide In</span>
          <div class="style-demo">
            <div class="animate-slide" style="padding: 1rem; background: var(--void2); border: 1px solid var(--rule); border-radius: 4px;">
              This slides in from below
            </div>
          </div>
          <div class="style-code">.animate-slide · transform: translateY(20px) → 0 · 0.5s ease</div>
        </div>

        <div class="style-item style-item--full">
          <span class="style-label">Duration Reference</span>
          <div class="style-demo" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; text-align: center;">
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">Instant</span><br><span style="font-size: 12px; color: var(--muted);">0s</span></div>
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">Fast</span><br><span style="font-size: 12px; color: var(--muted);">0.15s</span></div>
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">Medium</span><br><span style="font-size: 12px; color: var(--muted);">0.3s</span></div>
            <div><span style="font-family: var(--mono); font-size: 10px; color: var(--gold);">Slow</span><br><span style="font-size: 12px; color: var(--muted);">0.5s</span></div>
          </div>
          <div class="style-code">Use faster for UI, slower for ambient/entrance</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- PRINT STYLES                                   -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="print">
      <h2 class="style-section-title">Print Styles</h2>

      <div class="style-item">
        <span class="style-label">Print Preview</span>
        <div class="style-demo" style="background: var(--void2); padding: 1.5rem; border: 2px dashed var(--rule); text-align: center; color: var(--muted);">
          <span style="font-size: 14px;">📄</span>
          <p style="margin-top: 0.5rem; font-size: 13px;">Print styles are automatically applied when printing.</p>
          <p style="font-size: 12px; color: var(--ash);">• Dark backgrounds become white<br>• Text becomes black<br>• Links show URLs<br>• Navigation hidden</p>
        </div>
        <div class="style-code">@media print · Automatically applied</div>
      </div>
    </section>

  </div>
</div>

<style>
/* ============================================
   STYLE GUIDE — EXTENDED COMPONENTS
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
  background: rgba(255, 255, 255, 0.02);
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

.style-item--full {
  grid-column: 1 / -1;
}

/* ─── ITEMS ─── */
.style-item {
  padding: 1.25rem;
  border: 1px solid var(--rule);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.02);
  transition: border-color 0.2s ease;
}

.style-item:hover {
  border-color: var(--rule-mid);
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

.style-code {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--mid);
  margin-top: 0.75rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--rule);
  opacity: 0.7;
  line-height: 1.6;
}

.style-code code {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--gold-dim);
  background: var(--void);
  padding: 0.1rem 0.3rem;
  border-radius: 2px;
}

/* ─── DEMO CONTAINERS ─── */
.style-demo {
  padding: 0.75rem;
  border-radius: 4px;
  background: var(--void);
  border: 1px solid var(--rule);
}

/* ─── FORMS ─── */
.form-input,
.form-textarea,
.form-select {
  width: 100%;
  padding: 0.6rem 1rem;
  background: var(--void2);
  border: 1px solid var(--rule);
  border-radius: 4px;
  color: var(--cream);
  font-family: var(--text);
  font-size: 14px;
  transition: border-color 0.2s ease;
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
  outline: none;
  border-color: var(--gold-dim);
}

.form-textarea {
  resize: vertical;
  min-height: 80px;
}

.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%239e9282' stroke-width='1.5' fill='none'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  cursor: pointer;
}

.form-check,
.form-radio {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 13px;
  color: var(--pale);
  cursor: pointer;
}

.form-check input[type="checkbox"],
.form-radio input[type="radio"] {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 2px solid var(--rule);
  border-radius: 4px;
  background: var(--void);
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
}

.form-radio input[type="radio"] {
  border-radius: 50%;
}

.form-check input[type="checkbox"]:checked,
.form-radio input[type="radio"]:checked {
  border-color: var(--gold);
  background: var(--gold);
}

.form-check input[type="checkbox"]:checked::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: var(--void);
  font-size: 12px;
  font-weight: 700;
}

.form-radio input[type="radio"]:checked::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--void);
}

/* ─── SEARCH BAR ─── */
.search-bar {
  display: flex;
  align-items: center;
  background: var(--void2);
  border: 1px solid var(--rule);
  border-radius: 4px;
  transition: border-color 0.2s ease;
}

.search-bar:focus-within {
  border-color: var(--gold-dim);
}

.search-icon {
  padding: 0 0.75rem;
  color: var(--muted);
  font-size: 16px;
}

.search-input {
  flex: 1;
  padding: 0.6rem 0.75rem 0.6rem 0;
  background: transparent;
  border: none;
  color: var(--cream);
  font-family: var(--text);
  font-size: 14px;
}

.search-input:focus {
  outline: none;
}

.search-btn {
  padding: 0.5rem 1rem;
  margin: 0.25rem;
  background: var(--gold);
  color: var(--void);
  border: none;
  border-radius: 3px;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.search-btn:hover {
  opacity: 0.8;
}

/* ─── ALERTS ─── */
.alert {
  padding: 0.75rem 1rem;
  border-radius: 4px;
  border-left: 4px solid;
  font-size: 13px;
  line-height: 1.6;
}

.alert-info {
  background: rgba(212, 184, 122, 0.08);
  border-color: var(--gold-dim);
  color: var(--pale);
}

.alert-success {
  background: rgba(138, 170, 122, 0.12);
  border-color: var(--sage);
  color: var(--sage);
}

.alert-warning {
  background: rgba(192, 106, 74, 0.12);
  border-color: var(--rust);
  color: var(--rust);
}

.alert-error {
  background: rgba(192, 106, 74, 0.18);
  border-color: var(--rust);
  color: var(--rust);
}

/* ─── PAGINATION ─── */
.pagination {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.25rem;
  font-family: var(--mono);
  font-size: 11px;
}

.pagination a,
.pagination span {
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  text-decoration: none;
  color: var(--muted);
  transition: all 0.2s ease;
}

.pagination-link:hover {
  color: var(--cream);
  background: var(--void2);
}

.pagination-link.active {
  color: var(--gold);
  background: var(--void2);
  border: 1px solid var(--gold-dim);
}

.pagination-prev,
.pagination-next {
  color: var(--pale);
}

.pagination-prev:hover,
.pagination-next:hover {
  color: var(--cream);
  background: var(--void2);
}

.pagination-ellipsis {
  color: var(--muted);
}

/* ─── AVATARS ─── */
.avatar {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-family: var(--mono);
  font-weight: 700;
  color: var(--cream);
  background: var(--void2);
  border: 2px solid var(--rule);
  flex-shrink: 0;
}

.avatar-sm { width: 32px; height: 32px; font-size: 11px; }
.avatar-md { width: 48px; height: 48px; font-size: 14px; }
.avatar-lg { width: 64px; height: 64px; font-size: 18px; }
.avatar-xl { width: 96px; height: 96px; font-size: 28px; }

/* ─── MODALS ─── */
.modal-demo {
  position: relative;
  background: var(--void2);
  border-radius: 6px;
  overflow: hidden;
  min-height: 300px;
}

.modal-overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.6);
  min-height: 300px;
}

.modal {
  max-width: 480px;
  width: 100%;
  background: var(--void);
  border: 1px solid var(--rule-mid);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--rule);
}

.modal-title {
  font-family: var(--display);
  font-size: 18px;
  font-weight: 700;
  color: var(--cream);
  margin: 0;
}

.modal-close {
  background: transparent;
  border: none;
  color: var(--muted);
  font-size: 20px;
  cursor: pointer;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.modal-close:hover {
  color: var(--cream);
  background: var(--void2);
}

.modal-body {
  padding: 1.5rem;
}

.modal-body p {
  font-size: 14px;
  color: var(--pale);
  line-height: 1.7;
  margin: 0;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border-top: 1px solid var(--rule);
}

/* ─── LOADING ─── */
.spinner {
  width: 32px;
  height: 32px;
  border: 3px solid var(--void3);
  border-top-color: var(--gold);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.spinner-sm { width: 20px; height: 20px; border-width: 2px; }
.spinner-lg { width: 48px; height: 48px; border-width: 4px; }

@keyframes spin {
  to { transform: rotate(360deg); }
}

.skeleton {
  background: var(--void2);
  border-radius: 4px;
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

/* ─── ANIMATIONS ─── */
.animate-fade {
  animation: fadeIn 0.5s ease;
}

.animate-slide {
  animation: slideUp 0.5s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ─── RESPONSIVE UTILITIES ─── */
.hide-mobile {
  display: inline;
}

.show-mobile {
  display: none;
}

@media (max-width: 768px) {
  .hide-mobile {
    display: none;
  }
  
  .show-mobile {
    display: inline;
  }
}

/* ─── ACCESSIBILITY ─── */
.skip-link {
  position: absolute;
  top: -100%;
  left: 50%;
  transform: translateX(-50%);
  padding: 0.75rem 1.5rem;
  background: var(--gold);
  color: var(--void);
  font-family: var(--mono);
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 0 0 4px 4px;
  z-index: 1000;
}

.skip-link:focus {
  top: 0;
}

/* ─── RESPONSIVE ─── */
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
  
  .style-guide-body {
    padding: 0 0 3rem;
  }
  
  .style-section-title {
    font-size: 24px;
  }
  
  .style-item {
    padding: 1rem;
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
  
  .style-section-title {
    font-size: 20px;
  }
}

/* ─── PRINT ─── */
@media print {
  .style-toc {
    display: none;
  }
  
  .style-item {
    break-inside: avoid;
  }
}
</style>