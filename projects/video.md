<style>
    /* Нам нужен только один класс для видео, остальное берем из глобальных стилей */
    .video-row {
        display: flex;
        flex-direction: row;
        gap: 15px;
        margin: 20px 0;
    }
    .video-item {
        flex: 1;
    }
    .video-item video {
        width: 100%;
        height: auto;
        border-radius: 8px; /* Чтобы видео было в стиле картинок */
        margin: 15px 0;    /* Такой же отступ, как у картинок в style.css */
    }

    @media (max-width: 600px) {
        .video-row { flex-direction: column; }
    }
</style>

<!-- БЛОК ФОТО: Просто используем Markdown или HTML, стили подхватятся из style.css -->
<div class="video-row">
    <div class="video-item">
        <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp">
    </div>
    <div class="video-item">
        <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp">
    </div>
</div>

<!-- БЛОК ВИДЕО: Используем новый компактный класс -->
<div class="video-row">
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
</div>
