---
layout: default
title: Учебные проекты
---

<style>
    /* Используем ту же сетку и карточки, что и на главной */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 25px;
        width: 100%;
    }

    .category-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-top: 8px solid;
    }
    
    /* Цвета для разных направлений */
    .cat-electronics { border-top-color: #3498db; }
    .cat-radio { border-top-color: #e67e22; }
    .cat-computing { border-top-color: #2ecc71; }
    .cat-cybernetics { border-top-color: #9b59b6; }

    .card-header { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }
    
    .section-icon { 
        width: 50px; height: 50px; 
        border-radius: 50%; object-fit: cover; 
    }

    .project-list { list-style: none; padding: 0; margin: 0; }
    .project-list li { margin-bottom: 10px; }
    
    .project-list a {
        text-decoration: none;
        color: #555;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 12px;
        border-radius: 8px;
        background: #f9f9f9;
        font-size: 0.95rem;
    }

    .project-list a:hover {
        background: #fff;
        color: #000;
        border: 1px solid #ddd;
    }

    .level-tag {
        font-size: 0.75rem;
        background: #eee;
        padding: 2px 6px;
        border-radius: 4px;
        color: #666;
    }
</style>

В этом разделе представлены пошаговые проекты, разделенные по направлениям и уровням сложности.

<div class="grid-container">

    <!-- КАРТОЧКА: ЭЛЕКТРОНИКА -->
    <section class="category-card cat-electronics">
        <div class="card-header">
            <img src="/img/icons/electronics.png" class="section-icon">
            <h3>Электроника</h3>
        </div>
        <ul class="project-list">
            <li><a href="led-flashlight/"><span>💡 Фонарик</span> <small class="level-tag">Ур. 1</small></a></li>
            <li><a href="multivibrator/"><span>🚨 Мультивибратор</span> <small class="level-tag">Ур. 2</small></a></li>
        </ul>
    </section>

    <!-- КАРТОЧКА: РАДИОТЕХНИКА -->
    <section class="category-card cat-radio">
        <div class="card-header">
            <img src="/img/icons/radio.png" class="section-icon">
            <h3>Радио</h3>
        </div>
        <ul class="project-list">
            <li><a href="detector-radio/"><span>📻 Детекторный приемник</span> <small class="level-tag">Ур. 3</small></a></li>
        </ul>
    </section>

    <!-- КАРТОЧКА: ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА -->
    <section class="category-card cat-computing">
        <div class="card-header">
            <img src="/img/icons/computing.png" class="section-icon">
            <h3>Информатика</h3>
        </div>
        <ul class="project-list">
            <li><a href="binary-calc/"><span>🔢 Бинарный сумматор</span> <small class="level-tag">Ур. 4</small></a></li>
        </ul>
    </section>

</div>
