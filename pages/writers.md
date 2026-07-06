---
layout: default
title: Authors
permalink: /authors/
---
<div class="section-wrap">
  <div class="col-head">
    <span class="col-head-title">Authors</span>
    <span class="col-head-meta">Contributors to the archive · {{ site.people | size }} total</span>
  </div>
  <div class="cr-body">
    <ul class="cr-list">
      {% for person in site.people %}
        {% assign author_posts = site.posts | where: "author", person.slug %}
        <li><a href="{{ site.baseurl }}{{ person.url }}" style="color:inherit">{{ person.title }}</a> — {{ person.role }}, {{ person.discipline | downcase }} ({{ author_posts.size }} installments)</li>
      {% endfor %}
    </ul>
  </div>
</div>
