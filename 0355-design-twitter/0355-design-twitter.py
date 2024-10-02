from collections import defaultdict , deque
import heapq as hq
class Twitter:

    def __init__(self):
        self.usertweets = defaultdict(list)
        self.userfollow = defaultdict(set)
        self.timestamp  = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.usertweets:
            self.usertweets[userId] = deque()
        q = self.usertweets[userId]
        if len(q) >= 10:
            q.popleft()            
        q.append([self.timestamp,tweetId])
        
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = list(self.usertweets[userId])

        for followee_id in self.userfollow[userId]:
            if followee_id == userId:
                continue
            tweets += list(self.usertweets[followee_id])

        tweets.sort(key=lambda x: -x[0])
        ans = [tweet[1] for tweet in tweets]
        return ans[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userfollow:
            self.userfollow[followerId] = set()
        user_follow = self.userfollow[followerId]
        user_follow.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user_follow = self.userfollow[followerId]
        if followeeId in user_follow: 
            user_follow.remove(followeeId)        
