---
layout: default
title: Projects
permalink: /projects/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Projects</span>
    <span class="col-head-meta">Season 01 · {{ site.projects | size }} active · 2024 → Spring 2026</span>
  </div>
  <div class="projects-layout">
    
    {% include project-sidebar.html %}
    
    <div class="proj-main">
      {% include project-list.html %}
      {% include project-detail.html %}
    </div>
    
  </div>
</div>