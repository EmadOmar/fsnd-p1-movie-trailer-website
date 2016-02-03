import math
import os
import webbrowser

"""Generates and open an HTML page that contains the rendered movies.

Example:
    fly_and_open_movies_page([movie1, movie2])
"""

__movie_template__ = None
"""int: stores a copy of the movie template {@see _get_movie_template()}."""

def fly_and_open_movies_page(movies):
    """Render the list of movies objects into an HTML web page and open it.

    Args:
        movies (Movie[]): List of movies objects.

    """

    # Create or replace an HTML file to store the rendered web page
    output_file = open('lovely_dove.html', 'w')
    output_file.write(_render_site(movies))
    output_file.close()

    # Open the created HTML web page
    curr_path = os.path.abspath(output_file.name)
    webbrowser.open('file://' + curr_path)
    

def _render_site(movies):
    """Render the list of movies objects into an HTML web page.

    Args:
        movies (Movie[]): List of movies objects.

    Returns:
        HTML web page contains the rendered movies objects list.

    """

    # Open and read the site template
    site_tmpl_file = open('_site-template.html')
    site_tmpl = site_tmpl_file.read()
    site_tmpl_file.close()

    # Stores HTML string of rendered movies
    rendered_movies = ''

    for movie in movies:
        rendered_movies += _render_movie(movie)

    # Replace the `{movies}` placeholder with the rendered movies
    site = site_tmpl.replace('{movies}', rendered_movies)
    
    return site

def _render_movie(movie):
    """Render the movie object into an HTML string.

    Args:
        movie (Movie): A movie object.

    Returns:
        HTML string repersents the passed movie object.

    """

    # Get and render the movie template
    rendered_movie = _get_movie_template().format(
        title = movie.title,
        year = movie.year,
        director = movie.director,
        length = movie.length,
        genre = movie.genre,
        excerpt = movie.excerpt,
        cast = movie.cast_string,
        youtube_trailer = movie.youtube_trailer,
        rendered_rate = _render_rate(movie.rate),
        rate = movie.rate,
        poster_url = movie.poster_url,
        poster_source = movie.poster_source_url)
    
    return rendered_movie

def _get_movie_template():
    """Returns movie tempate from file `_movie-template.html`.

    Globals:
        __movie_template__

    Note:
        When this method called in the first time, it reads the
        file `_movie-template.html` and store its contents in the global
        variable `__movie_template__`. So, when it's called for another time,
        it returns the content from the global variable `__movie_template`.
    
    """
    
    global __movie_template__

    # Retrieve the movie template if it is already stored
    if __movie_template__:
        return __movie_template__

    # Open and read the movie template
    mv_tmpl_file = open('_movie-template.html')
    __movie_template__ = mv_tmpl_file.read()
    mv_tmpl_file.close()

    return __movie_template__

def _render_rate(rate):
    """Renders the rate number into an HTML format to appear as stars."""

    # If `rate` is a decimal number, this will implay that there's a half star.
    # And to detect that we ceil it's value and then compare it with its self.
    # Note: it doesn't matter using `ceil` or `floor` here, both will achieve
    #   the same thing.
    half_star = math.ceil(rate) != rate

    # Stores HTML string of rendered files
    rendered_stars = ''

    # Render all full stars, (exludes half stars using floor)    
    for _star in range(0, int(math.floor(rate))):
        rendered_stars += r'<i class="fa fa-star"></i> '

    # Render the half star if there's one
    if half_star:
        rendered_stars += r'<i class="fa fa-star-half-full"></i>'

    return rendered_stars
