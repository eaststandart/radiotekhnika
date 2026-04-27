<style>
    /* Общий контейнер для рядов (и фото, и видео) */
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 20px;
        margin: 10px 0 20px 0;
        align-items: flex-start;
    }

    /* Настройка для маленьких обложек/фото */
    .small-cover {
        width: 150px !important; 
        height: auto !important;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        display: block;
    }

    /* Настройка для колонок с видео */
    .video-item {
        flex: 1;
        max-width: 320px; /* Ограничиваем, чтобы видео не были огромными на весь экран */
    }

    .video-item video {
        width: 100%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin: 15px 0;
    }

    /* Адаптация для мобильных */
    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
        }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
        }
    }
</style>

<!-- БЛОК ФОТО: Теперь они будут по 150px в ряд -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="small-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="small-cover">
</div>

<!-- БЛОК ВИДЕО: В ряд, но не шире 320px каждое -->
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

<!-- БЛОК ФОТО: Теперь они будут по 150px в ряд -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="small-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="small-cover">
</div>

