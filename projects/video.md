<style>
    .media-row {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap; 
        gap: 0; 
        margin: 0 !important; 
        align-items: flex-start;
    }

    .video-item {
        padding-right: 15px; 
        flex: 0 0 calc(33.33%); /* 3 видео в ряд */
        min-width: 200px;
        box-sizing: border-box;
    }

    .video-item video {
        width: 100%;
        height: auto;
        margin-top: 0 !important;    
        margin-bottom: 15px !important; 
        display: block;
    }
   
        .book-page-cover {
        height: 200px !important; 
        width: auto !important; 
        max-width: calc(25% - 15px) !important;
        object-fit: contain; 
        border-radius: 8px;
        margin-top: 0 !important;
        margin-bottom: 15px !important; 
        margin-right: 15px !important;
    }

    @media (max-width: 800px) {
        .book-page-cover {
            max-width: calc(33.33% - 15px) !important;
            height: 180px !important;
        }
    }
    
    @media (max-width: 600px) {
        .media-row {
            flex-direction: column;
            align-items: center;
        }
        .video-item {
            width: 100% !important;
            max-width: 280px !important;
            padding-right: 0;
        }
        .book-page-cover {
            width: 100% !important;
            max-width: 250px !important;
            height: auto !important;
            margin-right: 0 !important;
        }
    }
</style>

<!-- БЛОК ФОТО -->
<div class="media-row">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="book-page-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="book-page-cover">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="book-page-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="book-page-cover">
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="book-page-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="book-page-cover">
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
    <img src="/biblio/img/borisov-v-g-enciklopediya-yunogo-radiolyubitelya-konstruktora-2001 {cover}.webp" class="book-page-cover">
    <img src="/biblio/img/borisov-v-g-yunyj-radiolyubitel-1992 {cover}.webp" class="book-page-cover">
</div>
