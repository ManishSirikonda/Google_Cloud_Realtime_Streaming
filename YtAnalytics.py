import requests
import json
from constants import YOUTUBE_API_KEY
if __name__ == '__main__':
    response = requests.get("https://www.googleapis.com/youtube/v3/videos",
                            {
                                'key' : YOUTUBE_API_KEY,
                                'id' : "kA3sNBh6vd8",
                                'part': 'snippet, statistics, status'
                            })

    response = json.loads(response.text)['items']
    for video in response: 
        video_res = {
            'title' : video['snippet']['title'],
            'likes' : video['statistics'].get('likeCount', 0),
            'comments' : video['statistics'].get('commentCount', 0),
            'views' : video['statistics'].get('viewCount', 0),
            'thumbnail' : video['snippet']['thumbnails']['default']['url']
            
        }
        print(video_res)