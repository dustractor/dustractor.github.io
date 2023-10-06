---
layout: default
title: Theoretically this is like my 'home' page or something
---

<video autoplay muted loop>
<source src="/img/handshands_small.webm" type="video/webm">
</video>

### Posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>


[VKAL](/vkal.html)

[YTSUBS](/ytsubs.html)
