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
        <span>A serial research publication<br>for thought still in motion</span>
      </h1>
      <div class="home-season-badge">
        Season {{ site.current_season }} · Autumn 2024 → ongoing
      </div>
    </div>

    <div>
      <div style="font-family:var(--mono);font-size:8px;letter-spacing:0.18em;text-transform:uppercase;color:var(--ash);margin-bottom:0.8rem">Active projects</div>
      <ul class="home-index">
        {% for project in site.projects %}
          <li class="home-index-item" onclick="location.href='{{ site.baseurl }}{{ project.url }}'">
            <span class="home-index-num">{{ project.id }}</span>
            <span class="home-index-title">{{ project.title }}</span>
            {% if project.status == 'Ongoing' %}
              <span class="home-index-status live">Live</span>
            {% elsif project.status == 'New' %}
              <span class="home-index-status" style="color:var(--gold-dim)">New</span>
            {% else %}
              <span class="home-index-status">Inst. {{ project.installments }}</span>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>

  <div class="home-right">
    <div class="home-temporal">
      <div class="home-bg-year">2025</div>
      <div class="home-latest">
        {% assign latest_post = site.posts | first %}
        {% if latest_post %}
          {% assign latest_project = site.projects | where: "slug", latest_post.project_slug | first %}
          {% assign latest_author = site.people | where: "slug", latest_post.author_slug | first %}
          <div class="home-latest-eyebrow">Latest installment · {{ latest_post.date | date: "%b %Y" }} · {{ latest_project.id | default: "P–??" }} Inst. {{ latest_post.installment | default: "?" }}</div>
          
          <!-- Clickable title -->
          <div class="home-latest-title">
            <a href="{{ site.baseurl }}{{ latest_post.url }}" style="color:var(--bright);text-decoration:none;transition:color 0.2s;">
              {{ latest_post.title }}
            </a>
          </div>
          
          <div class="home-latest-meta">{{ latest_author.name | default: latest_post.author_slug }} · {{ latest_project.title | default: latest_post.project_slug }}</div>
          
          <!-- Clickable excerpt -->
          <div class="home-latest-excerpt">
            <a href="{{ site.baseurl }}{{ latest_post.url }}" style="color:var(--pale);text-decoration:none;transition:color 0.2s;">
              {{ latest_post.excerpt | strip_html | truncatewords: 30 }}
            </a>
          </div>
        {% else %}
          <div class="home-latest-eyebrow">No installments yet</div>
          <div class="home-latest-title">Check back soon</div>
        {% endif %}
      </div>
    </div>

    <div class="home-timeline">
      {% for post in site.posts limit:5 %}
        <div class="timeline-inst {% if forloop.first %}current{% else %}done{% endif %}" onclick="location.href='{{ site.baseurl }}{{ post.url }}'">
          <div class="timeline-inst-num">I·{% if post.installment < 10 %}0{% endif %}{{ post.installment }} {{ post.date | date: "%b'%y" }}</div>
          <div class="timeline-inst-title">{{ post.title }}</div>
        </div>
      {% endfor %}
    </div>
  </div>
</div>