---
layout: home
title: The Unfinished Archive
permalink: /
---
<!-- ══════════════════════════════════════════
     HOME
══════════════════════════════════════════ -->

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
        {% for project in site.data.projects %}
          <li class="home-index-item" onclick="location.href='{{ site.baseurl }}/projects/#{{ project.slug }}'">
            <span class="home-index-num">{{ project.id }}</span>
            <span class="home-index-title">{{ project.title }}</span>
            <span class="home-index-status {% if project.status == 'Live' %}live{% endif %}">
              {{ project.status }}
            </span>
          </li>
        {% endfor %}
      </ul>
    </div>
  </div>

  <div class="home-right">
    <div class="home-temporal">
      <div class="home-bg-year">2025</div>
      <div class="home-latest">
        <div class="home-latest-eyebrow">Latest installment</div>
        {% assign latest_post = site.posts | first %}
        <div class="home-latest-title">{{ latest_post.title }}</div>
        <div class="home-latest-meta">{{ latest_post.author }} · {{ latest_post.date | date: "%B %d, %Y" }}</div>
        <div class="home-latest-excerpt">{{ latest_post.excerpt | strip_html | truncatewords: 30 }}</div>
      </div>
    </div>

    <div class="home-timeline">
      {% for post in site.posts limit:5 %}
        <div class="timeline-inst {% if forloop.first %}current{% else %}done{% endif %}">
          <div class="timeline-inst-num">{{ post.date | date: "I·%m %y" }}</div>
          <div class="timeline-inst-title">{{ post.title }}</div>
        </div>
      {% endfor %}
    </div>
  </div>
</div>

