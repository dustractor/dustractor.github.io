---
layout: default
title: Theoretically this is like my 'home' page or something
---

<video loop>
<source src="/img/handshands.webm" type="video/webm">
</video>

![hands](/img/handshands.webm)

### Posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

