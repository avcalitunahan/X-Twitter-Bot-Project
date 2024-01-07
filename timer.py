import time     

tweet_time = 7200 # 2 hours

def timer():
    for x in range(tweet_time, 0, -1):
        seconds = x % 60
        minutes = int(x /60) % 60
        hours = int(x / 3600 )
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

