def filter_leaderboard(leaderboard_data, params):

    # Extract filtering parameters from the 'params' dictionary
    name = params["name"]
    score_filter = params["score_filter"]
    score_threshold = params["score_threshold"]
    score_threshold_low = params["score_threshold_low"]
    score_threshold_high = params["score_threshold_high"]
    rank_filter = params["rank_filter"]
    rank_threshold = params["rank_threshold"]
    rank_threshold_low = params["rank_threshold_low"]
    rank_threshold_high = params["rank_threshold_high"]

    # Initialize the filtered leaderboard with the original leaderboard data (unfiltered)
    filtered_leaderboard = leaderboard_data  

    # If a name search filter is provided, iterate through the leaderboard data and perform a case-insensitive match for the user's name.
    # For each user whose name matches, add them to a temporary list, and finally update the filtered leaderboard with the results.
    # the results contains only the users whose names match the search query.
    if name:
        name_filtered = []  
        for user in leaderboard_data:
            if user['name'].lower() == name.lower():  
                name_filtered.append(user)  
        filtered_leaderboard = name_filtered  

    # Apply score filtering if a score filter and thresholds are provided.
    # Depending on the filter type ('above', 'below', or 'between'), iterate over the filtered leaderboard and check the users' scores.
    # Add users that meet the criteria to a temporary list, then update the filtered leaderboard with these users.
    if score_filter and score_threshold or (score_filter and (score_threshold_low or score_threshold_high)):
        score_filtered = []  
        if score_filter == 'above' and score_threshold: 
            for user in filtered_leaderboard:  
                if user['overall score'] > score_threshold: 
                    score_filtered.append(user)  
        elif score_filter == 'below' and score_threshold:  
            for user in filtered_leaderboard:  
                if user['overall score'] < score_threshold:  
                    score_filtered.append(user)  
        elif score_filter == 'between' and score_threshold_low and score_threshold_high: 
            for user in filtered_leaderboard:  
                if score_threshold_low <= user['overall score'] <= score_threshold_high:  
                    score_filtered.append(user) 
        filtered_leaderboard = score_filtered  

    # Apply rank filtering if a rank filter and thresholds are provided.
    # Depending on the filter type ('above', 'below', or 'between'), iterate over the filtered leaderboard and check the users' ranks.
    # Add users that meet the criteria (based on rank thresholds) to a temporary list, then update the filtered leaderboard with these users.
    if rank_filter and rank_threshold or (rank_filter and (rank_threshold_low and rank_threshold_high)):  
        rank_filtered = []  
        if rank_filter == 'above': 
                    for user in filtered_leaderboard: 
                        print(user)
                        if user['rank'] < rank_threshold: 
                            rank_filtered.append(user) 

        elif rank_filter == 'below':  
                    for user in filtered_leaderboard:  
                        if user['rank'] > rank_threshold:  
                            rank_filtered.append(user)  
        elif rank_filter == 'between' and (rank_threshold_low and rank_threshold_high):  
            for user in filtered_leaderboard: 
                if rank_threshold_low <= user['rank'] <= rank_threshold_high:  
                    rank_filtered.append(user) 
        filtered_leaderboard = rank_filtered 

    return filtered_leaderboard 
