def calculate_leaderboard_data(scores):
    leaderboard_data = [] 
    
    users_data = []  

    for user in scores:
        """
        For each user in the scores list:
        - Initialize the total score for the current user to 0.
        - Retrieve and sort the user's submissions by score in descending order.
        - If the user has at least 3 submissions, they are eligible to appear on the ranking.
        - Sum the scores of the top 24 submissions (or fewer if they have less than 24).
        - If the user has fewer than 3 submissions, they are not eligible to appear on the ranking.
        - If the user qualifies, append their name and total score to the 'users_data' list.
        """
        currentUserScoreTotal = 0 

        submissions = user["submissions"] 

        sorted_submissions = sorted(submissions, key=lambda x: x['score'], reverse=True) 

        numOfSubmissions = len(sorted_submissions) 

        userValidToAppear = False 

        if numOfSubmissions >= 3: 

            userValidToAppear = True 

            for submission in sorted_submissions[:24]: 
                currentUserScoreTotal += submission["score"] 
        
        else: 
            userValidToAppear = False 

        if userValidToAppear: 
            users_data.append({
                'name': user["name"],
                'overall score': currentUserScoreTotal            
            })
    
    # sort the users by overall score from highest to lowest
    sorted_users_data = sorted(users_data, key=lambda x: x['overall score'], reverse=True) 

    """
    Initialize the current user's rank to 0. 
    Loop through the sorted user data and increment the rank for each user.
    Which works because we sorted the users by overall score in descending order (meaning the highest ranked)
    would be at the top of the sorted user data.
    For each user, append their rank, name, and overall score to the leaderboard data.
    The result is a list of users with their ranks and scores (ordered from highet to lowest), which is returned at the end.
    """

    currentUserRank = 0 
    for user in sorted_users_data:
        currentUserRank += 1 
        leaderboard_data.append({
            'rank': currentUserRank, 
            'name': user['name'],
            'overall score': user['overall score']
        })
    
    return leaderboard_data 