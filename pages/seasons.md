---
layout: default
title: Seasons
permalink: /seasons/
---

<div class="section-wrap">

  {% include breadcrumb.html %}

  <div class="col-head">
    <span class="col-head-title">Seasons</span>
    <span class="col-head-meta">Each cycle becomes its own object</span>
  </div>

  <div class="container-narrow mt-lg">
    <div class="content">
      <p>
        Each seasonal cycle is archived as a distinct object — a record of the projects, contributors, and completed arcs that defined that period. This is how the archive builds institutional memory over time.
      </p>
    </div>

    <div class="list-container">
      {% assign sorted_seasons = site.seasons | sort: "code" %}
      {% for season in sorted_seasons %}
        {% assign season_posts = site.posts | where: "season", season.code %}
        {% assign season_projects = site.projects | where_exp: "project", "project.seasons contains season.code" %}

        <a href="{{ site.baseurl }}/seasons/{{ season.slug }}/" 
        class="list-item list-item-bordered" 
        style="align-items: flex-start; padding: 1.5rem 0; border-bottom: 1px solid var(--rule); text-decoration: none; color: inherit; 
          {% if season.pill == 'Archived' %}opacity: 0.7;{% elsif season.pill == 'Upcoming' %}opacity: 0.4;{% endif %}">
        

          <div class="list-item-left" style="min-width: 70px; display: flex; flex-direction: column; align-items: center; gap: 0.1rem;">
            <span class="text-display" style="font-size: 32px; font-weight: 900; font-style: italic; color: {% if season.pill == 'Live' %}var(--gold){% else %}var(--ash){% endif %}; line-height: 1;">
              {{ season.code | remove: 'S'}}
            </span>
            <span class="pill 
              {% if season.pill == 'Live' %}live
              {% elsif season.pill == 'Archived' %}archived
              {% else %}upcoming{% endif %}" 
              style="font-size: 6px; padding: 0.05rem 0.4rem;">
              {{ season.pill | default: "Upcoming" }}
            </span>
          </div>

          <div class="list-item-content">
            <div class="list-item-meta text-mono">
              Season {{ season.code | remove: 'S' }} · {{ season.range }}
            </div>

            <span class="list-item-title text-display text-fluid-xl mt-sm">
              {{ season.title }}
            </span>

            {% if season_posts.size > 0 %}
              {% assign author_slugs = "" | split: "" %}
              {% for post in season_posts %}
                {% assign author_slugs = author_slugs | concat: post.authors %}
              {% endfor %}
              {% assign unique_author_slugs = author_slugs | uniq %}
              {% assign contributor_names = "" | split: "" %}
              {% for slug in unique_author_slugs %}
                {% assign person = site.people | where: "slug", slug | first %}
                {% if person %}
                  {% assign contributor_names = contributor_names | push: person.name | default: person.title %}
                {% endif %}
              {% endfor %}

              <div class="list-item-meta text-italic">
                {{ contributor_names | join: " · " }}
              </div>

              <div class="card-stats mt-md">
                <span class="stat">
                  <span class="stat-number">{{ season_projects.size }}</span>
                  <span class="stat-label">projects</span>
                </span>
                <span class="stat">
                  <span class="stat-number">{{ season_posts.size }}</span>
                  <span class="stat-label">installments published</span>
                </span>
              </div>

            {% else %}
              <div class="list-item-meta text-italic">
                Call opens: TBA
              </div>
              <div class="list-item-meta text-mono">
                Projects to be selected
              </div>
            {% endif %}

            {% if season.pill != 'Live' and season.pill != 'Archived' %}
              <div style="margin-top: 0.8rem;">
                <span class="link-mono" onclick="event.stopPropagation();">Apply →</span>
              </div>
            {% endif %}
          </div>
        </a>
      {% endfor %}
    </div>
  </div>
</div>