---
layout: default
title: Поиск по тегам
---

<div class="tags-cloud" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px;">
  {% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
  {% assign tag_words = site_tags | split: ',' | sort %}

  {% for item in tag_words %}
    <a href="#{{ item | slugify }}" class="tag-item">#{{ item }}</a>
  {% endfor %}
</div>

<hr>

<div class="tags-lists">
  {% for item in tag_words %}
    <div class="tag-group" id="{{ item | slugify }}" style="margin-bottom: 30px;">
      <h2 style="color: var(--card-tech); border-bottom: 1px solid #eee;">#{{ item }}</h2>
      <ul style="list-style: none; padding-left: 10px;">
        {% for post in site.tags[item] %}
          <li style="margin-bottom: 10px;">
            <a href="{{ post.url | relative_url }}" style="text-decoration: none; font-weight: 500;">{{ post.title }}</a>
            <small style="color: #999; margin-left: 10px;">{{ post.date | date: "%d.%m.%Y" }}</small>
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>
