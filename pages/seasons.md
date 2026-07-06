---
layout: default
title: Seasons
permalink: /seasons/
---
<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Season Archive</span>
    <span class="col-head-meta">Each cycle becomes its own object</span>
  </div>
  <div class="seasons-body">
    <div style="max-width:560px;padding:2rem 0;border-bottom:1px solid var(--rule);margin-bottom:2rem;font-family:var(--text);font-size:14px;font-style:italic;color:var(--pale);line-height:1.9">
      Each seasonal cycle is archived as a distinct object — a record of the projects, contributors, and completed arcs that defined that period. This is how the archive builds institutional memory over time.
    </div>

    <ul style="list-style:none">
      {% assign sorted_seasons = site.seasons | sort: "order" %}
      {% for season in sorted_seasons %}
        {% assign season_posts = site.posts | where: "season", season.code %}
        {% assign season_projects = site.projects | where: "season", season.code %}
        <li class="season-entry {% if season.status == 'active' %}current{% else %}{% endif %}" {% unless season.status == 'active' %}style="opacity:0.38"{% endunless %}>
          <div class="season-num">{{ season.code | remove: "S" }}</div>
          <div>
            <div class="season-range">{{ season.title }} · {{ season.range }}{% if season.status == 'active' %} · Currently active{% endif %}</div>
            <div class="season-title">{{ season.subtitle }}</div>
            {% if season_posts.size > 0 %}
              {% assign author_slugs = "" | split: "" %}
              {% for post in season_posts %}{% assign author_slugs = author_slugs | push: post.author %}{% endfor %}
              {% assign unique_author_slugs = author_slugs | uniq %}
              {% assign contributor_names = "" | split: "" %}
              {% for slug in unique_author_slugs %}
                {% assign person = site.people | where: "slug", slug | first %}
                {% if person %}{% assign contributor_names = contributor_names | push: person.title %}{% endif %}
              {% endfor %}
              <div class="season-contribs">{{ contributor_names | join: " · " }}</div>
              <div class="season-arcs">{{ season_projects.size }} projects · {{ season_posts.size }} installments published</div>
            {% else %}
              <div class="season-contribs">Call opens: March 2026</div>
              <div class="season-arcs">Projects to be selected</div>
            {% endif %}
            <div style="margin-top:0.8rem">
              {% if season.status == 'active' %}
                <span class="pill live">Currently active</span>
              {% else %}
                <a href="{{ site.baseurl }}/contributors/" style="font-family:var(--mono);font-size:8.5px;letter-spacing:0.12em;text-transform:uppercase;color:var(--mid);border-bottom:1px solid var(--ash);padding-bottom:2px">Apply →</a>
              {% endif %}
            </div>
            <div style="margin-top:0.6rem">
              <a href="{{ site.baseurl }}/seasons/{{ season.slug }}/" style="font-family:var(--mono);font-size:8.5px;letter-spacing:0.12em;text-transform:uppercase;color:var(--mid);border-bottom:1px solid var(--ash);padding-bottom:2px">View season →</a>
            </div>
          </div>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>
