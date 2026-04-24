---
layout: default
title: Рекомендуемая литература
---

<style>
    .book-card {
        display: flex;
        align-items: flex-start;
        gap: 20px;
        background: #fff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 20px;
        transition: transform 0.2s, box-shadow 0.2s;
        text-decoration: none;
        color: inherit;
    }
    .book-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-color: var(--card-tech);
    }
    .book-cover {
        width: 100px;
        height: 140px;
        object-fit: cover;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        background: #f0f0f0; /* Заглушка, если нет фото */
    }
    .book-info {
        flex: 1;
    }
    .book-info h3 {
        margin: 0 0 10px 0;
        color: var(--card-tech);
        font-size: 1.2rem;
    }
    .book-info p {
        margin: 0;
        font-size: 0.9rem;
        color: #666;
        line-height: 1.4;
    }
    .book-author {
        font-weight: bold;
        display: block;
        margin-bottom: 5px;
        color: #333;
    }
</style>

В этом разделе собраны книги и учебники, проверенные временем и практикой.

<!-- ПРИМЕР КНИГИ 1 -->
<a href="borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.html" class="book-card">
    <img src="/img/books/cover1.jpg" alt="Обложка" class="book-cover">
    <div class="book-info">
        <h3>Электроника для детей</h3>
        <span class="book-author">Эйвинд Нидал Даль</span>
        <p>Лучшая книга для самого начала. Все объясняется на простых примерах и живых схемах без сложной математики.</p>
    </div>
</a>

<!-- ПРИМЕР КНИГИ 2 -->
<a href="radio-basics.html" class="book-card">
    <img src="/img/books/cover2.jpg" alt="Обложка" class="book-cover">
    <div class="book-info">
        <h3>Юный радиолюбитель</h3>
        <span class="book-author">В. Г. Борисов</span>
        <p>Классика инженерной литературы. Фундаментальные знания о радиосвязи и устройстве электронных компонентов.</p>
    </div>
</a>
