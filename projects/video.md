<style>
    .video-row {
        display: flex;
        flex-direction: row;
        gap: 15px;
        align-items: flex-start; /* Выравнивание по верху */
        flex-wrap: nowrap;
    }

    /* Настройка видео: добавляем отступ как у картинок в style.css */
    .video-item video {
        height: 200px;
        width: auto;
        margin: 15px 0; /* Такой же отступ, как у картинок в основном CSS */
        border-radius: 8px;
        display: block;
    }

    /* Настройка картинки: просто фиксируем высоту */
    .video-item img {
        height: 200px;
        width: auto;
        border-radius: 8px;
    }

    @media (max-width: 600px) {
        .video-row { flex-direction: column; align-items: center; }
        .video-item video, .video-item img { width: 100%; height: auto; }
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
