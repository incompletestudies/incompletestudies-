---
layout: default
title: Style Guide
permalink: /style-guide/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Style Guide</span>
    <span class="col-head-meta">Component Library v1.0</span>
  </div>

  <!-- ─── QUICK NAVIGATION ─── -->
  <div class="style-toc">
    <span class="style-toc-label">Jump to:</span>
    <a href="#typography">Typography</a>
    <a href="#colors">Colors</a>
    <a href="#badges">Badges</a>
    <a href="#cards">Cards</a>
    <a href="#tags">Tags</a>
    <a href="#links">Links</a>
    <a href="#breadcrumb">Breadcrumb</a>
    <a href="#headers">Headers</a>
    <a href="#grids">Grids</a>
    <a href="#spacing">Spacing</a>
    <a href="#interactive">Interactive</a>
    <a href="#buttons">Buttons</a>
    <a href="#links">Links</a>  
    <a href="#universal-lists">Universal Lists</a>  
  </div>

  <div class="style-guide-body">
    
    <!-- ─── TYPOGRAPHY ─── -->
    <section class="style-section" id="typography">
      <h2 class="style-section-title">Typography</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <h3 class="style-label">Display Font</h3>
          <p style="font-family: var(--display); font-size: 32px; font-style: italic; font-weight: 700;">
            The Journal of Incomplete Studies
          </p>
          <p class="style-code">font-family: var(--display)</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Text Font</h3>
          <p style="font-family: var(--text); font-size: 16px;">
            A serial research publication for ideas still in motion.
          </p>
          <p class="style-code">font-family: var(--text)</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Mono Font</h3>
          <p style="font-family: var(--mono); font-size: 14px;">
            Installment 03 · January 2026
          </p>
          <p class="style-code">font-family: var(--mono)</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Script Font</h3>
          <p style="font-family: var(--script); font-size: 24px; color: var(--gold);">
            Notes in the margin
          </p>
          <p class="style-code">font-family: var(--script)</p>
        </div>
      </div>
    </section>

    <!-- ─── COLORS ─── -->
    <section class="style-section" id="colors">
      <h2 class="style-section-title">Colors</h2>
      
      <div class="style-grid">
        <div class="color-swatch" style="background: var(--void); color: var(--cream);">
          <span class="color-name">--void</span>
          <span class="color-hex">#0c0b09</span>
        </div>
        <div class="color-swatch" style="background: var(--void2); color: var(--cream);">
          <span class="color-name">--void2</span>
          <span class="color-hex">#1a1714</span>
        </div>
        <div class="color-swatch" style="background: var(--void3); color: var(--cream);">
          <span class="color-name">--void3</span>
          <span class="color-hex">#28231e</span>
        </div>
        <div class="color-swatch" style="background: var(--cream); color: var(--void);">
          <span class="color-name">--cream</span>
          <span class="color-hex">#e8dfd0</span>
        </div>
        <div class="color-swatch" style="background: var(--pale); color: var(--void);">
          <span class="color-name">--pale</span>
          <span class="color-hex">#c8bfae</span>
        </div>
        <div class="color-swatch" style="background: var(--muted); color: var(--void);">
          <span class="color-name">--muted</span>
          <span class="color-hex">#9e9282</span>
        </div>
        <div class="color-swatch" style="background: var(--mid); color: var(--cream);">
          <span class="color-name">--mid</span>
          <span class="color-hex">#7a6e60</span>
        </div>
        <div class="color-swatch" style="background: var(--ash); color: var(--cream);">
          <span class="color-name">--ash</span>
          <span class="color-hex">#5a4f44</span>
        </div>
        <div class="color-swatch" style="background: var(--gold); color: var(--void);">
          <span class="color-name">--gold</span>
          <span class="color-hex">#d4b87a</span>
        </div>
        <div class="color-swatch" style="background: var(--gold-dim); color: var(--cream);">
          <span class="color-name">--gold-dim</span>
          <span class="color-hex">#a68b5c</span>
        </div>
        <div class="color-swatch" style="background: var(--sage); color: var(--void);">
          <span class="color-name">--sage</span>
          <span class="color-hex">#8aaa7a</span>
        </div>
        <div class="color-swatch" style="background: var(--rust); color: var(--cream);">
          <span class="color-name">--rust</span>
          <span class="color-hex">#c06a4a</span>
        </div>
      </div>
    </section>

    <!-- ─── BADGES ─── -->
    <section class="style-section" id="badges">
      <h2 class="style-section-title">Badges</h2>
      
      <div class="style-grid style-grid-badges">
        <div class="style-item">
          <h3 class="style-label">Project Status (from main.css)</h3>
          <div class="style-badge-row">
            <span class="badge ongoing">Ongoing</span>
            <span class="badge on-hold">On Hold</span>
            <span class="badge archived">Archived</span>
          </div>
          <p class="style-code">.badge {status}</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Installment Status (from main.css)</h3>
          <div class="style-badge-row">
            <span class="badge first">First Inst.</span>
            <span class="badge revised">Revised</span>
            <span class="badge last">Last Inst.</span>
          </div>
          <p class="style-code">.badge {type}</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Cohort Status (from main.css)</h3>
          <div class="style-badge-row">
            <span class="badge active">Active</span>
            <span class="badge on-leave">On Leave</span>
            <span class="badge alumni">Alumni</span>
          </div>
          <p class="style-code">.badge {type}</p>
        </div>

        <div class="style-item">
          <h3 class="style-label">Pills (from main.css)</h3>
          <div class="style-badge-row">
            <span class="pill live">● Live</span>
            <span class="pill new">✦ New</span>
            <span class="pill upcoming">Upcoming</span>
            <span class="pill draft">Draft</span>
          </div>
          <p class="style-code">.pill {variant}</p>
        </div>
      </div>
    </section>

    <!-- ─── CARDS ─── -->
    <section class="style-section" id="cards">
      <h2 class="style-section-title">Cards</h2>
      
      <div class="style-grid" style="grid-template-columns: 1fr 1fr;">
        <!-- Using actual card class from main.css -->
        <div class="card">
          <div class="card-header">
            <span class="card-id">P–01</span>
            <span class="badge ongoing">Ongoing</span>
          </div>
          <h3 class="card-title">Digital Archives Initiative</h3>
          <p class="card-subtitle">Dr. Jane Smith + 3 others</p>
          <p class="card-excerpt">A multi-year project exploring the preservation of born-digital cultural heritage through distributed ledger technologies.</p>
          <div class="card-meta">
            <span><span class="card-meta-number">12</span> installments</span>
            <span style="margin-left: auto;">[tag] [tag]</span>
          </div>
        </div>
        
        <div class="card">
          <div class="card-header">
            <span class="card-id">P–02</span>
            <span class="pill new">✦ New</span>
          </div>
          <h3 class="card-title">Incomplete Manuscripts</h3>
          <p class="card-subtitle">Dr. John Doe</p>
          <p class="card-excerpt">A study of unfinished literary manuscripts and what they reveal about creative processes.</p>
          <div class="card-meta">
            <span><span class="card-meta-number">3</span> installments</span>
            <span style="margin-left: auto;">[tag] [tag]</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ─── TAGS ─── -->
    <section class="style-section" id="tags">
      <h2 class="style-section-title">Tags</h2>
      
      <div class="style-item">
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center;">
          <span class="tag">Archives</span>
          <span class="tag">Digital Humanities</span>
          <span class="tag">Memory Studies</span>
          <span class="tag">Media Theory</span>
          <span class="tag-more">+3</span>
        </div>
        <p class="style-code">.tag .tag-more</p>
      </div>
    </section>

    <!-- ─── LINKS ─── -->
    <section class="style-section" id="links">
      <h2 class="style-section-title">Links</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <h3 class="style-label">Standard Link</h3>
          <a href="#" class="link-underline">Read more about this project →</a>
          <p class="style-code">.link-underline</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Mono Link</h3>
          <a href="#" class="link-mono">View all installments →</a>
          <p class="style-code">.link-mono</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Back Link</h3>
          <button class="back-link">← Back to all seasons</button>
          <p class="style-code">.back-link</p>
        </div>
      </div>
    </section>

    <!-- ─── BREADCRUMB ─── -->
    <section class="style-section" id="breadcrumb">
      <h2 class="style-section-title">Breadcrumb</h2>
      
      <div class="breadcrumb" style="padding: 1rem 0;">
        <a href="#">Home</a>
        <span class="crumb-sep">/</span>
        <a href="#">Projects</a>
        <span class="crumb-sep">/</span>
        <span class="crumb-current">Digital Archives Initiative</span>
      </div>
      <p class="style-code">.breadcrumb .crumb-current .crumb-sep</p>
    </section>

    <!-- ─── HEADERS ─── -->
    <section class="style-section" id="headers">
      <h2 class="style-section-title">Section Headers</h2>
      
      <div class="style-item">
        <div class="section-header">
          <h3 class="section-title">Current Projects</h3>
          <span class="section-meta">4 active</span>
        </div>
        <p class="style-code">.section-header .section-title .section-meta</p>
      </div>
      
      <div class="style-item">
        <div class="col-head" style="padding: 0.5rem 0;">
          <span class="col-head-title">Installments</span>
          <span class="col-head-meta">24 total · Season 01</span>
        </div>
        <p class="style-code">.col-head .col-head-title .col-head-meta</p>
      </div>
    </section>

    <!-- ─── GRIDS ─── -->
    <section class="style-section" id="grids">
      <h2 class="style-section-title">Grids</h2>
      
      <div class="style-item">
        <h3 class="style-label">2-Column Grid</h3>
        <div class="grid-2" style="border: 1px solid var(--rule); padding: 1rem;">
          <div style="background: var(--void2); padding: 1rem; border-radius: 4px;">Item 1</div>
          <div style="background: var(--void2); padding: 1rem; border-radius: 4px;">Item 2</div>
        </div>
        <p class="style-code">.grid-2</p>
      </div>
      
      <div class="style-item">
        <h3 class="style-label">3-Column Grid</h3>
        <div class="grid-3" style="border: 1px solid var(--rule); padding: 1rem;">
          <div style="background: var(--void2); padding: 1rem; border-radius: 4px;">Item 1</div>
          <div style="background: var(--void2); padding: 1rem; border-radius: 4px;">Item 2</div>
          <div style="background: var(--void2); padding: 1rem; border-radius: 4px;">Item 3</div>
        </div>
        <p class="style-code">.grid-3</p>
      </div>
    </section>

    <!-- ─── SPACING ─── -->
    <section class="style-section" id="spacing">
      <h2 class="style-section-title">Spacing Utilities</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <h3 class="style-label">Margin</h3>
          <div style="border: 1px solid var(--rule); padding: 0.5rem; background: var(--void3);">
            <div style="background: var(--void2); border: 1px solid var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px; margin-bottom: 0.25rem;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.mt-sm</span>
              <div class="mt-sm" style="background: rgba(212, 184, 122, 0.15); border: 1px dashed var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--gold);">0.25rem</span>
              </div>
            </div>
            <div style="background: var(--void2); border: 1px solid var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px; margin-bottom: 0.25rem;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.mt-md</span>
              <div class="mt-md" style="background: rgba(212, 184, 122, 0.15); border: 1px dashed var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--gold);">1rem</span>
              </div>
            </div>
            <div style="background: var(--void2); border: 1px solid var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px; margin-bottom: 0.25rem;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.mt-lg</span>
              <div class="mt-lg" style="background: rgba(212, 184, 122, 0.15); border: 1px dashed var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--gold);">1.5rem</span>
              </div>
            </div>
            <div style="background: var(--void2); border: 1px solid var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.mt-xl</span>
              <div class="mt-xl" style="background: rgba(212, 184, 122, 0.15); border: 1px dashed var(--gold-dim); padding: 0.25rem 0.5rem; border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--gold);">2.5rem</span>
              </div>
            </div>
          </div>
          <p class="style-code">.mt-{sm|md|lg|xl}</p>
        </div>
        
        <div class="style-item">
          <h3 class="style-label">Padding</h3>
          <div style="border: 1px solid var(--rule); padding: 0.5rem; background: var(--void3);">
            <div style="background: var(--void2); border: 1px solid var(--sage-dim); padding: 0.25rem 0.5rem; border-radius: 2px; margin-bottom: 0.25rem;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.p-sm</span>
              <div class="p-sm" style="background: rgba(138, 170, 122, 0.12); border: 1px dashed var(--sage-dim); border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--sage);">0.25rem</span>
              </div>
            </div>
            <div style="background: var(--void2); border: 1px solid var(--sage-dim); padding: 0.25rem 0.5rem; border-radius: 2px; margin-bottom: 0.25rem;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.p-md</span>
              <div class="p-md" style="background: rgba(138, 170, 122, 0.12); border: 1px dashed var(--sage-dim); border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--sage);">1rem</span>
              </div>
            </div>
            <div style="background: var(--void2); border: 1px solid var(--sage-dim); padding: 0.25rem 0.5rem; border-radius: 2px; margin-bottom: 0.25rem;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.p-lg</span>
              <div class="p-lg" style="background: rgba(138, 170, 122, 0.12); border: 1px dashed var(--sage-dim); border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--sage);">1.5rem</span>
              </div>
            </div>
            <div style="background: var(--void2); border: 1px solid var(--sage-dim); padding: 0.25rem 0.5rem; border-radius: 2px;">
              <span style="font-family: var(--mono); font-size: 8px; color: var(--muted);">.p-xl</span>
              <div class="p-xl" style="background: rgba(138, 170, 122, 0.12); border: 1px dashed var(--sage-dim); border-radius: 2px;">
                <span style="font-family: var(--mono); font-size: 7px; color: var(--sage);">2.5rem</span>
              </div>
            </div>
          </div>
          <p class="style-code">.p-{sm|md|lg|xl}</p>
        </div>
      </div>
    </section>

    <!-- ─── INTERACTIVE COMPONENTS ─── -->
    <section class="style-section" id="interactive">
      <h2 class="style-section-title">Interactive Components</h2>
      
      <div class="style-grid">
        <!-- Card Hover -->
        <div class="style-item">
          <h3 class="style-label">Card Hover</h3>
          <div class="card interactive-demo">
            <div class="card-header">
              <span class="card-id">P–01</span>
              <span class="badge active">Active</span>
            </div>
            <h3 class="card-title">Hover me</h3>
            <p class="card-subtitle">Dr. Jane Smith</p>
            <p class="card-excerpt">Hover over this card to see the interactive effect from main.css.</p>
            <div class="card-meta">
              <span><span class="card-meta-number">12</span> installments</span>
            </div>
          </div>
          <p class="style-code">.card:hover → border-color: var(--gold-dim) · transform: translateY(-3px)</p>
        </div>

        
        <!-- Buttons -->
        <div class="style-item">
          <h3 class="style-label">Buttons</h3>
          <div style="display: flex; gap: 1rem; flex-wrap: wrap; align-items: center;">
            <button class="demo-btn primary">Primary</button>
            <button class="demo-btn secondary">Secondary</button>
            <button class="demo-btn outline">Outline</button>
          </div>
          <p class="style-code">.demo-btn:hover → background/color transition</p>
        </div>

        <!-- Links -->
        <div class="style-item">
          <h3 class="style-label">Link Hover</h3>
          <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
            <a href="#" class="link-underline demo-link">Standard link</a>
            <a href="#" class="link-mono demo-link">Mono link</a>
          </div>
          <p class="style-code">.link-underline:hover → color: var(--gold) · border-color: var(--gold-dim)</p>
        </div>

        <!-- Accordion -->
        <div class="style-item">
          <h3 class="style-label">Accordion</h3>
          <details class="demo-details">
            <summary>Click to expand</summary>
            <div>
              <p style="font-family: var(--text); font-size: 13px; color: var(--pale); line-height: 1.6;">
                This is expandable content. Click the summary again to collapse.
              </p>
              <ul style="font-family: var(--mono); font-size: 11px; color: var(--muted); list-style: none; padding: 0.5rem 0;">
                <li style="padding: 0.3rem 0; border-bottom: 1px solid var(--rule);">• Interactive demo</li>
                <li style="padding: 0.3rem 0; border-bottom: 1px solid var(--rule);">• Shows toggle behavior</li>
                <li style="padding: 0.3rem 0;">• Works with details/summary</li>
              </ul>
            </div>
          </details>
          <p class="style-code">details[open] → shows content · summary::after → + / −</p>
        </div>

        <!-- Tooltip -->
        <div class="style-item">
          <h3 class="style-label">Tooltip</h3>
          <div style="padding: 1rem 0;">
            <span class="demo-tooltip" data-tooltip="This is a tooltip!">
              Hover over me
            </span>
          </div>
          <p class="style-code">::before + ::after on hover → shows tooltip</p>
        </div>

        <!-- Tags -->
        <div class="style-item">
          <h3 class="style-label">Tag Hover</h3>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <span class="tag demo-tag">Archives</span>
            <span class="tag demo-tag">Digital Humanities</span>
            <span class="tag demo-tag">Memory Studies</span>
          </div>
          <p class="style-code">.tag:hover → border-color: var(--gold-dim)</p>
        </div>
      </div>
    </section>


    <!-- ─── BUTTONS ─── -->
    <section class="style-section" id="buttons">
      <h2 class="style-section-title">Buttons</h2>
      
      <div class="style-grid">
        <!-- Primary -->
        <div class="style-item">
          <h3 class="style-label">Primary</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;">
            <button class="btn btn-primary">Primary</button>
            <button class="btn btn-primary btn-sm">Small</button>
            <button class="btn btn-primary btn-lg">Large</button>
          </div>
          <p class="style-code">.btn .btn-primary</p>
        </div>

        <!-- Secondary -->
        <div class="style-item">
          <h3 class="style-label">Secondary</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;">
            <button class="btn btn-secondary">Secondary</button>
            <button class="btn btn-secondary btn-sm">Small</button>
            <button class="btn btn-secondary btn-lg">Large</button>
          </div>
          <p class="style-code">.btn .btn-secondary</p>
        </div>

        <!-- Outline -->
        <div class="style-item">
          <h3 class="style-label">Outline</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;">
            <button class="btn btn-outline">Outline</button>
            <button class="btn btn-outline btn-sm">Small</button>
            <button class="btn btn-outline btn-lg">Large</button>
          </div>
          <p class="style-code">.btn .btn-outline</p>
        </div>

        <!-- Ghost -->
        <div class="style-item">
          <h3 class="style-label">Ghost</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;">
            <button class="btn btn-ghost">Ghost</button>
            <button class="btn btn-ghost btn-sm">Small</button>
            <button class="btn btn-ghost btn-lg">Large</button>
          </div>
          <p class="style-code">.btn .btn-ghost</p>
        </div>

        <!-- Block -->
        <div class="style-item">
          <h3 class="style-label">Block (Full Width)</h3>
          <button class="btn btn-primary btn-block">Full Width Button</button>
          <p class="style-code">.btn .btn-primary .btn-block</p>
        </div>

        <!-- Icon -->
        <div class="style-item">
          <h3 class="style-label">Icon Buttons</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;">
            <button class="btn btn-primary btn-icon">✕</button>
            <button class="btn btn-secondary btn-icon">✕</button>
            <button class="btn btn-outline btn-icon">✕</button>
            <button class="btn btn-primary btn-icon btn-sm">✕</button>
            <button class="btn btn-primary btn-icon btn-lg">✕</button>
          </div>
          <p class="style-code">.btn .btn-primary .btn-icon</p>
        </div>

        <!-- Link as Button -->
        <div class="style-item">
          <h3 class="style-label">Link as Button</h3>
          <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; align-items: center;">
            <button class="btn-link">← Back</button>
            <button class="btn-link">View All →</button>
            <button class="btn-link">Apply now</button>
          </div>
          <p class="style-code">.btn-link</p>
        </div>

        <!-- Disabled States -->
        <div class="style-item">
          <h3 class="style-label">Disabled States</h3>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;">
            <button class="btn btn-primary" disabled>Primary</button>
            <button class="btn btn-secondary" disabled>Secondary</button>
            <button class="btn btn-outline" disabled>Outline</button>
          </div>
          <p class="style-code">Add <code>disabled</code> attribute</p>
        </div>
      </div>
    </section>

    
    <!-- ─── LINKS ─── -->
    <section class="style-section" id="links">
      <h2 class="style-section-title">Links</h2>
      
      <div class="style-grid">
        <!-- 1. Mono Link -->
        <div class="style-item">
          <h3 class="style-label">Mono Link</h3>
          <a href="#" class="link-mono">View all installments →</a>
          <p class="style-code">.link-mono</p>
        </div>

        <!-- 2. Underline Link -->
        <div class="style-item">
          <h3 class="style-label">Underline Link</h3>
          <a href="#" class="link-underline">Read more about this project</a>
          <p class="style-code">.link-underline</p>
        </div>

        <!-- 3. Gold Fade Link -->
        <div class="style-item">
          <h3 class="style-label">Gold Fade Link</h3>
          <a href="#" class="link-gold-fade">Learn about this project</a>
          <p class="style-code">.link-gold-fade</p>
        </div>

        <!-- 4. Glow Link -->
        <div class="style-item">
          <h3 class="style-label">Glow Link</h3>
          <a href="#" class="link-glow">Hover to see the glow</a>
          <p class="style-code">.link-glow</p>
        </div>

        <!-- 5. Slide Link -->
        <div class="style-item">
          <h3 class="style-label">Slide Underline Link</h3>
          <a href="#" class="link-slide">Slide underline on hover</a>
          <p class="style-code">.link-slide</p>
        </div>

        <!-- 6. Double Underline Link -->
        <div class="style-item">
          <h3 class="style-label">Double Underline Link</h3>
          <a href="#" class="link-double">Double underline effect</a>
          <p class="style-code">.link-double</p>
        </div>

        <!-- 7. Arrow Link -->
        <div class="style-item">
          <h3 class="style-label">Arrow Link</h3>
          <a href="#" class="link-arrow">Continue reading</a>
          <p class="style-code">.link-arrow</p>
        </div>

        <!-- 8. Reverse Arrow Link -->
        <div class="style-item">
          <h3 class="style-label">Reverse Arrow Link</h3>
          <a href="#" class="link-arrow-reverse">Back to all seasons</a>
          <p class="style-code">.link-arrow-reverse</p>
        </div>

        <!-- 9. Scale Link -->
        <div class="style-item">
          <h3 class="style-label">Scale Link</h3>
          <a href="#" class="link-scale">Grow on hover</a>
          <p class="style-code">.link-scale</p>
        </div>

        <!-- 10. Color Shift Link -->
        <div class="style-item">
          <h3 class="style-label">Color Shift Link</h3>
          <a href="#" class="link-shift">Shift color on hover</a>
          <p class="style-code">.link-shift</p>
        </div>

        <!-- 11. Dot Link -->
        <div class="style-item">
          <h3 class="style-label">Dot Link</h3>
          <a href="#" class="link-dot">Dot appears below</a>
          <p class="style-code">.link-dot</p>
        </div>

        <!-- 12. Pulsing Link -->
        <div class="style-item">
          <h3 class="style-label">Pulsing Link</h3>
          <a href="#" class="link-pulse">Pulsing gold on hover</a>
          <p class="style-code">.link-pulse</p>
        </div>
      </div>

      <!-- ─── COMPARISON TABLE ─── -->
      <div class="style-item" style="margin-top: 2rem;">
        <h3 class="style-label">Quick Reference</h3>
        <div style="overflow-x: auto; font-size: 12px;">
          <table style="width: 100%; border-collapse: collapse; font-family: var(--mono); font-size: 10px; color: var(--muted);">
            <thead>
              <tr style="border-bottom: 2px solid var(--rule);">
                <th style="text-align: left; padding: 0.5rem 0.75rem;">Class</th>
                <th style="text-align: left; padding: 0.5rem 0.75rem;">Effect</th>
                <th style="text-align: left; padding: 0.5rem 0.75rem;">Best For</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-mono</code></td>
                <td style="padding: 0.4rem 0.75rem;">Mono + gold underline</td>
                <td style="padding: 0.4rem 0.75rem;">Navigation, CTAs</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-underline</code></td>
                <td style="padding: 0.4rem 0.75rem;">Simple underline</td>
                <td style="padding: 0.4rem 0.75rem;">Body text links</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-gold-fade</code></td>
                <td style="padding: 0.4rem 0.75rem;">Underline expands from left</td>
                <td style="padding: 0.4rem 0.75rem;">Subtle emphasis</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-glow</code></td>
                <td style="padding: 0.4rem 0.75rem;">Gold glow + underline</td>
                <td style="padding: 0.4rem 0.75rem;">Highlighting</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-slide</code></td>
                <td style="padding: 0.4rem 0.75rem;">Underline slides in</td>
                <td style="padding: 0.4rem 0.75rem;">Clean, modern</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-double</code></td>
                <td style="padding: 0.4rem 0.75rem;">Underline draws in</td>
                <td style="padding: 0.4rem 0.75rem;">Elegant</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-arrow</code></td>
                <td style="padding: 0.4rem 0.75rem;">Arrow appears on hover</td>
                <td style="padding: 0.4rem 0.75rem;">"Read more" links</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-arrow-reverse</code></td>
                <td style="padding: 0.4rem 0.75rem;">Arrow appears on left</td>
                <td style="padding: 0.4rem 0.75rem;">"Back" links</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-scale</code></td>
                <td style="padding: 0.4rem 0.75rem;">Slight scale + gold</td>
                <td style="padding: 0.4rem 0.75rem;">Buttons, prominent links</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-shift</code></td>
                <td style="padding: 0.4rem 0.75rem;">Color shifts</td>
                <td style="padding: 0.4rem 0.75rem;">Smooth transitions</td>
              </tr>
              <tr style="border-bottom: 1px solid var(--rule);">
                <td style="padding: 0.4rem 0.75rem;"><code>.link-dot</code></td>
                <td style="padding: 0.4rem 0.75rem;">Dot appears below</td>
                <td style="padding: 0.4rem 0.75rem;">Playful, creative</td>
              </tr>
              <tr>
                <td style="padding: 0.4rem 0.75rem;"><code>.link-pulse</code></td>
                <td style="padding: 0.4rem 0.75rem;">Pulsing gold</td>
                <td style="padding: 0.4rem 0.75rem;">Emphasis, active state</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    
    
    
    <!-- ─── UNIVERSAL LISTS ─── -->
    <section class="style-section" id="universal-lists">
      <h2 class="style-section-title">Universal Lists</h2>
      
      <div class="style-grid">
        <!-- Standard List -->
        <div class="style-item">
          <h3 class="style-label">Standard List</h3>
          <div class="list-container">
            <div class="list-item">
              <span class="list-item-left">01</span>
              <div class="list-item-content">
                <span class="list-item-title">List Item Title</span>
                <span class="list-item-meta">Meta information · Category</span>
              </div>
              <div class="list-item-right metrics-horizontal">
                <span class="metric metric-words">120 words</span>
                <span class="metric metric-sep">·</span>
                <span class="metric metric-time">~3 min</span>
              </div>
            </div>
            <div class="list-item">
              <span class="list-item-left">02</span>
              <div class="list-item-content">
                <span class="list-item-title">Another List Item</span>
                <span class="list-item-meta">More info · Another category</span>
              </div>
              <div class="list-item-right">
                <span class="badge badge-active">Active</span>
              </div>
            </div>
            <div class="list-item">
              <span class="list-item-left">03</span>
              <div class="list-item-content">
                <span class="list-item-title">Third Item</span>
                <span class="list-item-meta">With description</span>
              </div>
            </div>
          </div>
          <p class="style-code">.list-container .list-item .list-item-left .list-item-content .list-item-title .list-item-meta .list-item-right</p>
        </div>

        <!-- Compact List -->
        <div class="style-item">
          <h3 class="style-label">Compact List</h3>
          <div class="list-container">
            <a href="#" class="list-item list-item-compact">
              <div class="list-item-content">
                <span class="list-item-title">Compact Item</span>
                <span class="list-item-meta">With smaller padding</span>
              </div>
            </a>
            <a href="#" class="list-item list-item-compact">
              <div class="list-item-content">
                <span class="list-item-title">Another Compact Item</span>
                <span class="list-item-meta">Great for dense lists</span>
              </div>
            </a>
          </div>
          <p class="style-code">.list-item .list-item-compact</p>
        </div>

        <!-- Grid List -->
        <div class="style-item">
          <h3 class="style-label">Grid List</h3>
          <div class="list-grid">
            <a href="#" class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Project Alpha</span>
                <span class="list-item-meta">3 contributors</span>
              </div>
            </a>
            <a href="#" class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Project Beta</span>
                <span class="list-item-meta">5 contributors</span>
              </div>
            </a>
            <a href="#" class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Project Gamma</span>
                <span class="list-item-meta">2 contributors</span>
              </div>
            </a>
            <a href="#" class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Project Delta</span>
                <span class="list-item-meta">4 contributors</span>
              </div>
            </a>
          </div>
          <p class="style-code">.list-grid .list-item</p>
        </div>

        <!-- Bordered List -->
        <div class="style-item">
          <h3 class="style-label">Bordered List</h3>
          <div class="list-container">
            <div class="list-item list-item-bordered">
              <div class="list-item-content">
                <span class="list-item-title">Bordered Item</span>
                <span class="list-item-meta">With visible border</span>
              </div>
            </div>
            <div class="list-item list-item-bordered">
              <div class="list-item-content">
                <span class="list-item-title">Another Bordered Item</span>
                <span class="list-item-meta">Hover to see effect</span>
              </div>
            </div>
          </div>
          <p class="style-code">.list-item .list-item-bordered</p>
        </div>

        <!-- With Badges -->
        <div class="style-item">
          <h3 class="style-label">With Badges</h3>
          <div class="list-container">
            <div class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Item with Badge</span>
                <span class="list-item-meta">Status indicator</span>
              </div>
              <div class="list-item-right">
                <span class="badge badge-new">New</span>
              </div>
            </div>
            <div class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Another Item</span>
                <span class="list-item-meta">With different status</span>
              </div>
              <div class="list-item-right">
                <span class="badge badge-active">Active</span>
              </div>
            </div>
          </div>
          <p class="style-code">.list-item .list-item-right .badge</p>
        </div>
      </div>
    </section>

  </div>
</div>

<style>
/* ─── STYLE GUIDE SPECIFIC STYLES ─── */
/* These only exist for the style guide layout, 
   NOT for components (components use main.css) */

.style-toc {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 1.5rem;
  padding: 1rem 1.5rem;
  border: 1px solid var(--rule);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.02);
  margin: 1.5rem var(--gutter) 0;
}

.style-toc-label {
  font-family: var(--mono);
  font-size: 7px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ash);
  margin-right: 0.5rem;
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

.style-guide-body {
  padding: 2rem var(--gutter) 4rem;
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

.style-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.style-grid-badges {
  grid-template-columns: 1fr;
}

.style-item {
  padding: 1.25rem;
  border: 1px solid var(--rule);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.02);
}

.style-label {
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ash);
  margin-bottom: 0.75rem;
}

.style-code {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--mid);
  margin-top: 0.75rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--rule);
  opacity: 0.7;
}

.style-badge-row {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
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
  gap: 0.3rem;
  min-height: 80px;
}

.color-name {
  font-weight: 700;
}

.color-hex {
  opacity: 0.6;
  font-size: 8px;
}

/* ─── INTERACTIVE DEMOS ─── */

.interactive-demo {
  transition: all 0.2s ease;
}

.demo-btn {
  font-family: var(--mono);
  font-size: 8px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.5rem 1.25rem;
  border-radius: 2px;
  border: 1px solid;
  cursor: pointer;
  transition: all 0.25s ease;
}

.demo-btn.primary {
  background: var(--gold);
  color: var(--void);
  border-color: var(--gold);
}

.demo-btn.primary:hover {
  background: transparent;
  color: var(--gold);
}

.demo-btn.secondary {
  background: var(--void2);
  color: var(--muted);
  border-color: var(--rule);
}

.demo-btn.secondary:hover {
  border-color: var(--gold-dim);
  color: var(--cream);
}

.demo-btn.outline {
  background: transparent;
  color: var(--muted);
  border-color: var(--rule);
}

.demo-btn.outline:hover {
  border-color: var(--gold);
  color: var(--gold);
}

.demo-link {
  transition: all 0.25s ease !important;
}

.demo-tag {
  transition: all 0.25s ease !important;
  cursor: pointer;
}

.demo-tag:hover {
  border-color: var(--gold-dim) !important;
  background: rgba(255, 215, 0, 0.03) !important;
}

.demo-details {
  border: 1px solid var(--rule);
  border-radius: 4px;
  background: var(--void2);
}

.demo-details summary {
  cursor: pointer;
  list-style: none;
  padding: 0.75rem 1rem;
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  transition: color 0.2s ease;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.demo-details summary:hover {
  color: var(--cream);
}

.demo-details summary::-webkit-details-marker {
  display: none;
}

.demo-details summary::after {
  content: '+';
  font-size: 14px;
  color: var(--ash);
  transition: transform 0.2s ease;
}

.demo-details[open] summary::after {
  content: '−';
}

.demo-details[open] summary {
  border-bottom: 1px solid var(--rule);
}

.demo-details > div {
  padding: 0 1rem 1rem 1rem;
}

.demo-tooltip {
  position: relative;
  display: inline-block;
  font-family: var(--mono);
  font-size: 9px;
  letter-spacing: 0.08em;
  color: var(--gold);
  border-bottom: 1px dashed var(--gold-dim);
  cursor: help;
  padding: 0.25rem 0.5rem;
}

.demo-tooltip::before {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-8px);
  background: var(--void2);
  color: var(--cream);
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  border: 1px solid var(--rule);
  font-family: var(--text);
  font-size: 11px;
  font-style: italic;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s ease;
}

.demo-tooltip::after {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-2px);
  border: 6px solid transparent;
  border-top-color: var(--rule);
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s ease;
}

.demo-tooltip:hover::before,
.demo-tooltip:hover::after {
  opacity: 1;
  transform: translateX(-50%) translateY(-4px);
}

/* ─── RESPONSIVE ─── */

@media (max-width: 768px) {
  .style-toc {
    padding: 0.75rem 1rem;
    gap: 0.3rem 1rem;
    margin: 1rem 1rem 0;
  }
  
  .style-toc a {
    font-size: 7px;
  }
  
  .style-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .style-guide-body {
    padding: 1rem 1rem 3rem;
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
  
  .demo-tooltip::before {
    white-space: normal;
    max-width: 200px;
  }
}
</style>