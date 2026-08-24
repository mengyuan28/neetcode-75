from collections import defaultdict
from typing import List, Dict, Tuple

class Twitter:

    def __init__(self):
        self.followingList: Dict[int, set] = defaultdict(set)
        self.clock = 0
        self.tweets: Dict[int, List[Tuple[int, int]]] = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock += 1
        self.tweets[userId].append((tweetId, self.clock))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        all_tweets.extend(self.tweets[userId])
        for following_id in self.followingList[userId]:
            all_tweets.extend(self.tweets[following_id])
        all_tweets.sort(key=lambda x: x[1])
        count = 0
        ret = []
        for tweetId, time in reversed(all_tweets):
            ret.append(tweetId)
            count += 1
            if count >= 10:
                break
        return ret
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingList[followerId].discard(followeeId)
        
