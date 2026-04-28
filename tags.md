---
layout: default
title: Поиск по тегам
---

{%- assign all_pages = site.pages | concat: site.documents -%}
{%- assign raw_tags = "" -%}
{%- for p in all_pages -%}{%- if p.tags -%}{%- for t in p.tags -%}{%- assign raw_tags = raw_tags | append: t | append: "|" -%}{%- endfor -%}{%- endif -%}{%- endfor -%}
{%- assign unique_tags = raw_tags | split: "|" | uniq | sort -%}

<div class="tags-page">
    <!-- 1. Облако тегов -->
    <div id="tags-cloud" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
        {% for tag in unique_tags %}
            <a href="#{{ tag | slugify }}" class="tag-btn" onclick="filterTag('{{ tag | slugify }}')" style="padding: 5px 12px; background: #3498db; color: white; border-radius: 15px; text-decoration: none; font-size: 0.9rem;">#{{ tag }}</a>
        {% endfor %}
    </div>

    <div id="active-tag-name" style="margin-bottom: 20px; font-weight: bold; color: #2c3e50; font-size: 1.2rem; display: none;">
        Статьи по тегу: <span id="tag-label" style="color: #3498db;"></span>
        <a href="javascript:void(0)" onclick="resetFilter()" style="font-size: 0.8rem; margin-left: 15px; color: #999;">(показать все)</a>
    </div>

    <!-- 2. Списки страниц (скрыты по умолчанию) -->
    <div class="tags-lists">
        {% for tag in unique_tags %}
            <div class="tag-group" id="{{ tag | slugify }}" style="display: none; margin-bottom: 40px; border-bottom: 1px solid #eee; padding-bottom: 20px;">
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

<script>
function filterTag(tagSlug) {
    // Скрываем все группы
    const groups = document.querySelectorAll('.tag-group');
    groups.forEach(g => g.style.display = 'none');

    // Показываем нужную
    const target = document.getElementById(tagSlug);
    if (target) {
        target.style.display = 'block';
        document.getElementById('active-tag-name').style.display = 'block';
        document.getElementById('tag-label').innerText = '#' + tagSlug;
        window.scrollTo({top: document.getElementById('tags-cloud').offsetHeight, behavior: 'smooth'});
    }
}

function resetFilter() {
    const groups = document.querySelectorAll('.tag-group');
    groups.forEach(g => g.style.display = 'block');
    document.getElementById('active-tag-name').style.display = 'none';
}

// Если перешли по ссылке с якорем (например, tags.html#borisov)
window.addEventListener('load', () => {
    const hash = window.location.hash.substring(1);
    if (hash) {
        filterTag(decodeURIComponent(hash));
    } else {
        // По умолчанию показываем все или только облако (сейчас все группы видны)
        resetFilter(); 
    }
});
</script>
