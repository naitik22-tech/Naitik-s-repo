import time
import threading
import pygame

# Function to play the song
def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\naiti\\Python\\finding_her.mp3")
    pygame.mixer.music.play()
      # Replace with your MP3 file path

# Function to display lyrics
def show_lyrics():
    # Lyrics with approximate timings (in seconds)
    lyrics = [
        (0, "🎵 Finding Her - Sample Lyrics 🎵"),
        (16,"Jaana Tu Aata Nahi"),
        (4,"Sapno Se Jata Nahi"),
        (4,"Mil Jaye Kya Hi Baat Thi"),
        (5,"Kamil Ho Jata Wahin"),

        (4,"Jaana Mere Sawalon Ka Manzar Tu"),
        (4,"Han Mai Sukha Sa Sara Samandar Tu"),
        (4,"Haan Gulabi Si Surkhi Jo Dikhti Thi"),
        (5,"Phir Se Dikh Jaye Toh Jee Bhar Ke Saah Bhar Lu"),

        (5,"Kati Kitni Thi Raate Nai Soya Main"),
        (3,"Tujhko Kitna Bulaya Fir Roya Main"),
        (4,"Teri Sari Wo Baate Kyun Sone Nahi Deti"),
        (6,"Sataye Mujhe Haan Phir Khoya Main"),

        (4,"Tu Aata Nahi"),
        (3,"Sapno Se Jata Nahi"),
       (4,"Mil Jaye Kya Hi Baat Thi"),
        (4,"Kamil Ho Jata Wahin"),

        (5,"Jo Bhi Ho Raj Tera"),
        (4,"Mujhko Batata Nahi"),
        (3,"Mil Jaye Kya Hi Baat Thi"),
        (5,"Kamil Ho Jata Wahin"),

        (23,"Sambhal Ke Rakha Wo Phool Mera Tu"),
        (4,"Meri Shayari Me Zarur Raha Tu"),
        (4,"Jo Aakhon Mein Pyari Si Duniya Basayi"),
        (4,"Woh Duniya Bhi Tha Tu Woh Lamha Bhi Tha Tu"),

        (4,"Han Lagte Hain Mujhko Yeh Kisse Satane"),
        (4,"Deta Na Dil Mera Tujhko Bhulane"),
        (3,"Adhoore Se Wade Adhoori Si Raatein"),
        (5,"Ab Hisse Me Dakhil Mere Bas Woh Yaadein"),

        (4,"Rehna Tha Banke Humdum Tera"),
        (4,"Aise Jana Hi Tha Fir Tu Kyun Thehra"),
        (4,"Ab Na Maane Mera Dil Ke Na Tere Kabil"),
        (5,"Thi Ik Arzoo Ki Main Kehta Raha Par"),

        (4,"Tu Aata Nai") ,
        (3,"Sapno Se Jata Nai"),
        (3,"Mil Jaye Kya Hi Baat Thi"),
        (4,"Kaamil Ho Jaata Wahin"),

        (5,"Jo Bhi Ho Raaz Tera"),
       (4,"Mujhko Batata Nahi"),
        (3,"Miljaye Kya Hi Baat Thi"),
        (4,"Kaamil Ho Jata Wahin")
        
         # Add more lines as needed...
         ]

    for delay, line in lyrics:
        time.sleep(delay)
        print(line)

# Run both song and lyrics together
threading.Thread(target=play_song).start()
show_lyrics()
