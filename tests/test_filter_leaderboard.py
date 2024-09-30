#makes it run as if it was in the root directory
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import filter_leaderboard function we are testing
from services.leaderboard.leaderboard_filtering import filter_leaderboard

#import functions needed to setup test enviroment and test our function 

from services.json_file_handler import read_scores_json_file
from services.leaderboard.leaderboard_processor import calculate_leaderboard_data

# Setting up the testing environment
# In this section, we replicate the setup similar to what we use in the result endpoint.
# First, we read the raw scores data from the scores.json file using the read_scores_json_file function
# Then, we calculate the leaderboard data from the scores (using the calculate_leaderboard_data function)
# where the data is processed to generate the leaderboard, including name, overall scores, ranks
# This prepares the necessary data structure to be used in the subsequent test cases
# for what we testing today

scores = read_scores_json_file()

leaderboard_data = calculate_leaderboard_data(scores)

def test_search_leaderboard_for_name():
    # Test Case 1: Searching for a specific name "Shirley Russell"
    # No score or rank filters are applied, meaning we are only looking for this specific user by name.
    # We expect to get back data for "Shirley Russell" with their rank and overall score.

    # this is dummy params data to replicate those that would be recieved on the results endpoint
    params = {
        'name': "Shirley Russell",  # We're filtering by the name "Shirley Russell"
        'score_filter': "above",  # The score filter is set to "above" by default but no score_filter search is happening as can only search/filter either by name alone or rank and score and no threshold is provided 
        'score_threshold': None,           
        'score_threshold_low': None,  
        'score_threshold_high': None,
        'rank_filter': "above", # The rank filter is set to "above" by default but no rank_filter search is happening as can only search/filter either by name alone or rank and score and no threshold is provided 
        'rank_threshold': None, 
        'rank_threshold_low': None, 
        'rank_threshold_high': None,
    }

    # We expect the filtered leaderboard data to contain one entry for "Shirley Russell"
    # with a rank of 4 and an overall score of 4005.
    expected_filtered_leaderboard_data = [{'rank': 4, 'name': 'Shirley Russell', 'overall score': 4005}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected data
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

    # Test Case 2: Searching for a specific name "Douglas Hamilton"
    # No score or rank filters are applied, meaning we are only looking for this specific user by name.
    # We expect to get back data for "Douglas Hamilton" with their rank and overall score.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': "Douglas Hamilton",  # We're filtering by the name "Douglas Hamilton"
        'score_filter': "above",  # The score filter is set to "above" by default but no score_filter search is happening as can only search/filter either by name alone or rank and score and no threshold is provided
        'score_threshold': None,           
        'score_threshold_low': None,  
        'score_threshold_high': None,
        'rank_filter': "above",  # The rank filter is set to "above" by default but no rank_filter search is happening as can only search/filter either by name alone or rank and score and no threshold is provided
        'rank_threshold': None, 
        'rank_threshold_low': None, 
        'rank_threshold_high': None,
    }

    # We expect the filtered leaderboard data to contain one entry for "Douglas Hamilton"
    # with a rank of 242 and an overall score of 216.
    expected_filtered_leaderboard_data = [{'rank': 242, 'name': 'Douglas Hamilton', 'overall score': 216}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected data
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_score_above():

    # Test Case: Filtering leaderboard by score above 4000
    # In this test case, we are applying a filter to find users with an overall score above 4000
    # No name or rank filters are applied; we are only filtering based on score.
    # We expect to get back users who have an overall score higher than 4000

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above",  # We are using the "above" filter to find users with scores above the threshold.
        'score_threshold': 4000,  # The threshold is set to 4000, so we are looking for users with a score higher than this.
        'score_threshold_low': None,  
        'score_threshold_high': None,  # Not used in this case, as we are not doing a "between" filter.
        'rank_filter': "above",  # is set to "above" filter by default but as is no acompaniying rank_threshold, it is not being used
        'rank_threshold': None,  
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return the leaderboard data with only users with overall scores greater than 4000.
   
    # In this example, we expect four users: Damian Kirby-Russell, Toby Hargreaves, Jonathan Elliott-Potter
    # and Shirley Russell with scores above the threshold.
    expected_filtered_leaderboard_data = [{'rank': 1, 'name': 'Damian Kirby-Russell', 'overall score': 4025}, 
                                          {'rank': 2, 'name': 'Toby Hargreaves', 'overall score': 4025}, 
                                          {'rank': 3, 'name': 'Jonathan Elliott-Potter', 'overall score': 4014}, 
                                          {'rank': 4, 'name': 'Shirley Russell', 'overall score': 4005}]

    # Call the filter_leaderboard function with the generated leaderboard and with serach parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users whose scores are above the threshold
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_score_below():
    # Test Case: Filtering leaderboard by score below 150
    # In this test case, we are applying a filter to find users with an overall score below 150.
    # No name or rank filters are applied; we are only filtering based on score.
    # We expect to get back users who have an overall score lower than 150.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "below",  # We are using the "below" filter to find users with scores below the threshold.
        'score_threshold': 150,  # The threshold is set to 150, so we are looking for users with a score lower than this.
        'score_threshold_low': None,  
        'score_threshold_high': None,  # Not used in this case, as we are not doing a "between" filter.
        'rank_filter': "above",  # is set to "above" filter option by default but as there is no accompanying rank_threshold, it is not being used
        'rank_threshold': None,  
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return the leaderboard data with only users with overall scores lower than 150.
   
    # In this example, we expect two users: Bruce Johnson, Paula Skinner-Hunter and Bryan Palmer with scores below the threshold.
    expected_filtered_leaderboard_data = [{'rank': 244, 'name': 'Bruce Johnson', 'overall score': 130}, 
                                          {'rank': 245, 'name': 'Paula Skinner-Hunter', 'overall score': 123}, 
                                          {'rank': 246, 'name': 'Bryan Palmer', 'overall score': 73}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users whose scores are below the threshold
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_below():
    # Test Case : Filtering leaderboard by rank below 240
    # In this test case, we are applying a filter to find users with a rank below 240.
    # No name or score filters are applied; we are only filtering based on rank.
    # We expect to get back users who have a rank lower than 240.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above",  # is set to "above" filter by default but as is no acompaniying score_threshold, it is not being used
        'score_threshold': None,  
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "below",  # We are using the "below" filter to find users with ranks below the threshold.
        'rank_threshold': 240,  # The threshold is set to 240, so we are looking for users with ranks lower than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return the leaderboard data with only users with ranks lower than 240.
   
    # In this example, we expect six users with ranks below 240 as seen below.
    expected_filtered_leaderboard_data = [{'rank': 241, 'name': 'Mr Ben Davison', 'overall score': 253}, 
                                          {'rank': 242, 'name': 'Douglas Hamilton', 'overall score': 216}, 
                                          {'rank': 243, 'name': 'Julia Stephenson', 'overall score': 172}, 
                                          {'rank': 244, 'name': 'Bruce Johnson', 'overall score': 130}, 
                                          {'rank': 245, 'name': 'Paula Skinner-Hunter', 'overall score': 123},
                                          {'rank': 246, 'name': 'Bryan Palmer', 'overall score': 73}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users whose ranks are below the threshold
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_above():
    # Test Case: Filtering leaderboard by rank above 10
    # In this test case, we are applying a filter to find users with a rank above 10.
    # No name or score filters are applied; we are only filtering based on rank.
    # We expect to get back users who have a rank higher than 10.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above", # is set to "above" filter by default but as is no acompaniying score_threshold, it is not being used  
        'score_threshold': None,  
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "above",  # We are using the "above" filter to find users with ranks above the threshold.
        'rank_threshold': 10,  # The threshold is set to 10, so we are looking for users with ranks higher than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return the leaderboard data with only users with ranks higher than 10.
   
    # In this example, we expect 9 users as you can see below
    expected_filtered_leaderboard_data = [{'rank': 1, 'name': 'Damian Kirby-Russell', 'overall score': 4025},
                                          {'rank': 2, 'name': 'Toby Hargreaves', 'overall score': 4025},
                                          {'rank': 3, 'name': 'Jonathan Elliott-Potter', 'overall score': 4014},
                                          {'rank': 4, 'name': 'Shirley Russell', 'overall score': 4005},
                                          {'rank': 5, 'name': 'Jason Russell', 'overall score': 3894},
                                          {'rank': 6, 'name': 'Ms Irene Hanson', 'overall score': 3884},
                                          {'rank': 7, 'name': 'Anthony Turner', 'overall score': 3868},
                                          {'rank': 8, 'name': 'Martin Kaur', 'overall score': 3667}, 
                                          {'rank': 9, 'name': 'Dr Fiona Fleming', 'overall score': 3628}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users whose ranks are above the threshold
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_above_and_score_below():

    # Test Case: Filtering leaderboard by rank above 10 and score below 4000
    # In this test case, we are applying two filters: 
    # 1. Rank above 10: We want to find users who have ranks higher than 10.
    # 2. Score below 4000: We also want to filter users with scores lower than 4000.
    # We expect to get back users who meet both conditions: ranks higher than 10 and scores lower than 4000.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "below",  # We are using the "below" filter to find users with scores lower than 4000.
        'score_threshold': 4000,  # The threshold is set to 4000, so we are looking for users with a score lower than this.
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "above",  # We are using the "above" filter to find users with ranks higher than 10.
        'rank_threshold': 10,  # The threshold is set to 10, so we are looking for users with ranks higher than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None, 
    }

    # We expect the filtered leaderboard data to return users who have ranks higher than 10 and scores lower than 4000.
   
    # In this example, we expect five users as you can see below 
    expected_filtered_leaderboard_data = [{'rank': 5, 'name': 'Jason Russell', 'overall score': 3894}, 
                                          {'rank': 6, 'name': 'Ms Irene Hanson', 'overall score': 3884}, 
                                          {'rank': 7, 'name': 'Anthony Turner', 'overall score': 3868}, 
                                          {'rank': 8, 'name': 'Martin Kaur', 'overall score': 3667}, 
                                          {'rank': 9, 'name': 'Dr Fiona Fleming', 'overall score': 3628}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks above 10 and scores below 4000
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_score_above_and_rank_above():
    # Test Case: Filtering leaderboard by score above 4000 and rank above 10
    # In this test case, we are applying two filters: 
    # 1. Score above 4000: We want to find users who have scores higher than 4000.
    # 2. Rank above 10: We also want to filter users with ranks higher than 10.
    # We expect to get back users who meet both conditions: scores higher than 4000 and ranks higher than 10.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above",  # We are using the "above" filter to find users with scores higher than 4000.
        'score_threshold': 4000,  # The threshold is set to 4000, so we are looking for users with a score higher than this.
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "above",  # We are using the "above" filter to find users with ranks higher than 10.
        'rank_threshold': 10,  # The threshold is set to 10, so we are looking for users with ranks higher than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None, 
    }

    # We expect the filtered leaderboard data to return users who have scores higher than 4000 and ranks higher than 10.
   
    # In this example we expect 4 user's with ranks above and score higher than 4000
    expected_filtered_leaderboard_data = [{'rank': 1, 'name': 'Damian Kirby-Russell', 'overall score': 4025}, 
                                          {'rank': 2, 'name': 'Toby Hargreaves', 'overall score': 4025}, 
                                          {'rank': 3, 'name': 'Jonathan Elliott-Potter', 'overall score': 4014}, 
                                          {'rank': 4, 'name': 'Shirley Russell', 'overall score': 4005}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: scores above 4000 and ranks above 10
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_below_and_score_below():

    # Test Case 1: Filtering leaderboard by rank below 240 and score below 300
    # In this test case, we are applying two filters: 
    # 1. Rank below 240: We want to find users who have ranks lower than 240.
    # 2. Score below 300: We also want to filter users with scores lower than 300.
    # We expect to get back users who meet both conditions: ranks lower than 240 and scores lower than 300.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "below",  # We are using the "below" filter to find users with scores lower than 300.
        'score_threshold': 300,  # The threshold is set to 300, so we are looking for users with a score lower than this.
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "below",  # We are using the "below" filter to find users with ranks lower than 240.
        'rank_threshold': 240,  # The threshold is set to 240, so we are looking for users with ranks lower than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return users who have ranks lower than 240 and scores lower than 300.
   
    # In this example, we expect six users with ranks lower than 240 and scores lower than 300
    expected_filtered_leaderboard_data = [{'rank': 241, 'name': 'Mr Ben Davison', 'overall score': 253}, 
                                          {'rank': 242, 'name': 'Douglas Hamilton', 'overall score': 216}, 
                                          {'rank': 243, 'name': 'Julia Stephenson', 'overall score': 172}, 
                                          {'rank': 244, 'name': 'Bruce Johnson', 'overall score': 130}, 
                                          {'rank': 245, 'name': 'Paula Skinner-Hunter', 'overall score': 123}, 
                                          {'rank': 246, 'name': 'Bryan Palmer', 'overall score': 73}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks below 240 and scores below 300
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_below_and_score_above():

    # Test Case: Filtering leaderboard by rank below 230 and score above 2000
    # In this test case, we are applying two filters: 
    # 1. Rank below 230: We want to find users who have ranks lower than 230.
    # 2. Score above 2000: We also want to filter users with scores higher than 2000.
    # We expect to get back users who meet both conditions: ranks lower than 230 and scores higher than 2000.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above",  # We are using the "above" filter to find users with scores higher than 2000.
        'score_threshold': 2000,  # The threshold is set to 2000, so we are looking for users with a score higher than this.
        'score_threshold_low': None,  
        'score_threshold_high': None, 
        'rank_filter': "below",  # We are using the "below" filter to find users with ranks lower than 230.
        'rank_threshold': 230,  # The threshold is set to 230, so we are looking for users with ranks lower than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None, 
    }

    # We expect the filtered leaderboard data to return users who have ranks lower than 230 and scores higher than 2000.
   
    # In this example, as there an scores above 2000 with ranks under 230 we expect to get nothing back 
    expected_filtered_leaderboard_data = []

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks below 230 and scores above 2000
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_between():

    # Test Case: Filtering leaderboard by rank between 20 and 25
    # In this test case, we are applying a filter to find users with ranks between 20 and 25.
    # No name or score filters are applied; we are only filtering based on rank.
    # We expect to get back users who have ranks within this range.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above",  # is set to "above" by default but as no score_threshold then is not used 
        'score_threshold': None,  
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "between",  # We are using the "between" filter to find users with ranks between the thresholds.
        'rank_threshold': None,  # Not used since we are using a "between" filter.
        'rank_threshold_low': 20,  # The lower bound for rank_threshold is set to 20.
        'rank_threshold_high': 25,  # The upper bound for rank_threshold is set to 25.
    }

    # We expect the filtered leaderboard data to return users who have ranks between 20 and 25.

    # In this example, we expect five users as you can see below 
    expected_filtered_leaderboard_data = [{'rank': 20, 'name': 'Alexandra Smith', 'overall score': 3411},
                                          {'rank': 21, 'name': 'Tracey Johnson', 'overall score': 3381}, 
                                          {'rank': 22, 'name': 'Stewart Franklin', 'overall score': 3375}, 
                                          {'rank': 23, 'name': 'Gary Smith-Davies', 'overall score': 3355}, 
                                          {'rank': 24, 'name': 'Raymond Shaw', 'overall score': 3335}, 
                                          {'rank': 25, 'name': 'Shaun Jackson', 'overall score': 3296}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users whose ranks are between 20 and 25
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_between_and_score_above():

    # Test Case: Filtering leaderboard by rank between 35 and 50 and score above 3000
    # In this test case, we are applying two filters: 
    # 1. Rank between 35 and 50: We want to find users who have ranks within this range.
    # 2. Score above 3000: We also want to filter users with scores higher than 3000.
    # We expect to get back users who meet both conditions: ranks between 35 and 50, and scores higher than 3000.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "above",  # We are using the "above" filter to find users with scores higher than 3000.
        'score_threshold': 3000,  # The threshold is set to 3000, so we are looking for users with a score higher than this.
        'score_threshold_low': None,  
        'score_threshold_high': None, 
        'rank_filter': "between",  # We are using the "between" filter to find users with ranks between 35 and 50.
        'rank_threshold': None,  
        'rank_threshold_low': 35,  # The lower bound for rank is set to 35.
        'rank_threshold_high': 50,  # The upper bound for rank is set to 50.
    }

    # We expect the filtered leaderboard data to return users who have ranks between 35 and 50 and scores higher than 3000.
   
    # In this example, we expect four users as you can see below 
    expected_filtered_leaderboard_data = [{'rank': 35, 'name': 'Dr Frances Gregory', 'overall score': 3109}, 
                                          {'rank': 36, 'name': 'Stephen Williams', 'overall score': 3066}, 
                                          {'rank': 37, 'name': 'Marcus Price', 'overall score': 3055}, 
                                          {'rank': 38, 'name': 'Dr Iain Davis', 'overall score': 3022}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks between 35 and 50, and scores above 3000
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_between_and_score_below():

    # Test Case: Filtering leaderboard by rank between 100 and 120 and score below 1100
    # In this test case, we are applying two filters: 
    # 1. Rank between 100 and 120: We want to find users who have ranks within this range.
    # 2. Score below 1100: We also want to filter users with scores lower than 1100.
    # We expect to get back users who meet both conditions: ranks between 100 and 120, and scores lower than 1100.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "below",  # We are using the "below" filter to find users with scores lower than 1100.
        'score_threshold': 1100,  # The threshold is set to 1100, so we are looking for users with a score lower than this.
        'score_threshold_low': None,  
        'score_threshold_high': None,  
        'rank_filter': "between",  # We are using the "between" filter to find users with ranks between 100 and 120.
        'rank_threshold': None, 
        'rank_threshold_low': 100,  # The lower bound for rank is set to 100.
        'rank_threshold_high': 120,  # The upper bound for rank is set to 120.
    }

    # We expect the filtered leaderboard data to return users who have ranks between 100 and 120 and scores lower than 1100.
   
    # In this example, we expect five users with ranks between 100 and 120 and scores below 1100.
    expected_filtered_leaderboard_data = [{'rank': 116, 'name': 'Mr Terry Moore', 'overall score': 1095}, 
                                          {'rank': 117, 'name': 'Frederick Harper-Mitchell', 'overall score': 1067}, 
                                          {'rank': 118, 'name': 'Mr Jeremy Khan', 'overall score': 1050},
                                          {'rank': 119, 'name': 'Robin Lewis', 'overall score': 985}, 
                                          {'rank': 120, 'name': 'Mitchell Graham-Hughes', 'overall score': 977}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks between 100 and 120, and scores below 1100
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_rank_between_and_score_between():

    # Test Case: Filtering leaderboard by rank between 100 and 150 and score between 650 and 670
    # In this test case, we are applying two filters: 
    # 1. Rank between 100 and 150: We want to find users who have ranks within this range.
    # 2. Score between 650 and 670: We also want to filter users with scores within this range.
    # We expect to get back users who meet both conditions: ranks between 100 and 150, and scores between 650 and 670.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "between",  # We are using the "between" filter to find users with scores between 650 and 670.
        'score_threshold': None,  #
        'score_threshold_low': 650,  # The lower bound for score is set to 650.
        'score_threshold_high': 670,  # The upper bound for score is set to 670.
        'rank_filter': "between",  # We are using the "between" filter to find users with ranks between 100 and 150.
        'rank_threshold': None,  
        'rank_threshold_low': 100,  # The lower bound for rank is set to 100.
        'rank_threshold_high': 150,  # The upper bound for rank is set to 150.
    }

    # We expect the filtered leaderboard data to return users who have ranks between 100 and 150 and scores between 650 and 670.
   
    # In this example, we expect one user: Mr Roy Morgan with ranks between 100 and 150 and scores between 650 and 670.
    expected_filtered_leaderboard_data = [{'rank': 150, 'name': 'Mr Roy Morgan', 'overall score': 668}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks between 100 and 150, and scores between 650 and 670
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_score_between_and_rank_above():

    # Test Case: Filtering leaderboard by score between 1400 and 1600 and rank above 100
    # In this test case, we are applying two filters: 
    # 1. Score between 1400 and 1600: We want to find users who have scores within this range.
    # 2. Rank above 100: We also want to filter users with ranks higher than 100.
    # We expect to get back users who meet both conditions: scores between 1400 and 1600, and ranks above 100.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "between",  # We are using the "between" filter to find users with scores between 1400 and 1600.
        'score_threshold': None,  
        'score_threshold_low': 1400,  # The lower bound for score is set to 1400.
        'score_threshold_high': 1600,  # The upper bound for score is set to 1600.
        'rank_filter': "above",  # We are using the "above" filter to find users with ranks higher than 100.
        'rank_threshold': 100,  # The threshold is set to 100, so we are looking for users with ranks higher than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return users who have ranks above 100 and scores between 1400 and 1600.
   
    # In this example, we expect five users with rank above 100 and a score between 1400 and 1600.
    expected_filtered_leaderboard_data = [{'rank': 95, 'name': 'Dr Barbara Roberts', 'overall score': 1597}, 
                                          {'rank': 96, 'name': 'Abdul Cook', 'overall score': 1580}, 
                                          {'rank': 97, 'name': 'Bryan Jones', 'overall score': 1579}, 
                                          {'rank': 98, 'name': 'Roger Phillips', 'overall score': 1541}, 
                                          {'rank': 99, 'name': 'Miss Victoria Duffy', 'overall score': 1514}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks above 100 and scores between 1400 and 1600
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data

def test_filter_leaderboard_by_score_between_and_rank_below():

    # Test Case: Filtering leaderboard by score between 3000 and 3300 and rank below 36
    # In this test case, we are applying two filters: 
    # 1. Score between 3000 and 3300: We want to find users who have scores within this range.
    # 2. Rank below 36: We also want to filter users with ranks lower than 36.
    # We expect to get back users who meet both conditions: scores between 3000 and 3300, and ranks lower than 36.

    # this is dummy params data to replicate those that would be received on the results endpoint
    params = {
        'name': None,  
        'score_filter': "between",  # We are using the "between" filter to find users with scores between 3000 and 3300.
        'score_threshold': None,  
        'score_threshold_low': 3000,  # The lower bound for score is set to 3000.
        'score_threshold_high': 3300,  # The upper bound for score is set to 3300.
        'rank_filter': "below",  # We are using the "below" filter to find users with ranks lower than 36.
        'rank_threshold': 36,  # The threshold is set to 36, so we are looking for users with ranks lower than this.
        'rank_threshold_low': None,  
        'rank_threshold_high': None,  
    }

    # We expect the filtered leaderboard data to return users who have ranks lower than 36 and scores between 3000 and 3300.
   
    # In this example, we expect two user's: Marcus Price and Dr Iain Davis with a rank below 36 and a score between 3000 and 3300.
    expected_filtered_leaderboard_data = [{'rank': 37, 'name': 'Marcus Price', 'overall score': 3055}, 
                                          {'rank': 38, 'name': 'Dr Iain Davis', 'overall score': 3022}]

    # Call the filter_leaderboard function with the generated leaderboard and search parameters
    # this function is what we are testing
    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params)

    # Assert that the function correctly returns the expected users who meet both conditions: ranks below 36 and scores between 3000 and 3300
    assert filtered_leaderboard_data == expected_filtered_leaderboard_data



