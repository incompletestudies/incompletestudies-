---
layout: default
title: Under Construction
permalink: /under-construction/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">🚧 Under Construction</span>
    <span class="col-head-meta">Work in Progress · Coming Soon</span>
  </div>

  <!-- ─── QUICK NAVIGATION ─── -->
  <div class="style-toc">
    <span class="style-toc-label">Jump to:</span>
    <a href="#badges">Badges</a>
    <a href="#cards">Cards</a>
    <a href="#forms">Forms</a>
    <a href="#banners">Banners</a>
    <a href="#stamps">Stamps</a>
    <a href="#sidebar">Sidebar</a>
    <a href="#pages">Page States</a>
  </div>

  <div class="style-guide-body">

    <!-- ═══════════════════════════════════════════════ -->
    <!-- BADGES                                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="badges">
      <h2 class="style-section-title">Construction Badges</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Standard Badge</span>
          <div class="style-demo">
            <span class="badge-construction">🚧 Under Construction</span>
          </div>
          <div class="style-code">.badge-construction</div>
        </div>

        <div class="style-item">
          <span class="style-label">Work in Progress</span>
          <div class="style-demo">
            <span class="badge-construction badge-wip">⚡ Work in Progress</span>
          </div>
          <div class="style-code">.badge-construction.badge-wip</div>
        </div>

        <div class="style-item">
          <span class="style-label">Coming Soon</span>
          <div class="style-demo">
            <span class="badge-construction badge-coming">✨ Coming Soon</span>
          </div>
          <div class="style-code">.badge-construction.badge-coming</div>
        </div>

        <div class="style-item">
          <span class="style-label">In Development</span>
          <div class="style-demo">
            <span class="badge-construction badge-dev">🔨 In Development</span>
          </div>
          <div class="style-code">.badge-construction.badge-dev</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- CARDS                                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="cards">
      <h2 class="style-section-title">Construction Cards</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Default Construction Card</span>
          <div class="construction-card">
            <div class="construction-card-header">
              <span class="badge-construction">🚧 In Progress</span>
              <span class="construction-card-title">Feature Name</span>
            </div>
            <div class="construction-card-body">
              <p>This feature is currently being built. Check back soon.</p>
              <div class="construction-progress">
                <div class="progress-bar" style="width: 60%;"></div>
                <span class="progress-label">60%</span>
              </div>
            </div>
          </div>
          <div class="style-code">.construction-card</div>
        </div>

        <div class="style-item">
          <span class="style-label">Coming Soon Card</span>
          <div class="construction-card coming-soon">
            <div class="construction-card-header">
              <span class="badge-construction badge-coming">✨ Coming Soon</span>
              <span class="construction-card-title">Newsletter</span>
            </div>
            <div class="construction-card-body">
              <p>We're building a way to stay in touch. Enter your email to be notified when we launch.</p>
              <div class="construction-form">
                <input type="email" placeholder="Enter your email" disabled>
                <button disabled>Notify Me</button>
              </div>
              <div class="construction-note">
                <span class="construction-dot"></span>
                <span>You'll receive updates when we launch</span>
              </div>
            </div>
          </div>
          <div class="style-code">.construction-card.coming-soon</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- FORMS                                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="forms">
      <h2 class="style-section-title">Construction Forms</h2>
      
      <div class="style-grid">
        <div class="style-item style-item--full">
          <span class="style-label">Disabled Form</span>
          <div class="style-demo">
            <div class="construction-form">
              <div class="form-group">
                <label>Email Address</label>
                <input type="email" placeholder="Enter your email" disabled>
              </div>
              <div class="form-group">
                <label>Name</label>
                <input type="text" placeholder="Your name" disabled>
              </div>
              <button disabled>Submit (Coming Soon)</button>
              <div class="construction-note">
                <span class="construction-dot"></span>
                <span>This form is under construction</span>
              </div>
            </div>
          </div>
          <div class="style-code">.construction-form input:disabled · .construction-form button:disabled</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- BANNERS                                        -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="banners">
      <h2 class="style-section-title">Construction Banners</h2>
      
      <div class="style-grid">
        <div class="style-item style-item--full">
          <span class="style-label">Page Banner</span>
          <div class="style-demo">
            <div class="construction-banner">
              <span class="construction-banner-icon">🚧</span>
              <div class="construction-banner-content">
                <h3>This page is under construction</h3>
                <p>We're building something thoughtful. Check back soon.</p>
              </div>
            </div>
          </div>
          <div class="style-code">.construction-banner</div>
        </div>

        <div class="style-item style-item--full">
          <span class="style-label">Section Banner</span>
          <div class="style-demo">
            <div class="construction-banner section-banner">
              <span class="construction-banner-icon">🔨</span>
              <div class="construction-banner-content">
                <h4>This section is being developed</h4>
                <p>We're building thoughtfully — check back soon.</p>
              </div>
            </div>
          </div>
          <div class="style-code">.construction-banner.section-banner</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- STAMPS                                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="stamps">
      <h2 class="style-section-title">Construction Stamps</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Incomplete Stamp</span>
          <div class="style-demo">
            <div class="stamp-incomplete">Incomplete</div>
          </div>
          <div class="style-code">.stamp-incomplete</div>
        </div>

        <div class="style-item">
          <span class="style-label">Draft Stamp</span>
          <div class="style-demo">
            <div class="stamp-draft">Draft</div>
          </div>
          <div class="style-code">.stamp-draft</div>
        </div>

        <div class="style-item">
          <span class="style-label">Work in Progress Stamp</span>
          <div class="style-demo">
            <div class="stamp-wip">WIP</div>
          </div>
          <div class="style-code">.stamp-wip</div>
        </div>

        <div class="style-item">
          <span class="style-label">Coming Soon Stamp</span>
          <div class="style-demo">
            <div class="stamp-coming">Coming Soon</div>
          </div>
          <div class="style-code">.stamp-coming</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- SIDEBAR                                        -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="sidebar">
      <h2 class="style-section-title">Sidebar Components</h2>
      
      <div class="style-grid">
        <div class="style-item style-item--full">
          <span class="style-label">Coming Soon Sidebar Card</span>
          <div class="style-demo" style="max-width: 320px; margin: 0 auto;">
            <div class="sidebar-card coming-soon-card">
              <div class="coming-soon-header">
                <span class="badge-construction">🚧 In Progress</span>
                <span class="coming-soon-label">Newsletter</span>
              </div>
              <div class="coming-soon-body">
                <p>We're building a newsletter to share new installments and updates.</p>
                <div class="construction-form">
                  <input type="email" placeholder="Enter your email" disabled>
                  <button disabled>Coming Soon</button>
                </div>
                <div class="construction-note">
                  <span class="construction-dot"></span>
                  <span>This feature is under construction</span>
                </div>
              </div>
            </div>
          </div>
          <div class="style-code">.sidebar-card.coming-soon-card</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- PAGE STATES                                    -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="pages">
      <h2 class="style-section-title">Page States</h2>
      
      <div class="style-grid">
        <div class="style-item style-item--full">
          <span class="style-label">Full Page Under Construction</span>
          <div class="style-demo">
            <div class="page-construction">
              <div class="page-construction-icon">🚧</div>
              <h1>This page is under construction</h1>
              <p>We're building something meaningful here.</p>
              <div class="page-construction-progress">
                <div class="progress-bar" style="width: 45%;"></div>
                <span class="progress-label">45% complete</span>
              </div>
              <div class="page-construction-note">
                <span class="construction-dot"></span>
                <span>Check back soon for updates</span>
              </div>
            </div>
          </div>
          <div class="style-code">.page-construction</div>
        </div>
      </div>
    </section>

  </div>
</div>

<style>
/* ============================================
   UNDER CONSTRUCTION — STYLE GUIDE
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

/* ─── DEMO ─── */
.style-demo {
  padding: 0.75rem;
  border-radius: 4px;
  background: var(--void);
  border: 1px solid var(--rule);
}

/* ═══════════════════════════════════════════════ */
/* UNDER CONSTRUCTION COMPONENTS                  */
/* ═══════════════════════════════════════════════ */

/* ─── BADGES ─── */
.badge-construction {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--gold-dim);
  padding: 0.2rem 0.8rem;
  border: 1px dashed var(--gold-dim);
  border-radius: 20px;
  background: rgba(212, 184, 122, 0.05);
  animation: pulse-border 2s ease-in-out infinite;
}

.badge-wip {
  border-color: var(--sage);
  color: var(--sage);
}

.badge-coming {
  border-color: var(--gold);
  color: var(--gold);
}

.badge-dev {
  border-color: var(--rust);
  color: var(--rust);
}

@keyframes pulse-border {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* ─── CARDS ─── */
.construction-card {
  border: 1px dashed var(--gold-dim);
  border-radius: 6px;
  padding: 1.25rem;
  background: var(--void2);
}

.construction-card-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.construction-card-title {
  font-family: var(--display);
  font-size: 16px;
  font-weight: 700;
  color: var(--cream);
}

.construction-card-body p {
  font-size: 13px;
  color: var(--pale);
  line-height: 1.6;
  margin: 0 0 0.8rem 0;
}

.coming-soon .construction-card-body p {
  margin-bottom: 0.8rem;
}

/* ─── PROGRESS ─── */
.construction-progress {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.progress-bar {
  flex: 1;
  height: 4px;
  background: var(--void);
  border-radius: 2px;
  overflow: hidden;
  position: relative;
}

.progress-bar::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background: var(--gold-dim);
  border-radius: 2px;
  width: var(--progress, 60%);
}

.progress-label {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--muted);
}

/* ─── FORMS ─── */
.construction-form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.construction-form .form-group {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.construction-form label {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.construction-form input {
  padding: 0.5rem 0.8rem;
  background: var(--void);
  border: 1px dashed var(--rule);
  border-radius: 4px;
  color: var(--muted);
  font-size: 13px;
  opacity: 0.6;
  cursor: not-allowed;
}

.construction-form input:disabled,
.construction-form button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.construction-form button {
  padding: 0.5rem 1rem;
  background: var(--void2);
  border: 1px dashed var(--rule);
  border-radius: 4px;
  color: var(--muted);
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: not-allowed;
  transition: all 0.2s ease;
}

.construction-note {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0.5rem;
}

.construction-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--gold-dim);
  animation: pulse-dot 1.5s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.3; transform: scale(0.8); }
}

/* ─── BANNERS ─── */
.construction-banner {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.25rem 1.5rem;
  background: var(--void2);
  border: 1px dashed var(--gold-dim);
  border-radius: 6px;
}

.construction-banner-icon {
  font-size: 24px;
  line-height: 1;
  flex-shrink: 0;
}

.construction-banner-content h3 {
  font-family: var(--display);
  font-size: 18px;
  font-weight: 700;
  color: var(--cream);
  margin: 0 0 0.2rem 0;
}

.construction-banner-content h4 {
  font-family: var(--display);
  font-size: 16px;
  font-weight: 700;
  color: var(--cream);
  margin: 0 0 0.2rem 0;
}

.construction-banner-content p {
  font-size: 13px;
  color: var(--pale);
  line-height: 1.6;
  margin: 0;
}

.section-banner {
  border-color: var(--sage);
  background: rgba(138, 170, 122, 0.05);
}

/* ─── STAMPS ─── */
.stamp-incomplete,
.stamp-draft,
.stamp-wip,
.stamp-coming {
  display: inline-block;
  font-family: var(--display);
  font-size: 14px;
  font-style: italic;
  font-weight: 700;
  padding: 0.2rem 1rem;
  border-radius: 4px;
  transform: rotate(-2deg);
  letter-spacing: 0.04em;
}

.stamp-incomplete {
  color: var(--gold);
  border: 2px solid var(--gold-dim);
  background: rgba(212, 184, 122, 0.03);
}

.stamp-draft {
  color: var(--muted);
  border: 2px solid var(--rule);
  background: rgba(255, 255, 255, 0.02);
}

.stamp-wip {
  color: var(--sage);
  border: 2px solid var(--sage);
  background: rgba(138, 170, 122, 0.05);
}

.stamp-coming {
  color: var(--gold);
  border: 2px solid var(--gold);
  background: rgba(212, 184, 122, 0.05);
}

/* ─── SIDEBAR ─── */
.sidebar-card {
  background: var(--void2);
  border: 1px solid var(--rule);
  padding: 1.5rem;
  border-radius: 6px;
}

.sidebar-label {
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold-dim);
  margin-bottom: 0.8rem;
}

.coming-soon-card {
  border: 1px dashed var(--gold-dim) !important;
}

.coming-soon-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.coming-soon-label {
  font-family: var(--display);
  font-size: 16px;
  font-weight: 700;
  color: var(--cream);
}

.coming-soon-body p {
  font-size: 13px;
  color: var(--pale);
  line-height: 1.6;
  margin: 0 0 0.8rem 0;
}

/* ─── PAGE STATES ─── */
.page-construction {
  text-align: center;
  padding: 3rem 2rem;
  background: var(--void2);
  border: 1px dashed var(--gold-dim);
  border-radius: 8px;
}

.page-construction-icon {
  font-size: 48px;
  margin-bottom: 1rem;
}

.page-construction h1 {
  font-family: var(--display);
  font-size: 28px;
  font-weight: 700;
  color: var(--cream);
  margin: 0 0 0.5rem 0;
}

.page-construction p {
  font-size: 16px;
  color: var(--pale);
  margin: 0 0 1.5rem 0;
}

.page-construction-progress {
  max-width: 400px;
  margin: 0 auto 1rem auto;
}

.page-construction-note {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
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
  
  .construction-banner {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .page-construction h1 {
    font-size: 22px;
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
</style>