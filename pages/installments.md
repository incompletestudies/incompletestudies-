---
layout: default
title: Installments
permalink: /installments/
---

<div class="section-wrap">
  
  {% include breadcrumb.html %}

  <div class="col-head">
    <span class="col-head-title">Installments</span>
    <span class="col-head-meta">
      All published · Reverse-chronological · {{ site.posts | size }} total 
    </span>
  </div>

  <div class="feed-wrap">
    {% assign sorted_posts = site.posts | sort: "date" | reverse %}
    
    {% if sorted_posts.size == 0 %}
      <div style="padding: 3rem 0; font-family: var(--text); font-size: 14px; font-style: italic; color: var(--mid); text-align: center;">
        No installments published yet.
      </div>
    {% else %}
      
      {% assign current_month = "" %}
      
      {% for post in sorted_posts %}

        {% assign post_month = post.date | date: "%B %Y" %}
        
        {% comment %}─── Get project from post.projects array ───{% endcomment %}
        {% assign project_slug = post.projects | first %}
        {% assign project = site.projects | where: "slug", project_slug | first %}
        
        {% assign word_count = post.content | strip_html | number_of_words %}
        {% assign reading_time = word_count | divided_by: 200 | default: 1 %}
        
        {% comment %}─── MONTH SEPARATOR ───{% endcomment %}
        {% if post_month != current_month %}
          {% assign current_month = post_month %}
          
          {% assign month_count = 0 %}
          {% for p in sorted_posts %}
            {% assign p_month = p.date | date: "%B %Y" %}
            {% if p_month == post_month %}
              {% assign month_count = month_count | plus: 1 %}
            {% endif %}
          {% endfor %}
          
          <div class="month-divider">
            <span>{{ post_month }}</span>
            <span class="count">{{ month_count }} installment{% if month_count > 1 %}s{% endif %}</span>
          </div>
        {% endif %}
        
        <div class="feed-entry" data-project="{{ project_slug }}">
          
          <!-- ─── LEFT COLUMN (sticky) ─── -->
          <div class="feed-date-col">
            <div class="feed-month">{{ post.date | date: "%b" }}</div>
            <div class="feed-year">{{ post.date | date: "%Y" }}</div>
          </div>
          
          <!-- ─── CONTENT ─── -->
          <div>
            
            <!-- ─── TOP ROW: Installment + Info ─── -->
            <div style="display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 0.5rem; margin-bottom: 0.3rem;">
              <div class="feed-inst-tag" style="margin-bottom: 0;">
                Inst. {% if post.installment < 10 %}0{% endif %}{{ post.installment | default: "?" }}
                <span style="color: var(--ash); font-weight: 300; margin: 0 0.25rem;">·</span>
                {{ post.date | date: "%B %d, %Y" }}
              </div>
              
              <div style="font-family: var(--mono); font-size: 9px; color: var(--ash); letter-spacing: 0.05em; text-transform: uppercase; text-align: right; flex-shrink: 0;">
                <span>{{ word_count }} words</span>
                <span style="color: var(--void3); margin: 0 0.25rem;">·</span>
                <span>~{{ reading_time }} min read</span>
              </div>
            </div>
            
            <div class="feed-title">
              <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
            </div>
            
            <!-- ─── AUTHOR + PROJECT (with clickable authors) ─── -->
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; margin-bottom: 0.6rem;">
              

              {% if project %}
                <span class="feed-proj-tag" style="margin-top: 0; margin-bottom: 0;">
                  <a href="{{ site.baseurl }}/projects/{{ project.slug }}/">{{ project.title }}</a>
                </span>
              {% else %}
                <span class="feed-proj-tag" style="margin-top: 0; margin-bottom: 0; color: var(--mid);">
                  {% if post.projects %}{{ post.projects | first }}{% else %}Uncategorized{% endif %}
                </span>
              {% endif %}

              <span style="color: var(--ash);">·</span>
              
              {% if post.authors and post.authors.size > 0 %}
                <span class="feed-author" style="margin-bottom: 0;">
                  {% for slug in post.authors %}
                    {% assign person = site.people | where: "slug", slug | first %}
                    {% if person %}
                      <a href="{{ site.baseurl }}/authors/{{ person.slug }}/" style="color: var(--muted); text-decoration: none; border-bottom: 1px solid transparent; transition: border-color 0.2s, color 0.2s;">
                        {{ person.name | default: person.title }}
                      </a>{% unless forloop.last %}+ {% endunless %}
                    {% else %}
                      <span style="color: var(--muted);">{{ slug }}</span>{% unless forloop.last %}, {% endunless %}
                    {% endif %}
                  {% endfor %}
                </span>
              {% else %}
                <span class="feed-author" style="margin-bottom: 0; color: var(--ash);">Anonymous</span>
              {% endif %}


            </div>
            
            <div class="feed-excerpt">
              {{ post.excerpt | strip_html | truncatewords: 25 }}
            </div>
            
            {% if post.badge %}
              {% assign badge_class = post.badge | downcase | replace: ' ', '-' %}
          
              {% comment %}─── Fix for "First Inst." and "Last Inst." ───{% endcomment %}

              {% if badge_class == "first-inst." %}  <!-- Note the period -->
                {% assign badge_class = "first" %}
              {% elsif badge_class == "last-inst." %}  <!-- Note the period -->
                {% assign badge_class = "last" %}
              {% endif %}

              
              <span class="installment-badge {{ badge_class }}">
                {{ post.badge }}
              </span>
              
            {% endif %}

            
            
          </div>
        </div>
      {% endfor %}
    {% endif %}
  </div>
</div>





<style>
  /* ─── Installment Status ─── */
  .installment-badge {
    display: inline-block;
    font-family: var(--mono);
    font-size: 8px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 0.1rem 0.4rem;
    border-radius: 2px;
  }

  /* ─── First Inst. ─── */
  .installment-badge.first {
    color: #64B5F6;
    background: rgba(100, 181, 246, 0.08);
    border: 1px solid rgba(100, 181, 246, 0.2);
  }

  /* ─── Revised ─── */
  .installment-badge.revised {
    color: #CE93D8;
    background: rgba(206, 147, 216, 0.08);
    border: 1px solid rgba(206, 147, 216, 0.2);
  }

  /* ─── Last Inst. ─── */
  .installment-badge.last {
    color: #FF8A65;
    background: rgba(255, 138, 101, 0.08);
    border: 1px solid rgba(255, 138, 101, 0.2);
  }

</style>