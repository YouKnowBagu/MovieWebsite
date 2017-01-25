import fresh_tomatoes
import media


big_lebowski = media.Movie("The Big Lebowski",
                            "'The Dude' Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined  rug and enlists his bowling buddies to help get it.",
                            "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                            "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                            "1998")
my_neighbor_totoro = media.Movie("My Neighbor Totoro",
                                  "When two girls move to the country to be near their ailing mother, they have adventures with the wonderous forest spirits who live nearby.",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg/220px-My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                                  "https://www.youtube.com/watch?v=92a7Hj0ijLs",
                                  "1993")
saving_private_ryan = media.Movie("Saving Private Ryan",
                                   "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/Saving_Private_Ryan_poster.jpg/220px-Saving_Private_Ryan_poster.jpg",
                                   "https://www.youtube.com/watch?v=zwhP5b4tD6g",
                                   "1998")
jurassic_park = media.Movie("Jurassic Park",
                             "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=QWBKEmWWL38",
                             "1993")
memento = media.Movie("Memento",
                       "A man juggles searching for his wife's murderer and keeping his short-term memory loss from being an obstacle.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNThiYjM3MzktMDg3Yy00ZWQ3LTk3YWEtN2M0YmNmNWEwYTE3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=zgd0-VttkmA",
                       "2000")
blade_runner = media.Movie("Blade Runner",
                            "A blade runner must pursue and try to terminate four replicants who stole a ship in space and have returned to Earth to find their creator.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZWZlYmEyYTItNGRjYy00ZmMxLWEzMWItM2Q2NjZlNTMwMjQ3XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=KPcZHjKJBnE",
                            "1982")

movies_list = [big_lebowski,my_neighbor_totoro,saving_private_ryan,jurassic_park,memento,blade_runner]
fresh_tomatoes.open_movies_page(movies_list)
#Takes instances of movie for input create an HTML file.  Opens HTML file in browser.
