<style>
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 0; 
        margin: 0; 
        align-items: flex-start;
        flex-wrap: wrap; 
    }

    .video-item {
        /* Увеличиваем зазор между колонками до 15px */
        padding-right: 15px; 
        flex: 0 0 calc(33.33%); 
        min-width: 200px;
        box-sizing: border-box;
    }

    .small-cover, 
    .video-item video {
        margin-top: 0 !important;    
        /* Увеличиваем вертикальный зазор до 15px */
        margin-bottom: 15px !important; 
        width: 100%;
        height: auto;
        display: block;
    }

    .small-cover {
        width: 150px !important;
        /* Горизонтальный зазор для картинок тоже 15px */
        margin-right: 15px !important; 
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
        }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
            padding-right: 0;
        }
        .small-cover { margin-right: 0 !important; }
    }
</style>

<!-- БЛОК ФОТО -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="small-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="small-cover">
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
