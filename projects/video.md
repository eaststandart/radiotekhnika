<style>
    /* 1. Контейнер для рядов */
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 20px;
        margin: 0; 
        align-items: flex-start;
        flex-wrap: wrap; /* Чтобы 4 видео могли перенестись на новую строку, если тесно */
    }

    /* 2. Специфика для маленьких фото */
    .small-cover {
        width: 150px !important; 
        height: auto !important;
    }

    /* 3. Специфика для сетки видео */
    .video-item {
        flex: 1;
        min-width: 200px; /* Чтобы видео не сжимались в "ниточку" */
        max-width: 320px;
    }

    /* Все остальное (margin, border-radius, shadow) берется из style.css */

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
            gap: 0;
        }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
        }
    }
</style>

<!-- БЛОК ФОТО -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="small-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="small-cover">
</div>

<!-- БЛОК ВИДЕО (теперь 4 штуки в ряд на ПК) -->
<div class="media-row">
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
</div>

<!-- БЛОК ФОТО -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="small-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="small-cover">
</div>
