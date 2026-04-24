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
        padding: 0 15px 0px 15px; 
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 10px;
        text-decoration: none;
        color: inherit;
    }
    
    .book-cover {
        width: 100px !important;
        height: 140px !important;
        object-fit: cover;
        border-radius: 0 0 5px 5px;
    }

    .book-info {
        flex: 1;
    }

    .book-info h3 {
        margin: 0 0 8px 0;
        padding-top: 15px; /* Этот отступ выравнивает текст по картинке на ПК */
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

    /* Адаптация для телефона */
    @media (max-width: 600px) {
        .book-card { 
            flex-direction: column; /* Текст уходит под картинку */
            align-items: center;    /* Всё по центру */
            text-align: center;
            padding: 0 10px 15px 10px; 
        }
        .book-cover { 
            width: 130px !important; 
            height: auto !important;
            margin-bottom: 10px; 
        }
        .book-info h3 {
            padding-top: 0; /* На телефоне лишний отступ сверху не нужен */
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
