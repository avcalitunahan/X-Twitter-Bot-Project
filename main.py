import ai
import timer
import tweetFunctions

def main():
   horoscope_number = 0
   while True:
    tweet = ai.ai_Configuration(horoscope_number)
    tweetFunctions.createTweet(tweet)
    timer.timer()
    horoscope_number += 1
    if(horoscope_number > 11 ):
       horoscope_number = 0
       
    

if __name__ == "__main__":
    main()