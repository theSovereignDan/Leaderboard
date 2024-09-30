from datetime import datetime
#calculates user submissions data based on the parameters passed to the function
def calculate_user_submissions_data(scores, name, sort, order, qualifiedorall):
    current_user = []

    # loops through the user's until it finds a user with the same name as the name parameter passed to the function
    # when it does it assigns the user to the current_user variable
    for user in scores:
        if user["name"] == name:
            current_user = user
            break
    
    # if the user of the name entered is not found, return a message indicating so which is then used also on the user submissions page
    # to know what to display on the user submissions page
    if "name" not in current_user:
        return 'User not found'


    # get the submissions for the current user
    submissions = current_user["submissions"]

    # initialize the sorted_submissions list with the current user's submissions full list
    sorted_submissions = submissions

    # checks if the user has filtered for qualified submissions and if so checks if the user has at least 3 submissions
    # because you need 3 submissions to qualify for leaderboard ranking
    # if it does not then then returns "Not qualified" which is then used also on the user submissions page
    # to know what to show on the user submissions page
    # if it does then it carries on sorts the submissions based by score from highest to lowest and slices the top 24 submissions
    if qualifiedorall == "qualified":
        number_of_submissions = len(submissions)
        if number_of_submissions < 3:
            return "Not qualified"
        sorted_submissions = sorted(sorted_submissions, key=lambda x: x['score'], reverse=True)[:24] 

    # checks if the user has filtered by date or score and if date was selected then checks the order filter
    # if the order filter is "desc" then it sorts the submissions by date in descending order (latest to earliest)
    # if the order filter is "asc" then it sorts the submissions by date in ascending order (earliest to latest)
    # if score was selected then checks the order filter
    # if the order filter is "desc" then it sorts the submissions by score in descending order (highest to lowest)
    # if the order filter is "asc" then it sorts the submissions by score in ascending order (lowest to highest)
    if sort == "date":
        if order == "desc":
            sorted_submissions = sorted(sorted_submissions, key=lambda x: datetime.strptime(x['date'], "%d/%m/%Y"), reverse=True)
        elif order == "asc":
            sorted_submissions = sorted(sorted_submissions, key=lambda x: datetime.strptime(x['date'], "%d/%m/%Y"))
    elif sort == "score":
        if order == "desc":
            sorted_submissions = sorted(sorted_submissions, key=lambda x: x['score'], reverse=True)
        elif order == "asc":
            sorted_submissions = sorted(sorted_submissions, key=lambda x: x['score'])

    return sorted_submissions
    


    