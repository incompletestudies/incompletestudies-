---
layout: default
title: Projects
permalink: /projects/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Projects</span>
    <span class="col-head-meta">Season 01 · Summer 2026 · {{ site.projects | size }} active</span>
  </div>
  
  <div class="projects-layout">
    {% include project-sidebar.html %}
    <div class="proj-main">
      {% include project-list.html %}
      {% include project-detail.html %}
    </div>
  </div>
</div>

<script>
  // ─── Build PROJECTS array from Jekyll data ───
  const PROJECTS = [
    {% assign sorted_projects = site.projects | sort: "order" %}
    {% for project in sorted_projects %}
      {% assign author_names = "" | split: "" %}
      {% if project.people %}
        {% for slug in project.people %}
          {% assign person = site.people | where: "slug", slug | first %}
          {% if person %}
            {% assign name = person.title %}
            {% if person.role %}
              {% assign name = name | append: " · " | append: person.role %}
            {% endif %}
            {% if person.discipline %}
              {% assign name = name | append: ", " | append: person.discipline  %}
            {% endif %}
            {% assign author_names = author_names | push: name %}
          {% else %}
            {% assign author_names = author_names | push: slug %}
          {% endif %}
        {% endfor %}
      {% endif %}
      {% assign author_string = author_names | join: " + " %}
      {
        id: "{{ project.id | default: 'P' }}{{ forloop.index }}",
        title: {{ project.title | jsonify }},
        author: "{{ author_string }}",
        status: "{{ project.status | default: 'Active' }}",
        abstract: {{ project.abstract | default: "No abstract yet." | jsonify }},
        installments: {{ project.installments | default: 0 }},
        total: {{ project.total_installments | default: 5 }},
        last_updated: "{{ project.last_updated | default: 'Upcoming' }}",
        season: "{{ project.season | default: 'Season 01' }}",
        slug: "{{ project.slug }}"
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  // ─── Show project detail ───
  function showProjectDetailBySlug(slug) {
    const p = PROJECTS.find(proj => proj.slug === slug);
    if (!p) {
      console.error("Project not found:", slug);
      return;
    }

    // Update sidebar active state
    document.querySelectorAll('.proj-sidebar-item').forEach(el => {
      el.classList.toggle('active', el.dataset.slug === slug);
    });

    // Build detail content
    const content = `
      <div class="col-head" style="padding:0 0 1.5rem">
        <span class="col-head-title" style="font-size:clamp(20px,3vw,36px)">${p.title}</span>
        <span class="col-head-meta">${p.id} · ${p.last_updated}</span>
      </div>
      <div style="font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:0.04em;margin-bottom:2rem">
        ${p.author}
      </div>
      <div style="font-family:var(--text);font-size:13px;font-style:italic;color:var(--pale);line-height:1.8;margin-bottom:2rem">
        ${p.abstract}
      </div>
      <div style="display:flex;gap:2rem;flex-wrap:wrap;font-family:var(--mono);font-size:9px;color:var(--mid);letter-spacing:0.04em;">
        <div><strong style="color:var(--muted);">Status:</strong> ${p.status}</div>
        <div><strong style="color:var(--muted);">Progress:</strong> ${p.installments} of ${p.total} installments</div>
        <div><strong style="color:var(--muted);">Season:</strong> ${p.season}</div>
      </div>
      <div class="prog-dots" style="margin-top:1.5rem;justify-content:flex-start;">
        ${Array.from({length: p.total}, (_, i) => `
          <div class="prog-dot ${i < p.installments ? 'done' : i === p.installments ? 'now' : ''}"></div>
        `).join('')}
      </div>
      <div style="margin-top:2rem">
        <a href="{{ site.baseurl }}/projects/${p.slug}/" style="font-family:var(--mono);font-size:9px;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--gold-dim);padding-bottom:2px;text-decoration:none;transition:border-color 0.2s;">
          View Full Project Page →
        </a>
      </div>
    `;

    document.getElementById('proj-detail-content').innerHTML = content;
    document.getElementById('proj-list').classList.add('hidden');
    document.getElementById('proj-detail').classList.add('active');
    
    document.getElementById('proj-detail').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // ─── Hide project detail ───
  function hideProjectDetail() {
    document.getElementById('proj-list').classList.remove('hidden');
    document.getElementById('proj-detail').classList.remove('active');
  }
</script>