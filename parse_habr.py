import argparse
from habr_parser import fetch_raw_html_from_pages, create_bs4_objects_from_raw_html
from date_processor import calculate_week_and_week_corner_dates
from words_processor import filter_words_in_title, calculate_normal_form_word_frequency


def parse_dates_and_titles_from_articles(bs4_object):
    articles_info = []
    for article_block in bs4_object.find_all(
            'article',
            {'class': 'post post_preview'},
    ):
        title_link = article_block.find('a', {'class': 'post__title_link'})
        publish_date = article_block.find('span', {'class': 'post__time'})
        articles_info.append({
            'title': title_link.contents[0],
            'publish_date': calculate_week_and_week_corner_dates(publish_date.contents[0])
        })
    return articles_info


def output_word_stat(word_stat, top_size=4):
    i = 1
    for word, repetitions_amount in word_stat[:top_size]:
        print('%s) %s: %s' % (i, word, repetitions_amount))
        i += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pages', type=int, default=10)
    args = parser.parse_args()
    raw_pages_html = fetch_raw_html_from_pages(pages=int(args.pages))
    bs4_page_objects = create_bs4_objects_from_raw_html(raw_pages_html)

    articles_info = []
    for bs4_page_object in bs4_page_objects:
        articles_info += parse_dates_and_titles_from_articles(bs4_page_object)

    words_by_weeks = {}
    for article_info in articles_info:
        try:
            words_by_weeks[article_info['publish_date']] += filter_words_in_title(article_info['title'])
        except KeyError:
            words_by_weeks[article_info['publish_date']] = []

    print('Недельная статистика популярных слов на Хабре')
    print('-' * 45)
    for week in words_by_weeks:
        print('Неделя "{}" - "{}"'.format(week[1][0], week[1][1]))
        output_word_stat(calculate_normal_form_word_frequency(words_by_weeks[week]))
