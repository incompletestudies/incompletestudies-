---
layout: page
title: Our Authors
permalink: /authors/
---

All authors on this research project:

{% for person in site.people %}
  * <a href="{{ site.baseurl }}{{ person.url }}">{{ person.name }}</a>
{% endfor %}