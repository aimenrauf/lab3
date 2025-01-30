def longestStreak(streaks):
    maxStreaks = []
    userNames = ["User  1", "User  2", "User  3", "User  4", "User  5"] 
    for userStreaks in streaks:
        maxStreak = max(userStreaks)  
        maxStreaks.append(maxStreak) 
    longest_streak = max(maxStreaks)
    user_longest_streak = userNames[maxStreaks.index(longest_streak)]
    return user_longest_streak, longest_streak
streaks = [
    [1, 2, 3, 4, 2, 1, 0],  
    [0, 1, 1, 2, 3, 4, 5],  
    [2, 2, 2, 2, 2, 2, 2],  
    [1, 0, 0, 1, 1, 1, 1],  
    [3, 3, 3, 3, 3, 3, 3]   
]
user, longest_streak = longestStreak(streaks)
print(f"The user with the longest streak is {user} with a streak of {longest_streak}.")
