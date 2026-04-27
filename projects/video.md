<style>
    .media-row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap; 
        gap: 0; 
        margin: 0 !important; 
        align-items: flex-start;
    }

    .video-item {
        padding-right: 15px; 
        flex: 0 0 calc(33.33%); /* 3 видео в ряд */
        min-width: 200px;
        box-sizing: border-box;
    }

    .small-cover, 
    .video-item video {
        margin-top: 0 !important;    
        margin-bottom: 15px !important; 
        display: block;
    }

    .small-cover {
        /* Фиксируем высоту, чтобы разные обложки стояли ровно */
        height: 220px !important; 
        width: auto !important;
        object-fit: contain;
        margin-right: 15px !important; 
    }

    .video-item video {
        width: 100%;
        height: auto;
    }
    
    @media (max-width: 600px) {
        .media-row { flex-direction: column; align-items: center; }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
            padding-right: 0;
        }
        .small-cover { margin-right: 0 !important; height: auto !important; }
    }
</style>

<!-- БЛОК ФОТО -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="small-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="small-cover">
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
