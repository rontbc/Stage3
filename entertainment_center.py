import media
import fresh_tomatoes

rogue_one = media.Movie("Star Wars : Rogue One", "Rebels versus the Empire, missing story between Star Wars Episode 3 and 4", "http://fraghero.com/wp-content/uploads/2016/04/rg1.jpg", "https://youtu.be/frdj1zb9sMY")
dunkirk_ww2 = media.Movie("Dunkirk World War 2 Movie", "The evacuation of allied troops at Dunkirk during World War 2", "https://www.trailers.tube/wp-content/uploads/2016/08/Dunkirk-movie-poster-480x717.jpg", "https://youtu.be/yM9BWtppzko")
moana = media.Movie("Moana", "About a spirited teenager who sails out on a daring mission to prove herself a master wayfinder and fulfill her ancestors' unfinished quest", "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS", "https://www.youtube.com/watch?v=M5dnZKrUpdA")
doctor_strange = media.Movie("Doctor Strange", "Marvel's Dr. Strange origins story", "http://t3.gstatic.com/images?q=tbn:ANd9GcSmG4ms8wxdnuKOwetpc4qltTv7pHopDLRTi-t98dx-L-kt_b1t", "https://www.youtube.com/watch?v=HSzx-zryEgM")
life_of_pets = media.Movie("The Secret Life of Pets", "The life story of what pets do when their masters are away", "http://vignette3.wikia.nocookie.net/secretlifeofpets/images/e/ed/The-secret-life-of-pets-poster-max.jpg/revision/latest/scale-to-width-down/329?cb=20160706161022", "https://www.youtube.com/watch?v=i-80SGWfEjM")

#arrival = ("The Arrival", "A tale about alien contact on Earth", "http://t0.gstatic.com/images?q=tbn:ANd9GcSMztVicsYXcHHWNkejxIoFcW4H1eKhjSghAVixeAueuPEXmSKN", "https://www.youtube.com/watch?v=tFMo3UJ4B4g")
#deepwater_horizon = ("Deepwater Horizon", "Movie about a oil drilling rig explosion", "http://t2.gstatic.com/images?q=tbn:ANd9GcSoXHUjRemUrbCBO2Dsrw9lonK0kaaI0sLxm1sfwpK4ytlZt5Dm","https://www.youtube.com/watch?v=8yASbM8M2vg")

movies = [rogue_one, dunkirk_ww2, moana, life_of_pets, doctor_strange]
fresh_tomatoes.open_movies_page(movies)
