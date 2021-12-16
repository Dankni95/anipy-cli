from src import query, url, tools
import argparse
from threading import Thread

# TODO:
#     [] - add threading for mpv process to be able to do more stuff
#     [] - add more options
#     [] - add next ep ,last ep etc. 
#     [] - add downloading
#     [x] - add History with resume   

my_parser = argparse.ArgumentParser(description='Play Animes from gogoanime in local video-player.')
my_parser.add_argument('-q', '--quality', action='store', required=False, help='Pick quality. 1080, 720, 480 etc. / best,worst')
my_parser.add_argument('-H', '--history', required=False, dest="history", action='store_true', help='Play History. History file stored in history/history.txt')           
my_parser.add_argument('-d', '--delete-history', required=False, dest='delete', action='store_true', help='Delete your History.')
args = my_parser.parse_args()


if args.delete == True:
    try:
        open("history/history.txt", "w")
        print("Done.")
        
    except:
        print('\033[93m' + "There is no History-File.")
        
    quit()

def main():
    
    if args.history == False:
        search = input("Search for Anime: ")
        link = query.query(search)
        link_with_episode = query.episode(link)
    else:
        picked_history = tools.pick_history()
        link_with_episode = picked_history[0]
        
    embed_url = url.get_embed_url(link_with_episode)
    video_url = url.get_video_url(embed_url)    
    video_url = url.quality(video_url, embed_url, args.quality)
    
    if args.history == False:
        t1 = Thread(target=tools.play , args=(embed_url, video_url, link_with_episode, args.history,))
        t1.start()
    else:
        t1 = Thread(target=tools.play , args=(embed_url, video_url, link_with_episode, args.history, picked_history[1], ))
        t1.start()
        
if __name__ == "__main__":
    main()
