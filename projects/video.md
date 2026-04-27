<style>
    .video-row {
        display: flex !important;
        flex-direction: row !important; /* Строго в ряд */
        flex-wrap: nowrap;             /* Запрещаем перенос на новую строку */
        gap: 15px;
        align-items: flex-start;       /* Выравнивание по верхнему краю */
        margin: 20px 0;
        width: 100%;
    }

    .video-item {
        flex: 1;                       /* Равномерно делят место */
        min-width: 0;                  /* Важно: позволяет элементам сжиматься */
    }

    .video-item img, .video-item video {
        width: 100%;
        height: 180px;                 /* Одинаковая высота для всех */
        object-fit: cover;             /* Обрезка лишнего, чтобы не было искажений */
        border-radius: 8px;
        display: block;
    }

    /* На телефоне всё равно лучше сделать столбик, иначе будет слишком мелко */
    @media (max-width: 600px) {
        .video-row {
            flex-direction: column !important;
        }
        .video-item img, .video-item video {
            height: auto;              /* На телефоне пусть будут в полный рост */
        }
    }
</style>


<div class="video-row">

    <!-- Блок 1: Фото (Исправь путь на реальный без скобок, если можно) -->
    <div class="video-item">
        <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" alt="Схема">
    </div>

    <!-- Блок 2: Видео -->
    <div class="video-item">
        <video controls>
            <source src="/projects/1.webm" type="video/webm">
        </video>
    </div>

</div>

