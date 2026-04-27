<style>
    /* 1. Общий контейнер */
    .media-row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap; 
        gap: 0; 
        margin: 0; 
        align-items: flex-start;
    }

    /* 2. Универсальная обертка для КАЖДОГО элемента (и фото, и видео) */
    .media-item {
        /* Жестко 3 элемента в ряд на ПК (100 / 3 = 33.3) */
        flex: 0 0 calc(33.33% - 15px); 
        margin-right: 15px !important;
        margin-bottom: 15px !important;
        margin-top: 0 !important;
        box-sizing: border-box;
    }

    /* 3. Стили для контента внутри обертки */
    .media-item img, 
    .media-item video {
        width: 100%;       /* Заполняет свою колонку (1/3 строки) */
        height: 200px;     /* Одинаковая высота для всех */
        object-fit: cover; /* Обрезает лишнее, сохраняя ровный ряд */
        border-radius: 8px;
        display: block;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* 4. Специфика для маленьких обложек (если хочешь их в ряд по 150px, а не на 1/3) */
    /* Если применить этот класс к media-item, он перебьет ширину 33% */
    .item-small {
        flex: 0 0 auto !important;
        width: 150px !important;
    }

    /* 5. Адаптация */
    @media (max-width: 800px) {
        .media-item {
            flex: 0 0 calc(50% - 15px); /* По 2 в ряд на планшетах */
        }
    }

    @media (max-width: 600px) {
        .media-row { flex-direction: column; align-items: center; }
        .media-item {
            width: 100% !important;
            max-width: 280px;
            margin-right: 0 !important; /* Убираем боковой отступ в столбике */
            flex: 0 0 auto;
        }
        .media-item img, .media-item video { height: auto; }
    }
</style>

<!-- ПРИМЕР: РЯД ФОТО (маленькие, как в библио) -->
<div class="media-row">
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp"></div>
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp"></div>
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>    
</div>

<!-- ПРИМЕР: РЯД ВИДЕО (по 3 в ряд) -->
<div class="media-row">
    <div class="media-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="media-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="media-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="media-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
</div>

<!-- ПРИМЕР: РЯД ФОТО (маленькие, как в библио) -->
<div class="media-row">
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
    <div class="media-item item-small"><img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp"></div>
</div>
