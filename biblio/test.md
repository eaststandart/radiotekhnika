---
layout: default
title: Тест компактного списка
---

<style>
/* Компактный контейнер списка */
.compact-list {
    display: flex;
    flex-direction: column;
    gap: 10px; /* Минимальное расстояние между книгами */
    margin: 20px 0;
}

/* Сама карточка */
.compact-card {
    display: flex;
    flex-direction: row; /* Всегда в ряд, даже на мобилках */
    align-items: flex-start;
    gap: 12px;
    background: #fff;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #eee;
    text-decoration: none;
    color: inherit;
    transition: background 0.2s;
}

.compact-card:hover {
    background: #fdfdfd;
    border-color: #ddd;
}

/* Уменьшенная обложка */
.compact-img {
    width: 60px !important;   /* Маленькая ширина */
    height: 85px !important;  /* Пропорциональная высота */
    object-fit: cover;
    border-radius: 4px;
    flex-shrink: 0;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
}

.compact-info {
    flex: 1;
    min-width: 0; /* Чтобы текст не распирал флекс */
}

.compact-info h3 {
    margin: 0 0 2px 0 !important;
    color: var(--card-tech);
    font-size: 1rem !important;
    line-height: 1.2;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis; /* Если название очень длинное — сокращаем */
}

.compact-author {
    display: block;
    font-weight: bold;
    font-size: 0.8rem;
    color: #555;
    margin-bottom: 4px;
}

.compact-desc {
    margin: 0;
    font-size: 0.75rem;
    color: #777;
    line-height: 1.3;
    /* Показываем только 2 строки описания на всех устройствах */
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Мобильная коррекция */
@media (max-width: 600px) {
    .compact-card {
        padding: 8px;
        gap: 10px;
    }
    .compact-img {
        width: 50px !important;
        height: 70px !important;
    }
}
</style>

<div class="compact-list">

<a href="#" class="compact-card">
    <img src="img/chernenko-g-t-puteshestvie-v-stranu-robotov-1977.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книги по автоматике и робототехнике</h3>
        <span class="compact-author">Черненко Г.Т.</span>
        <p class="compact-desc">Введение в автоматику и робототехнику. Первые шаги в изучении механизмов и систем управления.</p>
    </div>
</a>

<a href="#" class="compact-card">
    <img src="img/kiselyov-l-kniga-yunogo-tekhnika-2025.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книга юного техника</h3>
        <span class="compact-author">Киселёв Л.</span>
        <p class="compact-desc">Практическое руководство по техническому творчеству. Обучает основам работы с материалами.</p>
    </div>
</a>

</div>
