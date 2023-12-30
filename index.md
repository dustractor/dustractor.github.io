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

[random neat sites](/neatsites.html)

[VKAL](/vkal.html) Vsts I have known and loved

[YTSUBS](/ytsubs.html) I scraped my youtube subscriptions

[Binned Polymaths 7](/binnedpolymaths7.html) A fucked up dream about a cult
