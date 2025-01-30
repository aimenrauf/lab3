def count_hashtags(tweets):
    hashtag_counts = {}
    for tweet in tweets:
        words = tweet.split()
        for word in words:
            if word.startswith("#"): 
                hashtag = word.lower()
                if hashtag in hashtag_counts:
                    hashtag_counts[hashtag] += 1
                else:
                    hashtag_counts[hashtag] = 1
    return hashtag_counts
def get_top_hashtags(hashtag_counts, top_n=3):
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_hashtags[:top_n] 
tweets = [
    "Loving the weather today! #sunny #happy",
    "Just had a great lunch! #food #happy",
    "Can't believe how sunny it is! #sunny #amazing",
    "Feeling great! #happy #motivation",
    "What a beautiful day! #sunny #nature",
    "Food is life! #food #delicious",
    "Stay positive! #motivation #happy"
]
hashtag_counts = count_hashtags(tweets)
top_hashtags = get_top_hashtags(hashtag_counts)
print("Top Hashtags:")
for hashtag, count in top_hashtags:
    print(f"{hashtag}: {count} occurrences")
