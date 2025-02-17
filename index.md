---
layout: default
title: "Home"
pagination: true
permalink: /
---

<div class="header-container">
    <nav class="navbar">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/privacy">Privacy Guide</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/mirrors">Mirrors</a></li>
            <li><a href="/pgp">PGP</a></li>
        </ul>
    </nav>

    <div class="banner">
        <img src="/assets/images/banner.jpg" alt="Banner">
    </div>
</div>

<div class="content-card">
    <h1>KATIE BUCKS THE INVISIBLE FUCKS!</h1>
    <p>Spitting facts and rewriting rules | Get schooled, fool! 🖕</p>
    <a href="/blog" class="button">LATEST POSTS</a>
</div>

<h1>Latest Posts</h1>

{% for post in paginator.posts %}
  <div class="blog-post">
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
    <p>{{ post.excerpt }}</p>
  </div>
{% endfor %}

<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}">&laquo; Previous</a>
  {% endif %}

  <span>Page {{ paginator.page }} of {{ paginator.total_pages }}</span>

  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}">Next &raquo;</a>
  {% endif %}
</div>
