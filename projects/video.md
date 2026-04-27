<style>
    /* 1. Общий контейнер для любых медиа-рядов */
    .media-row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap; 
        gap: 0; 
        margin: 0; 
        align-items: flex-start;
    }

    /* 2. Универсальный элемент ряда (и для видео, и для фото) */
    .media-item {
        margin-right: 15px !important;
        margin-bottom: 15px !important;
        margin-top: 0 !important;
    }

    /* 3. Выравнивание по ВЫСОТЕ (как в списке литературы) */
    .media-item img, 
    .media-item video {
        height: 200px !important; /* Единая высота для всех */
        width: auto !important;    /* Ширина подстроится пропорционально */
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        display: block;
        object-fit: contain;      /* Чтобы не искажались пропорции */
    }

    /* 4. Адаптация для мобильных */
    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
        }
        .media-item {
            margin-right: 0 !important;
            width: 100%;
            max-width: 280px; /* Чтобы на мобильном не были гигантскими */
        }
        .media-item img, 
        .media-item video {
            height: auto !important; /* На мобильном переходим на авто-высоту */
            width: 100% !important;
        }
    }
</style>

<!-- БЛОК ФОТО -->
<div class="media-row">
    <div class="media-item"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
    <div class="media-item"><img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp"></div>
    <div class="media-item"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
    <div class="media-item"><img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp"></div>
</div>

<!-- БЛОК ВИДЕО -->
<div class="media-row">
    <div class="media-item"><video controls><source src="/projects/1.webm" type="video/webm"></video></div>
    <div class="media-item"><video controls><source src="/projects/1.webm" type="video/webm"></video></div>
    <div class="media-item"><video controls><source src="/projects/1.webm" type="video/webm"></video></div>
    <div class="media-item"><video controls><source src="/projects/1.webm" type="video/webm"></video></div>
</div>

<!-- СНОВА ФОТО -->
<div class="media-row">
    <div class="media-item"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
    <div class="media-item"><img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp"></div>
    <div class="media-item"><img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp"></div>
</div>
