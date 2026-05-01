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

<a href="materialy-dlya-samostoyatelnogo-izucheniya-osnov-elektroniki.html" class="compact-card">
    <img src="img/materialy-dlya-samostoyatelnogo-izucheniya-osnov-elektroniki.webp" class="compact-img">
    <div class="compact-info">
        <h3>Материалы для изучения основ электроники</h3>
        <span class="compact-author">Автор</span>
        <p class="compact-desc">Первоначальный материал для самостоятельного изучения основ электроники детьми 8-16 лет.</p>
    </div>
</a>

<a href="chernenko-g-t-puteshestvie-v-stranu-robotov-1977.html" class="compact-card">
    <img src="img/chernenko-g-t-puteshestvie-v-stranu-robotov-1977.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книги по автоматике и робототехнике</h3>
        <span class="compact-author">Черненко Г.Т.</span>
        <p class="compact-desc">Введение в автоматику и робототехнику. Первые шаги в изучении механизмов и систем управления.</p>
    </div>
</a>

<a href="kiselyov-l-kniga-yunogo-tekhnika-1948.html" class="compact-card">
    <img src="img/kiselyov-l-kniga-yunogo-tekhnika-2025.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книга юного техника</h3>
        <span class="compact-author">Киселёв Л.</span>
        <p class="compact-desc">Практическое руководство по техническому творчеству. Обучает основам работы с материалами.</p>
    </div>
</a>

<a href="svoren-r-a-elektronika-shag-za-shagom-1991.html" class="compact-card">
    <img src="img/svoren-r-a-elektronika-shag-za-step-1991.webp" class="compact-img">
    <div class="compact-info">
        <h3>Электроника шаг за шагом</h3>
        <span class="compact-author">Сворень Р.А.</span>
        <p class="compact-desc">Фундаментальный курс практической электроники — от принципа работы до сложных систем.</p>
    </div>
</a>

<a href="borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.html" class="compact-card">
    <img src="img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.webp" class="compact-img">
    <div class="compact-info">
        <h3>Энциклопедия юного радиолюбителя</h3>
        <span class="compact-author">Борисов В.Г.</span>
        <p class="compact-desc">Фундаментальные знания о радиосвязи и принципах работы электронных устройств.</p>
    </div>
</a>

<a href="pchyolko-a-s-arifmetika-dlya-nachalnoj-shkoly-1955.html" class="compact-card">
    <img src="img/pchyolko-a-s-arifmetika-dlya-pervogo-klassa-nachalnoj-shkoly-2022.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книги по математике (арифметика)</h3>
        <span class="compact-author">Пчёлко А.С., Попова Н.С. и др.</span>
        <p class="compact-desc">Фундаментальная база для инженерных расчетов. Советские учебники по арифметике.</p>
    </div>
</a>

<a href="zak-a-z-intellektika-2024.html" class="compact-card">
    <img src="img/zak-a-z-intellektika-1-klass-2024.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книги для развития мышления</h3>
        <span class="compact-author">Зак А.З.</span>
        <p class="compact-desc">Курс развития мыслительных способностей. Задачи на выработку навыков анализа.</p>
    </div>
</a>

<a href="rostovcev-n-n-risovanie-1957.html" class="compact-card">
    <img src="img/rostovcev-n-n-risovanie-1-klass-1957.webp" class="compact-img">
    <div class="compact-info">
        <h3>Книги по рисованию</h3>
        <span class="compact-author">Ростовцев Н.Н.</span>
        <p class="compact-desc">Основа визуализации и пространственного мышления. База для зарисовки схем и чертежей.</p>
    </div>
</a>

</div>
