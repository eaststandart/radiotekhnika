<style>
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 20px;
        /* Уменьшили нижний отступ контейнера с 20px до 5px */
        margin: 10px 0 5px 0; 
        align-items: flex-start;
    }

    .small-cover {
        width: 150px !important; 
        height: auto !important;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        display: block;
    }

    .video-item {
        flex: 1;
        max-width: 320px;
    }

    .video-item video {
        width: 100%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        /* УБРАЛИ margin: 15px 0, теперь видео не "отталкивается" */
        margin: 0; 
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
            gap: 10px; /* На мобильном чуть плотнее */
        }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
        }
        .video-item video {
            margin-bottom: 10px; /* Чтобы видео не слипались в колонке */
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

