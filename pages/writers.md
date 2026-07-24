---
layout: default
title: Authors
permalink: /authors/
---

<div class="section-wrap">
  
  {% include breadcrumb.html %}

  <div class="col-head">
    <span class="col-head-title">Authors</span>
    <span class="col-head-meta">{{ site.people | size }} contributors to the archive</span>
  </div>

  <div class="cr-body">
    
    {% if site.people.size == 0 %}
      <div style="padding: 3rem 0; font-family: var(--text); font-size: 14px; font-style: italic; color: var(--mid); text-align: center;">
        No authors have been added yet.
      </div>
    {% else %}
      
      <!-- ─── FIND THE NEWEST AUTHOR ─── -->
      {% assign sorted_by_date = site.people | sort: "date" | reverse %}
      {% assign newest_author = sorted_by_date | first %}
      
      <!-- ─── AUTHOR GRID ─── -->
      {% assign sorted_people = site.people | sort: "name" %}
      <div class="author-grid">
        {% for person in sorted_people %}
          {% assign author_posts = site.posts | where_exp: "post", "post.authors contains person.slug" %}
          {% assign author_projects = site.projects | where_exp: "project", "project.people contains person.slug" %}
          
          <div class="author-card {% if person.slug == newest_author.slug %}new-author{% endif %}">
            <a href="{{ site.baseurl }}{{ person.url }}" class="author-card-link">
              <div class="author-card-avatar">
                {% if person.avatar %}
                  {% assign avatar_path = "/assets/images/people/" | append: person.slug | append: "/" | append: person.avatar %}
                  <img src="{{ avatar_path | relative_url }}" alt="{{ person.name | default: person.title }}">
                {% else %}
                  <div class="avatar-placeholder">{{ person.name | default: person.title | slice: 0 }}</div>
                {% endif %}
              </div>
              
              <div class="author-card-info">
                <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
                  <h3 class="author-card-name">{{ person.name | default: person.title }}</h3>

                  <!-- {% if person.slug == newest_author.slug %}
                    <span class="new-badge">✦ New</span>
                  {% endif %} -->
                  
                  {% if person.status %}
                    {% assign status_class = person.status | downcase | replace: ' ', '-' %}
                    <span class="researcher-status {{ status_class }}">
                      {{ person.status }}
                    </span>
                  {% else %}
                    <span class="researcher-status active">
                      Active
                    </span>
                  {% endif %}

                </div>
                <p class="author-card-role">{{ person.role }}</p>
                <p class="author-card-discipline">{{ person.discipline | downcase }}</p>
                <div class="author-card-stats">
                  <span class="stat">
                    <span class="stat-number">{{ author_projects.size }}</span>
                    <span class="stat-label">projects</span>
                  </span>
                  <span class="stat">
                    <span class="stat-number">{{ author_posts.size }}</span>
                    <span class="stat-label">installments</span>
                  </span>
                </div>
                
                <!-- ─── CLICKABLE "LATEST" ─── -->
                {% if author_posts.size > 0 %}
                  <div class="author-card-latest">
                    <span class="latest-label">Latest</span>
                    <a href="{{ site.baseurl }}{{ author_posts.last.url }}" class="latest-title">
                      {{ author_posts.last.title }}
                    </a>
                    <span class="latest-date">{{ author_posts.last.date | date: "%b %Y" }}</span>
                  </div>
                {% endif %}
                
              </div>
            </a>
          </div>
        {% endfor %}
      </div>
      
    {% endif %}
  </div>
</div>

<style>
  /* ─── Researcher Status ─── */
  .researcher-status {
    display: inline-block;
    font-family: var(--mono);
    font-size: 7px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.15rem 0.6rem;
    border-radius: 2px;
    border: 1px solid;
    background: transparent;
    transition: all 0.2s ease;
  }

  /* ─── Active ─── */
  .researcher-status.active {
    color: #4CAF50;
    border-color: rgba(76, 175, 80, 0.3);
    background: rgba(76, 175, 80, 0.05);
  }

  /* ─── On Leave ─── */
  .researcher-status.on-leave {
    color: #FFB74D;
    border-color: rgba(255, 183, 77, 0.3);
    background: rgba(255, 183, 77, 0.05);
  }

  /* ─── Alumni ─── */
  .researcher-status.alumni {
    color: #9E9E9E;
    border-color: rgba(158, 158, 158, 0.2);
    background: rgba(158, 158, 158, 0.05);
    opacity: 0.7;
  }

  /* ─── New ─── */
  .researcher-status.new {
    color: var(--gold);
    border-color: var(--gold-dim);
  }
  
  
  /* ─── AUTHORS PAGE ─── */

  .col-head {
    margin-bottom: 3rem;
    border-bottom: 1px solid var(--rule);
    padding-bottom: 1.5rem;
  }

  /* ─── "NEW" BADGE ─── */
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

  /* ─── NEW AUTHOR CARD (subtle highlight) ─── */
  .author-card.new-author {
    border-color: rgba(201, 168, 76, 0.2);
    background: rgba(201, 168, 76, 0.03);
  }

  .author-card.new-author:hover {
    border-color: var(--gold-dim);
    background: rgba(201, 168, 76, 0.06);
  }

  /* ─── AUTHOR GRID ─── */
  .author-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.5rem;
  }

  .author-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--rule);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s ease;
  }

  .author-card:hover {
    background: rgba(255, 255, 255, 0.04);
    border-color: var(--gold-dim);
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  }

  .author-card-link {
    text-decoration: none;
    color: inherit;
    display: block;
  }

  .author-card-avatar {
    margin-bottom: 1rem;
  }

  .author-card-avatar img,
  .author-card-avatar .avatar-placeholder {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    object-fit: cover;
  }

  .avatar-placeholder {
    background: rgba(201, 168, 76, 0.08);
    color: var(--gold);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--display);
    font-size: 1.5rem;
    font-weight: 700;
    border: 1px solid rgba(201, 168, 76, 0.1);
  }

  .author-card-name {
    font-family: var(--display);
    font-size: 1.25rem;
    margin: 0 0 0.1rem 0;
    color: var(--cream);
  }

  .author-card-role {
    font-family: var(--mono);
    font-size: 0.75rem;
    color: var(--muted);
    margin: 0 0 0.1rem 0;
    letter-spacing: 0.02em;
  }

  .author-card-discipline {
    font-family: var(--text);
    font-size: 0.9rem;
    font-style: italic;
    color: var(--pale);
    margin: 0 0 0.8rem 0;
  }

  .author-card-stats {
    display: flex;
    gap: 1.5rem;
    margin: 0 0 0.5rem 0;
  }

  .stat {
    display: flex;
    align-items: baseline;
    gap: 0.25rem;
  }

  .stat::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: var(--gold-dim);
    margin-right: 0.25rem;
  }

  .stat-number {
    font-family: var(--mono);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--cream);
  }

  .stat-label {
    font-family: var(--mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--muted);
  }

  /* ─── AUTHOR CARD "LATEST" ─── */
  .author-card-latest {
    display: flex;
    align-items: baseline;
    gap: 0.4rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
    padding-top: 0.5rem;
    border-top: 1px solid var(--rule);
  }

  .latest-label {
    font-family: var(--mono);
    font-size: 0.5rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ash);
    background: var(--void2);
    padding: 0.1rem 0.4rem;
    border-radius: 2px;
    border: 1px solid var(--rule);
  }

  .latest-title {
    font-family: var(--text);
    font-size: 0.8rem;
    font-style: italic;
    color: var(--cream);
    flex: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.2s, color 0.2s;
  }

  .latest-title:hover {
    color: var(--gold);
    border-color: var(--gold-dim);
  }

  .latest-date {
    font-family: var(--mono);
    font-size: 0.55rem;
    letter-spacing: 0.04em;
    color: var(--ash);
    flex-shrink: 0;
  }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 768px) {
    .author-grid {
      grid-template-columns: 1fr 1fr;
    }
  }

  @media (max-width: 480px) {
    .author-grid {
      grid-template-columns: 1fr;
    }

    .col-head-title {
      font-size: 2rem;
    }
  }
</style>