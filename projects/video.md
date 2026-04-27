<style>
.video-row {
    display: flex;
    flex-direction: row;
    gap: 15px;
    align-items: center; /* Элементы выровняются по своей середине */
    flex-wrap: wrap;
}
    .video-item {
        flex: 1;
        min-width: 250px; /* Если экран меньше 500px, они сами прыгнут в столбик */
        max-width: 48%;  /* Чтобы в ряд влезало ровно два или три */
    }
    .video-item img, .video-item video {
        width: 100%;
        display: block;
        border-radius: 8px;
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

