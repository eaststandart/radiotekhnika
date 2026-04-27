<style>
    .media-row {
        display: flex;
        flex-direction: row;
        /* ОБНУЛЯЕМ gap, чтобы он не суммировался с маржинами при переносе */
        gap: 0; 
        margin: 0; 
        align-items: flex-start;
        flex-wrap: wrap; 
    }

    .video-item {
        /* Добавляем зазор между колонками через padding справа */
        padding-right: 15px; 
        flex: 0 0 calc(33.33%); 
        min-width: 200px;
        box-sizing: border-box;
    }

    /* Убираем лишние отступы и выравниваем ритм */
    .small-cover, 
    .video-item video {
        margin-top: 0 !important;    
        margin-bottom: 10px !important; /* Твой стандарт 10px */
        width: 100%;
        height: auto;
        display: block;
    }

    .small-cover {
        width: 150px !important;
        /* Чтобы картинки в ряду тоже имели отступ справа как у видео */
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
            padding-right: 0; /* На мобильном отступ справа не нужен */
        }
        .small-cover { margin-right: 0 !important; }
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
