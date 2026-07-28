---
layout: default
title: Projects
permalink: /projects/
---

div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Projects</span>
    <span class="col-head-meta">
      {% assign current_season = site.seasons | where: "pill", "Live" | first %}
      {% assign active_projects = site.projects | where: "status", "Ongoing" %}
      {{ current_season.title }} · {{ current_season.range }} · {{ active_projects | size }} active
    </span>
  </div>


  
  <div class="projects-layout">
    
    <!-- ─── SIDEBAR ─── -->
    <aside class="proj-sidebar">
      <details class="accordion" id="sidebar-accordion">
        <summary>
          <span>Browse Projects</span>
          <span class="accordion-icon">✚</span>
        </summary>
        <div class="accordion-content proj-sidebar-content">
          <nav class="proj-sidebar-nav">
            {% assign sorted_projects = site.projects | sort: "order" %}
            {% for project in sorted_projects %}

              {% comment %}─── Count actual posts for this project ───{% endcomment %}
              {% assign post_count = 0 %}
              {% for post in site.posts %}
                {% if post.projects %}
                  {% if post.projects contains project.slug %}
                    {% assign post_count = post_count | plus: 1 %}
                  {% endif %}
                {% endif %}
              {% endfor %}

              <div class="proj-sidebar-item" data-slug="{{ project.slug }}" onclick="showProjectDetailBySlug('{{ project.slug }}')">
                <div class="proj-sidebar-id">
                  <span class="card-id">P–{{ forloop.index }}</span>
                  <span class="text-mono">{{ post_count }} inst.</span>
                </div>
                <div class="proj-sidebar-name">{{ project.title }}</div>
              </div>
            {% endfor %}
          </nav>
        </div>
      </details>
    </aside>

    <!-- ─── MAIN CONTENT ─── -->
    <main class="proj-main">
      
      <!-- Project List View -->
      <div id="proj-list">
        <div class="proj-list-header">
          <span class="proj-list-title">Select a project</span>
          <span class="proj-list-count">{{ site.projects | size }} projects</span>
        </div>
        
        <div class="proj-list-grid">
          {% assign sorted_projects = site.projects | sort: "order" %}
          {% for project in sorted_projects %}
            {% assign author_names = "" | split: "" %}
            {% if project.people %}
              {% for slug in project.people %}
                {% assign person = site.people | where: "slug", slug | first %}
                {% if person %}
                  {% assign author_names = author_names | push: person.name | default: person.title %}
                {% endif %}
              {% endfor %}
            {% endif %}
            {% assign author_string = author_names | join: " + " %}
            
            <div class="proj-card-clickable" onclick="showProjectDetailBySlug('{{ project.slug }}')">
              <div class="card">
                <div class="card-header">
                  {% assign status = project.status | default: "Ongoing" %}
                  {% assign status_class = status | downcase | replace: ' ', '-' %}
                  
                  <span class="card-id">P–{{ forloop.index }}</span>
                  <span class="badge {{ status_class }}">
                    {{ status }}
                  </span>
                </div>
                <h3 class="card-title">{{ project.title }}</h3>
                <p class="card-subtitle">{{ author_string | default: "No contributors listed" }}</p>
                <p class="card-excerpt">{{ project.abstract | truncate: 120 | default: "No abstract available." }}</p>
                
                
                {% if project.tags and project.tags.size > 0 %}
                  <div class="flex flex-wrap" style="gap: 0.3rem; margin-top: 0.5rem; align-items: center;">
                    <span class="text-mono text-ash" style="font-size: 10px; text-transform: uppercase; opacity: 0.6;">Tags:</span>
                    {% for tag in project.tags limit: 3 %}
                      <span class="tag">{{ tag }}</span>
                    {% endfor %}
                    {% if project.tags.size > 3 %}
                      <span class="tag-more">+{{ project.tags.size | minus: 3 }}</span>
                    {% endif %}
                  </div>
                {% endif %}
                
                <div class="card-meta mt-sm">
                  <span>Click to learn more →</span>
                </div>
              </div>
            </div>
          {% endfor %}
        </div>
      </div>

      <!-- Project Detail View -->
      <div id="proj-detail" class="proj-detail">
        <button class="proj-detail-back" onclick="hideProjectDetail()">← Back to all projects</button>
        <div id="proj-detail-content"></div>
      </div>
    </main>
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
              {% assign name = name | append: ", " | append: person.discipline %}
            {% endif %}
            {% assign author_names = author_names | push: name %}
          {% else %}
            {% assign author_names = author_names | push: slug %}
          {% endif %}
        {% endfor %}
      {% endif %}
      {% assign author_string = author_names | join: " + " %}
      
      {% comment %}─── Count installments for this project ───{% endcomment %}
      {% assign project_posts = site.posts | where_exp: "post", "post.projects contains project.slug" %}
      {% assign post_count = project_posts.size %}
      
      {
        title: {{ project.title | jsonify }},
        author: "{{ author_string }}",
        status: "{{ project.status | default: 'Ongoing' }}",
        abstract: {{ project.abstract | default: "No abstract yet." | jsonify }},
        installments: {{ post_count }},
        slug: "{{ project.slug }}",
        index: {{ forloop.index }}
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  // ─── Helper: Get pill class ───
  function getPillClass(status) {
    if (status === 'Ongoing') return 'live';
    if (status === 'New') return 'new-p';
    return 'upcoming';
  }

  // ─── Helper: Build timeline dots (only for existing installments) ───
  function buildTimelineDots(completed) {
    let dots = '';
    for (let i = 0; i < completed; i++) {
      dots += `<span class="timeline-dot done"></span>`;
    }
    return dots;
  }

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

    const content = `
      <div style="padding:0 0 1.5rem">
        <div style="display:flex;align-items:center;gap:1rem;margin-bottom:0.5rem;flex-wrap:wrap;">
          <span class="card-id">P–${p.index}</span>
          <span class="pill ${getPillClass(p.status)}">${p.status}</span>
        </div>
        <span class="col-head-title" style="font-size:clamp(20px,3vw,36px)">${p.title}</span>
      </div>

      <div style="font-family:var(--mono);font-size:10px;color:var(--muted);margin-bottom:2rem">
        ${p.author}
      </div>

      <div style="font-family:var(--text);font-size:13px;font-style:italic;color:var(--pale);line-height:1.8;margin-bottom:2rem">
        ${p.abstract}
      </div>

      <div class="flex flex-center" style="gap:0.5rem;margin-bottom:0.5rem;margin-top:0.25rem;">
        ${buildTimelineDots(p.installments)}
        <span style="font-family:var(--mono);font-size:7px;color:var(--muted);">· ${p.installments} so far</span>
      </div>

      <div style="margin-top:2rem">
        <a href="{{ site.baseurl }}/projects/${p.slug}/" class="link-mono">View Full Project Page →</a>
      </div>
    `;

    document.getElementById('proj-detail-content').innerHTML = content;
    document.getElementById('proj-list').classList.add('hidden');
    document.getElementById('proj-detail').classList.add('active');
    
    if (window.innerWidth <= 768) {
      document.getElementById('proj-detail').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  // ─── Hide project detail ───
  function hideProjectDetail() {
    document.getElementById('proj-list').classList.remove('hidden');
    document.getElementById('proj-detail').classList.remove('active');
    
    if (window.innerWidth <= 768) {
      document.getElementById('proj-list').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  // ─── Close accordion on mobile when project selected ───
  document.addEventListener('DOMContentLoaded', function() {
    const accordion = document.getElementById('sidebar-accordion');
    const items = document.querySelectorAll('.proj-sidebar-item');
    
    items.forEach(item => {
      item.addEventListener('click', function() {
        if (window.innerWidth <= 768) {
          accordion.open = false;
        }
      });
    });
  });
</script>

