**ScoreQuest Guide**

**ScoreQuest** is a web-based application that provides a dynamic leaderboard system, where users can view scores, search specific users, and filter results based on several criteria. Additionally, users can search and filter for user's submissions.

* * * * *

**Key Features Overview**

**1\. Leaderboards**

ScoreQuest offers several views of user scores:

-   **All Scores**: Displays a list of all users ranked by their total scores.
-   **Top 20 Scores**: Shows the top 20 users with the highest scores.
-   **Worst 20 Scores**: Displays the bottom 20 users with the lowest scores.

**2\. Search & Filter Leaderboard**

Users can search and filter the leaderboard based on the following:

-   **Search by Name**: Search for users by entering their name in the search bar.
-   **Filter by Score**:

-   Filter users with scores above or below a certain threshold.
-   Filter users with scores between two thresholds.

-   **Filter by Ranking**:

-   Search for users ranked above or below a specific rank.
-   Filter users ranked between two rank positions.

**Dynamic Filtering**: As users type or select filters, irrelevant fields are hidden, making the interface cleaner and more intuitive.

**3\. View and Sort User Submissions**

Each user's score is based on their individual submissions. Users can:

-   **Search by Name**: View submissions for a specific user.
-   **Sort by Date or Score**:

-   Sort submissions by date (ascending or descending).
-   Sort submissions by score (ascending or descending).

-   **Submission View**:

-   See a user's best 24 submissions (this impacts their leaderboard rank).
-   Alternatively, view all of a user's submissions.

**4\. Dynamic and Responsive UI**

-   **Dynamic Sidebar**: The sidebar automatically adjusts to screen sizes, shrinking on smaller devices to maximize screen space. On smaller screens, the sidebar is hidden and can be expanded by hovering over it, ensuring easy navigation without cluttering the interface. This responsive design enhances the user experience across devices of all sizes.
-   **Search & Filter Leaderboard**: The "Search & Filter" functionality allows users to search by name and apply additional filters based on score or rank. Users can filter by scores above, below, or between a specific range, and similarly for ranking.
-   **View and Sort User Submissions**: The "Find By User/Search User Submissions" page allows users to search by name and sort submissions by date or score. The search results can include a user's best 24 submissions or all of their submissions. Sorting can be done either in ascending or descending order for both date and score.

* * * * *

**Setup Instructions**

**1\. Clone the Repository**

To get started, clone the repository to your local machine:

bash

Copy code

git clone https://github.com/theSovereignDan/ScoreQuest

cd ScoreQuest

**2\. Install Dependencies**

Ensure you have Python and pip installed. Then, install the required dependencies:

-   Install the Python dependencies from requirements.txt:

pip install -r requirements.txt

**3\. Run the Application**

Start the server using Python:

python app.py

To view the web-app visit http://localhost:5015.

* * * * *

**Running Tests**

To run tests I have created for all the Python files:

bash

Pytest or Pytest -v

This will execute all the tests

* * * * *

**Directory Structure**

The application is organized into the following structure:

bash

.

├── static

│   ├── css

│   │   ├── findbyuser.css

│   │   ├── leaderboard.css

│   │   ├── result.css

│   │   ├── search.css

│   │   └── usersubmissions.css

│   ├── images

│   │   ├── logo.png

│   │   ├── notfound.png

│   │   ├── search.png

│   │   └── user.png

│   └── js

│       ├── findbyuser.js

│       └── search.js

├── templates

│   ├── partials

│   │   ├── popup.html

│   │   └── sidebar.html

│   ├── findbyuser.html

│   ├── leaderboard.html

│   ├── result.html

│   ├── search.html

│   └── usersubmissions.html

├── tests

│   ├── __pycache__

│   ├── test_calculate_leaderboard_data.py

│   ├── test_calculate_user_submissions.py

│   ├── test_filter_leaderboard.py

│   ├── test_leaderboard_message_generation.py

│   └── test_user_submissions_message_generation.py

├── services

│   ├── leaderboard

│   │   ├── leaderboard_filtering.py

│   │   ├── leaderboard_message_generation.py

│   │   └── leaderboard_processor.py

│   ├── user_submissions

│   │   ├── user_submissions_message_generation.py

│   │   └── user_submissions_processor.py

│   └── json_file_handler.py

├── data

│   └── scores.json

├── app.py

└── requirements.txt
