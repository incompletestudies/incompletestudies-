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
    <a href="#content">Content</a>
    <a href="#colors">Colors</a>
    <a href="#badges">Badges</a>
    <a href="#cards">Cards</a>
    <a href="#tags">Tags</a>
    <a href="#links">Links</a>
    <a href="#buttons">Buttons</a>
    <a href="#breadcrumb">Breadcrumb</a>
    <a href="#headers">Headers</a>
    <a href="#grids">Grids</a>
    <a href="#lists">Lists</a>
    <a href="#spacing">Spacing</a>
    <a href="#interactive">Interactive</a>
  </div>

  <div class="style-guide-body">
    
    <!-- ═══════════════════════════════════════════════ -->
    <!-- TYPOGRAPHY                                     -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="typography">
      <h2 class="style-section-title">Typography</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Display Font</span>
          <div class="style-demo" style="font-family: var(--display); font-size: 32px; font-style: italic; font-weight: 700; color: var(--cream);">
            The Journal of Incomplete Studies
          </div>
          <div class="style-code">font-family: var(--display) · Used for titles, headings, pull quotes</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Text Font</span>
          <div class="style-demo" style="font-family: var(--text); font-size: 16px; color: var(--pale);">
            A serial research publication for ideas still in motion.
          </div>
          <div class="style-code">font-family: var(--text) · Used for body copy, paragraphs</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Mono Font</span>
          <div class="style-demo" style="font-family: var(--mono); font-size: 14px; color: var(--muted);">
            Installment 03 · January 2026
          </div>
          <div class="style-code">font-family: var(--mono) · Used for metadata, code, labels</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Script Font</span>
          <div class="style-demo" style="font-family: var(--script); font-size: 24px; color: var(--gold);">
            Notes in the margin
          </div>
          <div class="style-code">font-family: var(--script) · Used for annotations, marginalia</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- CONTENT STYLES                                 -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="content">
      <h2 class="style-section-title">Content Styles</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Paragraphs</span>
          <div class="style-demo content">
            <p>This is a standard paragraph inside <code>.content</code>. It uses <code>var(--muted)</code> for text color and has a max-width of 720px.</p>
            <p>Paragraphs have a bottom margin of 1.5rem for proper spacing between blocks of text.</p>
          </div>
          <div class="style-code">.content p · max-width: 720px · line-height: 1.9</div>
        </div>

        <div class="style-item">
          <span class="style-label">Headings</span>
          <div class="style-demo content">
            <h1>Heading 1</h1>
            <h2>Heading 2</h2>
            <h3>Heading 3</h3>
            <h4>Heading 4</h4>
            <h5>Heading 5</h5>
            <h6>Heading 6</h6>
          </div>
          <div class="style-code">.content h1–h6 · Font sizes decrease from 2.5rem to 0.875rem</div>
        </div>

        <div class="style-item">
          <span class="style-label">Inline Elements</span>
          <div class="style-demo content">
            <p>This paragraph has <strong>strong text</strong>, <em>emphasized text</em>, and <code>inline code</code>.</p>
            <p>It also has <a href="#">a link</a> with gold underline.</p>
          </div>
          <div class="style-code">strong · em · code · a</div>
        </div>

        <div class="style-item">
          <span class="style-label">Blockquotes</span>
          <div class="style-demo content">
            <blockquote>
              The Unfinished Archive is for writers who are <em>mid-thought</em> — working at the edge of a question that is not yet ready to be resolved.
            </blockquote>
          </div>
          <div class="style-code">.content blockquote · Gold left border · Italic</div>
        </div>

        <div class="style-item">
          <span class="style-label">Unordered Lists</span>
          <div class="style-demo content">
            <ul>
              <li>Unordered list item one</li>
              <li>Unordered list item two</li>
              <li>Unordered list item three</li>
            </ul>
          </div>
          <div class="style-code">.content ul · Disc bullets · 1.2rem padding-left</div>
        </div>

        <div class="style-item">
          <span class="style-label">Ordered Lists</span>
          <div class="style-demo content">
            <ol>
              <li>Ordered list item one</li>
              <li>Ordered list item two</li>
              <li>Ordered list item three</li>
            </ol>
          </div>
          <div class="style-code">.content ol · Decimal numbering · 1.2rem padding-left</div>
        </div>

        <div class="style-item">
          <span class="style-label">Nested Lists</span>
          <div class="style-demo content">
            <ul>
              <li>Parent item one
                <ul>
                  <li>Child item one</li>
                  <li>Child item two</li>
                </ul>
              </li>
              <li>Parent item two
                <ol>
                  <li>Ordered child one</li>
                  <li>Ordered child two</li>
                </ol>
              </li>
            </ul>
          </div>
          <div class="style-code">.content ul ul · .content ul ol · Nested indentation</div>
        </div>

        <div class="style-item">
          <span class="style-label">Code Blocks</span>
          <div class="style-demo content">
            <pre><code>
    function hello() {
      console.log("Hello, world!");
    }
            </code></pre>
          </div>
          <div class="style-code">.content pre · .content code · Mono font · Dark background</div>
        </div>

        <div class="style-item">
          <span class="style-label">Tables</span>
          <div class="style-demo content">
            <table>
              <thead>
                <tr><th>Header 1</th><th>Header 2</th><th>Header 3</th></tr>
              </thead>
              <tbody>
                <tr><td>Row 1, Cell 1</td><td>Row 1, Cell 2</td><td>Row 1, Cell 3</td></tr>
                <tr><td>Row 2, Cell 1</td><td>Row 2, Cell 2</td><td>Row 2, Cell 3</td></tr>
              </tbody>
            </table>
          </div>
          <div class="style-code">.content table · Full width · Border-collapse: collapse</div>
        </div>

        <div class="style-item">
          <span class="style-label">Horizontal Rule</span>
          <div class="style-demo content">
            <p>Text above the horizontal rule.</p>
            <hr>
            <p>Text below the horizontal rule.</p>
          </div>
          <div class="style-code">.content hr · var(--rule) · 1px · 2rem margin</div>
        </div>

        <div class="style-item">
          <span class="style-label">Images</span>
          <div class="style-demo content">
            <div class="style-image-placeholder">
              <span>Image placeholder</span>
              <span class="style-image-caption">Images are responsive with rounded corners</span>
            </div>
          </div>
          <div class="style-code">.content img · max-width: 100% · border-radius: 4px</div>
        </div>

        <div class="style-item">
          <span class="style-label">Footnotes</span>
          <div class="style-demo content">
            <p>Text with a footnote.<sup><a href="#fn1" id="fnref1">1</a></sup></p>
            <div class="content footnotes">
              <ol>
                <li id="fn1">This is the footnote text. <a href="#fnref1" class="reversefootnote">↩</a></li>
              </ol>
            </div>
          </div>
          <div class="style-code">.content .footnotes · Small text · Separator border</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- COLORS                                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="colors">
      <h2 class="style-section-title">Colors</h2>
      
      <div class="style-grid style-grid-colors">
        <div class="color-swatch" style="background: var(--void); color: var(--cream);">
          <span class="color-name">--void</span>
          <span class="color-hex">#0c0b09</span>
          <span class="color-usage">Background</span>
        </div>
        <div class="color-swatch" style="background: var(--void2); color: var(--cream);">
          <span class="color-name">--void2</span>
          <span class="color-hex">#1a1714</span>
          <span class="color-usage">Cards, secondary bg</span>
        </div>
        <div class="color-swatch" style="background: var(--void3); color: var(--cream);">
          <span class="color-name">--void3</span>
          <span class="color-hex">#28231e</span>
          <span class="color-usage">Tertiary bg</span>
        </div>
        <div class="color-swatch" style="background: var(--cream); color: var(--void);">
          <span class="color-name">--cream</span>
          <span class="color-hex">#e8dfd0</span>
          <span class="color-usage">Primary text</span>
        </div>
        <div class="color-swatch" style="background: var(--pale); color: var(--void);">
          <span class="color-name">--pale</span>
          <span class="color-hex">#c8bfae</span>
          <span class="color-usage">Secondary text</span>
        </div>
        <div class="color-swatch" style="background: var(--muted); color: var(--void);">
          <span class="color-name">--muted</span>
          <span class="color-hex">#9e9282</span>
          <span class="color-usage">Tertiary text</span>
        </div>
        <div class="color-swatch" style="background: var(--mid); color: var(--cream);">
          <span class="color-name">--mid</span>
          <span class="color-hex">#7a6e60</span>
          <span class="color-usage">Border, subtle elements</span>
        </div>
        <div class="color-swatch" style="background: var(--ash); color: var(--cream);">
          <span class="color-name">--ash</span>
          <span class="color-hex">#5a4f44</span>
          <span class="color-usage">Accents, subtle text</span>
        </div>
        <div class="color-swatch" style="background: var(--gold); color: var(--void);">
          <span class="color-name">--gold</span>
          <span class="color-hex">#d4b87a</span>
          <span class="color-usage">Primary accent, links</span>
        </div>
        <div class="color-swatch" style="background: var(--gold-dim); color: var(--cream);">
          <span class="color-name">--gold-dim</span>
          <span class="color-hex">#a68b5c</span>
          <span class="color-usage">Subtle accent, hover</span>
        </div>
        <div class="color-swatch" style="background: var(--sage); color: var(--void);">
          <span class="color-name">--sage</span>
          <span class="color-hex">#8aaa7a</span>
          <span class="color-usage">Success, positive states</span>
        </div>
        <div class="color-swatch" style="background: var(--rust); color: var(--cream);">
          <span class="color-name">--rust</span>
          <span class="color-hex">#c06a4a</span>
          <span class="color-usage">Warning, negative states</span>
        </div>
        <div class="color-swatch" style="background: var(--void); color: var(--gold); border-color: var(--gold-dim);">
          <span class="color-name">--gold-dim</span>
          <span class="color-hex">#a68b5c</span>
          <span class="color-usage">Border, subtle accent</span>
        </div>
        <div class="color-swatch" style="background: var(--rule); color: var(--void);">
          <span class="color-name">--rule</span>
          <span class="color-hex">#2a2621</span>
          <span class="color-usage">Dividers, borders</span>
        </div>
        <div class="color-swatch" style="background: var(--rule-mid); color: var(--void);">
          <span class="color-name">--rule-mid</span>
          <span class="color-hex">#3d362e</span>
          <span class="color-usage">Prominent dividers</span>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- BADGES                                         -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="badges">
      <h2 class="style-section-title">Badges</h2>
      
      <div class="style-grid style-grid-badges">
        <div class="style-item">
          <span class="style-label">Project Status</span>
          <div class="style-badge-row">
            <span class="badge ongoing">Ongoing</span>
            <span class="badge on-hold">On Hold</span>
            <span class="badge archived">Archived</span>
          </div>
          <div class="style-code">.badge.ongoing · .badge.on-hold · .badge.archived</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Installment Status</span>
          <div class="style-badge-row">
            <span class="badge first">First Inst.</span>
            <span class="badge revised">Revised</span>
            <span class="badge last">Last Inst.</span>
          </div>
          <div class="style-code">.badge.first · .badge.revised · .badge.last</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Cohort Status</span>
          <div class="style-badge-row">
            <span class="badge active">Active</span>
            <span class="badge on-leave">On Leave</span>
            <span class="badge alumni">Alumni</span>
          </div>
          <div class="style-code">.badge.active · .badge.on-leave · .badge.alumni</div>
        </div>

        <div class="style-item">
          <span class="style-label">Pills</span>
          <div class="style-badge-row">
            <span class="pill live">● Live</span>
            <span class="pill new">✦ New</span>
            <span class="pill upcoming">Upcoming</span>
            <span class="pill draft">Draft</span>
          </div>
          <div class="style-code">.pill.live · .pill.new · .pill.upcoming · .pill.draft</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- CARDS                                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="cards">
      <h2 class="style-section-title">Cards</h2>
      
      <div class="style-grid" style="grid-template-columns: 1fr 1fr;">
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
      <div class="style-code" style="margin-top: 0.5rem;">.card · .card-header · .card-title · .card-subtitle · .card-excerpt · .card-meta</div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- TAGS                                           -->
    <!-- ═══════════════════════════════════════════════ -->
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
        <div class="style-code">.tag · .tag-more</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- LINKS                                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="links">
      <h2 class="style-section-title">Links</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Standard Link</span>
          <a href="#" class="link-underline">Read more about this project →</a>
          <div class="style-code">.link-underline</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Mono Link</span>
          <a href="#" class="link-mono">View all installments →</a>
          <div class="style-code">.link-mono</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Back Link</span>
          <a href="#" class="back-link">← Back to all seasons</a>
          <div class="style-code">.back-link</div>
        </div>

        <div class="style-item">
          <span class="style-label">Gold Fade Link</span>
          <a href="#" class="link-gold-fade">Learn about this project</a>
          <div class="style-code">.link-gold-fade</div>
        </div>

        <div class="style-item">
          <span class="style-label">Glow Link</span>
          <a href="#" class="link-glow">Hover to see the glow</a>
          <div class="style-code">.link-glow</div>
        </div>

        <div class="style-item">
          <span class="style-label">Arrow Link</span>
          <a href="#" class="link-arrow">Continue reading</a>
          <div class="style-code">.link-arrow</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- BUTTONS                                        -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="buttons">
      <h2 class="style-section-title">Buttons</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Primary</span>
          <div class="style-button-row">
            <button class="btn btn-primary">Primary</button>
            <button class="btn btn-primary btn-sm">Small</button>
            <button class="btn btn-primary btn-lg">Large</button>
          </div>
          <div class="style-code">.btn .btn-primary · .btn-sm · .btn-lg</div>
        </div>

        <div class="style-item">
          <span class="style-label">Secondary</span>
          <div class="style-button-row">
            <button class="btn btn-secondary">Secondary</button>
            <button class="btn btn-secondary btn-sm">Small</button>
            <button class="btn btn-secondary btn-lg">Large</button>
          </div>
          <div class="style-code">.btn .btn-secondary</div>
        </div>

        <div class="style-item">
          <span class="style-label">Outline</span>
          <div class="style-button-row">
            <button class="btn btn-outline">Outline</button>
            <button class="btn btn-outline btn-sm">Small</button>
            <button class="btn btn-outline btn-lg">Large</button>
          </div>
          <div class="style-code">.btn .btn-outline</div>
        </div>

        <div class="style-item">
          <span class="style-label">Ghost</span>
          <div class="style-button-row">
            <button class="btn btn-ghost">Ghost</button>
            <button class="btn btn-ghost btn-sm">Small</button>
            <button class="btn btn-ghost btn-lg">Large</button>
          </div>
          <div class="style-code">.btn .btn-ghost</div>
        </div>

        <div class="style-item">
          <span class="style-label">Block (Full Width)</span>
          <button class="btn btn-primary btn-block">Full Width Button</button>
          <div class="style-code">.btn .btn-primary .btn-block</div>
        </div>

        <div class="style-item">
          <span class="style-label">Icon Buttons</span>
          <div class="style-button-row">
            <button class="btn btn-primary btn-icon">✕</button>
            <button class="btn btn-secondary btn-icon">✕</button>
            <button class="btn btn-outline btn-icon">✕</button>
          </div>
          <div class="style-code">.btn .btn-icon</div>
        </div>

        <div class="style-item">
          <span class="style-label">Link as Button</span>
          <div class="style-button-row">
            <button class="btn-link">← Back</button>
            <button class="btn-link">View All →</button>
            <button class="btn-link">Apply now</button>
          </div>
          <div class="style-code">.btn-link</div>
        </div>

        <div class="style-item">
          <span class="style-label">Disabled States</span>
          <div class="style-button-row">
            <button class="btn btn-primary" disabled>Primary</button>
            <button class="btn btn-secondary" disabled>Secondary</button>
            <button class="btn btn-outline" disabled>Outline</button>
          </div>
          <div class="style-code">Add <code>disabled</code> attribute</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- BREADCRUMB                                     -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="breadcrumb">
      <h2 class="style-section-title">Breadcrumb</h2>
      
      <div class="style-item">
        <div class="breadcrumb" style="padding: 1rem 0;">
          <a href="#">Home</a>
          <span class="crumb-sep">/</span>
          <a href="#">Projects</a>
          <span class="crumb-sep">/</span>
          <span class="crumb-current">Digital Archives Initiative</span>
        </div>
        <div class="style-code">.breadcrumb · .crumb-current · .crumb-sep</div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- HEADERS                                        -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="headers">
      <h2 class="style-section-title">Section Headers</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Section Header</span>
          <div class="section-header">
            <h3 class="section-title">Current Projects</h3>
            <span class="section-meta">4 active</span>
          </div>
          <div class="style-code">.section-header · .section-title · .section-meta</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Column Header</span>
          <div class="col-head" style="padding: 0.5rem 0;">
            <span class="col-head-title">Installments</span>
            <span class="col-head-meta">24 total · Season 01</span>
          </div>
          <div class="style-code">.col-head · .col-head-title · .col-head-meta</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- GRIDS                                          -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="grids">
      <h2 class="style-section-title">Grids</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">2-Column Grid</span>
          <div class="grid-2" style="border: 1px solid var(--rule); padding: 1rem;">
            <div class="grid-demo-item">Item 1</div>
            <div class="grid-demo-item">Item 2</div>
          </div>
          <div class="style-code">.grid-2 · gap: 2rem</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">3-Column Grid</span>
          <div class="grid-3" style="border: 1px solid var(--rule); padding: 1rem;">
            <div class="grid-demo-item">Item 1</div>
            <div class="grid-demo-item">Item 2</div>
            <div class="grid-demo-item">Item 3</div>
          </div>
          <div class="style-code">.grid-3 · gap: 2rem</div>
        </div>

        <div class="style-item">
          <span class="style-label">4-Column Grid</span>
          <div class="grid-4" style="border: 1px solid var(--rule); padding: 1rem;">
            <div class="grid-demo-item">Item 1</div>
            <div class="grid-demo-item">Item 2</div>
            <div class="grid-demo-item">Item 3</div>
            <div class="grid-demo-item">Item 4</div>
          </div>
          <div class="style-code">.grid-4 · gap: 2rem</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- UNIVERSAL LISTS                                -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="lists">
      <h2 class="style-section-title">Universal Lists</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Standard List</span>
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
                <span class="badge active">Active</span>
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
          <div class="style-code">.list-container · .list-item · .list-item-left · .list-item-content · .list-item-title · .list-item-meta · .list-item-right</div>
        </div>

        <div class="style-item">
          <span class="style-label">Compact List</span>
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
          <div class="style-code">.list-item .list-item-compact</div>
        </div>

        <div class="style-item">
          <span class="style-label">Grid List</span>
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
          <div class="style-code">.list-grid · .list-item</div>
        </div>

        <div class="style-item">
          <span class="style-label">Bordered List</span>
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
          <div class="style-code">.list-item .list-item-bordered</div>
        </div>

        <div class="style-item">
          <span class="style-label">With Badges</span>
          <div class="list-container">
            <div class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Item with Badge</span>
                <span class="list-item-meta">Status indicator</span>
              </div>
              <div class="list-item-right">
                <span class="badge new">New</span>
              </div>
            </div>
            <div class="list-item">
              <div class="list-item-content">
                <span class="list-item-title">Another Item</span>
                <span class="list-item-meta">With different status</span>
              </div>
              <div class="list-item-right">
                <span class="badge active">Active</span>
              </div>
            </div>
          </div>
          <div class="style-code">.list-item .list-item-right .badge</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- SPACING                                        -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="spacing">
      <h2 class="style-section-title">Spacing Utilities</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Margin</span>
          <div class="style-spacing-demo">
            <div class="spacing-row">
              <span class="spacing-label">.mt-sm</span>
              <div class="mt-sm spacing-block"><span>0.25rem</span></div>
            </div>
            <div class="spacing-row">
              <span class="spacing-label">.mt-md</span>
              <div class="mt-md spacing-block"><span>1rem</span></div>
            </div>
            <div class="spacing-row">
              <span class="spacing-label">.mt-lg</span>
              <div class="mt-lg spacing-block"><span>1.5rem</span></div>
            </div>
            <div class="spacing-row">
              <span class="spacing-label">.mt-xl</span>
              <div class="mt-xl spacing-block"><span>2.5rem</span></div>
            </div>
          </div>
          <div class="style-code">.mt-{sm|md|lg|xl} · Margin top</div>
        </div>
        
        <div class="style-item">
          <span class="style-label">Padding</span>
          <div class="style-spacing-demo">
            <div class="spacing-row">
              <span class="spacing-label">.p-sm</span>
              <div class="p-sm spacing-block"><span>0.25rem</span></div>
            </div>
            <div class="spacing-row">
              <span class="spacing-label">.p-md</span>
              <div class="p-md spacing-block"><span>1rem</span></div>
            </div>
            <div class="spacing-row">
              <span class="spacing-label">.p-lg</span>
              <div class="p-lg spacing-block"><span>1.5rem</span></div>
            </div>
            <div class="spacing-row">
              <span class="spacing-label">.p-xl</span>
              <div class="p-xl spacing-block"><span>2.5rem</span></div>
            </div>
          </div>
          <div class="style-code">.p-{sm|md|lg|xl} · Padding all sides</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════════════════════════════ -->
    <!-- INTERACTIVE                                    -->
    <!-- ═══════════════════════════════════════════════ -->
    <section class="style-section" id="interactive">
      <h2 class="style-section-title">Interactive Components</h2>
      
      <div class="style-grid">
        <div class="style-item">
          <span class="style-label">Card Hover</span>
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
          <div class="style-code">.card:hover → border-color: var(--gold-dim) · transform: translateY(-3px)</div>
        </div>

        <div class="style-item">
          <span class="style-label">Tag Hover</span>
          <div class="style-button-row">
            <span class="tag demo-tag">Archives</span>
            <span class="tag demo-tag">Digital Humanities</span>
            <span class="tag demo-tag">Memory Studies</span>
          </div>
          <div class="style-code">.tag:hover → border-color: var(--gold-dim)</div>
        </div>

        <div class="style-item">
          <span class="style-label">Accordion</span>
          <details class="demo-details">
            <summary>Click to expand</summary>
            <div>
              <p>This is expandable content. Click the summary again to collapse.</p>
              <ul style="list-style: none; padding: 0.5rem 0;">
                <li>• Interactive demo</li>
                <li>• Shows toggle behavior</li>
                <li>• Works with details/summary</li>
              </ul>
            </div>
          </details>
          <div class="style-code">details[open] → shows content · summary::after → + / −</div>
        </div>

        <div class="style-item">
          <span class="style-label">Tooltip</span>
          <div style="padding: 1rem 0;">
            <span class="demo-tooltip" data-tooltip="This is a tooltip!">Hover over me</span>
          </div>
          <div class="style-code">::before + ::after on hover → shows tooltip</div>
        </div>

        <div class="style-item">
          <span class="style-label">Link Hover States</span>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <a href="#" class="link-underline demo-link">Standard link →</a>
            <a href="#" class="link-mono demo-link">Mono link →</a>
            <a href="#" class="link-glow demo-link">Glow link →</a>
          </div>
          <div class="style-code">Various link hover effects</div>
        </div>

        <div class="style-item">
          <span class="style-label">Button Hover States</span>
          <div class="style-button-row">
            <button class="demo-btn primary">Primary</button>
            <button class="demo-btn secondary">Secondary</button>
            <button class="demo-btn outline">Outline</button>
          </div>
          <div class="style-code">.demo-btn:hover → background/color transition</div>
        </div>
      </div>
    </section>

  </div>
</div>

<style>
/* ============================================
   STYLE GUIDE — IMPROVED USABILITY
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

.style-grid-badges {
  grid-template-columns: 1fr;
}

.style-grid-colors {
  grid-template-columns: repeat(4, 1fr);
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
  transform: scale(1.02);
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

/* ─── BADGE ROWS ─── */
.style-badge-row {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
}

/* ─── BUTTON ROWS ─── */
.style-button-row {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  align-items: center;
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

/* ─── ACCORDION ─── */
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

/* ─── TOOLTIP ─── */
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

/* ─── SPACING DEMO ─── */
.style-spacing-demo {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.spacing-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.spacing-label {
  font-family: var(--mono);
  font-size: 8px;
  color: var(--muted);
  min-width: 3rem;
}

.spacing-block {
  background: rgba(212, 184, 122, 0.12);
  border: 1px dashed var(--gold-dim);
  padding: 0.1rem 0.5rem;
  border-radius: 2px;
  flex: 1;
}

.spacing-block span {
  font-family: var(--mono);
  font-size: 7px;
  color: var(--gold);
}

/* ─── GRID DEMO ITEMS ─── */
.grid-demo-item {
  background: var(--void2);
  padding: 1rem;
  border-radius: 4px;
  text-align: center;
  font-family: var(--mono);
  font-size: 12px;
  color: var(--muted);
  border: 1px solid var(--rule);
}

/* ─── IMAGE PLACEHOLDER ─── */
.style-image-placeholder {
  background: var(--void2);
  padding: 2rem;
  text-align: center;
  color: var(--muted);
  border-radius: 4px;
  border: 1px dashed var(--rule);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.style-image-caption {
  font-size: 12px;
  color: var(--ash);
}

/* ─── RESPONSIVE ─── */
@media (max-width: 1024px) {
  .style-grid-colors {
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
  
  .style-grid-colors {
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
  
  .style-grid-colors {
    grid-template-columns: 1fr 1fr;
  }
  
  .style-section-title {
    font-size: 20px;
  }
  
  .demo-tooltip::before {
    white-space: normal;
    max-width: 200px;
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