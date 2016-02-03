# -*- coding: utf-8 -*-
from media import Cast, Movie
import lovely_dove

# You might consider using OMDb API instead (http://www.omdbapi.com/)

# Movies (Begin) ||==================================================

## Interstellar
interstellar = Movie('Interstellar', 2014, 'Christopher Nolan', 169,
                     'Adventure, Drama, Sci-Fi',
                     'A team of explorers travel '
                     'through a wormhole in space in an attempt to ensure '
                     'humanity\'s survival.',
                     'http://www.youtube.com/embed/zSWdZVtXT7E', 5,
                     'http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg')
interstellar.add_cast('Matthew McConaughey', True)
interstellar.add_cast('Anne Hathaway', True)
interstellar.add_cast('Jessica Chastain', True)
interstellar.add_cast('Mackenzie Foy', False)

## Agora
agora = Movie('Agora', 2009, 'Alejandro Amenábar', 127,
              'Adventure, Drama, History',
              'A historical drama set in Roman Egypt, concerning a slave who '
              'turns to the rising tide of Christianity in the hope of '
              'pursuing freedom while falling in love with his mistress, the '
              'famous philosophy and mathematics professor '
              'Hypatia of Alexandria.',
              'https://www.youtube.com/embed/RbuEhwselE0', 4.5,
              'https://upload.wikimedia.org/wikipedia/en/8/81/Agoraposter09.jpg')
agora.add_cast('Rachel Weisz', True)
agora.add_cast('Max Minghella', True)
agora.add_cast('Oscar Isaac', True)
agora.add_cast('Ashraf Barhom', False)

## A Beautiful Mind
beautiful_mind = Movie('A Beautiful Mind', 2001, 'Ron Howard', 135,
              'Biography, Drama',
              'After a brilliant but asocial mathematician, John Nash, accepts '
              'secret work in cryptography, his life takes a turn for the '
              'nightmarish.',
              'https://www.youtube.com/embed/UT4Oq_dOofY', 5,
              'https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg')
beautiful_mind.add_cast('Russell Crowe', True)
beautiful_mind.add_cast('Ed Harris', True)
beautiful_mind.add_cast('Jennifer Connelly', True)

## Gladiator
gladiator = Movie('Gladiator', 2000, 'Ridley Scott', 171,
              'Action, Drama',
              'When a Roman general is betrayed and his family murdered by an '
              'emperor\'s corrupt son, he comes to Rome as a gladiator to seek '
              'revenge.',
              'https://www.youtube.com/embed/Q-b7B8tOAQU', 4.5,
              'https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg')
gladiator.add_cast('Russell Crowe', True)
gladiator.add_cast('Joaquin Phoenix', True)
gladiator.add_cast('Connie Nielsen', True)

## PK
pk = Movie('PK', 2014, 'Rajkumar Hirani', 153,
              'Comedy, Drama, Romance',
              'A stranger in the city asks questions no one has asked before. '
              'Known only by his initials, P.K.\'s innocent questions and '
              'childlike curiosity will take him on a journey of love, '
              'laughter and letting go.',
              'https://www.youtube.com/embed/SOXWc32k4zA', 5,
              'https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg')
pk.add_cast('Aamir Khan', True)
pk.add_cast('Anushka Sharma', True)
pk.add_cast('Sanjay Dutt', True)
pk.add_cast('Boman Irani', False)

## I am Sam
i_am_sam = Movie('I am Sam', 2001, 'Jessie Nelson', 132,
              'Drama',
              'A mentally handicapped man fights for custody of his 7-year-old '
              'daughter, and in the process teaches his cold hearted lawyer the '
              'value of love and family.',
              'https://www.youtube.com/embed/ir6_2EkhzAc', 4.5,
              'https://upload.wikimedia.org/wikipedia/en/2/26/ImAmSamSeanMichelle.jpg')
i_am_sam.add_cast('Sean Penn', True)
i_am_sam.add_cast('Michelle Pfeiffer', True)
i_am_sam.add_cast('Dakota Fanning', True)
i_am_sam.add_cast('Dianne Wiest', False)

## Fury
fury = Movie('Fury', 2014, 'David Ayer', 134,
              'Action, Drama, War',
              'April, 1945. As the Allies make their final push in the European Theatre, a battle-hardened Army sergeant named Wardaddy commands a Sherman tank and his five-man crew on a deadly mission behind enemy lines. Outnumbered, out-gunned, and with a rookie soldier thrust into their platoon, Wardaddy and his men face overwhelming odds in their heroic attempts to strike at the heart of Nazi Germany.',
              'https://www.youtube.com/embed/SKu5lGfRBxc', 4.5,
              'https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg')
fury.add_cast('Brad Pitt', True)
fury.add_cast('Shia LaBeouf', True)
fury.add_cast('Logan Lerman', True)
fury.add_cast('Michael Peña', False)

## The Butler
the_butler = Movie('The Butler', 2013, 'Lee Daniels', 127,
              'Biography, Drama',
              'As Cecil Gaines serves eight presidents during his tenure as a '
              'butler at the White House, the civil rights movement, Vietnam, '
              'and other major events affect this man\'s life, family, and '
              'American society.',
              'https://www.youtube.com/embed/FuojHqfe4Vk', 4.5,
              'https://upload.wikimedia.org/wikipedia/en/2/2c/The_Butler_poster.jpg')
the_butler.add_cast('Forest Whitaker', True)
the_butler.add_cast('Oprah Winfrey', True)
the_butler.add_cast('John Cusack', True)

## Like Stars on Earth
like_stars_on_earth = Movie('Like Stars on Earth', 2007, 'Aamir Khan', 165,
              'Drama, Family, Music',
              'An eight-year-old boy is thought to be lazy and a '
              'trouble-maker, until the new art teacher has the patience and '
              'compassion to discover the real problem behind his struggles in '
              'school.',
              'https://www.youtube.com/embed/DBg6HSMF9X8', 5,
              'https://upload.wikimedia.org/wikipedia/en/b/bd/TaareZameenPar.jpg')
like_stars_on_earth.add_cast('Darsheel Safary', True)
like_stars_on_earth.add_cast('Aamir Khan', True)
like_stars_on_earth.add_cast('Tanay Chheda', True)

## Noah
noah = Movie('Noah', 2014, 'Darren Aronofsky', 138,
              'Action, Adventure, Drama',
              'A man is chosen by his world\'s creator to undertake a '
              'momentous mission before an apocalyptic flood cleanses '
              'the world.',
              'https://www.youtube.com/embed/fdu10cX3pWA', 4,
              'https://upload.wikimedia.org/wikipedia/en/4/41/Noah2014Poster.jpg')
noah.add_cast('Russell Crowe', True)
noah.add_cast('Jennifer Connelly', True)
noah.add_cast('Anthony Hopkins', True)
noah.add_cast('Emma Watson', False)

## 7 Pounds
seven_pounds = Movie('Seven Pounds', 2008, 'Gabriele Muccino', 123,
              'Drama, Romance',
              'A man with a fateful secret embarks on an extraordinary journey '
              'of redemption by forever changing the lives of seven strangers.',
              'https://www.youtube.com/embed/MwrtEI-fcmM', 4.5,
              'https://upload.wikimedia.org/wikipedia/en/2/2d/Seven_Pounds_poster.jpg')
seven_pounds.add_cast('Will Smith', True)
seven_pounds.add_cast('Rosario Dawson', True)
seven_pounds.add_cast('Woody Harrelson', True)
seven_pounds.add_cast('Robinne Lee', False)

## Dumb and Dumber
dumb_and_dumber_to = Movie('Dumb and Dumber To', 2014, 'Bobby Farrelly', 109,
              'Comedy',
              'Twenty years since their first adventure, Lloyd and Harry go on '
              'a road trip to find Harry\'s newly discovered daughter, who was '
              'given up for adoption.',
              'https://www.youtube.com/embed/bIqvQFqPavA', 4,
              'https://upload.wikimedia.org/wikipedia/en/8/83/Dumb_and_Dumber_To_Poster.jpg')
dumb_and_dumber_to.add_cast('Jim Carrey', True)
dumb_and_dumber_to.add_cast('Jeff Daniels', True)
dumb_and_dumber_to.add_cast('Rob Riggle', True)


# Movies (End) ||==================================================

# Group all movies in one list
movies = [interstellar, agora, beautiful_mind, gladiator,
          pk, i_am_sam, fury, the_butler, like_stars_on_earth,
          noah, seven_pounds, dumb_and_dumber_to]

# Launch the web page
lovely_dove.fly_and_open_movies_page(movies)
