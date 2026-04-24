---
layout: default
title: Рекомендуемая литература
---
<style>
    .book-card {
        display: flex;
        flex-direction: row;
        align-items: center; /* Центрирует картинку и текст по вертикали друг относительно друга */
        gap: 20px;
        background: #fff;
        padding: 10px 15px;  /* Равномерные отступы 10px сверху и снизу */
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 10px;
        text-decoration: none;
        color: inherit;
    }
    
    .book-cover {
        width: 90px !important;  /* Чуть уменьшили, чтобы легче входила */
        height: 125px !important;
        object-fit: cover;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }

    .book-info {
        flex: 1;
        padding: 0; /* Убираем все смещения */
    }

    .book-info h3 {
        margin: 0 0 5px 0; /* Только отступ снизу */
        color: var(--card-tech);
        font-size: 1.1rem;
    }

    .book-author {
        font-weight: bold;
        display: block;
        margin-bottom: 8px;
        color: #333;
        font-size: 0.95rem;
    }

    .book-info p {
        margin: 0;
        font-size: 0.88rem;
        color: #666;
        line-height: 1.4;
    }

    /* Адаптация списка книг для телефона */
    @media (max-width: 600px) {
        .book-card {
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 5px 10px 10px 10px; 
            gap: 0px;
        }
        .book-cover {
            width: 130px !important; /* Увеличиваем обложку на мобильном */
            height: auto !important;
            margin-bottom: 10px;
        }
        .book-info {
            padding-top: 0 !important; /* Убираем боковой отступ, чтобы на мобильном не было дырки */
        }
    }

</style>

В этом разделе собраны книги и учебники, проверенные временем и практикой.

<div class="bibliography-list">

<!-- КНИГА 1 -->
<a href="/bibliography/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.html" class="book-card">
<img src="/bibliography/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001.webp" alt="Обложка" class="book-cover">
<div class="book-info">
<h3>Энциклопедия юного радиолюбителя-конструктора (2001)</h3>
<span class="book-author">Борисов В.Г.</span>
<p>Классика инженерной литературы. Фундаментальные знания о радиосвязи и устройстве электронных компонентов.</p>
</div>
</a>

</div>
