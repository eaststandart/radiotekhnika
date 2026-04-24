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
        padding: 10px 15px;   /* Минимум сверху/снизу (10px) и стандарт по бокам (15px) */
        border-radius: 12px;
        border: 1px solid #eee;
        margin-bottom: 12px;  /* Уменьшили расстояние между самими карточками */
        transition: transform 0.2s, box-shadow 0.2s;
        text-decoration: none;
        color: inherit;
    }
    
    @media (max-width: 600px) {
        .book-card {
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 15px 10px;
        }
        .book-cover {
            width: 140px; 
            height: auto;
            margin-bottom: 10px;
        }
    }

    .book-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-color: var(--card-tech);
    }
    .book-cover {
        width: 100px;         /* Вернул как было */
        height: 140px;        /* Вернул как было */
        object-fit: cover;
        border-radius: 5px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        background: #f0f0f0;
    }
    .book-info {
        flex: 1;
        padding-top: 5px;     /* Небольшой сдвиг текста вниз, чтобы был вровень с верхом картинки */
    }
    .book-info h3 {
        margin: 0 0 5px 0;    /* Плотный отступ под заголовком */
        color: var(--card-tech);
        font-size: 1.2rem;
    }
    .book-author {
        font-weight: bold;
        display: block;
        margin-bottom: 3px;   /* Плотный отступ под автором */
        color: #333;
        font-size: 0.95rem;
    }
    .book-info p {
        margin: 0;
        font-size: 0.9rem;
        color: #666;
        line-height: 1.4;
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

