---
layout: default
title: Our Authors
permalink: /authors/
---

All authors on this research project:

{% for person in site.people %}
  * <a href="{{ site.baseurl }}{{ person.url }}">{{ person.name }}</a>
  {% assign author_posts = site.posts | where: "author", person.name %}
  ({{ author_posts | size }} installments)
{% endfor %}

---

## Posts by Author

{% for person in site.people %}
### {{ person.name }}

{{ person.content | markdownify }}

**Installments by {{ person.name }}:**
<ul>
{% for post in site.posts %}
  {% if post.author == person.name %}
    <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> ({{ post.date | date: "%B %d, %Y" }})</li>
  {% endif %}
{% endfor %}
</ul>

---
{% endfor %}