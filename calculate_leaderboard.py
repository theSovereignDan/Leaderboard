def calculate_leaderboard(scores):
    leaderboard_data = [] # create an empty list to store the leaderboard data
    
    users_data = []  # create an empty list to store the users data

    for user in scores:
        currentUserScoreTotal = 0 # Initialize the total score for the current user

        submissions = user["submissions"] # Get the submissions for the current user

        sorted_submissions = sorted(submissions, key=lambda x: x['score'], reverse=True) # Sort the submissions by score from highest to lowest

        numOfSubmissions = len(sorted_submissions) # Get the number of submissions for the current user

        userValidToAppear = False # creates variable to check if the user can appear on the ranking

        if numOfSubmissions >= 3: # If the user has made at least 3 submissions

            userValidToAppear = True # if the user has made at least 3 submissions then they can appear on the ranking so sets to true

            #loop through the top 24 submissions for the current user if the user has more than 24 submissions
            # if not it loops up to the number of submissions the user has made
            for submission in sorted_submissions[:24]: 
                currentUserScoreTotal += submission["score"] # adds the score to the total score for the current user
        
        else: # If the user has made less than 3 submissions
            userValidToAppear = False # if the user has made less than 3 submissions then they cannot appear on the ranking so sets to false

        if userValidToAppear: # if the user can appear on the ranking
            users_data.append({
                'name': user["name"],
                'overall score': currentUserScoreTotal            
            })
    
    sorted_users_data = sorted(users_data, key=lambda x: x['overall score'], reverse=True) # sort the users by overall score from highest to lowest

    currentUserRank = 0 # Initialize the current user rank to 0
    for user in sorted_users_data:
        currentUserRank += 1 # increment the current user rank by 1
        leaderboard_data.append({
            'rank': currentUserRank, 
            'name': user['name'],
            'overall score': user['overall score']
        })
    
    return leaderboard_data # return the leaderboard data