#makes it run as if it was in the root directory
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import calculate_user_submissions_data function we are testing
from services.user_submissions.user_submissions_processor import calculate_user_submissions_data

#import functions needed to setup test enviroment and test our function 

from services.json_file_handler import read_scores_json_file

# Setting up the testing environment
# In this section, we replicate the setup similar to what we use in the user submissions endpoint.
# Hence we read the scores data from the scores.json file using the read_scores_json_file function

scores = read_scores_json_file() 
def test_filter_qualified_user_submissions_data_by_date_in_asc_order():
    """Test case for filtering qualified user submissions data by date in ascending order.
    
       This test simulates filtering the submission data for a specific user 
       where the user submissions are sorted by date in ascending order and only 'qualified' 
       (best 24 and must have a minimum of 3 submissions)
       submissions are included.
    """

    # Dummy data to replicate those that would be retrieved from the params recieved on the usersubmissions endpoint

    name = "Kathleen Gray"  # We are looking for the user submissions by "Kathleen Gray"
    sort = "date"  # Submissions should be sorted by the 'date' field
    order = "asc"  # We are ordering the submissions in ascending order (oldest to newest)
    qualifiedorall = "qualified"  # Only include submissions (that are qualified or best 24)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by date in ascending order and only qualified submissions
    expected_user_submissions_data = [{'name': 'Hic porro ratione voluptates ipsa.', 'date': '26/08/2002', 'score': 97}, 
                                      {'name': 'Modi occaecati odit.', 'date': '18/10/2004', 'score': 95}, 
                                      {'name': 'Iure optio dicta error rem.', 'date': '27/02/2012', 'score': 113}]

    # Assert that the filtered and sorted submission data matches the expected data
    assert user_submissions_data == expected_user_submissions_data

def test_filter_qualified_user_submissions_data_by_date_in_desc_order():
    """Test case for filtering qualified user submissions data by date in descending order.
    
       This test simulates filtering the submission data for a specific user 
       where the user submissions are sorted by date in descending order and only 'qualified' 
       submissions are included (best 24 and must have a minimum of 3 submissions).
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Kathleen Gray"  # We are filtering for the user submissions by "Kathleen Gray"
    sort = "date"  # Submissions should be sorted by the 'date' field
    order = "desc"  # We are ordering the submissions in descending order (newest to oldest)
    qualifiedorall = "qualified"  # Only include submissions that are 'qualified' (best 24)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by date in descending order and only qualified submissions
    expected_user_submissions_data = [
        {'name': 'Iure optio dicta error rem.', 'date': '27/02/2012', 'score': 113},
        {'name': 'Modi occaecati odit.', 'date': '18/10/2004', 'score': 95}, 
        {'name': 'Hic porro ratione voluptates ipsa.', 'date': '26/08/2002', 'score': 97}
    ]

    # Assert that the user_submissions_data from function we testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_qualified_user_submissions_data_by_score_in_asc_order():
    """Test case for filtering qualified user submissions data by score in ascending order.
    
       This test simulates filtering the submission data for a specific user, "Iain Blake",
       where the user submissions are sorted by score in ascending order and only 'qualified' 
       submissions are included (best 24 and must have a minimum of 3 submissions).
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Iain Blake"  # We are filtering for the user submissions by "Iain Blake"
    sort = "score"  # Submissions should be sorted by the 'score' field
    order = "asc"  # We are ordering the submissions in ascending order (lowest score to highest score)
    qualifiedorall = "qualified"  # Only include submissions that are 'qualified' (best 24)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by score in ascending order and only qualified submissions
    expected_user_submissions_data = [{'name': 'Excepturi soluta libero.', 'date': '22/04/2000', 'score': 64}, 
                                      {'name': 'Aperiam molestias ab.', 'date': '28/12/2018', 'score': 90}, 
                                      {'name': 'Corporis consectetur minus nisi quae.', 'date': '31/12/2013', 'score': 123}]

    # Assert that the user_submissions_data from function we testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_qualified_user_submissions_data_by_score_in_desc_order():
    """Test case for filtering qualified user submissions data by score in descending order.
    
       This test simulates filtering the submission data for a specific user, "Iain Blake",
       where the user submissions are sorted by score in descending order and only 'qualified' 
       submissions are included (best 24 and must have a minimum of 3 submissions).
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Iain Blake"  # We are filtering for the user submissions by "Iain Blake"
    sort = "score"  # Submissions should be sorted by the 'score' field
    order = "desc"  # We are ordering the submissions in descending order (highest score to lowest score)
    qualifiedorall = "qualified"  # Only include submissions that are 'qualified' (best 24)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by score in descending order and only qualified submissions
    expected_user_submissions_data = [{'name': 'Corporis consectetur minus nisi quae.', 'date': '31/12/2013', 'score': 123},
                                      {'name': 'Aperiam molestias ab.', 'date': '28/12/2018', 'score': 90}, 
                                      {'name': 'Excepturi soluta libero.', 'date': '22/04/2000', 'score': 64}]

    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_all_user_submissions_data_by_score_in_asc_order():
    """Test case for filtering all user submissions data by score in ascending order.
    
       This test simulates filtering the submission data for a specific user, "Iain Blake",
       where all user submissions are sorted by score in ascending order.
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Iain Blake"  # We are filtering for the user submissions by "Iain Blake"
    sort = "score"  # Submissions should be sorted by the 'score' field
    order = "asc"  # We are ordering the submissions in ascending order (lowest score to highest score)
    qualifiedorall = "all"  # Include all submissions (not just qualified)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by score in ascending order with all submissions
    expected_user_submissions_data = [{'name': 'Excepturi soluta libero.', 'date': '22/04/2000', 'score': 64}, 
                                      {'name': 'Aperiam molestias ab.', 'date': '28/12/2018', 'score': 90}, 
                                      {'name': 'Corporis consectetur minus nisi quae.', 'date': '31/12/2013', 'score': 123}]
    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_all_user_submissions_data_by_score_in_desc_order():
    """Test case for filtering all user submissions data by score in descending order.
    
       This test simulates filtering the submission data for a specific user, "Iain Blake",
       where all user submissions are sorted by score in descending order.
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Iain Blake"  # We are filtering for the user submissions by "Iain Blake"
    sort = "score"  # Submissions should be sorted by the 'score' field
    order = "desc"  # We are ordering the submissions in descending order (highest score to lowest score)
    qualifiedorall = "all"  # Include all submissions (not just qualified)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by score in descending order with all submissions
    expected_user_submissions_data = [{'name': 'Corporis consectetur minus nisi quae.', 'date': '31/12/2013', 'score': 123}, 
                                      {'name': 'Aperiam molestias ab.', 'date': '28/12/2018', 'score': 90}, 
                                      {'name': 'Excepturi soluta libero.', 'date': '22/04/2000', 'score': 64}]

    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_all_user_submissions_data_by_date_in_asc_order():
    """Test case for filtering all user submissions data by date in ascending order.
    
       This test simulates filtering the submission data for a specific user, "Nicola Thompson",
       where all user submissions are sorted by date in ascending order.
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Nicola Thompson"  # We are filtering for the user submissions by "Nicola Thompson"
    sort = "date"  # Submissions should be sorted by the 'date' field
    order = "asc"  # We are ordering the submissions in ascending order (oldest to newest)
    qualifiedorall = "all"  # Include all submissions (not just qualified)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by date in ascending order with all submissions
    expected_user_submissions_data = [{'name': 'Dignissimos esse assumenda itaque exercitationem.', 'date': '05/04/2005', 'score': 92}, 
                                      {'name': 'Dolorum maxime corporis totam.', 'date': '12/02/2009', 'score': 76}, 
                                      {'name': 'Sunt officia aspernatur rem sit.', 'date': '06/08/2013', 'score': 133}]

    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_all_user_submissions_data_by_date_in_desc_order():
    """Test case for filtering all user submissions data by date in descending order.
    
       This test simulates filtering the submission data for a specific user, "Nicola Thompson",
       where all user submissions are sorted by date in descending order.
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Nicola Thompson"  # We are filtering for the user submissions by "Nicola Thompson"
    sort = "date"  # Submissions should be sorted by the 'date' field
    order = "desc"  # We are ordering the submissions in descending order (newest to oldest)
    qualifiedorall = "all"  # Include all submissions (not just qualified)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result after filtering: sorted by date in descending order with all submissions
    expected_user_submissions_data = [{'name': 'Sunt officia aspernatur rem sit.', 'date': '06/08/2013', 'score': 133}, 
                                      {'name': 'Dolorum maxime corporis totam.', 'date': '12/02/2009', 'score': 76}, 
                                      {'name': 'Dignissimos esse assumenda itaque exercitationem.', 'date': '05/04/2005', 'score': 92}]

    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_qualified_submissions_for_non_qualified_user():
    """Test case for filtering qualified submissions for a user who has submitted less than 3 rankings.
    
       This test simulates filtering the submission data for Hilary Carr who has fewer than 3 submissions.
       Since the user does not meet the qualification criteria (at least 3 submissions required), the 
       string "Not qualified" should be returned when we call the function we testing
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Hilary Carr"  # We are filtering for the user submissions by "Alex Johnson" (less than 3 submissions)
    sort = "score"  
    order = "asc"  
    qualifiedorall = "qualified"  # Only include submissions that are 'qualified' (but user doesn't meet qualifications)

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result is the string "Not qualified" because the user does not qualify with fewer than 3 submissions
    expected_user_submissions_data = "Not qualified"

    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data

def test_filter_submissions_for_non_existent_user():
    """Test case for filtering submissions for a non-existent user.
    
       This test simulates filtering the submission data for a user whose name does not exist in the dataset.
    """

    # Dummy data to replicate those that would be retrieved from the params received on the usersubmissions endpoint

    name = "Daniel Rice"  # We are filtering for the user submissions by a name that doesn't exist
    sort = "score"  
    order = "asc"  
    qualifiedorall = "all"  

    # This is where the function we are testing is called with the dummy data
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    # The expected result is the string "User not found" because the user does not exist 
    expected_user_submissions_data = "User not found"

    # Assert that the user_submissions_data from the function we are testing matches what is expected
    assert user_submissions_data == expected_user_submissions_data