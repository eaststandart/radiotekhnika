---
layout: default
title: Тест отступов и сетки
---

<style>
    /* 1. КОРРЕКЦИЯ ОБЕРТКИ (Чтобы убрать пустые поля по бокам на мобилках) */
    @media (max-width: 900px) {
        .content-wrapper {
            width: 100% !important;
            max-width: 100% !important;
            padding: 15px 12px !important; /* Единый отступ от края экрана для всего */
            border-radius: 0 !important;
            margin: 0 !important;
        }
    }

    /* 2. СТИЛИ КАРТОЧЕК (Аналог fair.css / inspiration.css) */
    .test-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 12px; 
        width: 100%;
        margin-top: 10px;
    }

    .test-card {
        display: flex;
        flex-direction: row;
        align-items: center; 
        gap: 12px;
        background: #fff;
        padding: 8px 12px;
        border-radius: 12px;
        border: 1px solid #eee;
        text-decoration: none;
        color: inherit;
    }

    .test-img {
        width: 50px !important;
        height: 50px !important;
        border-radius: 50%;
        object-fit: cover;
        flex-shrink: 0;
    }

    .test-card h3 {
        margin: 0;
        font-size: 1.1rem;
        color: var(--card-tech);
        line-height: 1.2;
    }

    /* 3. УНИФИКАЦИЯ ДЛЯ МОБИЛЬНЫХ (Горизонталь vs Вертикаль) */
    
    /* ВЕРТИКАЛЬНО: Один столбец, иконка 45px */
    @media (max-width: 600px) and (orientation: portrait) {
        .test-list { grid-template-columns: 1fr; }
        .test-img { width: 45px !important; height: 45px !important; }
    }

    /* ГОРИЗОНТАЛЬНО: Две колонки, чтобы не было гигантских пустых карточек */
    @media (max-height: 500px) and (orientation: landscape) {
        .test-list {
            grid-template-columns: 1fr 1fr; /* Две колонки уплотняют контент */
            gap: 10px;
        }
        .test-card { padding: 6px 10px; }
        .test-img { width: 40px !important; height: 40px !important; }
        .test-card h3 { font-size: 1rem; }
    }
</style>

<p>Пример текста над блоком для проверки выравнивания по левому краю.</p>

<div class="test-list">
    <a href="#" class="test-card">
        <img src="/inspiration/img/through-hole-red-led-2.webp" class="test-img">
        <h3>Первая поделка</h3>
    </a>
    <a href="#" class="test-card">
        <img src="/inspiration/img/through-hole-red-led-2.webp" class="test-img">
        <h3>Вторая поделка</h3>
    </a>
    <a href="#" class="test-card">
        <img src="/inspiration/img/through-hole-red-led-2.webp" class="test-img">
        <h3>Третья поделка с длинным названием</h3>
    </a>
    <a href="#" class="test-card">
        <img src="/inspiration/img/through-hole-red-led-2.webp" class="test-img">
        <h3>Четвертая поделка</h3>
    </a>
</div>
