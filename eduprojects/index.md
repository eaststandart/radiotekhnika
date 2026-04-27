---
layout: default
title: Учебные проекты
---

<style>
    /* Компактные карточки специально для сетки проектов */
    .project-grid-card {
        background: white;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-decoration: none;
        color: inherit;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        transition: transform 0.2s;
        border: 1px solid #eee;
    }
    .project-grid-card:hover { transform: translateY(-5px); border-color: var(--card-tech); }
    
    .project-grid-card img {
        width: 80px;
        height: 80px;
        object-fit: cover;
        border-radius: 50%;
        margin-bottom: 10px;
    }
    
    .project-grid-card h3 { margin: 5px 0; font-size: 1.1rem; color: var(--card-tech); }
    .project-grid-card .level { font-size: 0.8rem; color: #7f8c8d; font-weight: bold; }
</style>

## ⚡ Электроника
<div class="grid-container" style="margin-bottom: 40px;">
    
    <a href="led-flashlight/" class="project-grid-card">
        <img src="led-flashlight/img/preview.jpg" alt="⚡">
        <span class="level">Уровень 1</span>
        <h3>Фонарик</h3>
    </a>

    <a href="multivibrator/" class="project-grid-card">
        <img src="multivibrator/img/preview.jpg" alt="⚡">
        <span class="level">Уровень 2</span>
        <h3>Мультивибратор</h3>
    </a>

</div>

## 📻 Радиотехника
<div class="grid-container">
    
    <a href="detector-radio/" class="project-grid-card">
        <img src="detector-radio/img/preview.jpg" alt="📻">
        <span class="level">Уровень 3</span>
        <h3>Детекторный приемник</h3>
    </a>

</div>
