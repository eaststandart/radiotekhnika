---
layout: default
title: Рекомендуемая литература
---

<style>
    .book-card {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 20px;
        background: #fff;
        padding: 5px 15px;    /* Сверху и снизу 5px, по бокам 15px */
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 10px;
        transition: transform 0.2s, box-shadow 0.2s;
        text-decoration: none;
        color: inherit;
    }
    
    @media (max-width: 600px) {
        .book-card {
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 10px 10px;
        }
        .book-cover {
            width: 130px; 
            height: auto;
            margin-bottom: 12px;
        }
    }

    .book-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-color: var(--card-tech);
    }

    .book-cover {
        width: 100px;
        height: 140px;
        object-fit: cover;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        background: #f0f0f0;
    }

    .book-info {
        flex: 1;
        padding-top: 5px; /* Чуть опустили текст от самого края */
    }

    .book-info h3 {
        margin: 0 0 8px 0;    /* Увеличили отступ под названием книги */
        color: var(--card-tech);
        font-size: 1.15rem;
        line-height: 1.2;
    }

    .book-author {
        font-weight: bold;
        display: block;
        margin-bottom: 8px;   /* Увеличили отступ под именем автора */
        color: #333;
        font-size: 0.95rem;
    }

    .book-info p {
        margin: 0;
        font-size: 0.88rem;
        color: #666;
        line-height: 1.4;    /* Чуть увеличили расстояние между строками описания */
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

