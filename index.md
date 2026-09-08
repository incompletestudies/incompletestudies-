---
layout: default
title: Journal of Incomplete Studies
permalink: /
---

<div class="home-hero">
  <div class="home-left">
    <div>
      <div class="home-eyebrow">The Unfinished Archive</div>
      <h1 class="home-title">
        Journal of Incomplete Studies
      </h1>

      {% comment %}─── MANIFESTO — Editorial Proof ───{% endcomment %}
      <div class="home-tagline">
        <span class="home-tagline-text">
          A serial research publication for
          <span class="home-tagline-revision">
            <span class="home-tagline-original">finished</span>
            <span class="home-tagline-correction">still in motion</span>
          </span>
          ideas.
        </span>
      </div>

      {% comment %}─── BUTTONS ───{% endcomment %}
      {% assign latest_post = site.posts | first %}

      <div class="flex flex-wrap flex-gap-sm" style="margin-top: 1.7rem; margin-bottom: 1rem;">
        <a href="{% if latest_post %}{{ latest_post.url | relative_url }}{% else %}/installments/{% endif %}" 
          class="btn btn-primary">
          Read Latest
        </a>

        <a href="{{ "/projects/" | relative_url }}" 
          class="btn btn-secondary">
          Browse Projects
        </a>
      </div>
    </div>

    {% comment %}─── THIS MONTH — TABLE OF CONTENTS ───{% endcomment %}
    <div>
      <div class="section-header">
        <span class="section-title">This Month</span>
        <span class="section-meta">{{ site.time | date: "%B %Y" }}</span>
      </div>

      {% assign this_month = site.time | date: "%m" %}
      {% assign this_year = site.time | date: "%Y" %}
      {% assign month_posts = "" | split: "" %}

      {% for post in site.posts %}
        {% assign post_month = post.date | date: "%m" %}
        {% assign post_year = post.date | date: "%Y" %}
        {% if post_month == this_month and post_year == this_year %}
          {% assign month_posts = month_posts | push: post %}
        {% endif %}
      {% endfor %}

      {% if month_posts.size > 0 %}
        <div class="list-container">
          {% for post in month_posts %}
            {% assign project_slug = post.projects | first %}
            {% assign post_project = site.projects | where: "slug", project_slug | first %}
            {% assign author_slug = post.authors | first %}
            {% assign post_author = site.people | where: "slug", author_slug | first %}
            
            {% assign word_count = post.content | strip_html | number_of_words %}
            {% assign reading_time = word_count | divided_by: 200 | default: 1 %}
            
            <a href="{{ post.url | relative_url }}" class="list-item">
              <span class="list-item-left">{% if forloop.index < 10 %}0{% endif %}{{ forloop.index }}</span>
              
              <div class="list-item-content">
                <span class="list-item-title">{{ post.title }}</span>
                <span class="list-item-meta">
                  <span class="feed-proj-tag">
                    {% if post_project %}
                      {{ post_project.title }}
                    {% else %}
                      {{ post.projects | first | default: "Uncategorized" }}
                    {% endif %}
                  </span>
                  
                  <span class="feed-author">
                    {% if post_author %}
                      {{ post_author.name | default: post_author.title }}
                    {% elsif post.authors %}
                      {{ post.authors | first }}
                    {% else %}
                      Anonymous
                    {% endif %}
                  </span>
                </span>
              </div>

              <div class="metrics-horizontal">
                <span class="metric metric-words">{{ word_count }} words</span>
                <span class="metric metric-sep">·</span>
                <span class="metric metric-time">~{{ reading_time }} min</span>
              </div>
            </a>
          {% endfor %}
        </div>

        

      {% else %}
        <div class="empty-state">
          No installments published this month yet.
        </div>
      {% endif %}

      <a href="{{ "/installments/" | relative_url }}" class="link-arrow text-mono text-gold-dim text-fluid-sm text-left"> 
        View all installments
      </a>

    </div>



    {% comment %}─── PROJECTS ───{% endcomment %}
    {% assign active_projects = site.projects | where: "status", "Ongoing" %}

    {% if active_projects.size > 0 %}
      <div>
        <div class="section-header">
          <span class="section-title">Current Projects</span>
          <span class="section-meta">{{ active_projects.size }} Active Projects</span>
        </div>

        <div class="grid-2">
          {% for project in active_projects %}
            {% assign status_class = project.status | downcase | replace: ' ', '-' | default: "ongoing" %}
            {% assign pill_class = project.pill | downcase | replace: ' ', '-' | default: "new" %}
            
            {% assign project_posts = site.posts | where_exp: "post", "post.projects contains project.slug" %}
            {% assign post_count = project_posts.size %}
            
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
            
            <a href="{{ project.url | relative_url }}" class="card">
              <div class="card-header">
                <span class="card-id">P–{{ forloop.index }}</span>
                {% if project.pill %}
                  <span class="pill {{ pill_class }}">
                    {{ project.pill | default: "New" }}
                  </span>
                {% else %}
                  <span class="badge {{ status_class }}">
                    {{ project.status | default: "Ongoing" }}
                  </span>
                {% endif %}
              </div>
              
              <h3 class="card-title">{{ project.title }}</h3>
              
              {% if author_string != "" %}
                <div class="card-subtitle">{{ author_string }}</div>
              {% endif %}
              
              <div class="list-item-meta text-text text-fluid-sm mb-sm" >
                {{ project.content | strip_html | truncatewords: 20 }}
              </div>
              

              <div class="card-meta">
                <span>
                  <span class="card-meta-number">{{ post_count }}</span> installment{% if post_count != 1 %}s{% endif %}
                </span>

                <span style="margin-left: auto;">
                  {% if project.tags %}
                    {% for tag in project.tags limit: 3 %}
                      <span class="tag">{{ tag }}</span>
                    {% endfor %}
                  {% endif %}
                </span>
              </div>
            </a>
          {% endfor %}
        </div>
      </div>
    {% else %}
      <div>
        <div class="section-header">
          <span class="section-title">Current Projects</span>
          <span class="section-meta">0 Active Projects</span>
        </div>
        <div class="text-center" style="opacity: 0.5; padding: 2rem 0; font-family: var(--text); font-size: 13px; color: var(--mid);">
          No active projects at the moment — check back soon
        </div>
      </div>
    {% endif %}

    {% comment %}─── Current Cohort ───{% endcomment %}
    {% if site.people and site.people.size > 0 %}
      {% comment %}─── Find the newest author once ───{% endcomment %}
      {% assign sorted_by_date = site.people | sort: "date" | reverse %}
      {% assign newest_author = sorted_by_date | first %}

      <div class="section-header">
        <span class="section-title">Current Cohort</span>
        <span class="section-meta">{{ site.people | size }} contributors</span>
      </div>

      <div class="scroll-wrapper">
        <div class="scroll-container">
          {% for person in site.people %}
            <a href="{{ person.url | relative_url }}" class="contributor-card">
              <div class="contributor-avatar">
                {% if person.profile_image %}
                  {% assign avatar_path = "/assets/images/people/" | append: person.slug | append: "/" | append: person.profile_image %}
                  <img src="{{ avatar_path | relative_url }}" alt="{{ person.name | default: person.title }}">
                {% else %}
                  <span class="contributor-initial">{{ person.name | default: person.title | slice: 0 }}</span>
                {% endif %}
              </div>
              <span class="contributor-name">{{ person.name | default: person.title }}</span>
              <span class="contributor-role">{{ person.role | default: "Contributor" }}</span>
              {% if person.discipline %}
                <span class="contributor-discipline">{{ person.discipline }}</span>
              {% endif %}
              {% if person.slug == newest_author.slug %}
                <span class="new-badge mt-sm">✦ New</span>
              {% endif %}
            </a>
          {% endfor %}
        </div>
      </div>
    {% endif %}

    {% comment %}─── ARCHIVE STATISTICS ───{% endcomment %}
    <div>
      <div class="section-header">
        <span class="section-title">Archive Statistics</span>
      </div>
      <div class="grid-3" style="gap: 1rem; padding: 1rem 0;">
        <div class="text-center" style="padding: 0.75rem; border: 1px solid var(--rule); border-radius: 4px;">
          <span class="home-stat-number">{{ site.posts | size }}</span>
          <span class="home-stat-label">Installments</span>
        </div>
        <div class="text-center" style="padding: 0.75rem; border: 1px solid var(--rule); border-radius: 4px;">
          <span class="home-stat-number">{{ site.projects | size }}</span>
          <span class="home-stat-label">Projects</span>
        </div>
        <div class="text-center" style="padding: 0.75rem; border: 1px solid var(--rule); border-radius: 4px;">
          <span class="home-stat-number">{{ site.people | size }}</span>
          <span class="home-stat-label">Contributors</span>
        </div>
      </div>
    </div>

    {% comment %}─── ABOUT THE ARCHIVE ───{% endcomment %}
    <div class="section-header">
      <span class="section-title">About the Journal</span>
    </div>

    <div class="content">
      <p>
        The Journal of Incomplete Studies is a serial research publication
        dedicated to thought still in motion. It embraces the unfinished,
        the provisional, and the ongoing — publishing installments across
        disciplines without requiring closure.
      </p>
      <a href="{{ "/about/" | relative_url }}" class="link-arrow text-mono text-gold-dim text-fluid-sm">
        Read more about the publication
      </a>
    </div>
  </div>
</div>

<style>
  .new-badge {
    font-family: var(--mono);
    font-size: 0.6rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--gold);
    background: rgba(201, 168, 76, 0.12);
    padding: 0.1rem 0.5rem;
    border-radius: 12px;
    border: 1px solid rgba(201, 168, 76, 0.2);
    flex-shrink: 0;
  }

  /* ─── MINIMAL HOMEPAGE STYLES ─── */

  .home-tagline-revision {
    position: relative;
    display: inline-block;
  }

  .home-tagline-original {
    text-decoration: line-through;
    text-decoration-thickness: 1px;
    opacity: .65;
  }

  .home-tagline-correction {
    position: absolute;
    left: 0;
    top: 1.15em;
    white-space: nowrap;
    font-family: var(--mono);
    font-size: 0.82em;
    color: var(--gold);
  }

  .home-toc-footer {
    margin-top: 0.8rem;
    text-align: right;
  }

  .home-stat-number {
    display: block;
    font-family: var(--display);
    font-size: clamp(24px, 3vw, 36px);
    font-weight: 900;
    font-style: italic;
    color: var(--gold);
  }

  .home-stat-label {
    font-family: var(--mono);
    font-size: 7px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

</style>