<style>
    .video-row {
        display: flex !important;
        flex-direction: row !important;
        align-items: stretch; /* Растягивает контейнеры до одной высоты */
        gap: 15px;
        margin: 20px 0;
        flex-wrap: nowrap;
    }

    .video-item {
        /* Контейнер подстраивается под контент, но не меньше минимума */
        display: flex;
        align-items: flex-start;
    }

    .video-item video {
        height: 200px !important; /* Задаем жесткую высоту для видео */
        width: auto;               /* Ширина подстроится сама */
        border-radius: 8px;
        background: #000;
    }

    .video-item img {
        height: 200px !important; /* Такая же высота, как у видео */
        width: auto;               /* Картинка не растянется по ширине! */
        object-fit: contain;       /* Сохранит пропорции без обрезки */
        border-radius: 8px;
    }

    @media (max-width: 600px) {
        .video-row { flex-direction: column !important; align-items: center; }
        .video-item video, .video-item img { width: 100%; height: auto !important; }
    }
</style>

<div class="video-row">
    <div class="video-item">
        <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp">
    </div>
    <div class="video-item">
        <video controls>
            <source src="/projects/1.webm" type="video/webm">
        </video>
    </div>
</div>
