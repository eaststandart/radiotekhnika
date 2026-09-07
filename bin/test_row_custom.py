#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@module test_row_custom
@about Автономный тестовый модуль для обкатки кастомных групповых классов в теге <p>.
@purpose Парсит базовые картинки, идущие в столбик, вычисляет оси по формуле Ширина > Высота
         и генерирует правильные классы img-row-custom-landscape/portrait на основе is_row_mode.
@author TechLab
@version 1.1-test
"""

import re

def test_process_base_galleries(test_markdown):
    """
    Изолированный парсер базовых галерей в тегах <p> для проверки кастомных классов.
    """
    img_pattern = r'!\[(.*?)\]\((.*?\.(?:webp|jpg|jpeg|png|gif|svg))\)'
    transparent_pixel = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    
    base_lines = test_markdown.split('\n')
    final_processed_lines = []
    
    j = 0
    while j < len(base_lines):
        line = base_lines[j]
        line_stripped = line.strip()
        
        if not line_stripped:
            final_processed_lines.append(line)
            j += 1
            continue
            
        # 🚀 ИСПРАВЛЕНО: Ищем картинку в любом месте строки (защита от <p> и пробелов)
        is_image = re.search(img_pattern, line_stripped, re.IGNORECASE)
        
        if is_image:
            # 🚀 ИСПРАВЛЕНО: Сборщик плотной группы картинок тоже переведён на re.search
            image_group_lines = []
            while j < len(base_lines) and base_lines[j].strip() and re.search(img_pattern, base_lines[j].strip(), re.IGNORECASE):
                image_group_lines.append(base_lines[j].strip())
                j += 1
                
            is_row_mode = len(image_group_lines) > 1
            
            # Обрабатываем каждую картинку из собранного столбика-галереи
            for group_line in image_group_lines:
                # 🚀 ИСПРАВЛЕНО: Финальный разбор строки через re.search
                match = re.search(img_pattern, group_line, re.IGNORECASE)
                alt_content = match.group(1).strip()
                img_url = match.group(2).strip()
                
                # Очистка обсидианового хвоста ширины
                alt_content = re.sub(r'\|\s*\d+\s*$', '', alt_content).strip()
                
                if not alt_content:
                    final_class = 'img-row-landscape' if is_row_mode else 'img-single-landscape'
                    img_html_simple = f'<img class="{final_class}" alt="" src="{transparent_pixel}" data-src="{img_url}">'
                    final_processed_lines.append(img_html_simple)
                    continue
                    
                parts = [p.strip() for p in alt_content.split('|') if p.strip()]
                
                if not parts:
                    final_class = 'img-row-landscape' if is_row_mode else 'img-single-landscape'
                    img_html_simple = f'<img class="{final_class}" alt="" src="{transparent_pixel}" data-src="{img_url}">'
                    final_processed_lines.append(img_html_simple)
                    continue
                    
                classes = []
                custom_attrs = []
                
                first_key = parts[0].strip('{} ')

                # ЛЕВОСТОРОННИЙ РАЗБОР СЛУЖЕБНЫХ КЛЮЧЕЙ
                if first_key.lower() == 'v':
                    classes.append('img-row-portrait' if is_row_mode else 'img-single-portrait')
                    parts.pop(0)
                    
                # ОБРАБОТКА КАСТОМНЫХ РАЗМЕРОВ В ГРУППЕ
                elif re.match(r'^\d+[xх]\d+$', first_key, re.IGNORECASE):
                    dimensions = re.split(r'[xх]', first_key, flags=re.IGNORECASE)
                    width, height = int(dimensions[0]), int(dimensions[1])
                    
                    # Динамически собираем префикс из флага группы
                    custom_prefix = 'img-row-custom-' if is_row_mode else 'img-single-custom-'
                    
                    # Ваша нативная формула автоматического вычисления осей геометрии
                    if width > height:
                        classes.append(f'{custom_prefix}landscape')
                    else:
                        classes.append(f'{custom_prefix}portrait')
                    
                    custom_attrs.append(f'width="{width}"')
                    custom_attrs.append(f'height="{height}"')
                    custom_attrs.append(f'style="aspect-ratio: {width} / {height} !important;"')
                    parts.pop(0)
                    
                if not classes:
                    classes.append('img-row-landscape' if is_row_mode else 'img-single-landscape')
                    
                # Сборка очищенного SEO ALT текста
                clean_parts = [p.strip('{} ') for p in parts if p.strip()]
                clean_alt = " | ".join(clean_parts) if clean_parts else ""
                
                class_str = f' class="{" ".join(classes)}"' if classes else ''
                attr_str = f' {" ".join(custom_attrs)}' if custom_attrs else ''
                
                img_html = f'<img{class_str}{attr_str} alt="{clean_alt}" src="{transparent_pixel}" data-src="{img_url}">'
                final_processed_lines.append(img_html)
                    
        else:
            final_processed_lines.append(line)
            j += 1
            
    return '\n'.join(final_processed_lines)
