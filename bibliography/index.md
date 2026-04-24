---
layout: default
title: Рекомендуемая литература
---
<style>
    /* Стили только для списка книг */
    .book-card {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 20px;
        background: #fff;
        padding: 5px 15px;
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 10px;
        text-decoration: none;
        color: inherit;
    }
    
    .book-cover {
        width: 100px !important;  /* Жестко фиксируем размер */
        height: 140px !important; /* Жестко фиксируем размер */
        object-fit: cover;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        background: #f0f0f0;
    }

    .book-info {
        flex: 1;
        padding-top: 8px;
    }

    .book-info h3 {
        margin: 0 0 8px 0;
        color: var(--card-tech);
        font-size: 1.15rem;
        line-height: 1.2;
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
