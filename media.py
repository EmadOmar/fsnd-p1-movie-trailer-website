class Movie():
    """Holds a movie information

    Note:
        Args and Attributes are ordered according to their occurrence in
        the HTML web page.

    Args:
        title (str): Movie title.
        year (int): Release year.
        director (str): Director name.
        length (int): Movie length / duration.
        genre (str): Movie genre(s).
        excerpt (str): Short description of the movie.
        youtube_trailer (str): URL link to the movie trailer on Youtube.
        rate (int): Your personal rate of the movie in 5.
        poster_url (str): URL link to the poster image
            (should be on Wikipedia to auto identify
                the `self.poster_source_url`).

    Attributes:
        title (str): Movie title.
        year (int): Release year.
        director (str): Director name.
        length (int): Movie length / duration.
        genre (str): Movie genre(s).
        excerpt (str): Short description of the movie.
        youtube_trailer (str): URL link to the movie trailer on Youtube.
        rate (int): Your personal rate of the movie in 5.
        poster_url (str): URL link to the poster image.
        poster_source_url (str): URL link to the source of the poster image.
        cast (Cast[]): List of movie cast.

    """
    
    def __init__(self, title, year, director, length, genre,
                 excerpt, youtube_trailer, rate, poster_url):
        self.title = title
        self.year = year
        self.director = director
        self.length = length
        self.genre = genre
        self.excerpt = excerpt
        self.youtube_trailer = youtube_trailer
        self.rate = rate
        self.poster_url = poster_url

        """`self.poster_source_url` can be inferred from the `self.poster_url`
        if it uses Wikimedia link. We just take the image name from
        `self.poster_url` which is after the last `/` in the URL link. And
        then add it to the end of the static Wikipedia URL to form the
        `self.poster_source_url`.

        Note:
            the `poster_url.rsplit(r'/', 1)` statement will return an array
            contains the splited url in this form `[rest_of_url, img_name.ext]`.

            For example: The following URL poster link
                `http://upload.wikimedia.org/.../bc/Some_Poster.jpg`
                will be splited to
                `['http://upload.wikimedia.org/.../bc', 'Some_Poster.jpg']`

        """
        self.poster_source_url = r'https://en.wikipedia.org/wiki/File:' \
                                    + poster_url.rsplit(r'/', 1)[1]

        self.cast = []

    def add_cast(self, name, is_starring):
        """Adds a new cast person to the movie cast list.

        Example:
            add_cast('Someone Nice', True)

        Args:
            name (str): Cast person name.
            is_starring (bool): Whether the cast is starring in the current
                movie.

        """
        
        self.cast.append(Cast(name, is_starring))

    @property
    def cast_string(self):
        """str: List of movie cast repersented in a string form

        Note:
            - This is going to be passed to the HTML page to so that it
            understands the list and be able to render it as it wants.
        
            - The pattern of the cast string is: `cast name:[1|0]`
            seprated by a `,`. Where 1 means the cast is starring and 0 is not
            for example:
            `someone nice:1, someone two:0`.

        """
        
        cast_string = ''

        for cst in self.cast:
            cast_string += cst.name
            
            # This is to indicate whether the current cast is starring or not
            cast_string += ':' + ('1' if cst.is_starring else '0') + ','

        # check if cast string is not empty to remove the last `,`
        if cast_string:
            # remove the last charcter as the last `,` is definitely
            # the last character in the `cast_string`
            cast_string = cast_string[:-1]

        return cast_string

class Cast():
    """Hold information of a movie cast person.

    Args:
        name (str): Cast person name.
        is_starring (bool): Whether the cast is starring in the movie.

    Attributes:
        name (str): Cast person name.
        is_starring (bool): Whether the cast is starring in the movie.

    """
    
    def __init__(self, name, is_starring):
        self.name = name
        self.is_starring = is_starring
