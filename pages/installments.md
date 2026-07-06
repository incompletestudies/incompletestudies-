---
layout: default
title: Installments
permalink: /installments/
---
<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Installments</span>
    <span class="col-head-meta">All published · Reverse-chronological · Season 01</span>
  </div>
  <div class="feed-wrap" style="padding-bottom:4rem">
    {% assign sorted_posts = site.posts | sort: "date" | reverse %}
    {% for post in sorted_posts %}
      {% assign project = site.projects | where: "slug", post.project | first %}
      {% assign author = site.people | where: "slug", post.author | first %}
      <div class="feed-entry">
        <div class="feed-date-col">
          <div class="feed-month">{{ post.date | date: "%b" }}</div>
          <div class="feed-year">{{ post.date | date: "%Y" }}</div>
        </div>
        <div>
          <div class="feed-inst-tag">{{ project.id }} · Inst. {% if post.installment < 10 %}0{% endif %}{{ post.installment }}</div>
          <div class="feed-proj-tag">
            <a href="{{ site.baseurl }}/projects/{{ project.slug }}/" style="color:inherit">{{ project.title }}</a>
          </div>
          <div class="feed-title">
            <a href="{{ site.baseurl }}{{ post.url }}" style="color:inherit">{{ post.title }}</a>
          </div>
          <div class="feed-author">
            {% if author %}<a href="{{ site.baseurl }}/authors/{{ author.slug }}/" style="color:inherit">{{ author.title }}</a>{% endif %}
          </div>
          <div class="feed-excerpt">{{ post.excerpt }}</div>
          {% if post.badge %}
            <div style="margin-top:0.8rem"><span class="pill {{ post.badge_class }}">{{ post.badge }}</span></div>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
