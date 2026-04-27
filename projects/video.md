<style>
    .video-row {
        display: flex;
        flex-direction: row;
        gap: 15px;
        align-items: flex-start; 
        flex-wrap: nowrap;
        /* Разрешаем горизонтальную прокрутку, если видео совсем не влезают */
        overflow-x: auto; 
    }

    .video-item video {
        height: 200px;
        width: auto;
        margin: 15px 0; 
        border-radius: 8px;
        display: block;
        flex-shrink: 1; /* Видео могут немного сжиматься */
    }

    .video-item img {
        height: 200px;
        width: auto;
        border-radius: 8px;
        /* ГЛАВНОЕ: запрещаем картинке сужаться */
        flex-shrink: 0; 
        display: block;
    }

    @media (max-width: 600px) {
        .video-row { flex-direction: column; align-items: center; overflow-x: visible; }
        .video-item video, .video-item img { width: 100%; height: auto; }
    }
</style>

<div class="video-row">
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
    <div class="video-item">
        <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp">
    </div>
    <div class="video-item">
        <video controls><source src="/projects/1.webm" type="video/webm"></video>
    </div>
</div>
