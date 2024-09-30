#makes it run as if it was in the root directory
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# imports function we are testing
from services.leaderboard.leaderboard_processor import calculate_leaderboard_data

def test_calculate_leaderboard_data():
    # This test is to check if the function calculate_leaderboard_data is working as expected
    # and that we are getting the correct leaderboard data back

    #in the first test i am going test some fake data to check the function is working as expected

    # scores is a list of dictionaries, where each dictionary represents a user and their submissions.
    # this is the dummy data that we are going to use to test the function calculate_leaderboard_data
    # for our first test case
    scores = [
    {
        "name": "Elon Musk",
        "submissions": [
            {
                "name": "Submission 1",
                "date": "15/05/2015",
                "score": 85
            },
            {
                "name": "Submission 2",
                "date": "23/08/2017",
                "score": 42
            },
            {
                "name": "Submission 3",
                "date": "04/11/2020",
                "score": 77
            },
            {
                "name": "Submission 4",
                "date": "10/02/2021",
                "score": 94
            },
            {
                "name": "Submission 5",
                "date": "18/07/2022",
                "score": 61
            }
        ]
    },
    {
        "name": "Steve Jobs",
        "submissions": [
            {
                "name": "Submission 1",
                "date": "14/03/2005",
                "score": 93
            },
            {
                "name": "Submission 2",
                "date": "22/12/2010",
                "score": 58
            },
            {
                "name": "Submission 3",
                "date": "09/09/2013",
                "score": 72
            },
            {
                "name": "Submission 4",
                "date": "30/06/2015",
                "score": 88
            },
            {
                "name": "Submission 5",
                "date": "19/11/2018",
                "score": 65
            },
            {
                "name": "Submission 6",
                "date": "01/04/2020",
                "score": 47
            },
            {
                "name": "Submission 7",
                "date": "17/10/2021",
                "score": 80
            }
        ]
    }
    ]

    # this is where the function we are testing is called with dummy data
    leaderboard_data = calculate_leaderboard_data(scores)

    # this is the expected leaderboard data that we are expecting to get back
    expected_leaderboard_data = [
        {'rank': 1, 'name': 'Steve Jobs', 'overall score': 503},
        {'rank': 2, 'name': 'Elon Musk', 'overall score': 359}
    ]

    # this is where we are checking if the function is returning the expected leaderboard data
    assert leaderboard_data == expected_leaderboard_data

    # Dummy data for the second test case
    scores = [
        {
            "name": "Bill Gates",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "12/06/2010",
                    "score": 95
                },
                {
                    "name": "Submission 2",
                    "date": "22/08/2012",
                    "score": 87
                },
                {
                    "name": "Submission 3",
                    "date": "05/11/2015",
                    "score": 64
                },
                {
                    "name": "Submission 4",
                    "date": "15/01/2018",
                    "score": 73
                },
                {
                    "name": "Submission 5",
                    "date": "02/09/2021",
                    "score": 90
                }
            ]
        },
        {
            "name": "Sundar Pichai",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "03/03/2011",
                    "score": 88
                },
                {
                    "name": "Submission 2",
                    "date": "12/06/2013",
                    "score": 60
                },
                {
                    "name": "Submission 3",
                    "date": "17/08/2015",
                    "score": 79
                },
                {
                    "name": "Submission 4",
                    "date": "20/10/2019",
                    "score": 94
                },
                {
                    "name": "Submission 5",
                    "date": "23/04/2022",
                    "score": 68
                }
            ]
        },
        {
            "name": "Larry Page",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "09/09/2009",
                    "score": 72
                },
                {
                    "name": "Submission 2",
                    "date": "11/07/2014",
                    "score": 55
                },
                {
                    "name": "Submission 3",
                    "date": "22/12/2017",
                    "score": 80
                },
                {
                    "name": "Submission 4",
                    "date": "05/06/2020",
                    "score": 69
                }
            ]
        }
    ]

    # Function call for the second test case
    leaderboard_data = calculate_leaderboard_data(scores)

    # Expected leaderboard data for the second test case
    expected_leaderboard_data = [
        {'rank': 1, 'name': 'Bill Gates', 'overall score': 409},
        {'rank': 2, 'name': 'Sundar Pichai', 'overall score': 389},
        {'rank': 3, 'name': 'Larry Page', 'overall score': 276}
    ]

    # this is where we are checking if the function is returning the expected leaderboard data
    assert leaderboard_data == expected_leaderboard_data

    # Dummy data for the third test case
    scores = [
        {
            "name": "Mark Zuckerberg",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "05/05/2009",
                    "score": 82
                },
                {
                    "name": "Submission 2",
                    "date": "07/11/2012",
                    "score": 67
                },
                {
                    "name": "Submission 3",
                    "date": "14/09/2016",
                    "score": 90
                },
                {
                    "name": "Submission 4",
                    "date": "21/08/2020",
                    "score": 78
                }
            ]
        },
        {
            "name": "Tim Cook",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "10/12/2010",
                    "score": 79
                },
                {
                    "name": "Submission 2",
                    "date": "19/03/2013",
                    "score": 85
                },
                {
                    "name": "Submission 3",
                    "date": "25/06/2015",
                    "score": 70
                }
            ]
        },
        {
            "name": "Jeff Bezos",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "15/08/2005",
                    "score": 88
                },
                {
                    "name": "Submission 2",
                    "date": "24/02/2009",
                    "score": 92
                },
                {
                    "name": "Submission 3",
                    "date": "18/07/2013",
                    "score": 65
                },
                {
                    "name": "Submission 4",
                    "date": "03/11/2016",
                    "score": 80
                },
                {
                    "name": "Submission 5",
                    "date": "30/12/2020",
                    "score": 77
                }
            ]
        },
        {
            "name": "Satya Nadella",
            "submissions": [
                {
                    "name": "Submission 1",
                    "date": "20/01/2014",
                    "score": 91
                },
                {
                    "name": "Submission 2",
                    "date": "14/04/2017",
                    "score": 79
                },
                {
                    "name": "Submission 3",
                    "date": "12/11/2020",
                    "score": 86
                }
            ]
        }
    ]

    # Function call for the third test case
    leaderboard_data = calculate_leaderboard_data(scores)

    # Expected leaderboard data for the third test case
    expected_leaderboard_data = [
        {'rank': 1, 'name': 'Jeff Bezos', 'overall score': 402},
        {'rank': 2, 'name': 'Mark Zuckerberg', 'overall score': 317},
        {'rank': 3, 'name': 'Satya Nadella', 'overall score': 256},
        {'rank': 4, 'name': 'Tim Cook', 'overall score': 234}
    ]

    # this is where we are checking if the function is returning the expected leaderboard data
    assert leaderboard_data == expected_leaderboard_data