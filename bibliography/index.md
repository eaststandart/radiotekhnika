---
layout: default
title: Рекомендуемая литература
---

<style>
    .book-card {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 15px;            /* Уменьшили зазор между картинкой и текстом (было 20) */
        background: #fff;
        padding: 12px;        /* Уменьшили внутренний отступ карточки (было 20) */
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 15px;  /* Уменьшили отступ между карточками (было 20) */
        transition: transform 0.2s, box-shadow 0.2s;
        text-decoration: none;
        color: inherit;
    }
    
    @media (max-width: 600px) {
        .book-card {
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 15px 10px; /* Немного больше отступов для мобильных */
        }
        .book-cover {
            width: 120px;    /* Чуть уменьшили ширину на мобильных (было 140) */
            height: auto;
            margin-bottom: 5px; /* Зазор между фото и заголовком на мобильных */
        }
    }

    .book-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-color: var(--card-tech);
    }
    .book-cover {
        width: 80px;         /* Уменьшили ширину обложки для ПК (было 100) */
        height: 115px;       /* Уменьшили высоту обложки для ПК (было 140) */
        object-fit: cover;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        background: #f0f0f0;
    }
    .book-info {
        flex: 1;
    }
    .book-info h3 {
        margin: 0 0 5px 0;   /* Уменьшили отступ под заголовком (было 10) */
        color: var(--card-tech);
        font-size: 1.1rem;   /* Чуть уменьшили размер шрифта (было 1.2) */
        line-height: 1.2;
    }
    .book-author {
        font-weight: bold;
        display: block;
        margin-bottom: 3px;  /* Уменьшили отступ под автором (было 5) */
        color: #333;
        font-size: 0.9rem;
    }
    .book-info p {
        margin: 0;
        font-size: 0.85rem;  /* Чуть уменьшили текст описания (было 0.9) */
        color: #666;
        line-height: 1.3;    /* Сделали строки плотнее */
    }
</style>

В этом разделе собраны книги и учебники, проверенные временем и практикой.

<div class="bibliography-list">

<!-- КНИГА 1 -->

<a href="/bibliography/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.html" class="book-card">
<img src="img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.webp" alt="Обложка" class="book-cover">
<div class="book-info">
<h3>Энциклопедия юного радиолюбителя-конструктора. (2001)</h3>
<span class="book-author">Борисов В.Г.</span>
<p>Классика инженерной литературы. Фундаментальные знания о радиосвязи и устройстве электронных компонентов.</p>
</div>
</a>

</div>

