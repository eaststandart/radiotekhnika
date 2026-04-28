---
layout: default
title: Поиск по тегам
---

<div class="tags-page">
    <div class="tags-cloud" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
        {% assign tags = site.tags | sort %}
        {% for tag in tags %}
            <a href="#{{ tag[0] | slugify }}" style="padding: 5px 12px; background: #3498db; color: white; border-radius: 15px; text-decoration: none; font-size: 0.9rem;">#{{ tag[0] }} ({{ tag[1].size }})</a>
        {% endfor %}
    </div>

    <div class="tags-lists">
        {% for tag in tags %}
            <div class="tag-group" id="{{ tag[0] | slugify }}" style="margin-bottom: 40px; border-bottom: 1px solid #eee; padding-bottom: 20px;">
                <h2 style="color: #2c3e50; margin-bottom: 15px;">#{{ tag[0] }}</h2>
                <ul style="list-style: none; padding: 0;">
                    {% for post in tag[1] %}
                        <li style="margin: 10px 0;">
                            <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #3498db; font-weight: 500; font-size: 1.1rem;">{{ post.title }}</a>
                            {% if post.date %}
                            <span style="color: #999; font-size: 0.85rem; margin-left: 10px;">{{ post.date | date: "%d.%m.%Y" }}</span>
                            {% endif %}
                        </li>
                    {% endfor %}
                </ul>
            </div>
        {% endfor %}
    </div>
</div>
