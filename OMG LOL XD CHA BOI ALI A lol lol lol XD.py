import webbrowser as wb
import pyautogui as pg
points = 0
show = pg.prompt ("What is your favorite TV show? ")

if show == "Hannah Montana":
    pg.alert("OMG LOL xD ;P")
    points += .000002032000012
    wb.open("https://www.youtube.com/watch?v=s9q61m7S9yA")
elif show == "Happy Tree Friends":
    pg.alert("I love how much gore is in that show!")
    points -= .000000000000009
    wb.open("https://youtu.be/dfTPlsIq7d0?t=327")
elif show == "Dance Moms":
    pg.prompt ("      ")
    pg.alert ("OMG lol Jip Clarkes favorite too")
    points += .120000000000000000
    wb.open("https://www.youtube.com/watch?v=LEtorWba_Fg")
elif show == "The Office":
    wb.open("https://www.youtube.com/watch?v=PIQqKsY63xQ")
elif show == "Family Guy":
    wb.open("https://www.youtube.com/watch?v=9mjg9qEBfXs")
elif show == "Elmo":
    wb.open("https://www.youtube.com/watch?v=jzWcLBQGi-0")
else:
    pg.alert("Your favorite show is " + show)
    points += .3777777777779999028323
    wb.open("https://youtu.be/kOTRybt4wQQ?t=35")
    
dance = pg.prompt ("Whats your favorite fortnite dance?")
if dance == "Banana emote":
    pg.alert("OMEGALUL MY MOMS FAVORITE TOO!")
    points += 1
    wb.open("https://www.youtube.com/watch?v=0jep3Oj2Mkg")
elif dance == "Indian sacrifice ritual":
    pg.alert ("Ogwa suompi whi")
    points -= 6969
    wb.open("https://www.youtube.com/watch?v=SIaFtAKnqBU")
elif dance == "Disco fever":
    pg.alert ("That is french for stink lipstick")
    points += 6970
    wb.open("https://www.youtube.com/watch?v=SwFNtOVaSok")
elif dance == "Cha boi drop da bass":
    pg.alert ("Nerd")
    points -= 122330432
    wb.open("https://www.youtube.com/watch?v=ixscoaWEEnQ")
elif dance == "Family Guy":
    wb.open ("https://youtu.be/TEZQ2rg-Rlg?t=41")
elif dance == "American Dad":
    wb.open ("https://www.youtube.com/watch?v=EzkJGHD49gk")
else:
    pg.alert("Your favorite show is " + show)

    
food = pg.prompt ("What is your favorite TV food? ")

if food == "hot dog":
    pg.alert("HA")
    points += .000002032000012
    wb.open("https://www.youtube.com/watch?v=pY7hFRg2jvw")
elif food == "Tacos from the aztecs":
    pg.alert("Nice")
    points -= .000000000000009
    wb.open("https://youtu.be/dfTPlsIq7d0?t=327")
elif food == "Purple Chicken":
    pg.prompt ("      ")
    pg.alert ("OMG lol Jip Clarkes favorite too")
    points += .120000000000000000
    wb.open("https://sadanduseless.b-cdn.net/wp-content/uploads/2016/09/human-eyes18.jpg")
elif food == "The Office":
    wb.open("https://www.youtube.com/watch?v=PIQqKsY63xQ")
elif food == "Family Guy":
    wb.open("https://www.youtube.com/watch?v=9mjg9qEBfXs")
elif food == "Elmo":
    wb.open("https://www.youtube.com/watch?v=jzWcLBQGi-0")
else:
    pg.alert("Your favorite food is " + food)
    points += .3777777777779999028323
    wb.open("https://youtu.be/kOTRybt4wQQ?t=35")
    
movie = pg.prompt ("Whats your favorite fortnite movie?")
if movie == "Banana emote":
    pg.alert("OMEGALUL MY MOMS FAVORITE TOO!")
    points += 1
    wb.open("https://www.youtube.com/watch?v=0jep3Oj2Mkg")
elif movie == "Indian sacrifice ritual":
    pg.alert ("Ogwa suompi whi")
    points -= 6969
    wb.open("https://www.youtube.com/watch?v=SIaFtAKnqBU")
elif movie == "Disco fever":
    pg.alert ("That is french for stink lipstick")
    points += 6970
    wb.open("https://www.youtube.com/watch?v=SwFNtOVaSok")
elif movie == "Cha boi drop da bass":
    pg.alert ("Nerd")
    points -= 122330432
    wb.open("https://www.youtube.com/watch?v=ixscoaWEEnQ")
elif movie == "Family Guy":
    wb.open ("https://youtu.be/TEZQ2rg-Rlg?t=41")
elif movie == "American Dad":
    wb.open ("")
else:
    pg.alert("Your favorite show is " + movie)
    
pg.alert(points)

