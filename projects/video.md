<style>
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 20px;
        margin: 0; /* Обнуляем, чтобы управлять отступами самих элементов */
        align-items: flex-start;
    }

    /* Единый стиль отступа для всех медиа-элементов */
    .small-cover, .video-item video {
        margin-top: 10px;    /* Небольшой зазор сверху */
        margin-bottom: 15px; /* Стандартный зазор снизу */
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        display: block;
    }

    .small-cover {
        width: 150px !important; 
        height: auto !important;
    }

    .video-item {
        flex: 1;
        max-width: 320px;
    }

    .video-item video {
        width: 100%;
        height: auto;
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
            gap: 0; /* На мобильном зазоры будут за счет margin элементов */
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

