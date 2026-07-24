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


      {% comment %}─── PRIMARY CTAs ───{% endcomment %}
      <div class="home-ctas">
        {% assign latest_post = site.posts | first %}
        <a href="{% if latest_post %}{{ latest_post.url | relative_url }}{% else %}/installments/{% endif %}" class="home-cta primary">
          Read Latest
        </a>
        <a href="{{ "/projects/" | relative_url }}" class="home-cta secondary">
          Browse Projects
        </a>
      </div>
    </div>

    {% comment %}─── THIS MONTH — TABLE OF CONTENTS ───{% endcomment %}
    <div>
      <div class="home-toc-header">
        <span class="home-section-title">This Month</span>
        <span class="home-toc-month">{{ site.time | date: "%B %Y" }}</span>
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
        <div class="home-toc">
          {% for post in month_posts %}
            {% assign project_slug = post.projects | first %}
            {% assign post_project = site.projects | where: "slug", project_slug | first %}
            {% assign author_slug = post.authors | first %}
            {% assign post_author = site.people | where: "slug", author_slug | first %}
            
            {% comment %}─── Word count and reading time ───{% endcomment %}
            {% assign word_count = post.content | strip_html | number_of_words %}
            {% assign reading_time = word_count | divided_by: 200 | default: 1 %}
            
            <a href="{{ post.url | relative_url }}" class="home-toc-item">
              <span class="home-toc-number">{% if forloop.index < 10 %}0{% endif %}{{ forloop.index }}</span>
              <div class="home-toc-content">
                <span class="home-toc-title">{{ post.title }}</span>
                <span class="home-toc-meta">
                  <span class="feed-proj-tag">
                    {% if post_project %}
                      {{ post_project.title }}
                    {% else %}
                      {{ post.projects | first | default: "Uncategorized" }}
                    {% endif %}
                  </span>
                  ·
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
              <div class="home-toc-metrics">
                <span class="home-toc-words">{{ word_count }} words</span>
                <span class="home-toc-time">~{{ reading_time }} min</span>
              </div>
            </a>
          {% endfor %}
        </div>

        <div class="home-toc-footer">
          <a href="{{ "/installments/" | relative_url }}" class="home-toc-view-all">
            View all installments →
          </a>
        </div>
      {% else %}
        <div class="home-month-empty">
          No installments published this month yet.
        </div>
      {% endif %}
    </div>



    {% comment %}─── PROJECTS ───{% endcomment %}
    <div>
      <h2 class="home-section-title">Current Projects</h2>
      <div class="home-project-grid">
        {% if site.projects and site.projects.size > 0 %}
          {% for project in site.projects %}
            
            {% comment %}─── Set status class ───{% endcomment %}
            {% assign status_class = project.status | downcase | replace: ' ', '-' | default: "ongoing" %}
            
            {% comment %}─── Count installments for this project ───{% endcomment %}
            {% assign project_posts = site.posts | where_exp: "post", "post.projects contains project.slug" %}
            {% assign post_count = project_posts.size %}
            
            {% comment %}─── Get authors ───{% endcomment %}
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
            
            <a href="{{ project.url | relative_url }}" class="home-project-card">
              <div class="home-project-header">
                <span class="home-project-id">P–{{ forloop.index }}</span>
                <span class="project-status {{ status_class }}">
                  {{ project.status | default: "Ongoing" }}
                </span>
              </div>
              
              <h3 class="home-project-title">{{ project.title }}</h3>
              
              {% if author_string != "" %}
                <div class="home-project-authors">{{ author_string }}</div>
              {% endif %}
              
              {% if project.abstract %}
                <p class="home-project-abstract">{{ project.abstract | truncate: 120 }}</p>
              {% endif %}

              {% if project.tags %}
                <span class="home-project-tags">
                  {% for tag in project.tags limit: 3 %}
                    <span class="home-project-tag">{{ tag }}</span>
                  {% endfor %}
                  {% if project.tags.size > 2 %}
                    <span class="home-project-tag-more">+{{ project.tags.size | minus: 2 }}</span>
                  {% endif %}
                </span>
              {% endif %}

              <div class="home-project-meta">
                <span class="home-project-installments">
                  <span class="meta-number">{{ post_count }}</span> installment{% if post_count != 1 %}s{% endif %}
                </span>
                
                {% if project.tags %}
                  <span class="home-project-tags">
                    {% for tag in project.tags limit: 3 %}
                      <span class="home-project-tag">{{ tag }}</span>
                    {% endfor %}
                    {% if project.tags.size > 2 %}
                      <span class="home-project-tag-more">+{{ project.tags.size | minus: 2 }}</span>
                    {% endif %}
                  </span>
                {% endif %}
              </div>
            </a>
          {% endfor %}
        {% else %}
          <div class="home-empty-card">
            <span class="home-empty-text">No projects yet — check back soon</span>
          </div>
        {% endif %}
      </div>
    </div>
    
    

    {% comment %}─── Current Cohort ───{% endcomment %}
    {% if site.people and site.people.size > 0 %}
      <div class="home-cohort-wrapper">
        <div class="home-cohort-header">
          <span class="home-section-title">Current Cohort</span>
          <span class="home-cohort-count">{{ site.people | size }} contributors</span>
        </div>
        
        <div class="home-contributors-scroll-wrapper">
          <div class="home-contributors-scroll">
            {% for person in site.people %}
              <a href="{{ person.url | relative_url }}" class="home-contributor-card">
                <div class="home-contributor-avatar">
                  {% if person.avatar %}
                    {% assign avatar_path = "/assets/images/people/" | append: person.slug | append: "/" | append: person.avatar %}
                    <img src="{{ avatar_path | relative_url }}" alt="{{ person.name | default: person.title }}">
                  {% else %}
                    <span class="home-contributor-initial">{{ person.name | default: person.title | slice: 0 }}</span>
                  {% endif %}
                </div>
                <span class="home-contributor-name">{{ person.name | default: person.title }}</span>
                <span class="home-contributor-role">{{ person.role | default: "Contributor" }}</span>
                {% if person.discipline %}
                  <span class="home-contributor-discipline">{{ person.discipline }}</span>
                {% endif %}
              </a>
            {% endfor %}
          </div>
        </div>
      </div>
    {% endif %}

   

    {% comment %}─── ARCHIVE STATISTICS ───{% endcomment %}
    <div class="home-stats">
      <h2 class="home-section-title">Archive Statistics</h2>
      <div class="home-stats-grid">
        <div class="home-stat">
          <span class="home-stat-number">{{ site.posts | size }}</span>
          <span class="home-stat-label">Installments</span>
        </div>
        <div class="home-stat">
          <span class="home-stat-number">{{ site.projects | size }}</span>
          <span class="home-stat-label">Projects</span>
        </div>
        <div class="home-stat">
          <span class="home-stat-number">{{ site.people | size }}</span>
          <span class="home-stat-label">Contributors</span>
        </div>
      </div>
    </div>

    {% comment %}─── ABOUT THE ARCHIVE ───{% endcomment %}
    <div class="home-about">
      <h2 class="home-section-title">About the Journal</h2>
      <p class="home-about-text">
        The Journal of Incomplete Studies is a serial research publication
        dedicated to thought still in motion. It embraces the unfinished,
        the provisional, and the ongoing — publishing installments across
        disciplines without requiring closure.
      </p>
      <a href="{{ "/about/" | relative_url }}" class="home-about-link">
        Read more about the publication →
      </a>
    </div>
  </div>
</div>

<style>
  /* ─── Homepage — Editorial Table of Contents ─── */
  
  /* ─── Status Bars ─── */

  /* ─── Project Status ─── */
  .project-status {
    display: inline-block;
    font-family: var(--mono);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.15rem 0.6rem;
    border-radius: 2px;
    border: 1px solid;
    background: transparent;
  }

  /* ─── Ongoing ─── */
  .project-status.ongoing {
    color: var(--sage);
    border-color: var(--sage-dim);
  }


  /* ─── On Hold ─── */
  .project-status.on-hold {
    color: #FFB74D;
    border-color: rgba(255, 183, 77, 0.3);
    background: rgba(255, 183, 77, 0.05);
  }

  /* ─── Archived ─── */
  .project-status.archived {
    color: #9E9E9E;
    border-color: rgba(158, 158, 158, 0.2);
    background: rgba(158, 158, 158, 0.05);
  }

  /* ─── New ─── */
  .project-status.new {
    color: var(--gold);
    border-color: var(--gold-dim);
  }

  /* ─── Installment Status ─── */
  .installment-status {
    display: inline-block;
    font-family: var(--mono);
    font-size: 6px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.1rem 0.4rem;
    border-radius: 2px;
  }

  /* ─── First Inst. ─── */
  .installment-status.first {
    color: #64B5F6;
    background: rgba(100, 181, 246, 0.08);
    border: 1px solid rgba(100, 181, 246, 0.2);
  }

  /* ─── Revised ─── */
  .installment-status.revised {
    color: #CE93D8;
    background: rgba(206, 147, 216, 0.08);
    border: 1px solid rgba(206, 147, 216, 0.2);
  }

  /* ─── Last Inst. ─── */
  .installment-status.last {
    color: #FF8A65;
    background: rgba(255, 138, 101, 0.08);
    border: 1px solid rgba(255, 138, 101, 0.2);
  }

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


/* ─── REST ─── */

  /* ─── Section Labels ─── */
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

  .home-ctas {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-top: 1.7rem;
    margin-bottom: 1rem;
  }

  .home-cta {
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.5rem 1.25rem;
    border-radius: 2px;
    text-decoration: none;
    transition: all 0.2s;
  }

  .home-cta.primary {
    background: var(--gold);
    color: var(--void);
    border: 1px solid var(--gold);
  }

  .home-cta.primary:hover {
    background: transparent;
    color: var(--gold);
  }

  .home-cta.secondary {
    border: 1px solid var(--rule);
    color: var(--muted);
    background: transparent;
  }

  .home-cta.secondary:hover {
    border-color: var(--gold-dim);
    color: var(--cream);
  }

  .home-section-title {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--ash);
    margin-top: 2.5rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--rule);
  }

  .home-toc-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-top: 2.5rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--rule);
  }

  .home-toc-header .home-section-title {
    margin-top: 0;
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
  }

  .home-toc-month {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.05em;
  }

  .home-toc {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .home-toc-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.8rem 1rem;
    border-radius: 4px;
    text-decoration: none;
    color: inherit;
    transition: background 0.2s;
    border-bottom: 1px solid var(--rule);
  }

  .home-toc-item:hover {
    background: rgba(255, 255, 255, 0.02);
  }

  .home-toc-number {
    font-family: var(--mono);
    font-size: 16px;
    font-weight: 700;
    color: var(--gold-dim);
    flex-shrink: 0;
    min-width: 38px;
  }

  .home-toc-content {
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  .home-toc-title {
    font-family: var(--display);
    font-size: 22px;
    font-style: italic;
    font-weight: 700;
    color: var(--cream);
    line-height: 1.3;
  }

  .home-toc-meta {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.04em;
    margin-top: 0.1rem;
  }

  .home-toc-footer {
    margin-top: 0.8rem;
    text-align: right;
  }

  .home-toc-view-all {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--gold);
    text-decoration: none;
    border-bottom: 1px solid var(--gold-dim);
    padding-bottom: 2px;
    transition: border-color 0.2s;
  }

  .home-toc-view-all:hover {
    border-color: var(--gold);
  }

  .home-month-empty {
    padding: 1.5rem 0;
    font-family: var(--text);
    font-size: 13px;
    font-style: italic;
    color: var(--mid);
    text-align: center;
  }

  .home-project-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
  }

  /* ─── Homepage Project Cards (Enhanced) ─── */

  .home-project-card {
    display: block;
    padding: 1rem 1rem;
    border: 1px solid var(--rule);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.25s ease;
    background: rgba(255, 255, 255, 0.01);
    text-decoration: none;
  }

  .home-project-card:hover {
    border-color: var(--gold-dim);
    background: rgba(255, 255, 255, 0.03);
    transform: translateY(-3px);
  }

  .home-project-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.3rem;
  }

  .home-project-id {
    font-family: var(--mono);
    font-size: 7px;
    color: var(--ash);
    letter-spacing: 0.05em;
  }



  /* ─── Project Elements ─── */
  .home-project-title {
    font-family: var(--display);
    font-size: clamp(20px, 1.4vw, 26px);
    font-style: italic;
    text-transform: uppercase;
    font-weight: 700;
    color: var(--cream);
    margin: 0 0 0.2rem 0;
    line-height: 1.3;
  }

  .home-project-authors {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 0.03em;
    margin-bottom: 0.3rem;
  }

  .home-project-abstract {
    font-family: var(--text);
    font-size: 14px;
    font-style: italic;
    color: var(--pale);
    line-height: 1.6;
    margin: 0 0 0.5rem 0;
    opacity: 0.7;
  }

  .home-project-meta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.4rem 0.6rem;
    font-family: var(--mono);
    font-size: 10px;
    color: var(--ash);
    letter-spacing: 0.04em;
    margin-top: 0.2rem;
    padding-top: 0.4rem;
    border-top: 1px solid var(--rule);
  }

  .meta-number {
    color: var(--cream);
    font-weight: 700;
  }

  .home-project-total {
    color: var(--muted);
  }

  .home-project-tags {
    display: flex;
    gap: 0.2rem;
    flex-wrap: wrap;
    margin-left: auto;
  }

  .home-project-tag {
    background: var(--void2);
    border: 1px solid var(--rule);
    padding: 0.05rem 0.3rem;
    border-radius: 2px;
    color: var(--muted);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .home-project-tag-more {
    font-size: 5.5px;
    color: var(--ash);
  }

  
  /* ─── COHORT / CONTRIBUTORS SCROLL ─── */

  .home-cohort-wrapper {
    margin: 2.5rem 0 1rem 0;
    width: 100%;
    position: relative;
  }

  .home-cohort-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.8rem;
    padding: 0 1.5rem;
    border-bottom: 1px solid var(--rule);
    padding-bottom: 0.4rem;
  }

  .home-cohort-header .home-section-title {
    margin-top: 0;
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
  }

  .home-cohort-count {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--ash);
    letter-spacing: 0.04em;
  }

  /* ─── Wrapper handles the full-width bleed ─── */
  .home-contributors-scroll-wrapper {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    padding: 0;
    overflow: hidden;
    background: var(--void);
  }

  .home-contributors-scroll {
    display: flex;
    gap: 1.5rem;
    padding: 0.5rem 1.5rem 1.5rem 1.5rem;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: thin;
    width: 100%;
    margin: 0;
    box-sizing: border-box;
  }

  /* ─── Scrollbar Styling ─── */
  .home-contributors-scroll::-webkit-scrollbar {
    height: 4px;
  }

  .home-contributors-scroll::-webkit-scrollbar-track {
    background: var(--void2);
    border-radius: 2px;
  }

  .home-contributors-scroll::-webkit-scrollbar-thumb {
    background: var(--ash);
    border-radius: 2px;
  }

  .home-contributors-scroll::-webkit-scrollbar-thumb:hover {
    background: var(--gold-dim);
  }

  /* ─── Cards ─── */
  .home-contributor-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: inherit;
    flex: 0 0 auto;
    min-width: 80px;
    scroll-snap-align: start;
    transition: all 0.2s ease;
    padding: 0.5rem;
    border-radius: 6px;
  }

  .home-contributor-card:hover {
    background: rgba(255, 255, 255, 0.03);
    transform: translateY(-2px);
  }

  .home-contributor-card:active {
    transform: scale(0.98);
  }

  .home-contributor-avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: var(--void2);
    border: 2px solid var(--rule);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    margin-bottom: 0.5rem;
    transition: border-color 0.2s ease;
    flex-shrink: 0;
  }

  .home-contributor-card:hover .home-contributor-avatar {
    border-color: var(--gold-dim);
  }

  .home-contributor-avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .home-contributor-initial {
    font-family: var(--display);
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--muted);
  }

  .home-contributor-name {
    font-family: var(--text);
    font-size: 13px;
    font-style: italic;
    color: var(--pale);
    text-align: center;
    line-height: 1.3;
    margin-bottom: 0.1rem;
  }

  .home-contributor-role {
    font-family: var(--mono);
    font-size: 9px;
    color: var(--ash);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    text-align: center;
    opacity: 0.7;
  }

  /* ─── Contributor Discipline ─── */
  .home-contributor-discipline {
    display: block;
    font-family: var(--mono);
    font-size: 8px;
    color: var(--ash);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    text-align: center;
    margin-top: 0.1rem;
    opacity: 0.5;
    max-width: 76px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* ─── Responsive ─── */

  /* Tablet */
  @media (max-width: 768px) {
    .home-cohort-header {
      padding: 0 1.5rem;
    }
    
    .home-contributors-scroll {
      gap: 1.25rem;
      padding: 0.5rem 1.5rem 1.5rem 1.5rem;
    }
    
    .home-contributor-avatar {
      width: 56px;
      height: 56px;
    }
    
    .home-contributor-card {
      min-width: 72px;
    }
    
    .home-contributor-name {
      font-size: 10px;
    }
    
    .home-contributor-role {
      font-size: 7px;
    }
  }

  /* Mobile */
  @media (max-width: 480px) {
    .home-cohort-header {
      padding: 0 1rem;
    }
    
    .home-contributors-scroll-wrapper {
      width: 100vw;
      left: 50%;
      right: 50%;
      margin-left: -50vw;
      margin-right: -50vw;
    }
    
    .home-contributors-scroll {
      gap: 1rem;
      padding: 0.5rem 1rem 1.5rem 1rem;
    }
    
    .home-contributor-avatar {
      width: 48px;
      height: 48px;
      border-width: 1.5px;
    }
    
    .home-contributor-card {
      min-width: 64px;
    }
    
    .home-contributor-initial {
      font-size: 1.2rem;
    }
    
    .home-contributor-name {
      font-size: 9px;
    }
    
    .home-contributor-role {
      font-size: 6px;
    }
    
    .home-contributor-discipline {
      font-size: 5px;
      max-width: 56px;
    }
  }

  /* ─── Small screens ─── */
  @media (max-width: 380px) {
    .home-contributor-avatar {
      width: 40px;
      height: 40px;
    }
    
    .home-contributor-card {
      min-width: 56px;
    }
    
    .home-contributors-scroll {
      gap: 0.75rem;
      padding: 0.5rem 0.75rem 1.5rem 0.75rem;
    }
    
    .home-contributor-discipline {
      max-width: 44px;
      font-size: 4.5px;
    }
  }

  /* ─── Touch device optimizations ─── */
  @media (hover: none) {
    .home-contributor-card:hover {
      background: transparent;
      transform: none;
    }
    
    .home-contributor-card:hover .home-contributor-avatar {
      border-color: var(--rule);
    }
  }

  .home-stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    padding: 1rem 0;
  }

  .home-stat {
    text-align: center;
    padding: 0.75rem;
    border: 1px solid var(--rule);
    border-radius: 4px;
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

  .home-about-text {
    font-family: var(--text);
    font-size: 15px;
    font-style: italic;
    color: var(--pale);
    line-height: 1.8;
    max-width: 600px;
    margin-bottom: 0.8rem;
  }

  .home-about-link {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--gold);
    text-decoration: none;
    border-bottom: 1px solid var(--gold-dim);
    padding-bottom: 2px;
    transition: border-color 0.2s;
  }

  .home-about-link:hover {
    border-color: var(--gold);
  }

  .home-empty-card {
    opacity: 0.5;
    cursor: default;
    grid-column: 1/-1;
    text-align: center;
    padding: 2rem 0;
  }

  .home-empty-text {
    color: var(--mid);
    font-style: normal;
    font-family: var(--text);
    font-size: 13px;
  }

  @media (max-width: 768px) {
    .home-hero {
      padding: 0 1.5rem;
    }

    .home-left {
      padding: 1.5rem 0 2rem !important;
    }

    .home-title {
      font-size: clamp(32px, 6vw, 48px) !important;
    }

    .home-manifesto {
      font-size: clamp(14px, 2vw, 18px);
    }

    .home-cta {
      font-size: 8px;
      padding: 0.4rem 1rem;
    }

    .home-toc-item {
      padding: 0.5rem 0.6rem;
      gap: 0.75rem;
    }

    .home-toc-number {
      font-size: 10px;
      min-width: 28px;
    }

    .home-toc-title {
      font-size: 13px;
    }

    .home-project-grid {
      grid-template-columns: 1fr 1fr;
    }

    .home-stats-grid {
      grid-template-columns: repeat(3, 1fr);
      gap: 0.5rem;
    }

    .home-stat-number {
      font-size: clamp(20px, 4vw, 28px);
    }

    .home-stat {
      padding: 0.5rem;
    }
  }

  @media (max-width: 480px) {
    .home-hero {
      padding: 0 1rem;
    }

    .home-left {
      padding: 1rem 0 1.5rem !important;
    }

    .home-title {
      font-size: clamp(24px, 5vw, 32px) !important;
    }

    .home-toc-item {
      flex-wrap: wrap;
      gap: 0.3rem;
    }

    .home-toc-number {
      font-size: 9px;
      min-width: 24px;
    }

    .home-toc-title {
      font-size: 12px;
    }

    .home-toc-meta {
      font-size: 7px;
    }

    .home-project-grid {
      grid-template-columns: 1fr;
    }

    .home-stats-grid {
      grid-template-columns: 1fr 1fr 1fr;
      gap: 0.3rem;
    }

    .home-stat-number {
      font-size: clamp(18px, 5vw, 24px);
    }

    .home-stat-label {
      font-size: 6px;
    }

    .home-ctas {
      flex-direction: column;
    }

    .home-cta {
      text-align: center;
    }

    .home-contributors-scroll {
      gap: 0.75rem;
    }

    .home-contributor-card {
      min-width: 56px;
    }

    .home-contributor-avatar {
      width: 40px;
      height: 40px;
    }
  }
  /* ─── TOC Metrics ─── */
.home-toc-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.6rem 0.8rem;
  border-radius: 4px;
  text-decoration: none;
  color: inherit;
  transition: background 0.2s;
  border-bottom: 1px solid var(--rule);
}

.home-toc-metrics {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  flex-shrink: 0;
  gap: 0.05rem;
}

.home-toc-words {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--ash);
  letter-spacing: 0.04em;
}

.home-toc-time {
  font-family: var(--mono);
  font-size: 9px;
  color: var(--ash);
  letter-spacing: 0.04em;
  opacity: 0.6;
}
</style>