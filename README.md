# otus_python_web_habrparser
Additional task for course https://otus.ru/lessons/webpython/

Script parses https://habr.com pages and calculates statistics of usage words in article titles.
Script gets amount of pages as an argument. By default it parses 10 pages.

# Installation and usage

In order to use scrip do the following:

1) Clone this repo from github:

```bash
git clone git@github.com:samuraii/otus_python_web_habraparser.git
```

2) Install requirements:

```bash
pip install requirements.txt
```

Run script:

```bash
python parse_habr.py --pages 10
```

Output:
```bash
Недельная статистика популярных слов на Хабре
---------------------------------------------
Неделя "2018-05-07" - "2018-05-13"
1) май: 4
2) приглашать: 3
3) meetup: 3
4) приложение: 3
Неделя "2018-04-30" - "2018-05-06"
1) разработка: 2
2) фильтр: 2
3) закон: 2
4) smartmailhack: 1
```

# Progect objectives

Educational.