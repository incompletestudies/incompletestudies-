---
layout: default
title: Second Form Editions
permalink: /editions/
---
{% assign trace_project = site.projects | where: "slug", "trace-and-legibility" | first %}
<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Second Form Editions</span>
    <span class="col-head-meta">The moment thought becomes object</span>
  </div>
  <div class="editions-body">
    <div class="editions-lead">
      Some projects reach a point where the installment format is no longer adequate — where the work has accumulated enough to require a different kind of form. <em>Second Form Editions</em> is the publishing arm through which these projects become books.
    </div>

    <div class="editions-grid">
      <div class="edition-card">
        <div class="edition-card-num">001</div>
        <div class="edition-card-id">SFE–001 · 2025</div>
        <div class="edition-card-title">On the mark that remains</div>
        <div class="edition-card-author">E. Marchetti</div>
        <div class="edition-card-desc">Developed from P–01, Season 00. The book includes the original seven installments, their editorial correspondence, and three new essays written in reflection. Strikethroughs retained.</div>
        <a class="edition-card-link" href="{{ site.baseurl }}/projects/{{ trace_project.slug }}/">← View original installments</a>
      </div>
      <div class="edition-card">
        <div class="edition-card-num">002</div>
        <div class="edition-card-id">SFE–002 · Forthcoming 2026</div>
        <div class="edition-card-title">The pause and its weight</div>
        <div class="edition-card-author">A. Sørensen</div>
        <div class="edition-card-desc">In development from P–02, Season 01. Expected completion: Summer 2026. A book about musical silence that is itself structured by intervals of writing and not-writing.</div>
        <a class="edition-card-link" href="{{ site.baseurl }}/installments/">← Follow the current project</a>
      </div>
      <div class="edition-card ghost">
        <div class="edition-card-num">003</div>
        <div class="edition-card-id">SFE–003 · Open</div>
        <div class="edition-card-title">—</div>
        <div class="edition-card-author">Next season</div>
        <div class="edition-card-desc">The third edition is not yet determined. It will emerge from the current season's cohort, if and when a project reaches the condition for it.</div>
        <a class="edition-card-link" href="{{ site.baseurl }}/contributors/">Apply for Season 02 →</a>
      </div>
    </div>

    <div class="annotation">
      <div class="annotation-label">On the relationship between archive and edition</div>
      <div class="annotation-text">The archive does not disappear when a book is made from it. Both remain — the edition and the installments from which it came. The edition is not the final word. It is a different form of the same thought, produced at a particular moment in its development.</div>
    </div>
  </div>
</div>
