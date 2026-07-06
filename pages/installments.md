---
layout: default
title: Installments
permalink: /installments/
---

All published installments, in reverse chronological order.

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% for post in sorted_posts %}
### {{ post.date | date: "%B %d, %Y" }}
**{{ post.title }}**
{% if post.author %}By <a href="{{ site.baseurl }}/authors/#{{ post.author | slugify }}">{{ post.author }}</a>{% endif %}

{{ post.excerpt | default: post.content | strip_html | truncatewords: 30 }}

[Read More →]({{ site.baseurl }}{{ post.url }})

---
{% endfor %}