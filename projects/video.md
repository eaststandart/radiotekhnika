<style>
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 15px;
        margin: 0; 
        align-items: flex-start;
        flex-wrap: wrap; 
    }

    /* Убираем растягивание перенесенного видео */
    .video-item {
        flex: 0 0 calc(33.33% - 10px); 
        min-width: 200px;
    }

    /* ГЛАВНОЕ: Убиваем верхние отступы, оставляем только нижние */
    .small-cover, 
    .video-item video,
    .video-item img {
        margin-top: 0 !important;    /* Убираем 10px из style.css */
        margin-bottom: 15px !important; /* Оставляем 15px для ритма */
        width: 100%;
        height: auto;
        display: block;
    }

    .small-cover {
        width: 150px !important; 
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
            gap: 0; /* Чтобы работали только margin-bottom самих элементов */
        }
        .small-cover, .video-item {
            width: 100% !important;
            max-width: 280px !important;
            flex: 0 0 auto; /* Отключаем расчет ширины в 33% */
        }
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
