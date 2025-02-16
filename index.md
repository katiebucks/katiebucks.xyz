---
layout: default
title: "Home"
---

**Katie Bucks the Invisible FUCKS!**

## Latest Posts
{% for post in paginator.posts %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}

{% if paginator.total_pages > 1 %}
<div class="pagination">
    {% if paginator.previous_page %}
        <a href="{{ paginator.previous_page_path }}">&laquo; Previous</a>
    {% endif %}
    {% if paginator.next_page %}
        <a href="{{ paginator.next_page_path }}">Next &raquo;</a>
    {% endif %}
</div>
{% endif %}