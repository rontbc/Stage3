import media
import fresh_tomatoes

rogue_one = media.Movie("Star Wars : Rogue One", "Rebels versus the Empire, missing story between Star Wars Episode 3 and 4", "http://fraghero.com/wp-content/uploads/2016/04/rg1.jpg", "https://youtu.be/frdj1zb9sMY")
hacksaw_ridge = media.Movie("Hacksaw Ridge", "A story of a medic during the battle of Okinawa", "https://hustonsite.files.wordpress.com/2016/07/hacksawposter1.jpg?w=700&h=&crop=1", "https://www.youtube.com/watch?v=Vso5o11LuGU")
moana = media.Movie("Moana", "About a spirited teenager who sails out on a daring mission to prove herself a master wayfinder and fulfill her ancestors' unfinished quest", "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS", "https://www.youtube.com/watch?v=M5dnZKrUpdA")
doctor_strange = media.Movie("Doctor Strange", "Marvel's Dr. Strange origins story", "http://t3.gstatic.com/images?q=tbn:ANd9GcSmG4ms8wxdnuKOwetpc4qltTv7pHopDLRTi-t98dx-L-kt_b1t", "https://www.youtube.com/watch?v=HSzx-zryEgM")
life_of_pets = media.Movie("The Secret Life of Pets", "The life story of what pets do when their masters are away", "http://vignette3.wikia.nocookie.net/secretlifeofpets/images/e/ed/The-secret-life-of-pets-poster-max.jpg/revision/latest/scale-to-width-down/329?cb=20160706161022", "https://www.youtube.com/watch?v=i-80SGWfEjM")
storks = media.Movie("Storks", "Cartoon animation about the role of storks and babies", "http://t3.gstatic.com/images?q=tbn:ANd9GcSQq_t91J3Rtb5v1gbnqGPF6BSDeFvtFcVmxU50nuczt5KHWsP8", "https://www.youtube.com/watch?v=ZENmkJk9fBM")
#girl_on_train = ("The Girl on the Train", "A drama about a person coping with issues", "http://t0.gstatic.com/images?q=tbn:ANd9GcSmPddcMVTBtnUjJ8v6IpQez6NMo8WT-wCwgpTPJRYtAPA_NF2y", "https://www.youtube.com/watch?v=KkoEE1i0CX8")
#deepwater_horizon = ("Deepwater Horizon", "Movie about a oil drilling rig explosion", "http://t2.gstatic.com/images?q=tbn:ANd9GcSoXHUjRemUrbCBO2Dsrw9lonK0kaaI0sLxm1sfwpK4ytlZt5Dm","https://www.youtube.com/watch?v=8yASbM8M2vg")

movies = [rogue_one, hacksaw_ridge, moana, doctor_strange, life_of_pets, storks]
fresh_tomatoes.open_movies_page(movies)
