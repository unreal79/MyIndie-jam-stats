# MyIndie-jam-stats

Jupyter Notebook скрипт для сбора статистики по играм с сайта [MyIndie.ru](https://myindie.ru) для джемов.

## Установка

Python 3.12+ (может и более ранние версии)

Необходимые пакеты:

* requests
* pandas
* numpy

```bash
pip install requests pandas numpy
```

## Запуск

Запустите последовательно пункты 0, 2, 3.

Пункт 1 понадобится только для джема отличного от MyIndie Jam LVL9. Для LVL9 уже собраны данные в директории 'output/myindie-game-jam-level-9'.

## MyIndie Jam LVL9

В настоящее время собрана статистика по джему [MyIndie Jam LVL9](https://myindie.ru/jams/jam/myindie-game-jam-level-9).

### Статистический анализ судей (MyIndie Jam LVL9)

| username | reviews_count | avg_score | median_score | std_score | min_score | max_score | avg_review_chars |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| HelenAllienPoe | 14 | 3.829 | 3.917 | 0.485 | 2.917 | 4.583 | 572.643 |
| Saley | 32 | 3.528 | 3.500 | 0.671 | 2.083 | 4.667 | 777.625 |
| PoliKhai | 41 | 3.305 | 3.417 | 0.783 | 1.083 | 4.667 | 532.829 |
| DmitriySklyarov | 33 | 3.115 | 3.083 | 0.666 | 1.500 | 4.250 | 591.455 |

### Инсайты по поведению судей

| username | strictness_index | top_criteria | bottom_criteria | active_days | peak_hour_utc | reviews_per_day |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DmitriySklyarov | -0.259 | art (3.79) | gameplay (2.79) | 7 | 19 | 4.710 |
| PoliKhai | -0.067 | theme (3.7) | gameplay (2.83) | 3 | 13 | 13.670 |
| Saley | 0.151 | art (4.09) | gameplay (3.03) | 3 | 20 | 10.670 |
| HelenAllienPoe | 0.462 | sound (4.14) | narrative (3.36) | 4 | 5 | 3.500 |


