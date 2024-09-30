def generate_leaderboard_search_result_message(params):

    # Initialize message variable and extract filtering parameters (name, score, and rank filters) from 'params'.
    message = ""
    name = params.get('name')
    score_filter = params.get('score_filter')
    score_threshold = params.get('score_threshold')
    score_threshold_low = params.get('score_threshold_low')
    score_threshold_high = params.get('score_threshold_high')
    rank_filter = params.get('rank_filter')
    rank_threshold = params.get('rank_threshold')
    rank_threshold_low = params.get('rank_threshold_low')
    rank_threshold_high = params.get('rank_threshold_high')

    # if there is a name parameter, add it to the message about displaying results for a specific user.
    if name:
        message += "Displaying results for the user " + name

    # Message based on score filtering
    if score_filter and (score_threshold or (score_threshold_low and score_threshold_high)):
        if score_filter == "above":
            message += " Showing only scores higher than " + score_threshold + "."
        elif score_filter == "below":
            message += " Showing only scores lower than " + score_threshold + "."
        elif score_filter == "between":
            message += " Displaying scores between " + score_threshold_low + " and " + score_threshold_high + "."

    # Message based on rank filtering
    if rank_filter and (rank_threshold or (rank_threshold_low and rank_threshold_high)):
        if rank_filter == "above":
            message += " Showing ranks higher than " + rank_threshold + "."
        elif rank_filter == "below":
            message += " Showing ranks lower than " + rank_threshold + "."
        elif rank_filter == "between":
            message += " Displaying ranks between " + rank_threshold_low + " and " + rank_threshold_high + "."

    return message

