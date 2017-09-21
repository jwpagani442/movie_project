import media
import fresh_tomatoes

#Create movie objects for each of my favorite movies
the_sting = media.Movie("The Sting",
                        "A con job",
                        "https://en.wikipedia.org/wiki/The_Sting#/media/File:Stingredfordnewman.jpg",
                        "https://www.youtube.com/watch?v=_nAIb_J9T5M")


avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=-9ceBgWV8io")

inception = media.Movie("Inception",
                        "Are your dreams real?",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

dark_knight = media.Movie("The Dark Knight",
                        "The sequel to Batman Begins",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

star_wars = media.Movie("Star Wars: The Force Awakens",
                        "Episode VII",
                        "https://vignette.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest?cb=20151018162823",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

looper = media.Movie("Looper",
                        "Time travel",
                        "http://www.sonypictures.com/movies/looper/assets/images/onesheet.jpg",
                        "https://www.youtube.com/watch?v=5AXwtch744A")

#Movies dictionary
movies = [toy_story,avatar,inception,dark_knight,star_wars,looper]

#Call fresh_tomatoes class to create HTML page
fresh_tomatoes.open_movies_page(movies)
