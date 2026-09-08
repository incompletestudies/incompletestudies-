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

  <div class="list-container" style="padding: 0 var(--gutter);">
    {% assign sorted_posts = site.posts | sort: "date" | reverse %}
    
    {% if sorted_posts.size == 0 %}
      <div class="empty-state">
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
          
          <div class="month-divider text-display font-extrabold text-italic text-fixed-xl">
            {{ post_month }}
            
            <span class="section-meta">
              {{ month_count }} installment{% if month_count > 1 %}s{% endif %}
            </span>
          </div>

          
        {% endif %}
        
        <div class="list-item" style="align-items: flex-start; padding: 1.5rem 0; border-bottom: 1px solid var(--rule); gap: 2rem;">
          
          <!-- ─── LEFT COLUMN (sticky) ─── -->
          <div class="list-item-left" style="min-width: 60px; display: flex; flex-direction: column; align-items: flex-start; gap: 0.3rem; position: sticky; top: 80px; align-self: start;">
            <span class="text-display" style="font-size: 24px; font-weight: 900; font-style: italic; color: var(--void3); line-height: 1; letter-spacing: -0.02em;">
              {{ post.date | date: "%b" }}
            </span>
            <span class="text-mono" style="font-size: 8px; color: var(--ash); letter-spacing: 0.1em;">
              {{ post.date | date: "%Y" }}
            </span>
            {% if post.badge %}
              {% assign badge_class = post.badge | downcase | replace: ' ', '-' %}
              {% if badge_class == "first-inst." %}
                {% assign badge_class = "first" %}
              {% elsif badge_class == "last-inst." %}
                {% assign badge_class = "last" %}
              {% endif %}
              <span class="badge {{ badge_class }}" style="font-size: 7px; padding: 0.05rem 0.25rem; letter-spacing: 0.04em;">
                {{ post.badge }}
              </span>
            {% endif %}
          </div>
          
          <!-- ─── CONTENT ─── -->
          <div class="list-item-content">
            
            <!-- ─── TOP ROW: Installment + Info ─── -->
            <div class="flex flex-wrap" style="gap: 0.5rem; margin-bottom: 0.3rem; align-items: baseline; justify-content: space-between;">
              <div class="text-mono" style="font-size: 8px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--gold-dim); margin-bottom: 0;">
                {% if post.installment %}
                  {% assign inst_num = post.installment | plus: 0 %}
                  Inst. {% if inst_num < 10 %}0{% endif %}{{ inst_num }}
                {% else %}
                  Inst. ?
                {% endif %}
                <span class="text-ash" style="font-weight: 300; margin: 0 0.25rem;">·</span>
                {{ post.date | date: "%B %d, %Y" }}
              </div>
              
              <div class="metrics-horizontal" style="flex-shrink: 0;">
                <span class="metric metric-words">{{ word_count }} words</span>
                <span class="metric metric-sep">·</span>
                <span class="metric metric-time">~{{ reading_time }} min read</span>
              </div>
            </div>
            
            <span class="list-item-title" >
              <a href="{{ site.baseurl }}{{ post.url }}" class="link-scale text-fluid-2xl">{{ post.title }}</a>
            </span>
            
            
            <div class="flex flex-wrap" style="gap: 0.5rem; margin-bottom: 0.6rem; align-items: center;">
              
              {% if project %}
                <span class="text-mono" style="font-size: 8px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--mid);">
                  <a href="{{ site.baseurl }}/projects/{{ project.slug }}/" class="link-underline" style="color: var(--mid);">
                    {{ project.title }}
                  </a>
                </span>
              {% else %}
                <span class="text-mono" style="font-size: 8px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--mid);">
                  {% if post.projects %}{{ post.projects | first }}{% else %}Uncategorized{% endif %}
                </span>
              {% endif %}

              <span class="text-ash">·</span>
              
              {% if post.authors and post.authors.size > 0 %}
                <span class="text-mono" style="font-size: 9px; color: var(--muted);">
                  {% for slug in post.authors %}
                    {% assign person = site.people | where: "slug", slug | first %}
                    {% if person %}
                      <a href="{{ site.baseurl }}/authors/{{ person.slug }}/" class="link-underline" style="color: var(--muted);">
                        {{ person.name | default: person.title }}
                      </a>{% unless forloop.last %}<span class="text-ash"> + </span>{% endunless %}
                    {% else %}
                      <span class="text-muted">{{ slug }}</span>{% unless forloop.last %}<span class="text-ash">, </span>{% endunless %}
                    {% endif %}
                  {% endfor %}
                </span>
              {% else %}
                <span class="text-mono" style="font-size: 9px; color: var(--ash);">Anonymous</span>
              {% endif %}
            </div>
            
            
            <div class="list-item-meta text-text text-fluid-sm  " >
              {{ post.content | strip_html | truncatewords: 50 }}
            </div>

          </div>
        </div>
      {% endfor %}
    {% endif %}
  </div>
</div>