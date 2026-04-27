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
        margin-top: 0 !important; 
        margin-bottom: 15px !important;
    }

    .video-item {
        /* flex-grow: 1 позволяет заполнять строку, если осталось пустое место */
        flex: 1 1 calc(33.33% - 15px); 
        /* min-width не дает видео стать слишком узким */
        min-width: 240px; 
        max-width: 100%;
    }

    .video-item video {
        width: 100%;
        height: auto;
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
