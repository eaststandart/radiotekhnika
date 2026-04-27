<style>
    .media-row {
        display: flex;
        flex-direction: row;
        /* Уменьшаем зазор, чтобы 4 видео влезли в 800px */
        gap: 12px; 
        margin: 0; 
        align-items: flex-start;
        flex-wrap: wrap; 
    }

    .small-cover {
        width: 150px !important; 
        height: auto !important;
    }

    .video-item {
        flex: 1;
        /* Уменьшаем min-width, чтобы 4 колонки поместились в ряд (800 / 4 = 200) */
        min-width: 180px; 
        /* Убираем ограничение в 320px, чтобы они ровно делили строку */
        max-width: none; 
    }

    /* Убираем верхний отступ у всех элементов, чтобы не было "дыр" между рядами */
    .small-cover, .video-item video {
        margin-top: 0 !important; 
        margin-bottom: 15px; /* Оставляем только нижний отступ для ритма */
    }

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
        /* Возвращаем отступ для мобильной колонки */
        .video-item video { margin-bottom: 10px; }
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
