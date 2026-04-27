<style>
    .media-row {
        display: flex;
        flex-direction: row;
        gap: 15px; /* Зазор между картинками */
        margin: 0; 
        align-items: flex-start;
    }

    .book-page-cover {
        /* Устанавливаем единую высоту для всех обложек */
        height: 220px !important; 
        width: auto !important; 
        /* Сохраняем пропорции, чтобы картинка не сплющилась */
        object-fit: contain; 
        border-radius: 8px;
    }

    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }
        .book-page-cover {
            /* На мобильных возвращаемся к управлению через ширину */
            height: auto !important;
            width: 100% !important;
            max-width: 250px !important;
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
