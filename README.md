- Проект написан на python 3.7 Flask
- Требует установленного [Tesseract](https://github.com/tesseract-ocr/tesseract)
- Файл документа .tif\[f] вставлять на веб-странице http://127.0.0.1:5000/ , там же покажется результат и возможные ошибки.

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
                "text": "BROWN & WILLLAMSON TOBACCO CORPORATION RESEARCH, DEVELOPMENT & ENGINEERING TELEPHONE CONVERSATION KIMBERLY-CLARK/275 CONTACT: Ron Frear DATE: September 10, 1985 ce: Me. E. E. Kohnhorst, Mr. L. Reynolds, Or. J. N. Jewell, Mr. T. F. Riehl, Dr. &. F. Litzinger, Or. B. Chakraborty, Me. G. Strubel, Mr. L. T. Haag { talked with R. Frear on September 4th concerning reconstituted tobacco. R. Frear has arranged a mecting in Spotswood, NJ on September 26th. Attending for Kinberly-Clark witl be tte, Azeez, Mr. Frear, Dr. Cartwright, Mr. Natina, and Ur. Moskal. Currently will be represented by Dr. Chakraborty, Dr. Litzingec, Mr. and aysetf. \u2018The topics for the mecting are: 1, Further improvements in EER. 2, Quality control of ceconstituted tobaccos. Ne. R. Frear told me that the Kimberly-Clark plant will have a report available for us at the meeting oa improving EBR uniformity by changing or better controlling process paraneters. { reminded Mr, Frear that we had not as yet received the minutes From our first research program on reconstituted tobacco. Mr. Frear stated he had seen a draft and he believed that the draft was being reviewed by Dr. Todd. We can expect the draft minutes shortly. Dr. J. G. 09375 R a .",
                "tokens": [
                    {
                        "text": "BROWN",
                        "position": {
                            "left": 236.0,
                            "top": 88.0,
                            "width": 36.0,
                            "height": 10.0
                        },
                        "offset": 0
                    },
                    {
                        "text": "&",
                        "position": {
                            "left": 281.0,
                            "top": 88.0,
                            "width": 6.0,
                            "height": 9.0
                        },
                        "offset": 6
                    },
                    {
                        "text": "WILLLAMSON",
                        "position": {
                            "left": 296.0,
                            "top": 88.0,
                            "width": 75.0,
                            "height": 10.0
                        },
                        "offset": 8
                    },
                    {
                        "text": "TOBACCO",
                        "position": {
                            "left": 379.0,
                            "top": 88.0,
                            "width": 52.0,
                            "height": 10.0
                        },
                        "offset": 19
                    },
                    {
                        "text": "CORPORATION",
                        "position": {
                            "left": 440.0,
                            "top": 88.0,
                            "width": 81.0,
                            "height": 10.0
                        },
                        "offset": 27
                    },
                    {
                        "text": "RESEARCH,",
                        "position": {
                            "left": 248.0,
                            "top": 120.0,
                            "width": 66.0,
                            "height": 11.0
                        },
                        "offset": 39
                    },
                    {
                        "text": "DEVELOPMENT",
                        "position": {
                            "left": 324.0,
                            "top": 120.0,
                            "width": 82.0,
                            "height": 10.0
                        },
                        "offset": 49
                    },
                    {
                        "text": "&",
                        "position": {
                            "left": 414.0,
                            "top": 120.0,
                            "width": 7.0,
                            "height": 9.0
                        },
                        "offset": 61
                    },
                    {
                        "text": "ENGINEERING",
                        "position": {
                            "left": 430.0,
                            "top": 120.0,
                            "width": 81.0,
                            "height": 10.0
                        },
                        "offset": 63
                    },
                    {
                        "text": "TELEPHONE",
                        "position": {
                            "left": 297.0,
                            "top": 152.0,
                            "width": 67.0,
                            "height": 9.0
                        },
                        "offset": 75
                    },
                    {
                        "text": "CONVERSATION",
                        "position": {
                            "left": 372.0,
                            "top": 152.0,
                            "width": 90.0,
                            "height": 9.0
                        },
                        "offset": 85
                    },
                    {
                        "text": "KIMBERLY-CLARK/275",
                        "position": {
                            "left": 199.0,
                            "top": 197.0,
                            "width": 135.0,
                            "height": 11.0
                        },
                        "offset": 98
                    },
                    {
                        "text": "CONTACT:",
                        "position": {
                            "left": 109.0,
                            "top": 230.0,
                            "width": 58.0,
                            "height": 10.0
                        },
                        "offset": 117
                    },
                    {
                        "text": "Ron",
                        "position": {
                            "left": 230.0,
                            "top": 230.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 126
                    },
                    {
                        "text": "Frear",
                        "position": {
                            "left": 260.0,
                            "top": 230.0,
                            "width": 37.0,
                            "height": 9.0
                        },
                        "offset": 130
                    },
                    {
                        "text": "DATE:",
                        "position": {
                            "left": 109.0,
                            "top": 251.0,
                            "width": 35.0,
                            "height": 29.0
                        },
                        "offset": 136
                    },
                    {
                        "text": "September",
                        "position": {
                            "left": 200.0,
                            "top": 260.0,
                            "width": 67.0,
                            "height": 12.0
                        },
                        "offset": 142
                    },
                    {
                        "text": "10,",
                        "position": {
                            "left": 276.0,
                            "top": 260.0,
                            "width": 20.0,
                            "height": 12.0
                        },
                        "offset": 152
                    },
                    {
                        "text": "1985",
                        "position": {
                            "left": 307.0,
                            "top": 260.0,
                            "width": 28.0,
                            "height": 10.0
                        },
                        "offset": 156
                    },
                    {
                        "text": "ce:",
                        "position": {
                            "left": 110.0,
                            "top": 282.0,
                            "width": 20.0,
                            "height": 29.0
                        },
                        "offset": 161
                    },
                    {
                        "text": "Me.",
                        "position": {
                            "left": 200.0,
                            "top": 292.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 165
                    },
                    {
                        "text": "E.",
                        "position": {
                            "left": 231.0,
                            "top": 292.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 169
                    },
                    {
                        "text": "E.",
                        "position": {
                            "left": 254.0,
                            "top": 292.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 172
                    },
                    {
                        "text": "Kohnhorst,",
                        "position": {
                            "left": 276.0,
                            "top": 291.0,
                            "width": 73.0,
                            "height": 12.0
                        },
                        "offset": 175
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 359.0,
                            "top": 292.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 186
                    },
                    {
                        "text": "L.",
                        "position": {
                            "left": 413.0,
                            "top": 292.0,
                            "width": 11.0,
                            "height": 9.0
                        },
                        "offset": 190
                    },
                    {
                        "text": "Reynolds,",
                        "position": {
                            "left": 435.0,
                            "top": 292.0,
                            "width": 65.0,
                            "height": 11.0
                        },
                        "offset": 193
                    },
                    {
                        "text": "Or.",
                        "position": {
                            "left": 510.0,
                            "top": 292.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 203
                    },
                    {
                        "text": "J.",
                        "position": {
                            "left": 540.0,
                            "top": 292.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 207
                    },
                    {
                        "text": "N.",
                        "position": {
                            "left": 562.0,
                            "top": 292.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 210
                    },
                    {
                        "text": "Jewell,",
                        "position": {
                            "left": 585.0,
                            "top": 292.0,
                            "width": 50.0,
                            "height": 11.0
                        },
                        "offset": 213
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 200.0,
                            "top": 307.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 221
                    },
                    {
                        "text": "T.",
                        "position": {
                            "left": 230.0,
                            "top": 307.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 225
                    },
                    {
                        "text": "F.",
                        "position": {
                            "left": 254.0,
                            "top": 307.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 228
                    },
                    {
                        "text": "Riehl,",
                        "position": {
                            "left": 276.0,
                            "top": 306.0,
                            "width": 44.0,
                            "height": 12.0
                        },
                        "offset": 231
                    },
                    {
                        "text": "Dr.",
                        "position": {
                            "left": 329.0,
                            "top": 307.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 238
                    },
                    {
                        "text": "&.",
                        "position": {
                            "left": 360.0,
                            "top": 307.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 242
                    },
                    {
                        "text": "F.",
                        "position": {
                            "left": 383.0,
                            "top": 307.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 245
                    },
                    {
                        "text": "Litzinger,",
                        "position": {
                            "left": 406.0,
                            "top": 307.0,
                            "width": 72.0,
                            "height": 12.0
                        },
                        "offset": 248
                    },
                    {
                        "text": "Or.",
                        "position": {
                            "left": 488.0,
                            "top": 307.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 259
                    },
                    {
                        "text": "B.",
                        "position": {
                            "left": 518.0,
                            "top": 307.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 263
                    },
                    {
                        "text": "Chakraborty,",
                        "position": {
                            "left": 562.0,
                            "top": 307.0,
                            "width": 89.0,
                            "height": 12.0
                        },
                        "offset": 266
                    },
                    {
                        "text": "Me.",
                        "position": {
                            "left": 201.0,
                            "top": 322.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 279
                    },
                    {
                        "text": "G.",
                        "position": {
                            "left": 254.0,
                            "top": 322.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 283
                    },
                    {
                        "text": "Strubel,",
                        "position": {
                            "left": 277.0,
                            "top": 322.0,
                            "width": 58.0,
                            "height": 11.0
                        },
                        "offset": 286
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 344.0,
                            "top": 322.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 295
                    },
                    {
                        "text": "L.",
                        "position": {
                            "left": 376.0,
                            "top": 322.0,
                            "width": 11.0,
                            "height": 9.0
                        },
                        "offset": 299
                    },
                    {
                        "text": "T.",
                        "position": {
                            "left": 397.0,
                            "top": 322.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 302
                    },
                    {
                        "text": "Haag",
                        "position": {
                            "left": 420.0,
                            "top": 322.0,
                            "width": 29.0,
                            "height": 12.0
                        },
                        "offset": 305
                    },
                    {
                        "text": "{",
                        "position": {
                            "left": 112.0,
                            "top": 367.0,
                            "width": 5.0,
                            "height": 9.0
                        },
                        "offset": 310
                    },
                    {
                        "text": "talked",
                        "position": {
                            "left": 127.0,
                            "top": 367.0,
                            "width": 43.0,
                            "height": 9.0
                        },
                        "offset": 312
                    },
                    {
                        "text": "with",
                        "position": {
                            "left": 178.0,
                            "top": 367.0,
                            "width": 31.0,
                            "height": 9.0
                        },
                        "offset": 319
                    },
                    {
                        "text": "R.",
                        "position": {
                            "left": 217.0,
                            "top": 367.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 324
                    },
                    {
                        "text": "Frear",
                        "position": {
                            "left": 240.0,
                            "top": 367.0,
                            "width": 36.0,
                            "height": 9.0
                        },
                        "offset": 327
                    },
                    {
                        "text": "on",
                        "position": {
                            "left": 284.0,
                            "top": 370.0,
                            "width": 15.0,
                            "height": 6.0
                        },
                        "offset": 333
                    },
                    {
                        "text": "September",
                        "position": {
                            "left": 308.0,
                            "top": 367.0,
                            "width": 66.0,
                            "height": 12.0
                        },
                        "offset": 336
                    },
                    {
                        "text": "4th",
                        "position": {
                            "left": 383.0,
                            "top": 367.0,
                            "width": 22.0,
                            "height": 9.0
                        },
                        "offset": 346
                    },
                    {
                        "text": "concerning",
                        "position": {
                            "left": 413.0,
                            "top": 367.0,
                            "width": 74.0,
                            "height": 12.0
                        },
                        "offset": 350
                    },
                    {
                        "text": "reconstituted",
                        "position": {
                            "left": 496.0,
                            "top": 367.0,
                            "width": 96.0,
                            "height": 10.0
                        },
                        "offset": 361
                    },
                    {
                        "text": "tobacco.",
                        "position": {
                            "left": 112.0,
                            "top": 382.0,
                            "width": 57.0,
                            "height": 10.0
                        },
                        "offset": 375
                    },
                    {
                        "text": "R.",
                        "position": {
                            "left": 187.0,
                            "top": 382.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 384
                    },
                    {
                        "text": "Frear",
                        "position": {
                            "left": 210.0,
                            "top": 382.0,
                            "width": 36.0,
                            "height": 9.0
                        },
                        "offset": 387
                    },
                    {
                        "text": "has",
                        "position": {
                            "left": 255.0,
                            "top": 382.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 393
                    },
                    {
                        "text": "arranged",
                        "position": {
                            "left": 285.0,
                            "top": 383.0,
                            "width": 59.0,
                            "height": 11.0
                        },
                        "offset": 397
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 353.0,
                            "top": 385.0,
                            "width": 7.0,
                            "height": 6.0
                        },
                        "offset": 406
                    },
                    {
                        "text": "mecting",
                        "position": {
                            "left": 368.0,
                            "top": 382.0,
                            "width": 52.0,
                            "height": 12.0
                        },
                        "offset": 408
                    },
                    {
                        "text": "in",
                        "position": {
                            "left": 430.0,
                            "top": 382.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 416
                    },
                    {
                        "text": "Spotswood,",
                        "position": {
                            "left": 451.0,
                            "top": 383.0,
                            "width": 72.0,
                            "height": 11.0
                        },
                        "offset": 419
                    },
                    {
                        "text": "NJ",
                        "position": {
                            "left": 533.0,
                            "top": 383.0,
                            "width": 14.0,
                            "height": 9.0
                        },
                        "offset": 430
                    },
                    {
                        "text": "on",
                        "position": {
                            "left": 556.0,
                            "top": 385.0,
                            "width": 14.0,
                            "height": 6.0
                        },
                        "offset": 433
                    },
                    {
                        "text": "September",
                        "position": {
                            "left": 112.0,
                            "top": 398.0,
                            "width": 66.0,
                            "height": 11.0
                        },
                        "offset": 436
                    },
                    {
                        "text": "26th.",
                        "position": {
                            "left": 188.0,
                            "top": 397.0,
                            "width": 34.0,
                            "height": 10.0
                        },
                        "offset": 446
                    },
                    {
                        "text": "Attending",
                        "position": {
                            "left": 240.0,
                            "top": 397.0,
                            "width": 67.0,
                            "height": 12.0
                        },
                        "offset": 452
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 316.0,
                            "top": 397.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 462
                    },
                    {
                        "text": "Kinberly-Clark",
                        "position": {
                            "left": 345.0,
                            "top": 397.0,
                            "width": 105.0,
                            "height": 12.0
                        },
                        "offset": 466
                    },
                    {
                        "text": "witl",
                        "position": {
                            "left": 459.0,
                            "top": 397.0,
                            "width": 28.0,
                            "height": 10.0
                        },
                        "offset": 481
                    },
                    {
                        "text": "be",
                        "position": {
                            "left": 496.0,
                            "top": 397.0,
                            "width": 14.0,
                            "height": 10.0
                        },
                        "offset": 486
                    },
                    {
                        "text": "tte,",
                        "position": {
                            "left": 518.0,
                            "top": 398.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 489
                    },
                    {
                        "text": "Azeez,",
                        "position": {
                            "left": 549.0,
                            "top": 398.0,
                            "width": 43.0,
                            "height": 10.0
                        },
                        "offset": 494
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 112.0,
                            "top": 413.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 501
                    },
                    {
                        "text": "Frear,",
                        "position": {
                            "left": 143.0,
                            "top": 413.0,
                            "width": 42.0,
                            "height": 11.0
                        },
                        "offset": 505
                    },
                    {
                        "text": "Dr.",
                        "position": {
                            "left": 195.0,
                            "top": 413.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 512
                    },
                    {
                        "text": "Cartwright,",
                        "position": {
                            "left": 225.0,
                            "top": 412.0,
                            "width": 81.0,
                            "height": 12.0
                        },
                        "offset": 516
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 315.0,
                            "top": 413.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 528
                    },
                    {
                        "text": "Natina,",
                        "position": {
                            "left": 346.0,
                            "top": 412.0,
                            "width": 50.0,
                            "height": 12.0
                        },
                        "offset": 532
                    },
                    {
                        "text": "and",
                        "position": {
                            "left": 406.0,
                            "top": 413.0,
                            "width": 22.0,
                            "height": 9.0
                        },
                        "offset": 540
                    },
                    {
                        "text": "Ur.",
                        "position": {
                            "left": 436.0,
                            "top": 413.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 544
                    },
                    {
                        "text": "Moskal.",
                        "position": {
                            "left": 466.0,
                            "top": 413.0,
                            "width": 50.0,
                            "height": 9.0
                        },
                        "offset": 548
                    },
                    {
                        "text": "Currently",
                        "position": {
                            "left": 534.0,
                            "top": 413.0,
                            "width": 67.0,
                            "height": 11.0
                        },
                        "offset": 556
                    },
                    {
                        "text": "will",
                        "position": {
                            "left": 112.0,
                            "top": 428.0,
                            "width": 29.0,
                            "height": 9.0
                        },
                        "offset": 566
                    },
                    {
                        "text": "be",
                        "position": {
                            "left": 150.0,
                            "top": 428.0,
                            "width": 13.0,
                            "height": 10.0
                        },
                        "offset": 571
                    },
                    {
                        "text": "represented",
                        "position": {
                            "left": 173.0,
                            "top": 428.0,
                            "width": 81.0,
                            "height": 12.0
                        },
                        "offset": 574
                    },
                    {
                        "text": "by",
                        "position": {
                            "left": 263.0,
                            "top": 428.0,
                            "width": 14.0,
                            "height": 12.0
                        },
                        "offset": 586
                    },
                    {
                        "text": "Dr.",
                        "position": {
                            "left": 285.0,
                            "top": 428.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 589
                    },
                    {
                        "text": "Chakraborty,",
                        "position": {
                            "left": 316.0,
                            "top": 428.0,
                            "width": 88.0,
                            "height": 12.0
                        },
                        "offset": 593
                    },
                    {
                        "text": "Dr.",
                        "position": {
                            "left": 414.0,
                            "top": 428.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 606
                    },
                    {
                        "text": "Litzingec,",
                        "position": {
                            "left": 445.0,
                            "top": 428.0,
                            "width": 72.0,
                            "height": 11.0
                        },
                        "offset": 610
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 526.0,
                            "top": 428.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 621
                    },
                    {
                        "text": "and",
                        "position": {
                            "left": 625.0,
                            "top": 428.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 625
                    },
                    {
                        "text": "aysetf.",
                        "position": {
                            "left": 112.0,
                            "top": 443.0,
                            "width": 50.0,
                            "height": 12.0
                        },
                        "offset": 629
                    },
                    {
                        "text": "\u2018The",
                        "position": {
                            "left": 180.0,
                            "top": 443.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 637
                    },
                    {
                        "text": "topics",
                        "position": {
                            "left": 211.0,
                            "top": 443.0,
                            "width": 43.0,
                            "height": 12.0
                        },
                        "offset": 642
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 264.0,
                            "top": 443.0,
                            "width": 20.0,
                            "height": 10.0
                        },
                        "offset": 649
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 294.0,
                            "top": 444.0,
                            "width": 21.0,
                            "height": 8.0
                        },
                        "offset": 653
                    },
                    {
                        "text": "mecting",
                        "position": {
                            "left": 323.0,
                            "top": 443.0,
                            "width": 52.0,
                            "height": 12.0
                        },
                        "offset": 657
                    },
                    {
                        "text": "are:",
                        "position": {
                            "left": 384.0,
                            "top": 446.0,
                            "width": 27.0,
                            "height": 6.0
                        },
                        "offset": 665
                    },
                    {
                        "text": "1,",
                        "position": {
                            "left": 144.0,
                            "top": 474.0,
                            "width": 11.0,
                            "height": 9.0
                        },
                        "offset": 670
                    },
                    {
                        "text": "Further",
                        "position": {
                            "left": 174.0,
                            "top": 474.0,
                            "width": 50.0,
                            "height": 9.0
                        },
                        "offset": 673
                    },
                    {
                        "text": "improvements",
                        "position": {
                            "left": 234.0,
                            "top": 474.0,
                            "width": 88.0,
                            "height": 12.0
                        },
                        "offset": 681
                    },
                    {
                        "text": "in",
                        "position": {
                            "left": 333.0,
                            "top": 474.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 694
                    },
                    {
                        "text": "EER.",
                        "position": {
                            "left": 355.0,
                            "top": 474.0,
                            "width": 27.0,
                            "height": 9.0
                        },
                        "offset": 697
                    },
                    {
                        "text": "2,",
                        "position": {
                            "left": 144.0,
                            "top": 505.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 702
                    },
                    {
                        "text": "Quality",
                        "position": {
                            "left": 173.0,
                            "top": 505.0,
                            "width": 52.0,
                            "height": 12.0
                        },
                        "offset": 705
                    },
                    {
                        "text": "control",
                        "position": {
                            "left": 234.0,
                            "top": 504.0,
                            "width": 50.0,
                            "height": 10.0
                        },
                        "offset": 713
                    },
                    {
                        "text": "of",
                        "position": {
                            "left": 294.0,
                            "top": 504.0,
                            "width": 14.0,
                            "height": 10.0
                        },
                        "offset": 721
                    },
                    {
                        "text": "ceconstituted",
                        "position": {
                            "left": 318.0,
                            "top": 504.0,
                            "width": 96.0,
                            "height": 10.0
                        },
                        "offset": 724
                    },
                    {
                        "text": "tobaccos.",
                        "position": {
                            "left": 424.0,
                            "top": 504.0,
                            "width": 63.0,
                            "height": 10.0
                        },
                        "offset": 738
                    },
                    {
                        "text": "Ne.",
                        "position": {
                            "left": 114.0,
                            "top": 536.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 748
                    },
                    {
                        "text": "R.",
                        "position": {
                            "left": 144.0,
                            "top": 536.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 752
                    },
                    {
                        "text": "Frear",
                        "position": {
                            "left": 167.0,
                            "top": 536.0,
                            "width": 36.0,
                            "height": 9.0
                        },
                        "offset": 755
                    },
                    {
                        "text": "told",
                        "position": {
                            "left": 213.0,
                            "top": 535.0,
                            "width": 27.0,
                            "height": 10.0
                        },
                        "offset": 761
                    },
                    {
                        "text": "me",
                        "position": {
                            "left": 249.0,
                            "top": 538.0,
                            "width": 14.0,
                            "height": 7.0
                        },
                        "offset": 766
                    },
                    {
                        "text": "that",
                        "position": {
                            "left": 273.0,
                            "top": 535.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 769
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 311.0,
                            "top": 535.0,
                            "width": 20.0,
                            "height": 10.0
                        },
                        "offset": 774
                    },
                    {
                        "text": "Kimberly-Clark",
                        "position": {
                            "left": 340.0,
                            "top": 535.0,
                            "width": 104.0,
                            "height": 12.0
                        },
                        "offset": 778
                    },
                    {
                        "text": "plant",
                        "position": {
                            "left": 454.0,
                            "top": 535.0,
                            "width": 35.0,
                            "height": 12.0
                        },
                        "offset": 793
                    },
                    {
                        "text": "will",
                        "position": {
                            "left": 498.0,
                            "top": 535.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 799
                    },
                    {
                        "text": "have",
                        "position": {
                            "left": 536.0,
                            "top": 535.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 804
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 573.0,
                            "top": 538.0,
                            "width": 7.0,
                            "height": 6.0
                        },
                        "offset": 809
                    },
                    {
                        "text": "report",
                        "position": {
                            "left": 589.0,
                            "top": 536.0,
                            "width": 43.0,
                            "height": 11.0
                        },
                        "offset": 811
                    },
                    {
                        "text": "available",
                        "position": {
                            "left": 114.0,
                            "top": 551.0,
                            "width": 66.0,
                            "height": 9.0
                        },
                        "offset": 818
                    },
                    {
                        "text": "for",
                        "position": {
                            "left": 190.0,
                            "top": 550.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 828
                    },
                    {
                        "text": "us",
                        "position": {
                            "left": 219.0,
                            "top": 554.0,
                            "width": 14.0,
                            "height": 6.0
                        },
                        "offset": 832
                    },
                    {
                        "text": "at",
                        "position": {
                            "left": 242.0,
                            "top": 552.0,
                            "width": 14.0,
                            "height": 8.0
                        },
                        "offset": 835
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 266.0,
                            "top": 551.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 838
                    },
                    {
                        "text": "meeting",
                        "position": {
                            "left": 294.0,
                            "top": 550.0,
                            "width": 53.0,
                            "height": 12.0
                        },
                        "offset": 842
                    },
                    {
                        "text": "oa",
                        "position": {
                            "left": 355.0,
                            "top": 553.0,
                            "width": 15.0,
                            "height": 7.0
                        },
                        "offset": 850
                    },
                    {
                        "text": "improving",
                        "position": {
                            "left": 379.0,
                            "top": 550.0,
                            "width": 66.0,
                            "height": 13.0
                        },
                        "offset": 853
                    },
                    {
                        "text": "EBR",
                        "position": {
                            "left": 454.0,
                            "top": 550.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 863
                    },
                    {
                        "text": "uniformity",
                        "position": {
                            "left": 484.0,
                            "top": 550.0,
                            "width": 73.0,
                            "height": 12.0
                        },
                        "offset": 867
                    },
                    {
                        "text": "by",
                        "position": {
                            "left": 566.0,
                            "top": 550.0,
                            "width": 14.0,
                            "height": 12.0
                        },
                        "offset": 878
                    },
                    {
                        "text": "changing",
                        "position": {
                            "left": 115.0,
                            "top": 566.0,
                            "width": 58.0,
                            "height": 12.0
                        },
                        "offset": 881
                    },
                    {
                        "text": "or",
                        "position": {
                            "left": 182.0,
                            "top": 569.0,
                            "width": 14.0,
                            "height": 7.0
                        },
                        "offset": 890
                    },
                    {
                        "text": "better",
                        "position": {
                            "left": 204.0,
                            "top": 566.0,
                            "width": 44.0,
                            "height": 10.0
                        },
                        "offset": 893
                    },
                    {
                        "text": "controlling",
                        "position": {
                            "left": 257.0,
                            "top": 566.0,
                            "width": 82.0,
                            "height": 12.0
                        },
                        "offset": 900
                    },
                    {
                        "text": "process",
                        "position": {
                            "left": 349.0,
                            "top": 568.0,
                            "width": 50.0,
                            "height": 10.0
                        },
                        "offset": 912
                    },
                    {
                        "text": "paraneters.",
                        "position": {
                            "left": 409.0,
                            "top": 567.0,
                            "width": 79.0,
                            "height": 11.0
                        },
                        "offset": 920
                    },
                    {
                        "text": "{",
                        "position": {
                            "left": 116.0,
                            "top": 597.0,
                            "width": 5.0,
                            "height": 9.0
                        },
                        "offset": 932
                    },
                    {
                        "text": "reminded",
                        "position": {
                            "left": 131.0,
                            "top": 597.0,
                            "width": 58.0,
                            "height": 10.0
                        },
                        "offset": 934
                    },
                    {
                        "text": "Mr,",
                        "position": {
                            "left": 197.0,
                            "top": 597.0,
                            "width": 20.0,
                            "height": 10.0
                        },
                        "offset": 943
                    },
                    {
                        "text": "Frear",
                        "position": {
                            "left": 228.0,
                            "top": 597.0,
                            "width": 36.0,
                            "height": 9.0
                        },
                        "offset": 947
                    },
                    {
                        "text": "that",
                        "position": {
                            "left": 274.0,
                            "top": 597.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 953
                    },
                    {
                        "text": "we",
                        "position": {
                            "left": 310.0,
                            "top": 600.0,
                            "width": 15.0,
                            "height": 6.0
                        },
                        "offset": 958
                    },
                    {
                        "text": "had",
                        "position": {
                            "left": 334.0,
                            "top": 597.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 961
                    },
                    {
                        "text": "not",
                        "position": {
                            "left": 364.0,
                            "top": 598.0,
                            "width": 21.0,
                            "height": 8.0
                        },
                        "offset": 965
                    },
                    {
                        "text": "as",
                        "position": {
                            "left": 394.0,
                            "top": 599.0,
                            "width": 13.0,
                            "height": 7.0
                        },
                        "offset": 969
                    },
                    {
                        "text": "yet",
                        "position": {
                            "left": 416.0,
                            "top": 598.0,
                            "width": 22.0,
                            "height": 11.0
                        },
                        "offset": 972
                    },
                    {
                        "text": "received",
                        "position": {
                            "left": 448.0,
                            "top": 596.0,
                            "width": 57.0,
                            "height": 10.0
                        },
                        "offset": 976
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 515.0,
                            "top": 597.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 985
                    },
                    {
                        "text": "minutes",
                        "position": {
                            "left": 544.0,
                            "top": 598.0,
                            "width": 51.0,
                            "height": 8.0
                        },
                        "offset": 989
                    },
                    {
                        "text": "From",
                        "position": {
                            "left": 606.0,
                            "top": 597.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 997
                    },
                    {
                        "text": "our",
                        "position": {
                            "left": 115.0,
                            "top": 615.0,
                            "width": 22.0,
                            "height": 7.0
                        },
                        "offset": 1002
                    },
                    {
                        "text": "first",
                        "position": {
                            "left": 146.0,
                            "top": 612.0,
                            "width": 35.0,
                            "height": 10.0
                        },
                        "offset": 1006
                    },
                    {
                        "text": "research",
                        "position": {
                            "left": 191.0,
                            "top": 613.0,
                            "width": 59.0,
                            "height": 10.0
                        },
                        "offset": 1012
                    },
                    {
                        "text": "program",
                        "position": {
                            "left": 258.0,
                            "top": 615.0,
                            "width": 53.0,
                            "height": 10.0
                        },
                        "offset": 1021
                    },
                    {
                        "text": "on",
                        "position": {
                            "left": 318.0,
                            "top": 615.0,
                            "width": 15.0,
                            "height": 7.0
                        },
                        "offset": 1029
                    },
                    {
                        "text": "reconstituted",
                        "position": {
                            "left": 342.0,
                            "top": 612.0,
                            "width": 96.0,
                            "height": 10.0
                        },
                        "offset": 1032
                    },
                    {
                        "text": "tobacco.",
                        "position": {
                            "left": 448.0,
                            "top": 612.0,
                            "width": 56.0,
                            "height": 10.0
                        },
                        "offset": 1046
                    },
                    {
                        "text": "Mr.",
                        "position": {
                            "left": 521.0,
                            "top": 612.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 1055
                    },
                    {
                        "text": "Frear",
                        "position": {
                            "left": 552.0,
                            "top": 612.0,
                            "width": 36.0,
                            "height": 10.0
                        },
                        "offset": 1059
                    },
                    {
                        "text": "stated",
                        "position": {
                            "left": 598.0,
                            "top": 613.0,
                            "width": 43.0,
                            "height": 9.0
                        },
                        "offset": 1065
                    },
                    {
                        "text": "he",
                        "position": {
                            "left": 116.0,
                            "top": 628.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 1072
                    },
                    {
                        "text": "had",
                        "position": {
                            "left": 138.0,
                            "top": 628.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 1075
                    },
                    {
                        "text": "seen",
                        "position": {
                            "left": 168.0,
                            "top": 631.0,
                            "width": 29.0,
                            "height": 7.0
                        },
                        "offset": 1079
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 205.0,
                            "top": 631.0,
                            "width": 7.0,
                            "height": 7.0
                        },
                        "offset": 1084
                    },
                    {
                        "text": "draft",
                        "position": {
                            "left": 221.0,
                            "top": 628.0,
                            "width": 35.0,
                            "height": 10.0
                        },
                        "offset": 1086
                    },
                    {
                        "text": "and",
                        "position": {
                            "left": 265.0,
                            "top": 628.0,
                            "width": 22.0,
                            "height": 9.0
                        },
                        "offset": 1092
                    },
                    {
                        "text": "he",
                        "position": {
                            "left": 296.0,
                            "top": 628.0,
                            "width": 14.0,
                            "height": 9.0
                        },
                        "offset": 1096
                    },
                    {
                        "text": "believed",
                        "position": {
                            "left": 319.0,
                            "top": 627.0,
                            "width": 59.0,
                            "height": 10.0
                        },
                        "offset": 1099
                    },
                    {
                        "text": "that",
                        "position": {
                            "left": 388.0,
                            "top": 628.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 1108
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 425.0,
                            "top": 628.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 1113
                    },
                    {
                        "text": "draft",
                        "position": {
                            "left": 455.0,
                            "top": 627.0,
                            "width": 36.0,
                            "height": 10.0
                        },
                        "offset": 1117
                    },
                    {
                        "text": "was",
                        "position": {
                            "left": 499.0,
                            "top": 630.0,
                            "width": 21.0,
                            "height": 7.0
                        },
                        "offset": 1123
                    },
                    {
                        "text": "being",
                        "position": {
                            "left": 529.0,
                            "top": 628.0,
                            "width": 37.0,
                            "height": 11.0
                        },
                        "offset": 1127
                    },
                    {
                        "text": "reviewed",
                        "position": {
                            "left": 576.0,
                            "top": 628.0,
                            "width": 58.0,
                            "height": 9.0
                        },
                        "offset": 1133
                    },
                    {
                        "text": "by",
                        "position": {
                            "left": 115.0,
                            "top": 643.0,
                            "width": 15.0,
                            "height": 12.0
                        },
                        "offset": 1142
                    },
                    {
                        "text": "Dr.",
                        "position": {
                            "left": 139.0,
                            "top": 644.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 1145
                    },
                    {
                        "text": "Todd.",
                        "position": {
                            "left": 190.0,
                            "top": 644.0,
                            "width": 36.0,
                            "height": 9.0
                        },
                        "offset": 1149
                    },
                    {
                        "text": "We",
                        "position": {
                            "left": 243.0,
                            "top": 643.0,
                            "width": 14.0,
                            "height": 9.0
                        },
                        "offset": 1155
                    },
                    {
                        "text": "can",
                        "position": {
                            "left": 266.0,
                            "top": 646.0,
                            "width": 22.0,
                            "height": 7.0
                        },
                        "offset": 1158
                    },
                    {
                        "text": "expect",
                        "position": {
                            "left": 296.0,
                            "top": 644.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 1162
                    },
                    {
                        "text": "the",
                        "position": {
                            "left": 350.0,
                            "top": 643.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 1169
                    },
                    {
                        "text": "draft",
                        "position": {
                            "left": 379.0,
                            "top": 642.0,
                            "width": 37.0,
                            "height": 10.0
                        },
                        "offset": 1173
                    },
                    {
                        "text": "minutes",
                        "position": {
                            "left": 424.0,
                            "top": 642.0,
                            "width": 52.0,
                            "height": 10.0
                        },
                        "offset": 1179
                    },
                    {
                        "text": "shortly.",
                        "position": {
                            "left": 485.0,
                            "top": 643.0,
                            "width": 57.0,
                            "height": 12.0
                        },
                        "offset": 1187
                    },
                    {
                        "text": "Dr.",
                        "position": {
                            "left": 117.0,
                            "top": 720.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 1196
                    },
                    {
                        "text": "J.",
                        "position": {
                            "left": 147.0,
                            "top": 720.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 1200
                    },
                    {
                        "text": "G.",
                        "position": {
                            "left": 169.0,
                            "top": 720.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 1203
                    },
                    {
                        "text": "09375",
                        "position": {
                            "left": 117.0,
                            "top": 782.0,
                            "width": 36.0,
                            "height": 12.0
                        },
                        "offset": 1206
                    },
                    {
                        "text": "R",
                        "position": {
                            "left": 707.0,
                            "top": 785.0,
                            "width": 16.0,
                            "height": 26.0
                        },
                        "offset": 1212
                    },
                    {
                        "text": "a",
                        "position": {
                            "left": 707.0,
                            "top": 877.0,
                            "width": 16.0,
                            "height": 14.0
                        },
                        "offset": 1214
                    },
                    {
                        "text": ".",
                        "position": {
                            "left": 641.0,
                            "top": 908.0,
                            "width": 2.0,
                            "height": 2.0
                        },
                        "offset": 1216
                    }
                ],
                "source": {
                    "width": 769,
                    "height": 1000
                }
            }
        ]
    },
    "task_2": {},
    "task_3": {
        "source": {
            "width": null,
            "height": null,
            "type": "other"
        }
    },
    "task_4": [
        {
            "facts": [
                {
                    "text": "BROWN & WILLLAMSON TOBACCO CORPORATION RESEARCH",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "BROWN",
                            "position": {
                                "left": 236.0,
                                "top": 88.0,
                                "width": 36.0,
                                "height": 10.0
                            },
                            "offset": 0
                        },
                        {
                            "text": "&",
                            "position": {
                                "left": 281.0,
                                "top": 88.0,
                                "width": 6.0,
                                "height": 9.0
                            },
                            "offset": 6
                        },
                        {
                            "text": "WILLLAMSON",
                            "position": {
                                "left": 296.0,
                                "top": 88.0,
                                "width": 75.0,
                                "height": 10.0
                            },
                            "offset": 8
                        },
                        {
                            "text": "TOBACCO",
                            "position": {
                                "left": 379.0,
                                "top": 88.0,
                                "width": 52.0,
                                "height": 10.0
                            },
                            "offset": 19
                        },
                        {
                            "text": "CORPORATION",
                            "position": {
                                "left": 440.0,
                                "top": 88.0,
                                "width": 81.0,
                                "height": 10.0
                            },
                            "offset": 27
                        },
                        {
                            "text": "RESEARCH,",
                            "position": {
                                "left": 248.0,
                                "top": 120.0,
                                "width": 66.0,
                                "height": 11.0
                            },
                            "offset": 39
                        }
                    ]
                },
                {
                    "text": "DEVELOPMENT & ENGINEERING TELEPHONE",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "DEVELOPMENT",
                            "position": {
                                "left": 324.0,
                                "top": 120.0,
                                "width": 82.0,
                                "height": 10.0
                            },
                            "offset": 49
                        },
                        {
                            "text": "&",
                            "position": {
                                "left": 414.0,
                                "top": 120.0,
                                "width": 7.0,
                                "height": 9.0
                            },
                            "offset": 61
                        },
                        {
                            "text": "ENGINEERING",
                            "position": {
                                "left": 430.0,
                                "top": 120.0,
                                "width": 81.0,
                                "height": 10.0
                            },
                            "offset": 63
                        },
                        {
                            "text": "TELEPHONE",
                            "position": {
                                "left": 297.0,
                                "top": 152.0,
                                "width": 67.0,
                                "height": 9.0
                            },
                            "offset": 75
                        }
                    ]
                },
                {
                    "text": "CONVERSATION",
                    "tag": "O",
                    "tokens": {
                        "text": "CONVERSATION",
                        "position": {
                            "left": 372.0,
                            "top": 152.0,
                            "width": 90.0,
                            "height": 9.0
                        },
                        "offset": 85
                    }
                },
                {
                    "text": "KIMBERLY-CLARK/275",
                    "tag": "O",
                    "tokens": {
                        "text": "KIMBERLY-CLARK/275",
                        "position": {
                            "left": 199.0,
                            "top": 197.0,
                            "width": 135.0,
                            "height": 11.0
                        },
                        "offset": 98
                    }
                },
                {
                    "text": "CONTACT:",
                    "tag": "O",
                    "tokens": {
                        "text": "CONTACT:",
                        "position": {
                            "left": 109.0,
                            "top": 230.0,
                            "width": 58.0,
                            "height": 10.0
                        },
                        "offset": 117
                    }
                },
                {
                    "text": "Ron",
                    "tag": "O",
                    "tokens": {
                        "text": "Ron",
                        "position": {
                            "left": 230.0,
                            "top": 230.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 126
                    }
                },
                {
                    "text": "Frear",
                    "tag": "O",
                    "tokens": {
                        "text": "Frear",
                        "position": {
                            "left": 260.0,
                            "top": 230.0,
                            "width": 37.0,
                            "height": 9.0
                        },
                        "offset": 130
                    }
                },
                {
                    "text": "DATE:",
                    "tag": "O",
                    "tokens": {
                        "text": "DATE:",
                        "position": {
                            "left": 109.0,
                            "top": 251.0,
                            "width": 35.0,
                            "height": 29.0
                        },
                        "offset": 136
                    }
                },
                {
                    "text": "September 10, 1985",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "September",
                            "position": {
                                "left": 200.0,
                                "top": 260.0,
                                "width": 67.0,
                                "height": 12.0
                            },
                            "offset": 142
                        },
                        {
                            "text": "10,",
                            "position": {
                                "left": 276.0,
                                "top": 260.0,
                                "width": 20.0,
                                "height": 12.0
                            },
                            "offset": 152
                        },
                        {
                            "text": "1985",
                            "position": {
                                "left": 307.0,
                                "top": 260.0,
                                "width": 28.0,
                                "height": 10.0
                            },
                            "offset": 156
                        }
                    ]
                },
                {
                    "text": "ce:",
                    "tag": "O",
                    "tokens": {
                        "text": "ce:",
                        "position": {
                            "left": 110.0,
                            "top": 282.0,
                            "width": 20.0,
                            "height": 29.0
                        },
                        "offset": 161
                    }
                },
                {
                    "text": "Me.",
                    "tag": "O",
                    "tokens": {
                        "text": "Me.",
                        "position": {
                            "left": 200.0,
                            "top": 292.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 165
                    }
                },
                {
                    "text": "E. E. Kohnhorst",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "E.",
                            "position": {
                                "left": 231.0,
                                "top": 292.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 169
                        },
                        {
                            "text": "E.",
                            "position": {
                                "left": 254.0,
                                "top": 292.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 172
                        },
                        {
                            "text": "Kohnhorst,",
                            "position": {
                                "left": 276.0,
                                "top": 291.0,
                                "width": 73.0,
                                "height": 12.0
                            },
                            "offset": 175
                        }
                    ]
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 359.0,
                            "top": 292.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 186
                    }
                },
                {
                    "text": "L. Reynolds",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "L.",
                            "position": {
                                "left": 413.0,
                                "top": 292.0,
                                "width": 11.0,
                                "height": 9.0
                            },
                            "offset": 190
                        },
                        {
                            "text": "Reynolds,",
                            "position": {
                                "left": 435.0,
                                "top": 292.0,
                                "width": 65.0,
                                "height": 11.0
                            },
                            "offset": 193
                        }
                    ]
                },
                {
                    "text": "Or.",
                    "tag": "O",
                    "tokens": {
                        "text": "Or.",
                        "position": {
                            "left": 510.0,
                            "top": 292.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 203
                    }
                },
                {
                    "text": "J. N. Jewell",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "J.",
                            "position": {
                                "left": 540.0,
                                "top": 292.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 207
                        },
                        {
                            "text": "N.",
                            "position": {
                                "left": 562.0,
                                "top": 292.0,
                                "width": 13.0,
                                "height": 9.0
                            },
                            "offset": 210
                        },
                        {
                            "text": "Jewell,",
                            "position": {
                                "left": 585.0,
                                "top": 292.0,
                                "width": 50.0,
                                "height": 11.0
                            },
                            "offset": 213
                        }
                    ]
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 200.0,
                            "top": 307.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 221
                    }
                },
                {
                    "text": "T. F. Riehl",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "T.",
                            "position": {
                                "left": 230.0,
                                "top": 307.0,
                                "width": 13.0,
                                "height": 9.0
                            },
                            "offset": 225
                        },
                        {
                            "text": "F.",
                            "position": {
                                "left": 254.0,
                                "top": 307.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 228
                        },
                        {
                            "text": "Riehl,",
                            "position": {
                                "left": 276.0,
                                "top": 306.0,
                                "width": 44.0,
                                "height": 12.0
                            },
                            "offset": 231
                        }
                    ]
                },
                {
                    "text": "Dr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Dr.",
                        "position": {
                            "left": 329.0,
                            "top": 307.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 238
                    }
                },
                {
                    "text": "&.",
                    "tag": "O",
                    "tokens": {
                        "text": "&.",
                        "position": {
                            "left": 360.0,
                            "top": 307.0,
                            "width": 12.0,
                            "height": 9.0
                        },
                        "offset": 242
                    }
                },
                {
                    "text": "F. Litzinger",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "F.",
                            "position": {
                                "left": 383.0,
                                "top": 307.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 245
                        },
                        {
                            "text": "Litzinger,",
                            "position": {
                                "left": 406.0,
                                "top": 307.0,
                                "width": 72.0,
                                "height": 12.0
                            },
                            "offset": 248
                        }
                    ]
                },
                {
                    "text": "Or.",
                    "tag": "O",
                    "tokens": {
                        "text": "Or.",
                        "position": {
                            "left": 488.0,
                            "top": 307.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 259
                    }
                },
                {
                    "text": "B. Chakraborty",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "B.",
                            "position": {
                                "left": 518.0,
                                "top": 307.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 263
                        },
                        {
                            "text": "Chakraborty,",
                            "position": {
                                "left": 562.0,
                                "top": 307.0,
                                "width": 89.0,
                                "height": 12.0
                            },
                            "offset": 266
                        }
                    ]
                },
                {
                    "text": "Me.",
                    "tag": "O",
                    "tokens": {
                        "text": "Me.",
                        "position": {
                            "left": 201.0,
                            "top": 322.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 279
                    }
                },
                {
                    "text": "G. Strubel",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "G.",
                            "position": {
                                "left": 254.0,
                                "top": 322.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 283
                        },
                        {
                            "text": "Strubel,",
                            "position": {
                                "left": 277.0,
                                "top": 322.0,
                                "width": 58.0,
                                "height": 11.0
                            },
                            "offset": 286
                        }
                    ]
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 344.0,
                            "top": 322.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 295
                    }
                },
                {
                    "text": "L. T. Haag",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "L.",
                            "position": {
                                "left": 376.0,
                                "top": 322.0,
                                "width": 11.0,
                                "height": 9.0
                            },
                            "offset": 299
                        },
                        {
                            "text": "T.",
                            "position": {
                                "left": 397.0,
                                "top": 322.0,
                                "width": 13.0,
                                "height": 9.0
                            },
                            "offset": 302
                        },
                        {
                            "text": "Haag",
                            "position": {
                                "left": 420.0,
                                "top": 322.0,
                                "width": 29.0,
                                "height": 12.0
                            },
                            "offset": 305
                        }
                    ]
                },
                {
                    "text": "{",
                    "tag": "O",
                    "tokens": {
                        "text": "{",
                        "position": {
                            "left": 112.0,
                            "top": 367.0,
                            "width": 5.0,
                            "height": 9.0
                        },
                        "offset": 310
                    }
                },
                {
                    "text": "talked",
                    "tag": "O",
                    "tokens": {
                        "text": "talked",
                        "position": {
                            "left": 127.0,
                            "top": 367.0,
                            "width": 43.0,
                            "height": 9.0
                        },
                        "offset": 312
                    }
                },
                {
                    "text": "with",
                    "tag": "O",
                    "tokens": {
                        "text": "with",
                        "position": {
                            "left": 178.0,
                            "top": 367.0,
                            "width": 31.0,
                            "height": 9.0
                        },
                        "offset": 319
                    }
                },
                {
                    "text": "R.",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "R.",
                            "position": {
                                "left": 217.0,
                                "top": 367.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 324
                        }
                    ]
                },
                {
                    "text": "Frear",
                    "tag": "O",
                    "tokens": {
                        "text": "Frear",
                        "position": {
                            "left": 240.0,
                            "top": 367.0,
                            "width": 36.0,
                            "height": 9.0
                        },
                        "offset": 327
                    }
                },
                {
                    "text": "on",
                    "tag": "O",
                    "tokens": {
                        "text": "on",
                        "position": {
                            "left": 284.0,
                            "top": 370.0,
                            "width": 15.0,
                            "height": 6.0
                        },
                        "offset": 333
                    }
                },
                {
                    "text": "September 4th",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "September",
                            "position": {
                                "left": 308.0,
                                "top": 367.0,
                                "width": 66.0,
                                "height": 12.0
                            },
                            "offset": 336
                        },
                        {
                            "text": "4th",
                            "position": {
                                "left": 383.0,
                                "top": 367.0,
                                "width": 22.0,
                                "height": 9.0
                            },
                            "offset": 346
                        }
                    ]
                },
                {
                    "text": "concerning",
                    "tag": "O",
                    "tokens": {
                        "text": "concerning",
                        "position": {
                            "left": 413.0,
                            "top": 367.0,
                            "width": 74.0,
                            "height": 12.0
                        },
                        "offset": 350
                    }
                },
                {
                    "text": "reconstituted",
                    "tag": "O",
                    "tokens": {
                        "text": "reconstituted",
                        "position": {
                            "left": 496.0,
                            "top": 367.0,
                            "width": 96.0,
                            "height": 10.0
                        },
                        "offset": 361
                    }
                },
                {
                    "text": "tobacco.",
                    "tag": "O",
                    "tokens": {
                        "text": "tobacco.",
                        "position": {
                            "left": 112.0,
                            "top": 382.0,
                            "width": 57.0,
                            "height": 10.0
                        },
                        "offset": 375
                    }
                },
                {
                    "text": "R. Frear",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "R.",
                            "position": {
                                "left": 187.0,
                                "top": 382.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 384
                        },
                        {
                            "text": "Frear",
                            "position": {
                                "left": 210.0,
                                "top": 382.0,
                                "width": 36.0,
                                "height": 9.0
                            },
                            "offset": 387
                        }
                    ]
                },
                {
                    "text": "has",
                    "tag": "O",
                    "tokens": {
                        "text": "has",
                        "position": {
                            "left": 255.0,
                            "top": 382.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 393
                    }
                },
                {
                    "text": "arranged",
                    "tag": "O",
                    "tokens": {
                        "text": "arranged",
                        "position": {
                            "left": 285.0,
                            "top": 383.0,
                            "width": 59.0,
                            "height": 11.0
                        },
                        "offset": 397
                    }
                },
                {
                    "text": "a",
                    "tag": "O",
                    "tokens": {
                        "text": "a",
                        "position": {
                            "left": 353.0,
                            "top": 385.0,
                            "width": 7.0,
                            "height": 6.0
                        },
                        "offset": 406
                    }
                },
                {
                    "text": "mecting",
                    "tag": "O",
                    "tokens": {
                        "text": "mecting",
                        "position": {
                            "left": 368.0,
                            "top": 382.0,
                            "width": 52.0,
                            "height": 12.0
                        },
                        "offset": 408
                    }
                },
                {
                    "text": "in",
                    "tag": "O",
                    "tokens": {
                        "text": "in",
                        "position": {
                            "left": 430.0,
                            "top": 382.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 416
                    }
                },
                {
                    "text": "Spotswood,",
                    "tag": "O",
                    "tokens": {
                        "text": "Spotswood,",
                        "position": {
                            "left": 451.0,
                            "top": 383.0,
                            "width": 72.0,
                            "height": 11.0
                        },
                        "offset": 419
                    }
                },
                {
                    "text": "NJ",
                    "tag": "O",
                    "tokens": {
                        "text": "NJ",
                        "position": {
                            "left": 533.0,
                            "top": 383.0,
                            "width": 14.0,
                            "height": 9.0
                        },
                        "offset": 430
                    }
                },
                {
                    "text": "on",
                    "tag": "O",
                    "tokens": {
                        "text": "on",
                        "position": {
                            "left": 556.0,
                            "top": 385.0,
                            "width": 14.0,
                            "height": 6.0
                        },
                        "offset": 433
                    }
                },
                {
                    "text": "September 26th",
                    "tag": "DATE",
                    "tokens": [
                        {
                            "text": "September",
                            "position": {
                                "left": 112.0,
                                "top": 398.0,
                                "width": 66.0,
                                "height": 11.0
                            },
                            "offset": 436
                        },
                        {
                            "text": "26th.",
                            "position": {
                                "left": 188.0,
                                "top": 397.0,
                                "width": 34.0,
                                "height": 10.0
                            },
                            "offset": 446
                        }
                    ]
                },
                {
                    "text": "Attending",
                    "tag": "O",
                    "tokens": {
                        "text": "Attending",
                        "position": {
                            "left": 240.0,
                            "top": 397.0,
                            "width": 67.0,
                            "height": 12.0
                        },
                        "offset": 452
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 316.0,
                            "top": 397.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 462
                    }
                },
                {
                    "text": "Kinberly-Clark",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "Kinberly-Clark",
                            "position": {
                                "left": 345.0,
                                "top": 397.0,
                                "width": 105.0,
                                "height": 12.0
                            },
                            "offset": 466
                        }
                    ]
                },
                {
                    "text": "witl",
                    "tag": "O",
                    "tokens": {
                        "text": "witl",
                        "position": {
                            "left": 459.0,
                            "top": 397.0,
                            "width": 28.0,
                            "height": 10.0
                        },
                        "offset": 481
                    }
                },
                {
                    "text": "be",
                    "tag": "O",
                    "tokens": {
                        "text": "be",
                        "position": {
                            "left": 496.0,
                            "top": 397.0,
                            "width": 14.0,
                            "height": 10.0
                        },
                        "offset": 486
                    }
                },
                {
                    "text": "tte,",
                    "tag": "O",
                    "tokens": {
                        "text": "tte,",
                        "position": {
                            "left": 518.0,
                            "top": 398.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 489
                    }
                },
                {
                    "text": "Azeez",
                    "tag": "LOCATION",
                    "tokens": [
                        {
                            "text": "Azeez,",
                            "position": {
                                "left": 549.0,
                                "top": 398.0,
                                "width": 43.0,
                                "height": 10.0
                            },
                            "offset": 494
                        }
                    ]
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 112.0,
                            "top": 413.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 501
                    }
                },
                {
                    "text": "Frear",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Frear,",
                            "position": {
                                "left": 143.0,
                                "top": 413.0,
                                "width": 42.0,
                                "height": 11.0
                            },
                            "offset": 505
                        }
                    ]
                },
                {
                    "text": "Dr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Dr.",
                        "position": {
                            "left": 195.0,
                            "top": 413.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 512
                    }
                },
                {
                    "text": "Cartwright",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Cartwright,",
                            "position": {
                                "left": 225.0,
                                "top": 412.0,
                                "width": 81.0,
                                "height": 12.0
                            },
                            "offset": 516
                        }
                    ]
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 315.0,
                            "top": 413.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 528
                    }
                },
                {
                    "text": "Natina",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Natina,",
                            "position": {
                                "left": 346.0,
                                "top": 412.0,
                                "width": 50.0,
                                "height": 12.0
                            },
                            "offset": 532
                        }
                    ]
                },
                {
                    "text": "and",
                    "tag": "O",
                    "tokens": {
                        "text": "and",
                        "position": {
                            "left": 406.0,
                            "top": 413.0,
                            "width": 22.0,
                            "height": 9.0
                        },
                        "offset": 540
                    }
                },
                {
                    "text": "Ur.",
                    "tag": "O",
                    "tokens": {
                        "text": "Ur.",
                        "position": {
                            "left": 436.0,
                            "top": 413.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 544
                    }
                },
                {
                    "text": "Moskal.",
                    "tag": "O",
                    "tokens": {
                        "text": "Moskal.",
                        "position": {
                            "left": 466.0,
                            "top": 413.0,
                            "width": 50.0,
                            "height": 9.0
                        },
                        "offset": 548
                    }
                },
                {
                    "text": "Currently",
                    "tag": "O",
                    "tokens": {
                        "text": "Currently",
                        "position": {
                            "left": 534.0,
                            "top": 413.0,
                            "width": 67.0,
                            "height": 11.0
                        },
                        "offset": 556
                    }
                },
                {
                    "text": "will",
                    "tag": "O",
                    "tokens": {
                        "text": "will",
                        "position": {
                            "left": 112.0,
                            "top": 428.0,
                            "width": 29.0,
                            "height": 9.0
                        },
                        "offset": 566
                    }
                },
                {
                    "text": "be",
                    "tag": "O",
                    "tokens": {
                        "text": "be",
                        "position": {
                            "left": 150.0,
                            "top": 428.0,
                            "width": 13.0,
                            "height": 10.0
                        },
                        "offset": 571
                    }
                },
                {
                    "text": "represented",
                    "tag": "O",
                    "tokens": {
                        "text": "represented",
                        "position": {
                            "left": 173.0,
                            "top": 428.0,
                            "width": 81.0,
                            "height": 12.0
                        },
                        "offset": 574
                    }
                },
                {
                    "text": "by",
                    "tag": "O",
                    "tokens": {
                        "text": "by",
                        "position": {
                            "left": 263.0,
                            "top": 428.0,
                            "width": 14.0,
                            "height": 12.0
                        },
                        "offset": 586
                    }
                },
                {
                    "text": "Dr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Dr.",
                        "position": {
                            "left": 285.0,
                            "top": 428.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 589
                    }
                },
                {
                    "text": "Chakraborty",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Chakraborty,",
                            "position": {
                                "left": 316.0,
                                "top": 428.0,
                                "width": 88.0,
                                "height": 12.0
                            },
                            "offset": 593
                        }
                    ]
                },
                {
                    "text": "Dr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Dr.",
                        "position": {
                            "left": 414.0,
                            "top": 428.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 606
                    }
                },
                {
                    "text": "Litzingec",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Litzingec,",
                            "position": {
                                "left": 445.0,
                                "top": 428.0,
                                "width": 72.0,
                                "height": 11.0
                            },
                            "offset": 610
                        }
                    ]
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 526.0,
                            "top": 428.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 621
                    }
                },
                {
                    "text": "and",
                    "tag": "O",
                    "tokens": {
                        "text": "and",
                        "position": {
                            "left": 625.0,
                            "top": 428.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 625
                    }
                },
                {
                    "text": "aysetf.",
                    "tag": "O",
                    "tokens": {
                        "text": "aysetf.",
                        "position": {
                            "left": 112.0,
                            "top": 443.0,
                            "width": 50.0,
                            "height": 12.0
                        },
                        "offset": 629
                    }
                },
                {
                    "text": "\u2018The",
                    "tag": "O",
                    "tokens": {
                        "text": "\u2018The",
                        "position": {
                            "left": 180.0,
                            "top": 443.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 637
                    }
                },
                {
                    "text": "topics",
                    "tag": "O",
                    "tokens": {
                        "text": "topics",
                        "position": {
                            "left": 211.0,
                            "top": 443.0,
                            "width": 43.0,
                            "height": 12.0
                        },
                        "offset": 642
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 264.0,
                            "top": 443.0,
                            "width": 20.0,
                            "height": 10.0
                        },
                        "offset": 649
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 294.0,
                            "top": 444.0,
                            "width": 21.0,
                            "height": 8.0
                        },
                        "offset": 653
                    }
                },
                {
                    "text": "mecting",
                    "tag": "O",
                    "tokens": {
                        "text": "mecting",
                        "position": {
                            "left": 323.0,
                            "top": 443.0,
                            "width": 52.0,
                            "height": 12.0
                        },
                        "offset": 657
                    }
                },
                {
                    "text": "are:",
                    "tag": "O",
                    "tokens": {
                        "text": "are:",
                        "position": {
                            "left": 384.0,
                            "top": 446.0,
                            "width": 27.0,
                            "height": 6.0
                        },
                        "offset": 665
                    }
                },
                {
                    "text": "1",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "1,",
                            "position": {
                                "left": 144.0,
                                "top": 474.0,
                                "width": 11.0,
                                "height": 9.0
                            },
                            "offset": 670
                        }
                    ]
                },
                {
                    "text": "Further",
                    "tag": "O",
                    "tokens": {
                        "text": "Further",
                        "position": {
                            "left": 174.0,
                            "top": 474.0,
                            "width": 50.0,
                            "height": 9.0
                        },
                        "offset": 673
                    }
                },
                {
                    "text": "improvements",
                    "tag": "O",
                    "tokens": {
                        "text": "improvements",
                        "position": {
                            "left": 234.0,
                            "top": 474.0,
                            "width": 88.0,
                            "height": 12.0
                        },
                        "offset": 681
                    }
                },
                {
                    "text": "in",
                    "tag": "O",
                    "tokens": {
                        "text": "in",
                        "position": {
                            "left": 333.0,
                            "top": 474.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 694
                    }
                },
                {
                    "text": "EER.",
                    "tag": "O",
                    "tokens": {
                        "text": "EER.",
                        "position": {
                            "left": 355.0,
                            "top": 474.0,
                            "width": 27.0,
                            "height": 9.0
                        },
                        "offset": 697
                    }
                },
                {
                    "text": "2",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "2,",
                            "position": {
                                "left": 144.0,
                                "top": 505.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 702
                        }
                    ]
                },
                {
                    "text": "Quality",
                    "tag": "O",
                    "tokens": {
                        "text": "Quality",
                        "position": {
                            "left": 173.0,
                            "top": 505.0,
                            "width": 52.0,
                            "height": 12.0
                        },
                        "offset": 705
                    }
                },
                {
                    "text": "control",
                    "tag": "O",
                    "tokens": {
                        "text": "control",
                        "position": {
                            "left": 234.0,
                            "top": 504.0,
                            "width": 50.0,
                            "height": 10.0
                        },
                        "offset": 713
                    }
                },
                {
                    "text": "of",
                    "tag": "O",
                    "tokens": {
                        "text": "of",
                        "position": {
                            "left": 294.0,
                            "top": 504.0,
                            "width": 14.0,
                            "height": 10.0
                        },
                        "offset": 721
                    }
                },
                {
                    "text": "ceconstituted",
                    "tag": "O",
                    "tokens": {
                        "text": "ceconstituted",
                        "position": {
                            "left": 318.0,
                            "top": 504.0,
                            "width": 96.0,
                            "height": 10.0
                        },
                        "offset": 724
                    }
                },
                {
                    "text": "tobaccos.",
                    "tag": "O",
                    "tokens": {
                        "text": "tobaccos.",
                        "position": {
                            "left": 424.0,
                            "top": 504.0,
                            "width": 63.0,
                            "height": 10.0
                        },
                        "offset": 738
                    }
                },
                {
                    "text": "Ne.",
                    "tag": "O",
                    "tokens": {
                        "text": "Ne.",
                        "position": {
                            "left": 114.0,
                            "top": 536.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 748
                    }
                },
                {
                    "text": "R. Frear",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "R.",
                            "position": {
                                "left": 144.0,
                                "top": 536.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 752
                        },
                        {
                            "text": "Frear",
                            "position": {
                                "left": 167.0,
                                "top": 536.0,
                                "width": 36.0,
                                "height": 9.0
                            },
                            "offset": 755
                        }
                    ]
                },
                {
                    "text": "told",
                    "tag": "O",
                    "tokens": {
                        "text": "told",
                        "position": {
                            "left": 213.0,
                            "top": 535.0,
                            "width": 27.0,
                            "height": 10.0
                        },
                        "offset": 761
                    }
                },
                {
                    "text": "me",
                    "tag": "O",
                    "tokens": {
                        "text": "me",
                        "position": {
                            "left": 249.0,
                            "top": 538.0,
                            "width": 14.0,
                            "height": 7.0
                        },
                        "offset": 766
                    }
                },
                {
                    "text": "that",
                    "tag": "O",
                    "tokens": {
                        "text": "that",
                        "position": {
                            "left": 273.0,
                            "top": 535.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 769
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 311.0,
                            "top": 535.0,
                            "width": 20.0,
                            "height": 10.0
                        },
                        "offset": 774
                    }
                },
                {
                    "text": "Kimberly-Clark",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "Kimberly-Clark",
                            "position": {
                                "left": 340.0,
                                "top": 535.0,
                                "width": 104.0,
                                "height": 12.0
                            },
                            "offset": 778
                        }
                    ]
                },
                {
                    "text": "plant",
                    "tag": "O",
                    "tokens": {
                        "text": "plant",
                        "position": {
                            "left": 454.0,
                            "top": 535.0,
                            "width": 35.0,
                            "height": 12.0
                        },
                        "offset": 793
                    }
                },
                {
                    "text": "will",
                    "tag": "O",
                    "tokens": {
                        "text": "will",
                        "position": {
                            "left": 498.0,
                            "top": 535.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 799
                    }
                },
                {
                    "text": "have",
                    "tag": "O",
                    "tokens": {
                        "text": "have",
                        "position": {
                            "left": 536.0,
                            "top": 535.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 804
                    }
                },
                {
                    "text": "a",
                    "tag": "O",
                    "tokens": {
                        "text": "a",
                        "position": {
                            "left": 573.0,
                            "top": 538.0,
                            "width": 7.0,
                            "height": 6.0
                        },
                        "offset": 809
                    }
                },
                {
                    "text": "report",
                    "tag": "O",
                    "tokens": {
                        "text": "report",
                        "position": {
                            "left": 589.0,
                            "top": 536.0,
                            "width": 43.0,
                            "height": 11.0
                        },
                        "offset": 811
                    }
                },
                {
                    "text": "available",
                    "tag": "O",
                    "tokens": {
                        "text": "available",
                        "position": {
                            "left": 114.0,
                            "top": 551.0,
                            "width": 66.0,
                            "height": 9.0
                        },
                        "offset": 818
                    }
                },
                {
                    "text": "for",
                    "tag": "O",
                    "tokens": {
                        "text": "for",
                        "position": {
                            "left": 190.0,
                            "top": 550.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 828
                    }
                },
                {
                    "text": "us",
                    "tag": "O",
                    "tokens": {
                        "text": "us",
                        "position": {
                            "left": 219.0,
                            "top": 554.0,
                            "width": 14.0,
                            "height": 6.0
                        },
                        "offset": 832
                    }
                },
                {
                    "text": "at",
                    "tag": "O",
                    "tokens": {
                        "text": "at",
                        "position": {
                            "left": 242.0,
                            "top": 552.0,
                            "width": 14.0,
                            "height": 8.0
                        },
                        "offset": 835
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 266.0,
                            "top": 551.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 838
                    }
                },
                {
                    "text": "meeting",
                    "tag": "O",
                    "tokens": {
                        "text": "meeting",
                        "position": {
                            "left": 294.0,
                            "top": 550.0,
                            "width": 53.0,
                            "height": 12.0
                        },
                        "offset": 842
                    }
                },
                {
                    "text": "oa",
                    "tag": "O",
                    "tokens": {
                        "text": "oa",
                        "position": {
                            "left": 355.0,
                            "top": 553.0,
                            "width": 15.0,
                            "height": 7.0
                        },
                        "offset": 850
                    }
                },
                {
                    "text": "improving",
                    "tag": "O",
                    "tokens": {
                        "text": "improving",
                        "position": {
                            "left": 379.0,
                            "top": 550.0,
                            "width": 66.0,
                            "height": 13.0
                        },
                        "offset": 853
                    }
                },
                {
                    "text": "EBR",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "EBR",
                            "position": {
                                "left": 454.0,
                                "top": 550.0,
                                "width": 21.0,
                                "height": 10.0
                            },
                            "offset": 863
                        }
                    ]
                },
                {
                    "text": "uniformity",
                    "tag": "O",
                    "tokens": {
                        "text": "uniformity",
                        "position": {
                            "left": 484.0,
                            "top": 550.0,
                            "width": 73.0,
                            "height": 12.0
                        },
                        "offset": 867
                    }
                },
                {
                    "text": "by",
                    "tag": "O",
                    "tokens": {
                        "text": "by",
                        "position": {
                            "left": 566.0,
                            "top": 550.0,
                            "width": 14.0,
                            "height": 12.0
                        },
                        "offset": 878
                    }
                },
                {
                    "text": "changing",
                    "tag": "O",
                    "tokens": {
                        "text": "changing",
                        "position": {
                            "left": 115.0,
                            "top": 566.0,
                            "width": 58.0,
                            "height": 12.0
                        },
                        "offset": 881
                    }
                },
                {
                    "text": "or",
                    "tag": "O",
                    "tokens": {
                        "text": "or",
                        "position": {
                            "left": 182.0,
                            "top": 569.0,
                            "width": 14.0,
                            "height": 7.0
                        },
                        "offset": 890
                    }
                },
                {
                    "text": "better",
                    "tag": "O",
                    "tokens": {
                        "text": "better",
                        "position": {
                            "left": 204.0,
                            "top": 566.0,
                            "width": 44.0,
                            "height": 10.0
                        },
                        "offset": 893
                    }
                },
                {
                    "text": "controlling",
                    "tag": "O",
                    "tokens": {
                        "text": "controlling",
                        "position": {
                            "left": 257.0,
                            "top": 566.0,
                            "width": 82.0,
                            "height": 12.0
                        },
                        "offset": 900
                    }
                },
                {
                    "text": "process",
                    "tag": "O",
                    "tokens": {
                        "text": "process",
                        "position": {
                            "left": 349.0,
                            "top": 568.0,
                            "width": 50.0,
                            "height": 10.0
                        },
                        "offset": 912
                    }
                },
                {
                    "text": "paraneters.",
                    "tag": "O",
                    "tokens": {
                        "text": "paraneters.",
                        "position": {
                            "left": 409.0,
                            "top": 567.0,
                            "width": 79.0,
                            "height": 11.0
                        },
                        "offset": 920
                    }
                },
                {
                    "text": "{",
                    "tag": "O",
                    "tokens": {
                        "text": "{",
                        "position": {
                            "left": 116.0,
                            "top": 597.0,
                            "width": 5.0,
                            "height": 9.0
                        },
                        "offset": 932
                    }
                },
                {
                    "text": "reminded",
                    "tag": "O",
                    "tokens": {
                        "text": "reminded",
                        "position": {
                            "left": 131.0,
                            "top": 597.0,
                            "width": 58.0,
                            "height": 10.0
                        },
                        "offset": 934
                    }
                },
                {
                    "text": "Mr, Frear",
                    "tag": "ORGANIZATION",
                    "tokens": [
                        {
                            "text": "Mr,",
                            "position": {
                                "left": 197.0,
                                "top": 597.0,
                                "width": 20.0,
                                "height": 10.0
                            },
                            "offset": 943
                        },
                        {
                            "text": "Frear",
                            "position": {
                                "left": 228.0,
                                "top": 597.0,
                                "width": 36.0,
                                "height": 9.0
                            },
                            "offset": 947
                        }
                    ]
                },
                {
                    "text": "that",
                    "tag": "O",
                    "tokens": {
                        "text": "that",
                        "position": {
                            "left": 274.0,
                            "top": 597.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 953
                    }
                },
                {
                    "text": "we",
                    "tag": "O",
                    "tokens": {
                        "text": "we",
                        "position": {
                            "left": 310.0,
                            "top": 600.0,
                            "width": 15.0,
                            "height": 6.0
                        },
                        "offset": 958
                    }
                },
                {
                    "text": "had",
                    "tag": "O",
                    "tokens": {
                        "text": "had",
                        "position": {
                            "left": 334.0,
                            "top": 597.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 961
                    }
                },
                {
                    "text": "not",
                    "tag": "O",
                    "tokens": {
                        "text": "not",
                        "position": {
                            "left": 364.0,
                            "top": 598.0,
                            "width": 21.0,
                            "height": 8.0
                        },
                        "offset": 965
                    }
                },
                {
                    "text": "as",
                    "tag": "O",
                    "tokens": {
                        "text": "as",
                        "position": {
                            "left": 394.0,
                            "top": 599.0,
                            "width": 13.0,
                            "height": 7.0
                        },
                        "offset": 969
                    }
                },
                {
                    "text": "yet",
                    "tag": "O",
                    "tokens": {
                        "text": "yet",
                        "position": {
                            "left": 416.0,
                            "top": 598.0,
                            "width": 22.0,
                            "height": 11.0
                        },
                        "offset": 972
                    }
                },
                {
                    "text": "received",
                    "tag": "O",
                    "tokens": {
                        "text": "received",
                        "position": {
                            "left": 448.0,
                            "top": 596.0,
                            "width": 57.0,
                            "height": 10.0
                        },
                        "offset": 976
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 515.0,
                            "top": 597.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 985
                    }
                },
                {
                    "text": "minutes",
                    "tag": "O",
                    "tokens": {
                        "text": "minutes",
                        "position": {
                            "left": 544.0,
                            "top": 598.0,
                            "width": 51.0,
                            "height": 8.0
                        },
                        "offset": 989
                    }
                },
                {
                    "text": "From",
                    "tag": "O",
                    "tokens": {
                        "text": "From",
                        "position": {
                            "left": 606.0,
                            "top": 597.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 997
                    }
                },
                {
                    "text": "our",
                    "tag": "O",
                    "tokens": {
                        "text": "our",
                        "position": {
                            "left": 115.0,
                            "top": 615.0,
                            "width": 22.0,
                            "height": 7.0
                        },
                        "offset": 1002
                    }
                },
                {
                    "text": "first",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "first",
                            "position": {
                                "left": 146.0,
                                "top": 612.0,
                                "width": 35.0,
                                "height": 10.0
                            },
                            "offset": 1006
                        }
                    ]
                },
                {
                    "text": "research",
                    "tag": "O",
                    "tokens": {
                        "text": "research",
                        "position": {
                            "left": 191.0,
                            "top": 613.0,
                            "width": 59.0,
                            "height": 10.0
                        },
                        "offset": 1012
                    }
                },
                {
                    "text": "program",
                    "tag": "O",
                    "tokens": {
                        "text": "program",
                        "position": {
                            "left": 258.0,
                            "top": 615.0,
                            "width": 53.0,
                            "height": 10.0
                        },
                        "offset": 1021
                    }
                },
                {
                    "text": "on",
                    "tag": "O",
                    "tokens": {
                        "text": "on",
                        "position": {
                            "left": 318.0,
                            "top": 615.0,
                            "width": 15.0,
                            "height": 7.0
                        },
                        "offset": 1029
                    }
                },
                {
                    "text": "reconstituted",
                    "tag": "O",
                    "tokens": {
                        "text": "reconstituted",
                        "position": {
                            "left": 342.0,
                            "top": 612.0,
                            "width": 96.0,
                            "height": 10.0
                        },
                        "offset": 1032
                    }
                },
                {
                    "text": "tobacco.",
                    "tag": "O",
                    "tokens": {
                        "text": "tobacco.",
                        "position": {
                            "left": 448.0,
                            "top": 612.0,
                            "width": 56.0,
                            "height": 10.0
                        },
                        "offset": 1046
                    }
                },
                {
                    "text": "Mr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Mr.",
                        "position": {
                            "left": 521.0,
                            "top": 612.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 1055
                    }
                },
                {
                    "text": "Frear",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Frear",
                            "position": {
                                "left": 552.0,
                                "top": 612.0,
                                "width": 36.0,
                                "height": 10.0
                            },
                            "offset": 1059
                        }
                    ]
                },
                {
                    "text": "stated",
                    "tag": "O",
                    "tokens": {
                        "text": "stated",
                        "position": {
                            "left": 598.0,
                            "top": 613.0,
                            "width": 43.0,
                            "height": 9.0
                        },
                        "offset": 1065
                    }
                },
                {
                    "text": "he",
                    "tag": "O",
                    "tokens": {
                        "text": "he",
                        "position": {
                            "left": 116.0,
                            "top": 628.0,
                            "width": 13.0,
                            "height": 9.0
                        },
                        "offset": 1072
                    }
                },
                {
                    "text": "had",
                    "tag": "O",
                    "tokens": {
                        "text": "had",
                        "position": {
                            "left": 138.0,
                            "top": 628.0,
                            "width": 21.0,
                            "height": 10.0
                        },
                        "offset": 1075
                    }
                },
                {
                    "text": "seen",
                    "tag": "O",
                    "tokens": {
                        "text": "seen",
                        "position": {
                            "left": 168.0,
                            "top": 631.0,
                            "width": 29.0,
                            "height": 7.0
                        },
                        "offset": 1079
                    }
                },
                {
                    "text": "a",
                    "tag": "O",
                    "tokens": {
                        "text": "a",
                        "position": {
                            "left": 205.0,
                            "top": 631.0,
                            "width": 7.0,
                            "height": 7.0
                        },
                        "offset": 1084
                    }
                },
                {
                    "text": "draft",
                    "tag": "O",
                    "tokens": {
                        "text": "draft",
                        "position": {
                            "left": 221.0,
                            "top": 628.0,
                            "width": 35.0,
                            "height": 10.0
                        },
                        "offset": 1086
                    }
                },
                {
                    "text": "and",
                    "tag": "O",
                    "tokens": {
                        "text": "and",
                        "position": {
                            "left": 265.0,
                            "top": 628.0,
                            "width": 22.0,
                            "height": 9.0
                        },
                        "offset": 1092
                    }
                },
                {
                    "text": "he",
                    "tag": "O",
                    "tokens": {
                        "text": "he",
                        "position": {
                            "left": 296.0,
                            "top": 628.0,
                            "width": 14.0,
                            "height": 9.0
                        },
                        "offset": 1096
                    }
                },
                {
                    "text": "believed",
                    "tag": "O",
                    "tokens": {
                        "text": "believed",
                        "position": {
                            "left": 319.0,
                            "top": 627.0,
                            "width": 59.0,
                            "height": 10.0
                        },
                        "offset": 1099
                    }
                },
                {
                    "text": "that",
                    "tag": "O",
                    "tokens": {
                        "text": "that",
                        "position": {
                            "left": 388.0,
                            "top": 628.0,
                            "width": 28.0,
                            "height": 9.0
                        },
                        "offset": 1108
                    }
                },
                {
                    "text": "the",
                    "tag": "O",
                    "tokens": {
                        "text": "the",
                        "position": {
                            "left": 425.0,
                            "top": 628.0,
                            "width": 21.0,
                            "height": 9.0
                        },
                        "offset": 1113
                    }
                },
                {
                    "text": "draft",
                    "tag": "O",
                    "tokens": {
                        "text": "draft",
                        "position": {
                            "left": 455.0,
                            "top": 627.0,
                            "width": 36.0,
                            "height": 10.0
                        },
                        "offset": 1117
                    }
                },
                {
                    "text": "was",
                    "tag": "O",
                    "tokens": {
                        "text": "was",
                        "position": {
                            "left": 499.0,
                            "top": 630.0,
                            "width": 21.0,
                            "height": 7.0
                        },
                        "offset": 1123
                    }
                },
                {
                    "text": "being",
                    "tag": "O",
                    "tokens": {
                        "text": "being",
                        "position": {
                            "left": 529.0,
                            "top": 628.0,
                            "width": 37.0,
                            "height": 11.0
                        },
                        "offset": 1127
                    }
                },
                {
                    "text": "reviewed",
                    "tag": "O",
                    "tokens": {
                        "text": "reviewed",
                        "position": {
                            "left": 576.0,
                            "top": 628.0,
                            "width": 58.0,
                            "height": 9.0
                        },
                        "offset": 1133
                    }
                },
                {
                    "text": "by",
                    "tag": "O",
                    "tokens": {
                        "text": "by",
                        "position": {
                            "left": 115.0,
                            "top": 643.0,
                            "width": 15.0,
                            "height": 12.0
                        },
                        "offset": 1142
                    }
                },
                {
                    "text": "Dr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Dr.",
                        "position": {
                            "left": 139.0,
                            "top": 644.0,
                            "width": 19.0,
                            "height": 9.0
                        },
                        "offset": 1145
                    }
                },
                {
                    "text": "Todd",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "Todd.",
                            "position": {
                                "left": 190.0,
                                "top": 644.0,
                                "width": 36.0,
                                "height": 9.0
                            },
                            "offset": 1149
                        }
                    ]
                },
                {
                    "text": "We",
                    "tag": "O",
                    "tokens": {
                        "text": "We",
                        "position": {
                            "left": 243.0,
                            "top": 643.0,
                            "width": 14.0,
                            "height": 9.0
                        },
                        "offset": 1155
                    }
                },
                {
                    "text": "can",
                    "tag": "O",
                    "tokens": {
                        "text": "can",
                        "position": {
                            "left": 266.0,
                            "top": 646.0,
                            "width": 22.0,
                            "height": 7.0
                        },
                        "offset": 1158
                    }
                },
                {
                    "text": "expect",
                    "tag": "O",
                    "tokens": {
                        "text": "expect",
                        "position": {
                            "left": 296.0,
                            "top": 644.0,
                            "width": 44.0,
                            "height": 11.0
                        },
                        "offset": 1162
                    }
                },
                {
                    "text": "the draft minutes",
                    "tag": "O",
                    "tokens": [
                        {
                            "text": "the",
                            "position": {
                                "left": 350.0,
                                "top": 643.0,
                                "width": 20.0,
                                "height": 9.0
                            },
                            "offset": 1169
                        },
                        {
                            "text": "draft",
                            "position": {
                                "left": 379.0,
                                "top": 642.0,
                                "width": 37.0,
                                "height": 10.0
                            },
                            "offset": 1173
                        },
                        {
                            "text": "minutes",
                            "position": {
                                "left": 424.0,
                                "top": 642.0,
                                "width": 52.0,
                                "height": 10.0
                            },
                            "offset": 1179
                        }
                    ]
                },
                {
                    "text": "shortly.",
                    "tag": "O",
                    "tokens": {
                        "text": "shortly.",
                        "position": {
                            "left": 485.0,
                            "top": 643.0,
                            "width": 57.0,
                            "height": 12.0
                        },
                        "offset": 1187
                    }
                },
                {
                    "text": "Dr.",
                    "tag": "O",
                    "tokens": {
                        "text": "Dr.",
                        "position": {
                            "left": 117.0,
                            "top": 720.0,
                            "width": 20.0,
                            "height": 9.0
                        },
                        "offset": 1196
                    }
                },
                {
                    "text": "J. G. 09375",
                    "tag": "PERSON",
                    "tokens": [
                        {
                            "text": "J.",
                            "position": {
                                "left": 147.0,
                                "top": 720.0,
                                "width": 12.0,
                                "height": 9.0
                            },
                            "offset": 1200
                        },
                        {
                            "text": "G.",
                            "position": {
                                "left": 169.0,
                                "top": 720.0,
                                "width": 13.0,
                                "height": 9.0
                            },
                            "offset": 1203
                        },
                        {
                            "text": "09375",
                            "position": {
                                "left": 117.0,
                                "top": 782.0,
                                "width": 36.0,
                                "height": 12.0
                            },
                            "offset": 1206
                        }
                    ]
                },
                {
                    "text": "R",
                    "tag": "O",
                    "tokens": {
                        "text": "R",
                        "position": {
                            "left": 707.0,
                            "top": 785.0,
                            "width": 16.0,
                            "height": 26.0
                        },
                        "offset": 1212
                    }
                },
                {
                    "text": "a",
                    "tag": "O",
                    "tokens": {
                        "text": "a",
                        "position": {
                            "left": 707.0,
                            "top": 877.0,
                            "width": 16.0,
                            "height": 14.0
                        },
                        "offset": 1214
                    }
                },
                {
                    "text": ".",
                    "tag": "O",
                    "tokens": {
                        "text": ".",
                        "position": {
                            "left": 641.0,
                            "top": 908.0,
                            "width": 2.0,
                            "height": 2.0
                        },
                        "offset": 1216
                    }
                }
            ],
            "source": {
                "width": 769,
                "height": 1000
            }
        }
    ]
}

```
