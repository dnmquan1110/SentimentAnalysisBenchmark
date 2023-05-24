import crawl_data


def main():
    top_movies = 'https://www.imdb.com/search/title/?groups=top_100'
    bottom_movies = 'https://www.imdb.com/chart/bottom'
    crawl_data.get_reviews(top_movies, 30, 400, 'top_movie_reviews', top_movie = True)
    crawl_data.get_reviews(bottom_movies, 30, 400, 'bottom_movie_reviews', top_movie = False)

if __name__ == "__main__":
    main()