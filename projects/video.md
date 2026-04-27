<style>
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 15px;
        margin: 0; 
        align-items: flex-start;
        flex-wrap: wrap; 
    }

    .small-cover {
        width: 150px !important; 
        height: auto !important;
        /* Убираем верхний маржин, чтобы не суммировался */
        margin-top: 0 !important; 
        margin-bottom: 15px !important;
    }

    .video-item {
        /* Рассчитываем ширину ровно на 3 колонки (33.3% минус зазоры) */
        flex: 0 0 calc(33.33% - 10px); 
        min-width: 200px;
    }

    .video-item video {
        width: 100%;
        height: auto;
        /* Убираем верхний маржин, чтобы не было "дыр" между рядами */
        margin-top: 0 !important; 
        margin-bottom: 15px !important;
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
        }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
            flex: 1 1 auto;
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
