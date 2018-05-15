import fresh_tomatoes
import media

# Main file - creates a list of movies and passes them to the function that opens them in a web page.
# Bijan Marashi (bm6410@att.com)
# Borrowed heavily from the tutorials in Udacity

bill_and_ted = media.Movie("Bill & Ted's Excellent Adventure",
  "Be excellent to each other...",
  "https://upload.wikimedia.org/wikipedia/en/b/bc/Bill_%26_Ted.jpg",
  "https://www.youtube.com/watch?v=q3fx6TugN7g")

elvira = media.Movie("Elvira: Mistress of the Dark",
  "Elvira makes her big SCREAM debut!",
  "https://upload.wikimedia.org/wikipedia/en/4/4f/Elviramistressofthedarkposter.jpg",
  "https://www.youtube.com/watch?v=ZIWLCcCj2h8")

woodstock = media.Movie("Woodstock",
  "Three days of peace, love, and music",
  "https://upload.wikimedia.org/wikipedia/en/3/35/WoodstockFilmPoster.jpg",
  "https://www.youtube.com/watch?v=CiiKwN32yqg")

godfather = media.Movie("The Godfather",
  "An offer you can't refuse",
  "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
  "https://www.youtube.com/watch?v=sY1S34973zA")

date_night = media.Movie("Date Night",
  "Just a boring couple from New Jersey",
  "https://upload.wikimedia.org/wikipedia/en/0/08/Date_night_poster.jpg",
  "https://www.youtube.com/watch?v=aspBKFz2dBI")

mission_impossible = media.Movie("Mission Impossible: Ghost Protocol",
  "No Plan. No Backup. No Choice.",
  "https://upload.wikimedia.org/wikipedia/en/b/b5/Mission_impossible_ghost_protocol.jpg",
  "https://www.youtube.com/watch?v=EDGYVFZxsXQ")

movies = [bill_and_ted, elvira, woodstock, godfather, date_night, mission_impossible]

fresh_tomatoes.open_movies_page(movies)

# TODO(bm6410@att.com) Remove the debugging code at some point
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
