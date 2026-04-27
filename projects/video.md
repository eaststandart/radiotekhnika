<style>
    /* Контейнер для ряда видео */
    .video-row {
        display: flex;
        flex-direction: row; /* В ряд на ПК */
        gap: 15px;           /* Зазор между плеерами */
        margin: 20px 0;
        flex-wrap: wrap;     /* Чтобы видео могли переноситься, если не влезают */
    }

    /* Стиль каждого видео-блока */
    .video-item {
        flex: 1;             /* Равномерно распределяем место */
        min-width: 200px;    /* Чтобы видео не становились слишком мелкими */
        max-width: 320px;    /* Ограничиваем максимальную ширину в ряду */
    }

    .video-item video {
        width: 100%;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* Адаптация для телефона */
    @media (max-width: 600px) {
        .video-row {
            flex-direction: column; /* На смартфоне строго друг под другом */
            align-items: center;
        }
        .video-item {
            max-width: 100%;        /* На телефоне — на всю ширину */
        }
    }
</style>

<div class="video-row">
    <!-- Видео 1 -->
    <div class="video-item">
        <video controls>
            <source src="1.webm" type="video/webm">
        </video>
    </div>

    <!-- Видео 2 -->
    <div class="video-item">
        <video controls>
            <source src="img/video2.webm" type="video/webm">
        </video>
    </div>

    <!-- Видео 3 -->
    <div class="video-item">
        <video controls>
            <source src="img/video3.webm" type="video/webm">
        </video>
    </div>
</div>
