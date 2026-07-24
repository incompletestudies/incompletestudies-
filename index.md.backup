---
layout: default
title: The Unfinished Archive
permalink: /
---

<div class="home-hero">
  <div class="home-left">
    <div>
      <div class="home-eyebrow">The Unfinished Archive</div>
      <h1 class="home-title">
        Journal of Incomplete Studies
      </h1>
      <div class="home-season-badge">
        Season {{ site.current_season | default: "1" }} · Autumn 2026 → ongoing
      </div>
    </div>

    <div>
      <div style="font-family:var(--mono);font-size:8px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ash);margin-bottom:0.8rem">Active projects</div>
      <ul class="home-index">
        {% if site.projects and site.projects.size > 0 %}
          {% for project in site.projects %}
            <li class="home-index-item" onclick="location.href='{{ site.baseurl }}{{ project.url }}'" role="link" tabindex="0">
              <span class="home-index-num">P–{{ forloop.index }}</span>
              <span class="home-index-title">{{ project.title }}</span>
              {% if project.status == 'Ongoing' %}
                <span class="home-index-status live">Live</span>
              {% elsif project.status == 'New' %}
                <span class="home-index-status" style="color:var(--gold-dim)">New</span>
              {% else %}
                <span class="home-index-status">Inst. {{ project.installments | default: "?" }}</span>
              {% endif %}
            </li>
          {% endfor %}
        {% else %}
          <li class="home-index-item" style="opacity:0.5;cursor:default;">
            <span class="home-index-title" style="color:var(--mid);font-style:normal;">No projects yet — check back soon</span>
          </li>
        {% endif %}
      </ul>
    </div>
  </div>

  <div class="home-right">
    <div class="home-temporal">
      <div class="home-bg-year">{{ site.time | date: "%Y" }}</div>
      <div class="home-latest">
        {% assign latest_post = site.posts | first %}
        {% if latest_post %}
          {% assign latest_project = site.projects | where: "slug", latest_post.project_slug | first %}
          {% assign latest_author = site.people | where: "slug", latest_post.author_slug | first %}
          
          <div class="home-latest-eyebrow">
            Latest installment · 
            {{ latest_post.date | date: "%b %Y" }} · 
            {% if latest_project.id %}
              {{ latest_project.id }}
            {% else %}
              {{ latest_post.project_slug | default: "P–?" }}
            {% endif %}
            Inst. {{ latest_post.installment | default: "?" }}
          </div>
          
          <div class="home-latest-title">
            <a href="{{ site.baseurl }}{{ latest_post.url }}" style="color:var(--bright);text-decoration:none;transition:color 0.2s;">
              {{ latest_post.title }}
            </a>
          </div>
          
          <div class="home-latest-meta">
            {% if latest_author %}
              {{ latest_author.title }}
            {% elsif latest_post.author %}
              {{ latest_post.author }}
            {% else %}
              {{ latest_post.author_slug | default: "Anonymous" }}
            {% endif %}
            ·
            {% if latest_project %}
              {{ latest_project.title }}
            {% elsif latest_post.project %}
              {{ latest_post.project }}
            {% else %}
              {{ latest_post.project_slug | default: "Uncategorized" }}
            {% endif %}
          </div>
          
          <div class="home-latest-excerpt">
            <a href="{{ site.baseurl }}{{ latest_post.url }}" style="color:var(--pale);text-decoration:none;transition:color 0.2s;">
              {{ latest_post.excerpt | strip_html | truncatewords: 30 }}
            </a>
          </div>
        {% else %}
          <div class="home-latest-eyebrow">No installments yet</div>
          <div class="home-latest-title">Check back soon</div>
          <div class="home-latest-excerpt" style="color:var(--mid);font-style:normal;">
            The first installment will appear here.
          </div>
        {% endif %}
      </div>
    </div>

    <div class="home-timeline">
      {% if site.posts and site.posts.size > 0 %}
        {% for post in site.posts limit:5 %}
          <div class="timeline-inst {% if forloop.first %}current{% else %}done{% endif %}" onclick="location.href='{{ site.baseurl }}{{ post.url }}'" role="link" tabindex="0">
            <div class="timeline-inst-num">
              I·{% if post.installment < 10 %}0{% endif %}{{ post.installment | default: "?" }} 
              {{ post.date | date: "%b'%y" }}
            </div>
            <div class="timeline-inst-title">{{ post.title }}</div>
          </div>
        {% endfor %}
      {% else %}
        <div class="timeline-inst" style="opacity:0.3;cursor:default;flex:1;text-align:center;">
          <div class="timeline-inst-num">—</div>
          <div class="timeline-inst-title" style="color:var(--mid);font-style:normal;">No installments yet</div>
        </div>
      {% endif %}
    </div>
  </div>
</div>