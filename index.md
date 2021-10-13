---
layout: default
title: so is this like my blog or something
---

hey blah
===

hello world.

---

### Posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

