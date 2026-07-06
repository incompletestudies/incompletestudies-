---
layout: default
title: Seasons
permalink: /seasons/
---

Each seasonal cycle is archived as a distinct object — a record of the projects, contributors, and completed arcs that defined that period.

---

## Season 01 · Autumn 2024 → Spring 2026 (Currently Active)

**First form, first season**

**Contributors:**
{% assign season_authors = "" | split: "" %}
{% for post in site.posts %}
  {% assign post_year = post.date | date: "%Y" %}
  {% if post_year == "2024" or post_year == "2025" %}
    {% if post.author %}
      {% assign season_authors = season_authors | push: post.author %}
    {% endif %}
  {% endif %}
{% endfor %}
{% assign unique_authors = season_authors | uniq %}
{{ unique_authors | join: " · " }}

**Installments in Season 01:**
<ul>
{% for post in site.posts %}
  {% assign post_year = post.date | date: "%Y" %}
  {% if post_year == "2024" or post_year == "2025" %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      ({{ post.date | date: "%B %d, %Y" }})
      {% if post.author %}by {{ post.author }}{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

---

## Season 02 · Opens Spring 2026

**Call opens: March 2026**
Projects to be selected. [Apply →]({{ site.baseurl }}/contributors/)

---

## About the Seasons

Each season runs for approximately 6 months. Contributors publish monthly installments, and projects develop over time. At the end of a season, projects may:
- **Continue** into the next season
- **Conclude** and be archived
- **Become a book** through Second Form Editions