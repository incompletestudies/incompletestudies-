---
layout: default
title: Seasons
permalink: /seasons/
---

<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Seasons</span>
    <span class="col-head-meta">Each cycle becomes its own object</span>
  </div>
  
  <div class="seasons-body">
    <div class="seasons-intro">
      Each seasonal cycle is archived as a distinct object — a record of the projects, contributors, and completed arcs that defined that period. This is how the archive builds institutional memory over time.
    </div>

    <ul class="seasons-list">
      {% assign sorted_seasons = site.seasons | sort: "order" %}
      {% for season in sorted_seasons %}
        {% assign season_posts = site.posts | where: "season", season.code %}
        {% assign season_projects = site.projects | where: "season", season.code %}
        
        <li class="season-entry {% if season.status == 'active' %}current{% endif %}">
          <div class="season-num">{{ season.code | remove: "S" }}</div>
          <div class="season-content">
            <div class="season-range">
              {{ season.title }} · {{ season.range }}
              {% if season.status == 'active' %}
                <span class="season-active-badge">● Currently active</span>
              {% endif %}
            </div>
            <div class="season-title">{{ season.subtitle }}</div>
            
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
              <div class="season-contribs">{{ contributor_names | join: " · " }}</div>
              <div class="season-arcs">{{ season_projects.size }} projects · {{ season_posts.size }} installments published</div>
            {% else %}
              <div class="season-contribs">Call opens: March 2026</div>
              <div class="season-arcs">Projects to be selected</div>
            {% endif %}
            
            <div class="season-actions">
              {% if season.status == 'active' %}
                <span class="pill live">Currently active</span>
              {% else %}
                <a href="{{ site.baseurl }}/contributors/" class="season-action-link">Apply →</a>
              {% endif %}
              <a href="{{ site.baseurl }}/seasons/{{ season.slug }}/" class="season-action-link">View season →</a>
            </div>
          </div>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>



<style>
  /* ─── SEASONS PAGE ─── */

  .seasons-body {
    max-width: 760px;
    margin: 0 auto;
    padding: 2rem 0;
  }

  .seasons-intro {
    max-width: 560px;
    padding: 2rem 0;
    border-bottom: 1px solid var(--rule);
    margin-bottom: 2rem;
    font-family: var(--text);
    font-size: 14px;
    font-style: italic;
    color: var(--pale);
    line-height: 1.9;
  }

  .seasons-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  /* ─── Season Entry ─── */
  .season-entry {
    display: flex;
    gap: 2rem;
    padding: 1.5rem 0;
    border-bottom: 1px solid var(--rule);
    transition: opacity 0.3s ease;
  }

  .season-entry:last-child {
    border-bottom: none;
  }

  .season-entry.current {
    opacity: 1 !important;
  }

  /* ─── Season Number ─── */
  .season-num {
    font-family: var(--display);
    font-size: 32px;
    font-weight: 900;
    font-style: italic;
    color: var(--gold-dim);
    flex-shrink: 0;
    min-width: 60px;
    line-height: 1;
  }

  /* ─── Season Content ─── */
  .season-content {
    flex: 1;
  }

  .season-range {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.05em;
    margin-bottom: 0.2rem;
  }

  .season-active-badge {
    color: var(--sage);
    margin-left: 0.5rem;
    font-size: 9px;
    letter-spacing: 0.08em;
  }

  .season-title {
    font-family: var(--display);
    font-size: 22px;
    font-style: italic;
    font-weight: 700;
    color: var(--cream);
    margin-bottom: 0.5rem;
    line-height: 1.3;
  }

  .season-contribs {
    font-family: var(--text);
    font-size: 13px;
    color: var(--pale);
    font-style: italic;
    margin-bottom: 0.1rem;
  }

  .season-arcs {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--ash);
    letter-spacing: 0.04em;
    opacity: 0.7;
  }

  /* ─── Season Actions ─── */
  .season-actions {
    display: flex;
    gap: 1.5rem;
    margin-top: 0.8rem;
    flex-wrap: wrap;
  }

  .season-action-link {
    font-family: var(--mono);
    font-size: 8.5px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--mid);
    border-bottom: 1px solid var(--ash);
    padding-bottom: 2px;
    text-decoration: none;
    transition: all 0.2s ease;
  }

  .season-action-link:hover {
    color: var(--gold);
    border-bottom-color: var(--gold);
  }

  /* ─── Pill Badge ─── */
  .pill {
    display: inline-block;
    font-family: var(--mono);
    font-size: 7px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.15rem 0.6rem;
    border-radius: 12px;
    border: 1px solid;
  }

  .pill.live {
    color: var(--sage);
    border-color: var(--sage-dim);
    background: rgba(76, 175, 80, 0.05);
  }

  /* ─── Responsive ─── */

  /* Tablet */
  @media (max-width: 768px) {
    .seasons-body {
      padding: 1.5rem 0;
    }
    
    .seasons-intro {
      font-size: 13px;
      padding: 1.5rem 0;
    }
    
    .season-entry {
      gap: 1.5rem;
      padding: 1.25rem 0;
    }
    
    .season-num {
      font-size: 28px;
      min-width: 50px;
    }
    
    .season-title {
      font-size: 19px;
    }
    
    .season-range {
      font-size: 10px;
    }
  }

  /* Mobile */
  @media (max-width: 480px) {
    .seasons-body {
      padding: 1rem 0;
    }
    
    .seasons-intro {
      font-size: 12px;
      padding: 1rem 0;
      margin-bottom: 1.5rem;
      max-width: 100%;
    }
    
    .season-entry {
      gap: 1rem;
      padding: 1rem 0;
      flex-wrap: wrap;
    }
    
    .season-num {
      font-size: 24px;
      min-width: 44px;
    }
    
    .season-title {
      font-size: 17px;
    }
    
    .season-range {
      font-size: 9px;
      flex-wrap: wrap;
    }
    
    .season-active-badge {
      display: block;
      margin-left: 0;
      margin-top: 0.2rem;
    }
    
    .season-contribs {
      font-size: 12px;
    }
    
    .season-arcs {
      font-size: 9px;
    }
    
    .season-actions {
      gap: 1rem;
      margin-top: 0.6rem;
    }
    
    .season-action-link {
      font-size: 7.5px;
    }
    
    .pill {
      font-size: 6px;
      padding: 0.1rem 0.5rem;
    }
  }

  /* ─── Small screens ─── */
  @media (max-width: 380px) {
    .season-num {
      font-size: 20px;
      min-width: 36px;
    }
    
    .season-title {
      font-size: 15px;
    }
    
    .season-content {
      flex: 1;
    }
    
    .season-actions {
      flex-direction: column;
      gap: 0.5rem;
    }
  }
</style>