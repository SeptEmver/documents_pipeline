- Проект написан на python 3.7 
- Требует установленного [Tesseract](https://github.com/tesseract-ocr/tesseract)
- Файл вставлять на веб-странице http://127.0.0.1:5000/ , там же покажется результат и возможные ошибки.

## Data
Предоставили только сами задания, без датасетов.
Использовал те документы, что смог найти. На русском языке найти не получилось, использовал английские.
Для тестирования использовал переконвертированные из .jpg в .tiff документы [отсюда](https://www.kaggle.com/shaz13/real-world-documents-collections) (from directory /memo)
Находятся в папке collection_tiff_docs. memo.tiff, memo_light.tiff - многостраничные варианты, всё остальное одностраничное

## Task_1
В качестве OCR использовался [tesseract](https://github.com/tesseract-ocr/tesseract)

## Task_4
Для извлечения данных использовал [spaСy](https://spacy.io/) с готовой моделью

Сначала не совсем правильно понял задание, думал что  области текста(position) (напр: \["Bob", "Rassel"]) нужно объединить в одну область в соответствии с тем как проставилась метка \["Bob Rassel", "Person"], сделал для этого большую часть функционала, но он оказался ненужным.

## Flask
WSGI не делал, debug=True оставил. Без нормального вебинтерфейса. Для текущего задания думаю этого достаточно.

## Что ещё хотел сделать, но не хватило времени.

На структурную реализацию task_2, task_3. 
На реализацию и тестирование нормального api. Который, например, мог бы возвращать результат какого-то одного таска.


## Пример результата.
Для 0000066230.tiff

```
 {
    "task_1": {
        "pages": [
            {
                "text": "MEMORANDUM July 29, 1983 To: R. D, Sharp cc: M. J. Novak FROM: Gustafson SUBJECT: BATTLE KIT SUPPORT HISTORY PURPOSE: Response to your request for past levels of suppart - for Battle Kit. DISCUSSION: BATTLE KIT BUDGET HISTORY PROPOSED 1980 1981 1982 1983 1984 1.754M 1,274MM BATTLE KIT ITEM HISTORY 1980 1981 1982 1983 1984 2.2994M 3.755MM 2.992MM \u201cBased on budget and .61 average cost per : item in 1983, Because there are so many contradictory recards on past Battle Kit items, it is impossiple to determine the actual figures for 1980 and 1981. The budget figures represent the amount spent on @attle Kit in a given year. The item amounts represent what was available for use in a given yeat, some of which were carried over from previous years and SMP pragrams. a x Let me know if you need additional information. rey g",
                "tokens": [
                    {
                        "text": "MEMORANDUM",
                        "position": {
                            "left": 145.0,
                            "top": 86.0,
                            "width": 88.0,
                            "height": 11.0
                        },
                        "offset": 0
                    },
                    {
                        "text": "July",
                        "position": {
                            "left": 145.0,
                            "top": 116.0,
                            "width": 33.0,
                            "height": 14.0
                        },
                        "offset": 11
                    },
                    {
                        "text": "29,",
                        "position": {
                            "left": 190.0,
                            "top": 117.0,
                            "width": 23.0,
                            "height": 13.0
                        },
                        "offset": 16
                    },
                    {
                        "text": "1983",
                        "position": {
                            "left": 226.0,
                            "top": 117.0,
                            "width": 35.0,
                            "height": 11.0
                        },
                        "offset": 20
                    },
                    {
                        "text": "To:",
                        "position": {
                            "left": 145.0,
                            "top": 177.0,
                            "width": 22.0,
                            "height": 11.0
                        },
                        "offset": 25
                    },
                    {
                        "text": "R.",
                        "position": {
                            "left": 226.0,
                            "top": 178.0,
                            "width": 14.0,
                            "height": 11.0
                        },
                        "offset": 29
                    },
                    {
                        "text": "D,",
                        "position": {
                            "left": 253.0,
                            "top": 178.0,
                            "width": 14.0,
                            "height": 11.0
                        },
                        "offset": 32
                    },
                    {
                        "text": "Sharp",
                        "position": {
                            "left": 280.0,
                            "top": 178.0,
                            "width": 43.0,
                            "height": 13.0
                        },
                        "offset": 35
                    },
                    {
                        "text": "cc:",
                        "position": {
                            "left": 144.0,
                            "top": 207.0,
                            "width": 23.0,
                            "height": 11.0
                        },
                        "offset": 41
                    },
                    {
                        "text": "M.",
                        "position": {
                            "left": 225.0,
                            "top": 208.0,
                            "width": 15.0,
                            "height": 10.0
                        },
                        "offset": 45
                    },
                    {
                        "text": "J.",
                        "position": {
                            "left": 253.0,
                            "top": 208.0,
                            "width": 14.0,
                            "height": 11.0
                        },
                        "offset": 48
                    },
                    {
                        "text": "Novak",
                        "position": {
                            "left": 280.0,
                            "top": 208.0,
                            "width": 43.0,
                            "height": 11.0
                        },
                        "offset": 51
                    },
                    {
                        "text": "FROM:",
                        "position": {
                            "left": 144.0,
                            "top": 237.0,
                            "width": 41.0,
                            "height": 11.0
                        },
                        "offset": 57
                    },
                    {
                        "text": "Gustafson",
                        "position": {
                            "left": 280.0,
                            "top": 238.0,
                            "width": 79.0,
                            "height": 11.0
                        },
                        "offset": 63
                    },
                    {
                        "text": "SUBJECT:",
                        "position": {
                            "left": 143.0,
                            "top": 267.0,
                            "width": 69.0,
                            "height": 11.0
                        },
                        "offset": 73
                    },
                    {
                        "text": "BATTLE",
                        "position": {
                            "left": 225.0,
                            "top": 268.0,
                            "width": 52.0,
                            "height": 10.0
                        },
                        "offset": 82
                    },
                    {
                        "text": "KIT",
                        "position": {
                            "left": 288.0,
                            "top": 268.0,
                            "width": 26.0,
                            "height": 11.0
                        },
                        "offset": 89
                    },
                    {
                        "text": "SUPPORT",
                        "position": {
                            "left": 324.0,
                            "top": 269.0,
                            "width": 62.0,
                            "height": 10.0
                        },
                        "offset": 93
                    },
                    {
                        "text": "HISTORY",
                        "position": {
                            "left": 397.0,
                            "top": 269.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 101
                    },
                    {
                        "text": "PURPOSE:",
                        "position": {
                            "left": 143.0,
                            "top": 312.0,
                            "width": 68.0,
                            "height": 11.0
                        },
                        "offset": 109
                    },
                    {
                        "text": "Response",
                        "position": {
                            "left": 143.0,
                            "top": 343.0,
                            "width": 70.0,
                            "height": 13.0
                        },
                        "offset": 118
                    },
                    {
                        "text": "to",
                        "position": {
                            "left": 225.0,
                            "top": 344.0,
                            "width": 16.0,
                            "height": 10.0
                        },
                        "offset": 127
                    },
                    {
                        "text": "your",
                        "position": {
                            "left": 252.0,
                            "top": 346.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 130
                    },
                    {
                        "text": "request",
                        "position": {
                            "left": 297.0,
                            "top": 344.0,
                            "width": 61.0,
                            "height": 13.0
                        },
                        "offset": 135
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 370.0,
                            "top": 344.0,
                            "width": 24.0,
                            "height": 11.0
                        },
                        "offset": 143
                    },
                    {
                        "text": "past",
                        "position": {
                            "left": 405.0,
                            "top": 345.0,
                            "width": 34.0,
                            "height": 13.0
                        },
                        "offset": 147
                    },
                    {
                        "text": "levels",
                        "position": {
                            "left": 451.0,
                            "top": 345.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 152
                    },
                    {
                        "text": "of",
                        "position": {
                            "left": 514.0,
                            "top": 345.0,
                            "width": 17.0,
                            "height": 11.0
                        },
                        "offset": 159
                    },
                    {
                        "text": "suppart",
                        "position": {
                            "left": 541.0,
                            "top": 346.0,
                            "width": 61.0,
                            "height": 13.0
                        },
                        "offset": 162
                    },
                    {
                        "text": "-",
                        "position": {
                            "left": 39.0,
                            "top": 366.0,
                            "width": 8.0,
                            "height": 4.0
                        },
                        "offset": 170
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 144.0,
                            "top": 357.0,
                            "width": 24.0,
                            "height": 12.0
                        },
                        "offset": 172
                    },
                    {
                        "text": "Battle",
                        "position": {
                            "left": 179.0,
                            "top": 358.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 176
                    },
                    {
                        "text": "Kit.",
                        "position": {
                            "left": 242.0,
                            "top": 359.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 183
                    },
                    {
                        "text": "DISCUSSION:",
                        "position": {
                            "left": 143.0,
                            "top": 404.0,
                            "width": 95.0,
                            "height": 11.0
                        },
                        "offset": 188
                    },
                    {
                        "text": "BATTLE",
                        "position": {
                            "left": 269.0,
                            "top": 436.0,
                            "width": 53.0,
                            "height": 10.0
                        },
                        "offset": 200
                    },
                    {
                        "text": "KIT",
                        "position": {
                            "left": 332.0,
                            "top": 437.0,
                            "width": 26.0,
                            "height": 10.0
                        },
                        "offset": 207
                    },
                    {
                        "text": "BUDGET",
                        "position": {
                            "left": 367.0,
                            "top": 436.0,
                            "width": 54.0,
                            "height": 11.0
                        },
                        "offset": 211
                    },
                    {
                        "text": "HISTORY",
                        "position": {
                            "left": 432.0,
                            "top": 437.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 218
                    },
                    {
                        "text": "PROPOSED",
                        "position": {
                            "left": 540.0,
                            "top": 468.0,
                            "width": 71.0,
                            "height": 11.0
                        },
                        "offset": 226
                    },
                    {
                        "text": "1980",
                        "position": {
                            "left": 160.0,
                            "top": 480.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 235
                    },
                    {
                        "text": "1981",
                        "position": {
                            "left": 260.0,
                            "top": 481.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 240
                    },
                    {
                        "text": "1982",
                        "position": {
                            "left": 359.0,
                            "top": 482.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 245
                    },
                    {
                        "text": "1983",
                        "position": {
                            "left": 459.0,
                            "top": 482.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 250
                    },
                    {
                        "text": "1984",
                        "position": {
                            "left": 558.0,
                            "top": 483.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 255
                    },
                    {
                        "text": "1.754M",
                        "position": {
                            "left": 142.0,
                            "top": 510.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 260
                    },
                    {
                        "text": "1,274MM",
                        "position": {
                            "left": 350.0,
                            "top": 512.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 267
                    },
                    {
                        "text": "BATTLE",
                        "position": {
                            "left": 277.0,
                            "top": 557.0,
                            "width": 52.0,
                            "height": 10.0
                        },
                        "offset": 275
                    },
                    {
                        "text": "KIT",
                        "position": {
                            "left": 340.0,
                            "top": 557.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 282
                    },
                    {
                        "text": "ITEM",
                        "position": {
                            "left": 377.0,
                            "top": 558.0,
                            "width": 34.0,
                            "height": 10.0
                        },
                        "offset": 286
                    },
                    {
                        "text": "HISTORY",
                        "position": {
                            "left": 422.0,
                            "top": 558.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 291
                    },
                    {
                        "text": "1980",
                        "position": {
                            "left": 159.0,
                            "top": 585.0,
                            "width": 35.0,
                            "height": 11.0
                        },
                        "offset": 299
                    },
                    {
                        "text": "1981",
                        "position": {
                            "left": 259.0,
                            "top": 586.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 304
                    },
                    {
                        "text": "1982",
                        "position": {
                            "left": 358.0,
                            "top": 587.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 309
                    },
                    {
                        "text": "1983",
                        "position": {
                            "left": 458.0,
                            "top": 588.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 314
                    },
                    {
                        "text": "1984",
                        "position": {
                            "left": 558.0,
                            "top": 589.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 319
                    },
                    {
                        "text": "2.2994M",
                        "position": {
                            "left": 150.0,
                            "top": 615.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 324
                    },
                    {
                        "text": "3.755MM",
                        "position": {
                            "left": 249.0,
                            "top": 616.0,
                            "width": 62.0,
                            "height": 11.0
                        },
                        "offset": 332
                    },
                    {
                        "text": "2.992MM",
                        "position": {
                            "left": 349.0,
                            "top": 617.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 340
                    },
                    {
                        "text": "\u201cBased",
                        "position": {
                            "left": 158.0,
                            "top": 646.0,
                            "width": 53.0,
                            "height": 10.0
                        },
                        "offset": 348
                    },
                    {
                        "text": "on",
                        "position": {
                            "left": 222.0,
                            "top": 648.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 355
                    },
                    {
                        "text": "budget",
                        "position": {
                            "left": 330.0,
                            "top": 647.0,
                            "width": 52.0,
                            "height": 13.0
                        },
                        "offset": 358
                    },
                    {
                        "text": "and",
                        "position": {
                            "left": 394.0,
                            "top": 648.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 365
                    },
                    {
                        "text": ".61",
                        "position": {
                            "left": 432.0,
                            "top": 648.0,
                            "width": 23.0,
                            "height": 10.0
                        },
                        "offset": 369
                    },
                    {
                        "text": "average",
                        "position": {
                            "left": 466.0,
                            "top": 651.0,
                            "width": 62.0,
                            "height": 11.0
                        },
                        "offset": 373
                    },
                    {
                        "text": "cost",
                        "position": {
                            "left": 539.0,
                            "top": 649.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 381
                    },
                    {
                        "text": "per",
                        "position": {
                            "left": 584.0,
                            "top": 652.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 386
                    },
                    {
                        "text": ":",
                        "position": {
                            "left": 77.0,
                            "top": 664.0,
                            "width": 2.0,
                            "height": 2.0
                        },
                        "offset": 390
                    },
                    {
                        "text": "item",
                        "position": {
                            "left": 167.0,
                            "top": 660.0,
                            "width": 35.0,
                            "height": 11.0
                        },
                        "offset": 392
                    },
                    {
                        "text": "in",
                        "position": {
                            "left": 213.0,
                            "top": 660.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 397
                    },
                    {
                        "text": "1983,",
                        "position": {
                            "left": 240.0,
                            "top": 660.0,
                            "width": 41.0,
                            "height": 12.0
                        },
                        "offset": 400
                    },
                    {
                        "text": "Because",
                        "position": {
                            "left": 140.0,
                            "top": 690.0,
                            "width": 61.0,
                            "height": 10.0
                        },
                        "offset": 406
                    },
                    {
                        "text": "there",
                        "position": {
                            "left": 212.0,
                            "top": 690.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 414
                    },
                    {
                        "text": "are",
                        "position": {
                            "left": 267.0,
                            "top": 693.0,
                            "width": 25.0,
                            "height": 8.0
                        },
                        "offset": 420
                    },
                    {
                        "text": "so",
                        "position": {
                            "left": 303.0,
                            "top": 693.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 424
                    },
                    {
                        "text": "many",
                        "position": {
                            "left": 330.0,
                            "top": 693.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 427
                    },
                    {
                        "text": "contradictory",
                        "position": {
                            "left": 375.0,
                            "top": 692.0,
                            "width": 115.0,
                            "height": 14.0
                        },
                        "offset": 432
                    },
                    {
                        "text": "recards",
                        "position": {
                            "left": 502.0,
                            "top": 694.0,
                            "width": 61.0,
                            "height": 10.0
                        },
                        "offset": 446
                    },
                    {
                        "text": "on",
                        "position": {
                            "left": 574.0,
                            "top": 696.0,
                            "width": 17.0,
                            "height": 8.0
                        },
                        "offset": 454
                    },
                    {
                        "text": "past",
                        "position": {
                            "left": 139.0,
                            "top": 705.0,
                            "width": 35.0,
                            "height": 12.0
                        },
                        "offset": 457
                    },
                    {
                        "text": "Battle",
                        "position": {
                            "left": 185.0,
                            "top": 705.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 462
                    },
                    {
                        "text": "Kit",
                        "position": {
                            "left": 248.0,
                            "top": 705.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 469
                    },
                    {
                        "text": "items,",
                        "position": {
                            "left": 285.0,
                            "top": 705.0,
                            "width": 50.0,
                            "height": 14.0
                        },
                        "offset": 473
                    },
                    {
                        "text": "it",
                        "position": {
                            "left": 348.0,
                            "top": 706.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 480
                    },
                    {
                        "text": "is",
                        "position": {
                            "left": 375.0,
                            "top": 706.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 483
                    },
                    {
                        "text": "impossiple",
                        "position": {
                            "left": 402.0,
                            "top": 707.0,
                            "width": 88.0,
                            "height": 13.0
                        },
                        "offset": 486
                    },
                    {
                        "text": "to",
                        "position": {
                            "left": 502.0,
                            "top": 708.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 497
                    },
                    {
                        "text": "determine",
                        "position": {
                            "left": 529.0,
                            "top": 708.0,
                            "width": 79.0,
                            "height": 12.0
                        },
                        "offset": 500
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 140.0,
                            "top": 720.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 510
                    },
                    {
                        "text": "actual",
                        "position": {
                            "left": 176.0,
                            "top": 720.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 514
                    },
                    {
                        "text": "figures",
                        "position": {
                            "left": 240.0,
                            "top": 720.0,
                            "width": 61.0,
                            "height": 13.0
                        },
                        "offset": 521
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 313.0,
                            "top": 721.0,
                            "width": 24.0,
                            "height": 10.0
                        },
                        "offset": 529
                    },
                    {
                        "text": "1980",
                        "position": {
                            "left": 348.0,
                            "top": 721.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 533
                    },
                    {
                        "text": "and",
                        "position": {
                            "left": 393.0,
                            "top": 722.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 538
                    },
                    {
                        "text": "1981.",
                        "position": {
                            "left": 430.0,
                            "top": 722.0,
                            "width": 41.0,
                            "height": 11.0
                        },
                        "offset": 542
                    },
                    {
                        "text": "The",
                        "position": {
                            "left": 493.0,
                            "top": 723.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 548
                    },
                    {
                        "text": "budget",
                        "position": {
                            "left": 529.0,
                            "top": 723.0,
                            "width": 52.0,
                            "height": 14.0
                        },
                        "offset": 552
                    },
                    {
                        "text": "figures",
                        "position": {
                            "left": 140.0,
                            "top": 735.0,
                            "width": 60.0,
                            "height": 13.0
                        },
                        "offset": 559
                    },
                    {
                        "text": "represent",
                        "position": {
                            "left": 212.0,
                            "top": 736.0,
                            "width": 79.0,
                            "height": 12.0
                        },
                        "offset": 567
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 303.0,
                            "top": 736.0,
                            "width": 24.0,
                            "height": 10.0
                        },
                        "offset": 577
                    },
                    {
                        "text": "amount",
                        "position": {
                            "left": 338.0,
                            "top": 736.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 581
                    },
                    {
                        "text": "spent",
                        "position": {
                            "left": 402.0,
                            "top": 737.0,
                            "width": 43.0,
                            "height": 13.0
                        },
                        "offset": 588
                    },
                    {
                        "text": "on",
                        "position": {
                            "left": 456.0,
                            "top": 740.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 594
                    },
                    {
                        "text": "@attle",
                        "position": {
                            "left": 483.0,
                            "top": 738.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 597
                    },
                    {
                        "text": "Kit",
                        "position": {
                            "left": 547.0,
                            "top": 739.0,
                            "width": 24.0,
                            "height": 11.0
                        },
                        "offset": 604
                    },
                    {
                        "text": "in",
                        "position": {
                            "left": 583.0,
                            "top": 739.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 608
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 610.0,
                            "top": 742.0,
                            "width": 7.0,
                            "height": 8.0
                        },
                        "offset": 611
                    },
                    {
                        "text": "given",
                        "position": {
                            "left": 139.0,
                            "top": 749.0,
                            "width": 44.0,
                            "height": 14.0
                        },
                        "offset": 613
                    },
                    {
                        "text": "year.",
                        "position": {
                            "left": 194.0,
                            "top": 752.0,
                            "width": 41.0,
                            "height": 11.0
                        },
                        "offset": 619
                    },
                    {
                        "text": "The",
                        "position": {
                            "left": 257.0,
                            "top": 750.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 625
                    },
                    {
                        "text": "item",
                        "position": {
                            "left": 294.0,
                            "top": 750.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 629
                    },
                    {
                        "text": "amounts",
                        "position": {
                            "left": 338.0,
                            "top": 752.0,
                            "width": 61.0,
                            "height": 10.0
                        },
                        "offset": 634
                    },
                    {
                        "text": "represent",
                        "position": {
                            "left": 411.0,
                            "top": 753.0,
                            "width": 79.0,
                            "height": 12.0
                        },
                        "offset": 642
                    },
                    {
                        "text": "what",
                        "position": {
                            "left": 501.0,
                            "top": 753.0,
                            "width": 35.0,
                            "height": 11.0
                        },
                        "offset": 652
                    },
                    {
                        "text": "was",
                        "position": {
                            "left": 547.0,
                            "top": 756.0,
                            "width": 25.0,
                            "height": 8.0
                        },
                        "offset": 657
                    },
                    {
                        "text": "available",
                        "position": {
                            "left": 139.0,
                            "top": 765.0,
                            "width": 79.0,
                            "height": 11.0
                        },
                        "offset": 661
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 230.0,
                            "top": 765.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 671
                    },
                    {
                        "text": "use",
                        "position": {
                            "left": 266.0,
                            "top": 768.0,
                            "width": 25.0,
                            "height": 9.0
                        },
                        "offset": 675
                    },
                    {
                        "text": "in",
                        "position": {
                            "left": 302.0,
                            "top": 766.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 679
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 329.0,
                            "top": 769.0,
                            "width": 7.0,
                            "height": 8.0
                        },
                        "offset": 682
                    },
                    {
                        "text": "given",
                        "position": {
                            "left": 347.0,
                            "top": 767.0,
                            "width": 43.0,
                            "height": 13.0
                        },
                        "offset": 684
                    },
                    {
                        "text": "yeat,",
                        "position": {
                            "left": 401.0,
                            "top": 770.0,
                            "width": 42.0,
                            "height": 11.0
                        },
                        "offset": 690
                    },
                    {
                        "text": "some",
                        "position": {
                            "left": 456.0,
                            "top": 771.0,
                            "width": 34.0,
                            "height": 8.0
                        },
                        "offset": 696
                    },
                    {
                        "text": "of",
                        "position": {
                            "left": 501.0,
                            "top": 768.0,
                            "width": 17.0,
                            "height": 11.0
                        },
                        "offset": 701
                    },
                    {
                        "text": "which",
                        "position": {
                            "left": 528.0,
                            "top": 769.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 704
                    },
                    {
                        "text": "were",
                        "position": {
                            "left": 582.0,
                            "top": 772.0,
                            "width": 35.0,
                            "height": 9.0
                        },
                        "offset": 710
                    },
                    {
                        "text": "carried",
                        "position": {
                            "left": 139.0,
                            "top": 780.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 715
                    },
                    {
                        "text": "over",
                        "position": {
                            "left": 211.0,
                            "top": 783.0,
                            "width": 35.0,
                            "height": 9.0
                        },
                        "offset": 723
                    },
                    {
                        "text": "from",
                        "position": {
                            "left": 258.0,
                            "top": 781.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 728
                    },
                    {
                        "text": "previous",
                        "position": {
                            "left": 302.0,
                            "top": 781.0,
                            "width": 70.0,
                            "height": 13.0
                        },
                        "offset": 733
                    },
                    {
                        "text": "years",
                        "position": {
                            "left": 383.0,
                            "top": 785.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 742
                    },
                    {
                        "text": "and",
                        "position": {
                            "left": 438.0,
                            "top": 783.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 748
                    },
                    {
                        "text": "SMP",
                        "position": {
                            "left": 474.0,
                            "top": 783.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 752
                    },
                    {
                        "text": "pragrams.",
                        "position": {
                            "left": 510.0,
                            "top": 786.0,
                            "width": 77.0,
                            "height": 11.0
                        },
                        "offset": 756
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 706.0,
                            "top": 787.0,
                            "width": 16.0,
                            "height": 13.0
                        },
                        "offset": 766
                    },
                    {
                        "text": "x",
                        "position": {
                            "left": 706.0,
                            "top": 801.0,
                            "width": 16.0,
                            "height": 13.0
                        },
                        "offset": 768
                    },
                    {
                        "text": "Let",
                        "position": {
                            "left": 139.0,
                            "top": 810.0,
                            "width": 24.0,
                            "height": 11.0
                        },
                        "offset": 770
                    },
                    {
                        "text": "me",
                        "position": {
                            "left": 174.0,
                            "top": 813.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 774
                    },
                    {
                        "text": "know",
                        "position": {
                            "left": 202.0,
                            "top": 811.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 777
                    },
                    {
                        "text": "if",
                        "position": {
                            "left": 247.0,
                            "top": 811.0,
                            "width": 17.0,
                            "height": 11.0
                        },
                        "offset": 782
                    },
                    {
                        "text": "you",
                        "position": {
                            "left": 274.0,
                            "top": 814.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 785
                    },
                    {
                        "text": "need",
                        "position": {
                            "left": 310.0,
                            "top": 812.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 789
                    },
                    {
                        "text": "additional",
                        "position": {
                            "left": 355.0,
                            "top": 812.0,
                            "width": 89.0,
                            "height": 12.0
                        },
                        "offset": 794
                    },
                    {
                        "text": "information.",
                        "position": {
                            "left": 456.0,
                            "top": 813.0,
                            "width": 104.0,
                            "height": 12.0
                        },
                        "offset": 805
                    },
                    {
                        "text": "rey",
                        "position": {
                            "left": 705.0,
                            "top": 842.0,
                            "width": 16.0,
                            "height": 12.0
                        },
                        "offset": 818
                    },
                    {
                        "text": "g",
                        "position": {
                            "left": 704.0,
                            "top": 869.0,
                            "width": 17.0,
                            "height": 41.0
                        },
                        "offset": 822
                    }
                ],
                "source": {
                    "width": 774,
                    "height": 1000
                }
            }
        ]
    },
    "task_4": [
        {
            "facts": [
                {
                    "text": "MEMORANDUM",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "MEMORANDUM",
                            "position": {
                                "left": 145.0,
                                "top": 86.0,
                                "width": 88.0,
                                "height": 11.0
                            },
                            "offset": 0
                        }
                    ]
                },
                {
                    "text": "July 29, 1983",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "July",
                            "position": {
                                "left": 145.0,
                                "top": 116.0,
                                "width": 33.0,
                                "height": 14.0
                            },
                            "offset": 11
                        },
                        {
                            "text": "29,",
                            "position": {
                                "left": 190.0,
                                "top": 117.0,
                                "width": 23.0,
                                "height": 13.0
                            },
                            "offset": 16
                        },
                        {
                            "text": "1983",
                            "position": {
                                "left": 226.0,
                                "top": 117.0,
                                "width": 35.0,
                                "height": 11.0
                            },
                            "offset": 20
                        }
                    ]
                },
                {
                    "text": "To:",
                    "tag": "O",
                    "tokens": {
                        "text": "To:",
                        "position": {
                            "left": 145.0,
                            "top": 177.0,
                            "width": 22.0,
                            "height": 11.0
                        },
                        "offset": 25
                    }
                },
                {
                    "text": "R. D",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "R.",
                            "position": {
                                "left": 226.0,
                                "top": 178.0,
                                "width": 14.0,
                                "height": 11.0
                            },
                            "offset": 29
                        },
                        {
                            "text": "D,",
                            "position": {
                                "left": 253.0,
                                "top": 178.0,
                                "width": 14.0,
                                "height": 11.0
                            },
                            "offset": 32
                        }
                    ]
                },
                {
                    "text": "Sharp",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Sharp",
                            "position": {
                                "left": 280.0,
                                "top": 178.0,
                                "width": 43.0,
                                "height": 13.0
                            },
                            "offset": 35
                        }
                    ]
                },
                {
                    "text": "cc:",
                    "tag": "O",
                    "tokens": {
                        "text": "cc:",
                        "position": {
                            "left": 144.0,
                            "top": 207.0,
                            "width": 23.0,
                            "height": 11.0
                        },
                        "offset": 41
                    }
                },
                {
                    "text": "M. J. Novak",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "M.",
                            "position": {
                                "left": 225.0,
                                "top": 208.0,
                                "width": 15.0,
                                "height": 10.0
                            },
                            "offset": 45
                        },
                        {
                            "text": "J.",
                            "position": {
                                "left": 253.0,
                                "top": 208.0,
                                "width": 14.0,
                                "height": 11.0
                            },
                            "offset": 48
                        },
                        {
                            "text": "Novak",
                            "position": {
                                "left": 280.0,
                                "top": 208.0,
                                "width": 43.0,
                                "height": 11.0
                            },
                            "offset": 51
                        }
                    ]
                },
                {
                    "text": "FROM:",
                    "tag": "O",
                    "tokens": {
                        "text": "FROM:",
                        "position": {
                            "left": 144.0,
                            "top": 237.0,
                            "width": 41.0,
                            "height": 11.0
                        },
                        "offset": 57
                    }
                },
                {
                    "text": "Gustafson SUBJECT",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "Gustafson",
                            "position": {
                                "left": 280.0,
                                "top": 238.0,
                                "width": 79.0,
                                "height": 11.0
                            },
                            "offset": 63
                        },
                        {
                            "text": "SUBJECT:",
                            "position": {
                                "left": 143.0,
                                "top": 267.0,
                                "width": 69.0,
                                "height": 11.0
                            },
                            "offset": 73
                        }
                    ]
                },
                {
                    "text": "BATTLE",
                    "tag": "O",
                    "tokens": {
                        "text": "BATTLE",
                        "position": {
                            "left": 225.0,
                            "top": 268.0,
                            "width": 52.0,
                            "height": 10.0
                        },
                        "offset": 82
                    }
                },
                {
                    "text": "KIT",
                    "tag": "O",
                    "tokens": {
                        "text": "KIT",
                        "position": {
                            "left": 288.0,
                            "top": 268.0,
                            "width": 26.0,
                            "height": 11.0
                        },
                        "offset": 89
                    }
                },
                {
                    "text": "SUPPORT",
                    "tag": "O",
                    "tokens": {
                        "text": "SUPPORT",
                        "position": {
                            "left": 324.0,
                            "top": 269.0,
                            "width": 62.0,
                            "height": 10.0
                        },
                        "offset": 93
                    }
                },
                {
                    "text": "HISTORY",
                    "tag": "O",
                    "tokens": {
                        "text": "HISTORY",
                        "position": {
                            "left": 397.0,
                            "top": 269.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 101
                    }
                },
                {
                    "text": "PURPOSE:",
                    "tag": "O",
                    "tokens": {
                        "text": "PURPOSE:",
                        "position": {
                            "left": 143.0,
                            "top": 312.0,
                            "width": 68.0,
                            "height": 11.0
                        },
                        "offset": 109
                    }
                },
                {
                    "text": "Response",
                    "tag": "O",
                    "tokens": {
                        "text": "Response",
                        "position": {
                            "left": 143.0,
                            "top": 343.0,
                            "width": 70.0,
                            "height": 13.0
                        },
                        "offset": 118
                    }
                },
                {
                    "text": "to",
                    "tag": "O",
                    "tokens": {
                        "text": "to",
                        "position": {
                            "left": 225.0,
                            "top": 344.0,
                            "width": 16.0,
                            "height": 10.0
                        },
                        "offset": 127
                    }
                },
                {
                    "text": "your",
                    "tag": "O",
                    "tokens": {
                        "text": "your",
                        "position": {
                            "left": 252.0,
                            "top": 346.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 130
                    }
                },
                {
                    "text": "request",
                    "tag": "O",
                    "tokens": {
                        "text": "request",
                        "position": {
                            "left": 297.0,
                            "top": 344.0,
                            "width": 61.0,
                            "height": 13.0
                        },
                        "offset": 135
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 370.0,
                            "top": 344.0,
                            "width": 24.0,
                            "height": 11.0
                        },
                        "offset": 143
                    }
                },
                {
                    "text": "past",
                    "tag": "O",
                    "tokens": {
                        "text": "past",
                        "position": {
                            "left": 405.0,
                            "top": 345.0,
                            "width": 34.0,
                            "height": 13.0
                        },
                        "offset": 147
                    }
                },
                {
                    "text": "levels",
                    "tag": "O",
                    "tokens": {
                        "text": "levels",
                        "position": {
                            "left": 451.0,
                            "top": 345.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 152
                    }
                },
                {
                    "text": "of",
                    "tag": "O",
                    "tokens": {
                        "text": "of",
                        "position": {
                            "left": 514.0,
                            "top": 345.0,
                            "width": 17.0,
                            "height": 11.0
                        },
                        "offset": 159
                    }
                },
                {
                    "text": "suppart",
                    "tag": "O",
                    "tokens": {
                        "text": "suppart",
                        "position": {
                            "left": 541.0,
                            "top": 346.0,
                            "width": 61.0,
                            "height": 13.0
                        },
                        "offset": 162
                    }
                },
                {
                    "text": "-",
                    "tag": "O",
                    "tokens": {
                        "text": "-",
                        "position": {
                            "left": 39.0,
                            "top": 366.0,
                            "width": 8.0,
                            "height": 4.0
                        },
                        "offset": 170
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 144.0,
                            "top": 357.0,
                            "width": 24.0,
                            "height": 12.0
                        },
                        "offset": 172
                    }
                },
                {
                    "text": "Battle",
                    "tag": "O",
                    "tokens": {
                        "text": "Battle",
                        "position": {
                            "left": 179.0,
                            "top": 358.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 176
                    }
                },
                {
                    "text": "Kit.",
                    "tag": "O",
                    "tokens": {
                        "text": "Kit.",
                        "position": {
                            "left": 242.0,
                            "top": 359.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 183
                    }
                },
                {
                    "text": "DISCUSSION:",
                    "tag": "O",
                    "tokens": {
                        "text": "DISCUSSION:",
                        "position": {
                            "left": 143.0,
                            "top": 404.0,
                            "width": 95.0,
                            "height": 11.0
                        },
                        "offset": 188
                    }
                },
                {
                    "text": "BATTLE",
                    "tag": "O",
                    "tokens": {
                        "text": "BATTLE",
                        "position": {
                            "left": 269.0,
                            "top": 436.0,
                            "width": 53.0,
                            "height": 10.0
                        },
                        "offset": 200
                    }
                },
                {
                    "text": "KIT",
                    "tag": "O",
                    "tokens": {
                        "text": "KIT",
                        "position": {
                            "left": 332.0,
                            "top": 437.0,
                            "width": 26.0,
                            "height": 10.0
                        },
                        "offset": 207
                    }
                },
                {
                    "text": "BUDGET",
                    "tag": "O",
                    "tokens": {
                        "text": "BUDGET",
                        "position": {
                            "left": 367.0,
                            "top": 436.0,
                            "width": 54.0,
                            "height": 11.0
                        },
                        "offset": 211
                    }
                },
                {
                    "text": "HISTORY",
                    "tag": "O",
                    "tokens": {
                        "text": "HISTORY",
                        "position": {
                            "left": 432.0,
                            "top": 437.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 218
                    }
                },
                {
                    "text": "PROPOSED",
                    "tag": "O",
                    "tokens": {
                        "text": "PROPOSED",
                        "position": {
                            "left": 540.0,
                            "top": 468.0,
                            "width": 71.0,
                            "height": 11.0
                        },
                        "offset": 226
                    }
                },
                {
                    "text": "1980 1981",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "1980",
                            "position": {
                                "left": 160.0,
                                "top": 480.0,
                                "width": 34.0,
                                "height": 11.0
                            },
                            "offset": 235
                        },
                        {
                            "text": "1981",
                            "position": {
                                "left": 260.0,
                                "top": 481.0,
                                "width": 33.0,
                                "height": 11.0
                            },
                            "offset": 240
                        }
                    ]
                },
                {
                    "text": "1982",
                    "tag": "O",
                    "tokens": {
                        "text": "1982",
                        "position": {
                            "left": 359.0,
                            "top": 482.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 245
                    }
                },
                {
                    "text": "1983",
                    "tag": "O",
                    "tokens": {
                        "text": "1983",
                        "position": {
                            "left": 459.0,
                            "top": 482.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 250
                    }
                },
                {
                    "text": "1984",
                    "tag": "O",
                    "tokens": {
                        "text": "1984",
                        "position": {
                            "left": 558.0,
                            "top": 483.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 255
                    }
                },
                {
                    "text": "1.754M 1,274MM",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "1.754M",
                            "position": {
                                "left": 142.0,
                                "top": 510.0,
                                "width": 52.0,
                                "height": 11.0
                            },
                            "offset": 260
                        },
                        {
                            "text": "1,274MM",
                            "position": {
                                "left": 350.0,
                                "top": 512.0,
                                "width": 61.0,
                                "height": 11.0
                            },
                            "offset": 267
                        }
                    ]
                },
                {
                    "text": "BATTLE",
                    "tag": "O",
                    "tokens": {
                        "text": "BATTLE",
                        "position": {
                            "left": 277.0,
                            "top": 557.0,
                            "width": 52.0,
                            "height": 10.0
                        },
                        "offset": 275
                    }
                },
                {
                    "text": "KIT",
                    "tag": "O",
                    "tokens": {
                        "text": "KIT",
                        "position": {
                            "left": 340.0,
                            "top": 557.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 282
                    }
                },
                {
                    "text": "ITEM",
                    "tag": "O",
                    "tokens": {
                        "text": "ITEM",
                        "position": {
                            "left": 377.0,
                            "top": 558.0,
                            "width": 34.0,
                            "height": 10.0
                        },
                        "offset": 286
                    }
                },
                {
                    "text": "HISTORY",
                    "tag": "O",
                    "tokens": {
                        "text": "HISTORY",
                        "position": {
                            "left": 422.0,
                            "top": 558.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 291
                    }
                },
                {
                    "text": "1980",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "1980",
                            "position": {
                                "left": 159.0,
                                "top": 585.0,
                                "width": 35.0,
                                "height": 11.0
                            },
                            "offset": 299
                        }
                    ]
                },
                {
                    "text": "1981",
                    "tag": "O",
                    "tokens": {
                        "text": "1981",
                        "position": {
                            "left": 259.0,
                            "top": 586.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 304
                    }
                },
                {
                    "text": "1982",
                    "tag": "O",
                    "tokens": {
                        "text": "1982",
                        "position": {
                            "left": 358.0,
                            "top": 587.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 309
                    }
                },
                {
                    "text": "1983",
                    "tag": "O",
                    "tokens": {
                        "text": "1983",
                        "position": {
                            "left": 458.0,
                            "top": 588.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 314
                    }
                },
                {
                    "text": "1984",
                    "tag": "O",
                    "tokens": {
                        "text": "1984",
                        "position": {
                            "left": 558.0,
                            "top": 589.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 319
                    }
                },
                {
                    "text": "2.2994",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "2.2994M",
                            "position": {
                                "left": 150.0,
                                "top": 615.0,
                                "width": 61.0,
                                "height": 11.0
                            },
                            "offset": 324
                        }
                    ]
                },
                {
                    "text": "3.755MM",
                    "tag": "O",
                    "tokens": {
                        "text": "3.755MM",
                        "position": {
                            "left": 249.0,
                            "top": 616.0,
                            "width": 62.0,
                            "height": 11.0
                        },
                        "offset": 332
                    }
                },
                {
                    "text": "2.992MM",
                    "tag": "O",
                    "tokens": {
                        "text": "2.992MM",
                        "position": {
                            "left": 349.0,
                            "top": 617.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 340
                    }
                },
                {
                    "text": "\u201cBased",
                    "tag": "O",
                    "tokens": {
                        "text": "\u201cBased",
                        "position": {
                            "left": 158.0,
                            "top": 646.0,
                            "width": 53.0,
                            "height": 10.0
                        },
                        "offset": 348
                    }
                },
                {
                    "text": "on",
                    "tag": "O",
                    "tokens": {
                        "text": "on",
                        "position": {
                            "left": 222.0,
                            "top": 648.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 355
                    }
                },
                {
                    "text": "budget",
                    "tag": "O",
                    "tokens": {
                        "text": "budget",
                        "position": {
                            "left": 330.0,
                            "top": 647.0,
                            "width": 52.0,
                            "height": 13.0
                        },
                        "offset": 358
                    }
                },
                {
                    "text": "and",
                    "tag": "O",
                    "tokens": {
                        "text": "and",
                        "position": {
                            "left": 394.0,
                            "top": 648.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 365
                    }
                },
                {
                    "text": ".61",
                    "tag": "O",
                    "tokens": {
                        "text": ".61",
                        "position": {
                            "left": 432.0,
                            "top": 648.0,
                            "width": 23.0,
                            "height": 10.0
                        },
                        "offset": 369
                    }
                },
                {
                    "text": "average",
                    "tag": "O",
                    "tokens": {
                        "text": "average",
                        "position": {
                            "left": 466.0,
                            "top": 651.0,
                            "width": 62.0,
                            "height": 11.0
                        },
                        "offset": 373
                    }
                },
                {
                    "text": "cost",
                    "tag": "O",
                    "tokens": {
                        "text": "cost",
                        "position": {
                            "left": 539.0,
                            "top": 649.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 381
                    }
                },
                {
                    "text": "per",
                    "tag": "O",
                    "tokens": {
                        "text": "per",
                        "position": {
                            "left": 584.0,
                            "top": 652.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 386
                    }
                },
                {
                    "text": ":",
                    "tag": "O",
                    "tokens": {
                        "text": ":",
                        "position": {
                            "left": 77.0,
                            "top": 664.0,
                            "width": 2.0,
                            "height": 2.0
                        },
                        "offset": 390
                    }
                },
                {
                    "text": "item",
                    "tag": "O",
                    "tokens": {
                        "text": "item",
                        "position": {
                            "left": 167.0,
                            "top": 660.0,
                            "width": 35.0,
                            "height": 11.0
                        },
                        "offset": 392
                    }
                },
                {
                    "text": "in",
                    "tag": "O",
                    "tokens": {
                        "text": "in",
                        "position": {
                            "left": 213.0,
                            "top": 660.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 397
                    }
                },
                {
                    "text": "1983",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "1983,",
                            "position": {
                                "left": 240.0,
                                "top": 660.0,
                                "width": 41.0,
                                "height": 12.0
                            },
                            "offset": 400
                        }
                    ]
                },
                {
                    "text": "Because",
                    "tag": "O",
                    "tokens": {
                        "text": "Because",
                        "position": {
                            "left": 140.0,
                            "top": 690.0,
                            "width": 61.0,
                            "height": 10.0
                        },
                        "offset": 406
                    }
                },
                {
                    "text": "there",
                    "tag": "O",
                    "tokens": {
                        "text": "there",
                        "position": {
                            "left": 212.0,
                            "top": 690.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 414
                    }
                },
                {
                    "text": "are",
                    "tag": "O",
                    "tokens": {
                        "text": "are",
                        "position": {
                            "left": 267.0,
                            "top": 693.0,
                            "width": 25.0,
                            "height": 8.0
                        },
                        "offset": 420
                    }
                },
                {
                    "text": "so",
                    "tag": "O",
                    "tokens": {
                        "text": "so",
                        "position": {
                            "left": 303.0,
                            "top": 693.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 424
                    }
                },
                {
                    "text": "many",
                    "tag": "O",
                    "tokens": {
                        "text": "many",
                        "position": {
                            "left": 330.0,
                            "top": 693.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 427
                    }
                },
                {
                    "text": "contradictory",
                    "tag": "O",
                    "tokens": {
                        "text": "contradictory",
                        "position": {
                            "left": 375.0,
                            "top": 692.0,
                            "width": 115.0,
                            "height": 14.0
                        },
                        "offset": 432
                    }
                },
                {
                    "text": "recards",
                    "tag": "O",
                    "tokens": {
                        "text": "recards",
                        "position": {
                            "left": 502.0,
                            "top": 694.0,
                            "width": 61.0,
                            "height": 10.0
                        },
                        "offset": 446
                    }
                },
                {
                    "text": "on",
                    "tag": "O",
                    "tokens": {
                        "text": "on",
                        "position": {
                            "left": 574.0,
                            "top": 696.0,
                            "width": 17.0,
                            "height": 8.0
                        },
                        "offset": 454
                    }
                },
                {
                    "text": "past",
                    "tag": "O",
                    "tokens": {
                        "text": "past",
                        "position": {
                            "left": 139.0,
                            "top": 705.0,
                            "width": 35.0,
                            "height": 12.0
                        },
                        "offset": 457
                    }
                },
                {
                    "text": "Battle Kit",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Battle",
                            "position": {
                                "left": 185.0,
                                "top": 705.0,
                                "width": 52.0,
                                "height": 11.0
                            },
                            "offset": 462
                        },
                        {
                            "text": "Kit",
                            "position": {
                                "left": 248.0,
                                "top": 705.0,
                                "width": 25.0,
                                "height": 11.0
                            },
                            "offset": 469
                        }
                    ]
                },
                {
                    "text": "items,",
                    "tag": "O",
                    "tokens": {
                        "text": "items,",
                        "position": {
                            "left": 285.0,
                            "top": 705.0,
                            "width": 50.0,
                            "height": 14.0
                        },
                        "offset": 473
                    }
                },
                {
                    "text": "it",
                    "tag": "O",
                    "tokens": {
                        "text": "it",
                        "position": {
                            "left": 348.0,
                            "top": 706.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 480
                    }
                },
                {
                    "text": "is",
                    "tag": "O",
                    "tokens": {
                        "text": "is",
                        "position": {
                            "left": 375.0,
                            "top": 706.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 483
                    }
                },
                {
                    "text": "impossiple",
                    "tag": "O",
                    "tokens": {
                        "text": "impossiple",
                        "position": {
                            "left": 402.0,
                            "top": 707.0,
                            "width": 88.0,
                            "height": 13.0
                        },
                        "offset": 486
                    }
                },
                {
                    "text": "to",
                    "tag": "O",
                    "tokens": {
                        "text": "to",
                        "position": {
                            "left": 502.0,
                            "top": 708.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 497
                    }
                },
                {
                    "text": "determine",
                    "tag": "O",
                    "tokens": {
                        "text": "determine",
                        "position": {
                            "left": 529.0,
                            "top": 708.0,
                            "width": 79.0,
                            "height": 12.0
                        },
                        "offset": 500
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 140.0,
                            "top": 720.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 510
                    }
                },
                {
                    "text": "actual",
                    "tag": "O",
                    "tokens": {
                        "text": "actual",
                        "position": {
                            "left": 176.0,
                            "top": 720.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 514
                    }
                },
                {
                    "text": "figures",
                    "tag": "O",
                    "tokens": {
                        "text": "figures",
                        "position": {
                            "left": 240.0,
                            "top": 720.0,
                            "width": 61.0,
                            "height": 13.0
                        },
                        "offset": 521
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 313.0,
                            "top": 721.0,
                            "width": 24.0,
                            "height": 10.0
                        },
                        "offset": 529
                    }
                },
                {
                    "text": "1980",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "1980",
                            "position": {
                                "left": 348.0,
                                "top": 721.0,
                                "width": 34.0,
                                "height": 11.0
                            },
                            "offset": 533
                        }
                    ]
                },
                {
                    "text": "and",
                    "tag": "O",
                    "tokens": {
                        "text": "and",
                        "position": {
                            "left": 393.0,
                            "top": 722.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 538
                    }
                },
                {
                    "text": "1981",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "1981.",
                            "position": {
                                "left": 430.0,
                                "top": 722.0,
                                "width": 41.0,
                                "height": 11.0
                            },
                            "offset": 542
                        }
                    ]
                },
                {
                    "text": "The",
                    "tag": "O",
                    "tokens": {
                        "text": "The",
                        "position": {
                            "left": 493.0,
                            "top": 723.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 548
                    }
                },
                {
                    "text": "budget",
                    "tag": "O",
                    "tokens": {
                        "text": "budget",
                        "position": {
                            "left": 529.0,
                            "top": 723.0,
                            "width": 52.0,
                            "height": 14.0
                        },
                        "offset": 552
                    }
                },
                {
                    "text": "figures",
                    "tag": "O",
                    "tokens": {
                        "text": "figures",
                        "position": {
                            "left": 140.0,
                            "top": 735.0,
                            "width": 60.0,
                            "height": 13.0
                        },
                        "offset": 559
                    }
                },
                {
                    "text": "represent",
                    "tag": "O",
                    "tokens": {
                        "text": "represent",
                        "position": {
                            "left": 212.0,
                            "top": 736.0,
                            "width": 79.0,
                            "height": 12.0
                        },
                        "offset": 567
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 303.0,
                            "top": 736.0,
                            "width": 24.0,
                            "height": 10.0
                        },
                        "offset": 577
                    }
                },
                {
                    "text": "amount",
                    "tag": "O",
                    "tokens": {
                        "text": "amount",
                        "position": {
                            "left": 338.0,
                            "top": 736.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 581
                    }
                },
                {
                    "text": "spent",
                    "tag": "O",
                    "tokens": {
                        "text": "spent",
                        "position": {
                            "left": 402.0,
                            "top": 737.0,
                            "width": 43.0,
                            "height": 13.0
                        },
                        "offset": 588
                    }
                },
                {
                    "text": "on",
                    "tag": "O",
                    "tokens": {
                        "text": "on",
                        "position": {
                            "left": 456.0,
                            "top": 740.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 594
                    }
                },
                {
                    "text": "@attle",
                    "tag": "O",
                    "tokens": {
                        "text": "@attle",
                        "position": {
                            "left": 483.0,
                            "top": 738.0,
                            "width": 52.0,
                            "height": 11.0
                        },
                        "offset": 597
                    }
                },
                {
                    "text": "Kit",
                    "tag": "O",
                    "tokens": {
                        "text": "Kit",
                        "position": {
                            "left": 547.0,
                            "top": 739.0,
                            "width": 24.0,
                            "height": 11.0
                        },
                        "offset": 604
                    }
                },
                {
                    "text": "in",
                    "tag": "O",
                    "tokens": {
                        "text": "in",
                        "position": {
                            "left": 583.0,
                            "top": 739.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 608
                    }
                },
                {
                    "text": "a given year",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "a",
                            "position": {
                                "left": 610.0,
                                "top": 742.0,
                                "width": 7.0,
                                "height": 8.0
                            },
                            "offset": 611
                        },
                        {
                            "text": "given",
                            "position": {
                                "left": 139.0,
                                "top": 749.0,
                                "width": 44.0,
                                "height": 14.0
                            },
                            "offset": 613
                        },
                        {
                            "text": "year.",
                            "position": {
                                "left": 194.0,
                                "top": 752.0,
                                "width": 41.0,
                                "height": 11.0
                            },
                            "offset": 619
                        }
                    ]
                },
                {
                    "text": "The",
                    "tag": "O",
                    "tokens": {
                        "text": "The",
                        "position": {
                            "left": 257.0,
                            "top": 750.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 625
                    }
                },
                {
                    "text": "item",
                    "tag": "O",
                    "tokens": {
                        "text": "item",
                        "position": {
                            "left": 294.0,
                            "top": 750.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 629
                    }
                },
                {
                    "text": "amounts",
                    "tag": "O",
                    "tokens": {
                        "text": "amounts",
                        "position": {
                            "left": 338.0,
                            "top": 752.0,
                            "width": 61.0,
                            "height": 10.0
                        },
                        "offset": 634
                    }
                },
                {
                    "text": "represent",
                    "tag": "O",
                    "tokens": {
                        "text": "represent",
                        "position": {
                            "left": 411.0,
                            "top": 753.0,
                            "width": 79.0,
                            "height": 12.0
                        },
                        "offset": 642
                    }
                },
                {
                    "text": "what",
                    "tag": "O",
                    "tokens": {
                        "text": "what",
                        "position": {
                            "left": 501.0,
                            "top": 753.0,
                            "width": 35.0,
                            "height": 11.0
                        },
                        "offset": 652
                    }
                },
                {
                    "text": "was",
                    "tag": "O",
                    "tokens": {
                        "text": "was",
                        "position": {
                            "left": 547.0,
                            "top": 756.0,
                            "width": 25.0,
                            "height": 8.0
                        },
                        "offset": 657
                    }
                },
                {
                    "text": "available",
                    "tag": "O",
                    "tokens": {
                        "text": "available",
                        "position": {
                            "left": 139.0,
                            "top": 765.0,
                            "width": 79.0,
                            "height": 11.0
                        },
                        "offset": 661
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 230.0,
                            "top": 765.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 671
                    }
                },
                {
                    "text": "use",
                    "tag": "O",
                    "tokens": {
                        "text": "use",
                        "position": {
                            "left": 266.0,
                            "top": 768.0,
                            "width": 25.0,
                            "height": 9.0
                        },
                        "offset": 675
                    }
                },
                {
                    "text": "in",
                    "tag": "O",
                    "tokens": {
                        "text": "in",
                        "position": {
                            "left": 302.0,
                            "top": 766.0,
                            "width": 16.0,
                            "height": 11.0
                        },
                        "offset": 679
                    }
                },
                {
                    "text": "a",
                    "tag": "O",
                    "tokens": {
                        "text": "a",
                        "position": {
                            "left": 329.0,
                            "top": 769.0,
                            "width": 7.0,
                            "height": 8.0
                        },
                        "offset": 682
                    }
                },
                {
                    "text": "given",
                    "tag": "O",
                    "tokens": {
                        "text": "given",
                        "position": {
                            "left": 347.0,
                            "top": 767.0,
                            "width": 43.0,
                            "height": 13.0
                        },
                        "offset": 684
                    }
                },
                {
                    "text": "yeat,",
                    "tag": "O",
                    "tokens": {
                        "text": "yeat,",
                        "position": {
                            "left": 401.0,
                            "top": 770.0,
                            "width": 42.0,
                            "height": 11.0
                        },
                        "offset": 690
                    }
                },
                {
                    "text": "some",
                    "tag": "O",
                    "tokens": {
                        "text": "some",
                        "position": {
                            "left": 456.0,
                            "top": 771.0,
                            "width": 34.0,
                            "height": 8.0
                        },
                        "offset": 696
                    }
                },
                {
                    "text": "of",
                    "tag": "O",
                    "tokens": {
                        "text": "of",
                        "position": {
                            "left": 501.0,
                            "top": 768.0,
                            "width": 17.0,
                            "height": 11.0
                        },
                        "offset": 701
                    }
                },
                {
                    "text": "which",
                    "tag": "O",
                    "tokens": {
                        "text": "which",
                        "position": {
                            "left": 528.0,
                            "top": 769.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 704
                    }
                },
                {
                    "text": "were",
                    "tag": "O",
                    "tokens": {
                        "text": "were",
                        "position": {
                            "left": 582.0,
                            "top": 772.0,
                            "width": 35.0,
                            "height": 9.0
                        },
                        "offset": 710
                    }
                },
                {
                    "text": "carried",
                    "tag": "O",
                    "tokens": {
                        "text": "carried",
                        "position": {
                            "left": 139.0,
                            "top": 780.0,
                            "width": 61.0,
                            "height": 11.0
                        },
                        "offset": 715
                    }
                },
                {
                    "text": "over",
                    "tag": "O",
                    "tokens": {
                        "text": "over",
                        "position": {
                            "left": 211.0,
                            "top": 783.0,
                            "width": 35.0,
                            "height": 9.0
                        },
                        "offset": 723
                    }
                },
                {
                    "text": "from",
                    "tag": "O",
                    "tokens": {
                        "text": "from",
                        "position": {
                            "left": 258.0,
                            "top": 781.0,
                            "width": 33.0,
                            "height": 11.0
                        },
                        "offset": 728
                    }
                },
                {
                    "text": "previous years",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "previous",
                            "position": {
                                "left": 302.0,
                                "top": 781.0,
                                "width": 70.0,
                                "height": 13.0
                            },
                            "offset": 733
                        },
                        {
                            "text": "years",
                            "position": {
                                "left": 383.0,
                                "top": 785.0,
                                "width": 44.0,
                                "height": 11.0
                            },
                            "offset": 742
                        }
                    ]
                },
                {
                    "text": "and",
                    "tag": "O",
                    "tokens": {
                        "text": "and",
                        "position": {
                            "left": 438.0,
                            "top": 783.0,
                            "width": 25.0,
                            "height": 10.0
                        },
                        "offset": 748
                    }
                },
                {
                    "text": "SMP",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "SMP",
                            "position": {
                                "left": 474.0,
                                "top": 783.0,
                                "width": 25.0,
                                "height": 11.0
                            },
                            "offset": 752
                        }
                    ]
                },
                {
                    "text": "pragrams.",
                    "tag": "O",
                    "tokens": {
                        "text": "pragrams.",
                        "position": {
                            "left": 510.0,
                            "top": 786.0,
                            "width": 77.0,
                            "height": 11.0
                        },
                        "offset": 756
                    }
                },
                {
                    "text": "a",
                    "tag": "O",
                    "tokens": {
                        "text": "a",
                        "position": {
                            "left": 706.0,
                            "top": 787.0,
                            "width": 16.0,
                            "height": 13.0
                        },
                        "offset": 766
                    }
                },
                {
                    "text": "x",
                    "tag": "O",
                    "tokens": {
                        "text": "x",
                        "position": {
                            "left": 706.0,
                            "top": 801.0,
                            "width": 16.0,
                            "height": 13.0
                        },
                        "offset": 768
                    }
                },
                {
                    "text": "Let",
                    "tag": "O",
                    "tokens": {
                        "text": "Let",
                        "position": {
                            "left": 139.0,
                            "top": 810.0,
                            "width": 24.0,
                            "height": 11.0
                        },
                        "offset": 770
                    }
                },
                {
                    "text": "me",
                    "tag": "O",
                    "tokens": {
                        "text": "me",
                        "position": {
                            "left": 174.0,
                            "top": 813.0,
                            "width": 16.0,
                            "height": 8.0
                        },
                        "offset": 774
                    }
                },
                {
                    "text": "know",
                    "tag": "O",
                    "tokens": {
                        "text": "know",
                        "position": {
                            "left": 202.0,
                            "top": 811.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 777
                    }
                },
                {
                    "text": "if",
                    "tag": "O",
                    "tokens": {
                        "text": "if",
                        "position": {
                            "left": 247.0,
                            "top": 811.0,
                            "width": 17.0,
                            "height": 11.0
                        },
                        "offset": 782
                    }
                },
                {
                    "text": "you",
                    "tag": "O",
                    "tokens": {
                        "text": "you",
                        "position": {
                            "left": 274.0,
                            "top": 814.0,
                            "width": 25.0,
                            "height": 11.0
                        },
                        "offset": 785
                    }
                },
                {
                    "text": "need",
                    "tag": "O",
                    "tokens": {
                        "text": "need",
                        "position": {
                            "left": 310.0,
                            "top": 812.0,
                            "width": 34.0,
                            "height": 11.0
                        },
                        "offset": 789
                    }
                },
                {
                    "text": "additional",
                    "tag": "O",
                    "tokens": {
                        "text": "additional",
                        "position": {
                            "left": 355.0,
                            "top": 812.0,
                            "width": 89.0,
                            "height": 12.0
                        },
                        "offset": 794
                    }
                },
                {
                    "text": "information.",
                    "tag": "O",
                    "tokens": {
                        "text": "information.",
                        "position": {
                            "left": 456.0,
                            "top": 813.0,
                            "width": 104.0,
                            "height": 12.0
                        },
                        "offset": 805
                    }
                },
                {
                    "text": "rey",
                    "tag": "O",
                    "tokens": {
                        "text": "rey",
                        "position": {
                            "left": 705.0,
                            "top": 842.0,
                            "width": 16.0,
                            "height": 12.0
                        },
                        "offset": 818
                    }
                },
                {
                    "text": "g",
                    "tag": "O",
                    "tokens": {
                        "text": "g",
                        "position": {
                            "left": 704.0,
                            "top": 869.0,
                            "width": 17.0,
                            "height": 41.0
                        },
                        "offset": 822
                    }
                }
            ],
            "source": {
                "width": 774,
                "height": 1000
            }
        }

```
