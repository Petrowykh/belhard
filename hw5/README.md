# ПРОЕКТ #

![image](https://github.com/Petrowykh/belhard/assets/31277728/8287f08e-d62d-43fd-8e63-93e267ea8177)



Задача: Создать модель детектирования китайский марок автомобилей по фото логотипа
Цель: Пройти все этапы подготовки и проектирования модели

Этапы:
1. Создание датасета
2. Предобработка
3. Аугментация
4. Обучение
5. Тестирование
6. Оценка работы


## Создание датасета ##
  
Использовался сайт https://auto.ru/

Для 6 брендов были сделаны по 10 скриншотов разных машин

## Предобработка ##

Для аннотирования был использован LabelStudio [https://github.com/HumanSignal/labelImg](https://github.com/HumanSignal/label-studio)https://github.com/HumanSignal/label-studio
![image](https://github.com/Petrowykh/belhard/assets/31277728/55494a50-a0c3-46de-8ba4-980f1aaf0bca)


Для каждого изображения была проставлена метка
![image](https://github.com/Petrowykh/belhard/assets/31277728/37c2f588-1aff-490d-994b-75e24a60994c)

Результаты возможно экспортировтаь в любые форматы
![image](https://github.com/Petrowykh/belhard/assets/31277728/ba3f7460-879a-4100-8d9b-7823e3868b4b)

## Аугментация ##
Для обработки изображений использовал 
https://roboflow.com/

Процесс состоит из нескольких шагов
1. Создание проекта

![image](https://github.com/Petrowykh/belhard/assets/31277728/cd6d6afb-0b64-4093-9663-9fc12315ffdc)

2. Загрузка данных
![image](https://github.com/Petrowykh/belhard/assets/31277728/1cb9658c-85ee-4b28-98e5-7505e8edf842)

3. Разбиение на train, val, test
![image](https://github.com/Petrowykh/belhard/assets/31277728/8fbc4219-e0b4-4efd-be0f-7b096b4b635e)

4. Препроцессинг
В данном случае изменил размер 416х416
![image](https://github.com/Petrowykh/belhard/assets/31277728/65f62832-0dd2-4510-a382-66975421e2c4)

5. Аугментация
![image](https://github.com/Petrowykh/belhard/assets/31277728/363a45bf-1c8b-464e-8e08-d840d7aa46a5)
типы аугментации — Crop, Brightness, Exposure, Noise
![image](https://github.com/Petrowykh/belhard/assets/31277728/5afc6f53-012e-4015-9709-b878bc9ab8d3)


## Обучение ##

Обучение модели проводилось в самой среде
![image](https://github.com/Petrowykh/belhard/assets/31277728/63b14fa3-6491-413f-a824-b368767cfc7a)

Результат тренировки модели
![image](https://github.com/Petrowykh/belhard/assets/31277728/ee359314-f7ed-4d4d-bcdc-ce5331bbe928)

## Тестирование ##
На тестовых изображениях модель показывала хорошие результаты
![image](https://github.com/Petrowykh/belhard/assets/31277728/e389479f-a79c-4aea-8194-1e7fd4c8fec2)
>{
  "predictions": [
    {
      "x": 376,
      "y": 314.5,
      "width": 92,
      "height": 57,
      "confidence": 0.941,
      "class": "gac",
      "class_id": 3,
      "detection_id": "956adff3-8b79-461c-990e-e99c2e06e4f6"
    }
  ]
}





   

