<style>
    /* Базовый контейнер как у Борисова */
    .media-row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap; 
        gap: 0; 
        margin: 0 !important; 
        align-items: flex-start;
    }

    /* Видео: 3 в ряд, пропорции не трогаем */
    .video-item {
        flex: 0 0 calc(33.33% - 15px); 
        min-width: 200px;
        margin-right: 15px !important;
        margin-bottom: 15px !important;
    }

    .video-item video {
        width: 100%;
        height: auto; /* Видео само держит свои пропорции */
        border-radius: 8px;
        display: block;
    }

    /* Фото: как в файле Борисова — фиксируем только высоту */
    .small-cover {
        height: 220px !important; 
        width: auto !important; 
        object-fit: contain; 
        border-radius: 8px;
        margin-right: 15px !important;
        margin-bottom: 15px !important;
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
        }
        .video-item, .small-cover {
            width: 100% !important;
            max-width: 280px !important;
            margin-right: 0 !important;
            flex: 0 0 auto;
        }
        .small-cover { height: auto !important; }
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
