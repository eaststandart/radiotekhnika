---
layout: default
title: Поиск по тегам
---

{%- assign all_pages = site.pages | concat: site.documents -%}
{%- assign raw_tags = "" -%}
{%- for p in all_pages -%}
    {%- if p.tags -%}
        {%- for t in p.tags -%}
            {%- assign raw_tags = raw_tags | append: t | append: "|" -%}
        {%- endfor -%}
    {%- endif -%}
{%- endfor -%}
{%- assign unique_tags = raw_tags | split: "|" | uniq | sort -%}

<div class="tags-page">
    <!-- Облако тегов -->
    <div class="tags-cloud" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
        {% for tag in unique_tags %}
            <a href="#{{ tag | slugify }}" style="padding: 5px 12px; background: #3498db; color: white; border-radius: 15px; text-decoration: none; font-size: 0.9rem;">#{{ tag }}</a>
        {% endfor %}
    </div>

    <!-- Списки страниц -->
    <div class="tags-lists">
        {% for tag in unique_tags %}
            <div class="tag-group" id="{{ tag | slugify }}" style="margin-bottom: 40px; border-bottom: 1px solid #eee; padding-bottom: 20px;">
                <h2 style="color: #2c3e50; margin-bottom: 15px;">#{{ tag }}</h2>
                <ul style="list-style: none; padding: 0;">
                    {% for p in all_pages %}
                        {% if p.tags contains tag %}
                            <li style="margin: 10px 0;">
                                <a href="{{ p.url | relative_url }}" style="text-decoration: none; color: #3498db; font-weight: 500; font-size: 1.1rem;">{{ p.title | default: p.url }}</a>
                                <span style="color: #999; font-size: 0.85rem; margin-left: 10px;">{{ p.parent_name }}</span>
                            </li>
                        {% endif %}
                    {% endfor %}
                </ul>
            </div>
        {% endfor %}
    </div>
</div>
