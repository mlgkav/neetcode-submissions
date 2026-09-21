class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweet_map[userId]
        if len(tweets) == 10: # discard stale tweets
            tweets.pop(0)
        self.count -= 1
        tweets.append((self.count, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.follow_map[userId] | {userId}

        # build heap
        max_heap = []
        for followee in following:
            tweets = self.tweet_map[followee]
            if not tweets:
                continue
            time_stamp, tweet_id = tweets[-1]
            heap_val = (time_stamp, tweet_id, tweets, len(tweets) - 1)
            if len(max_heap) == 10: # keep heap size to 10
                heapq.heappushpop(max_heap, heap_val)
            else:
                heapq.heappush(max_heap, heap_val)
        
        # build feed from heap
        feed = []
        while max_heap: 
            _, tweet_id, tweets, idx = heapq.heappop(max_heap)

            feed.append(tweet_id)
            if len(feed) == 10:
                break

            # only push to heap if there are remaining tweets
            if idx != 0:
                idx -= 1
                time_stamp, tweet_id = tweets[idx]
                heap_val = (time_stamp, tweet_id, tweets, idx)
                heapq.heappush(max_heap, heap_val)

        return feed



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
