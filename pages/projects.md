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
    
    <!-- SIDEBAR -->
    <aside class="proj-sidebar">
      <div class="proj-sidebar-label">Project index</div>
      <ul style="list-style:none">
        {% for project in site.projects %}
          <li class="proj-sidebar-item {% if forloop.first %}active{% endif %}" 
              onclick="showProjectDetail({{ forloop.index0 }})">
            <div class="proj-sidebar-id">{{ project.id }} <span>{{ project.installments }} inst.</span></div>
            <div class="proj-sidebar-name">{{ project.title }}</div>
          </li>
        {% endfor %}
      </ul>
    </aside>

    <!-- MAIN CONTENT -->
    <div class="proj-main">
      
      <!-- LIST VIEW -->
      <div class="proj-list-view" id="proj-list">
        {% for project in site.projects %}
          <div class="proj-card" onclick="showProjectDetail({{ forloop.index0 }})">
            <div>
              <div class="proj-card-top">
                <span class="proj-card-id">{{ project.id }}</span>
                <span class="pill {% if project.status == 'Ongoing' %}live{% elsif project.status == 'New' %}new-p{% endif %}">
                  {{ project.status }}
                </span>
              </div>
              <div class="proj-card-title">{{ project.title }}</div>
              <div class="proj-card-contrib">— {{ project.author }}</div>
              <div class="proj-card-abstract">{{ project.abstract }}</div>
            </div>
            <div class="proj-card-right">
              <div class="proj-card-cycle">
                Inst. {{ project.installments }} of {{ project.total_installments }}<br>
                {{ project.last_updated }}<br>
                {{ project.id }} · {{ project.season }}
              </div>
              <div class="prog-dots">
                {% assign completed = project.installments %}
                {% assign total = project.total_installments %}
                {% for i in (1..total) %}
                  <div class="prog-dot 
                    {% if i < completed %}done
                    {% elsif i == completed %}now
                    {% endif %}">
                  </div>
                {% endfor %}
              </div>
            </div>
          </div>
        {% endfor %}
      </div>

      <!-- DETAIL VIEW -->
      <div class="proj-detail" id="proj-detail">
        <button class="back-link" onclick="hideProjectDetail()">← All projects</button>
        <div id="proj-detail-content"></div>
      </div>

    </div>
  </div>
</div>

<script>
  const PROJECTS = [
    {% for project in site.projects %}
      {
        id: "{{ project.id }}",
        title: "{{ project.title }}",
        author: "{{ project.author }}",
        status: "{{ project.status }}",
        abstract: {{ project.abstract | jsonify }},
        installments: {{ project.installments }},
        total: {{ project.total_installments }},
        last_updated: "{{ project.last_updated }}",
        season: "{{ project.season }}",
        slug: "{{ project.slug }}"
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  function showProjectDetail(index) {
    const p = PROJECTS[index];
    
    // Update sidebar
    document.querySelectorAll('.proj-sidebar-item').forEach((el, i) => {
      el.classList.toggle('active', i === index);
    });

    // Build detail content
    const content = `
      <div class="col-head" style="padding:0 0 1.5rem">
        <span class="col-head-title" style="font-size:clamp(20px,3vw,36px)">${p.title}</span>
        <span class="col-head-meta">${p.id} · ${p.last_updated}</span>
      </div>
      <div style="font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:0.04em;margin-bottom:2rem">${p.author}</div>
      <div style="font-family:var(--text);font-size:13px;font-style:italic;color:var(--pale);line-height:1.8;margin-bottom:2rem">${p.abstract}</div>
      <div style="display:flex;gap:2rem;flex-wrap:wrap">
        <div><strong>Status:</strong> ${p.status}</div>
        <div><strong>Progress:</strong> ${p.installments} of ${p.total} installments</div>
        <div><strong>Season:</strong> ${p.season}</div>
      </div>
      <div class="prog-dots" style="margin-top:1.5rem">
        ${Array.from({length: p.total}, (_, i) => `
          <div class="prog-dot ${i < p.installments ? 'done' : ''}"></div>
        `).join('')}
      </div>
      <div style="margin-top:2rem">
        <a href="{{ site.baseurl }}/projects/${p.slug}/" style="font-family:var(--mono);font-size:9px;letter-spacing:0.12em;text-transform:uppercase;color:var(--gold);border-bottom:1px solid var(--gold-dim);padding-bottom:2px">
          View Full Project Page →
        </a>
      </div>
    `;

    document.getElementById('proj-detail-content').innerHTML = content;
    document.getElementById('proj-list').classList.add('hidden');
    document.getElementById('proj-detail').classList.add('active');
  }

  function hideProjectDetail() {
    document.getElementById('proj-list').classList.remove('hidden');
    document.getElementById('proj-detail').classList.remove('active');
  }
</script>