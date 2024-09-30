# takes the sort parameter, order parameter, and qualifiedorall parameter as input and returns a formatted message.
# which is used on the user submissions page to display the message to the user based on the search parameters
def generate_user_submissions_search_result_message(sort, order, qualifiedorall):
    message = ""    
    if qualifiedorall == "qualified":
        message += "Displaying only the user's top 24 submissions, with a minimum of 3 submissions required to qualify for ranking "
    elif qualifiedorall == "all":
        message += "Displaying all submissions "
    if sort:
        if order == "desc":
            message += "& sorting user submissions by " + sort + " in descending order."
        elif order == "asc":
            message += "& sorting user submissions by " + sort + " in ascending order."
    return message
