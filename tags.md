---
layout: default
title: Поиск по тегам
---

<style>
    .tags-cloud {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 30px;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 8px;
    }
    .tag-link {
        padding: 5px 12px;
        background: var(--card-tech);
        color: white !important;
        border-radius: 15px;
        text-decoration: none;
        font-size: 0.9rem;
    }
    .tag-link:hover { opacity: 0.8; }
    
    .tag-group { margin-bottom: 40px; }
    .tag-group h2 { 
        border-bottom: 2px solid var(--card-tech); 
        padding-bottom: 5px;
        color: var(--card-tech);
    }
    .tagged-posts { list-style: none; padding: 0; }
    .tagged-posts li { margin: 10px 0; }
    .tagged-posts a { text-decoration: none; color: #333; font-weight: 500; }
    .tagged-posts a:hover { color: var(--card-tech); }
</style>

<!-- 1. Облако тегов (список всех тегов вверху) -->
<div class="tags-cloud">
    {% assign tags = site.tags | sort %}
    {% for tag in tags %}
        <a href="#{{ tag[0] | slugify }}" class="tag-link">#{{ tag[0] }} ({{ tag[1].size }})</a>
    {% endfor %}
</div>

<!-- 2. Списки статей по каждому тегу -->
<div class="tags-lists">
    {% for tag in tags %}
        <div class="tag-group" id="{{ tag[0] | slugify }}">
            <h2>#{{ tag[0] }}</h2>
            <ul class="tagged-posts">
                {% for post in tag[1] %}
                    <li>
                        <a href="{{ post.url }}">{{ post.title }}</a>
                        <span style="color: #999; font-size: 0.8rem; margin-left: 10px;">{{ post.date | date: "%d.%m.%Y" }}</span>
                    </li>
                {% endfor %}
            </ul>
        </div>
    {% endfor %}
</div>
