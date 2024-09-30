// gets the values for the inputs (comes from HTML form elements)
const nameInput = document.getElementById('name');
const scoreFilterInput = document.getElementById('score');
const scoreThresholdInput = document.getElementById('score-threshold');
const rankFilterInput = document.getElementById('rank');
const rankThresholdInput = document.getElementById('rank-threshold');

const scoreThresholdLowInput = document.getElementById('score-threshold-low');
const scoreThresholdHighInput = document.getElementById('score-threshold-high');
const rankThresholdLowInput = document.getElementById('rank-threshold-low');
const rankThresholdHighInput = document.getElementById('rank-threshold-high');

// gets elements for the labels (from HTML form elements)
const rankLabel = document.getElementById('ranklabel');
const scoreLabel = document.getElementById('scorelabel');
const nameLabel = document.getElementById('namelabel');


// function to turn the rank and score labels and input fields grey
// it also reduces the opacity 
// this is used when the user types in the name input field
// because if they searching for a name. its not useful to filter by rank or score
// it does this by addiing a class to the labels
function greyoutScoreAndRank() {
    rankLabel.classList.add('greyed-out');
    scoreLabel.classList.add('greyed-out');

    scoreFilterInput.classList.add('greyed-out');
    scoreThresholdInput.classList.add('greyed-out');

    scoreThresholdLowInput.classList.add('greyed-out');
    scoreThresholdHighInput.classList.add('greyed-out');

    rankFilterInput.classList.add('greyed-out');
    rankThresholdInput.classList.add('greyed-out');

    rankThresholdLowInput.classList.add('greyed-out');
    rankThresholdHighInput.classList.add('greyed-out');
}

// Function to bring default styling back to rank and score 
// labels and input fields, it brings the opacity back to 1
// and colours back to normal by removing class
// from all the labels and input fields
// it is used when the user clears the name input field
function makeScoreAndRankNormal() {
    rankLabel.classList.remove('greyed-out');
    scoreLabel.classList.remove('greyed-out');

    scoreFilterInput.classList.remove('greyed-out');
    scoreThresholdInput.classList.remove('greyed-out');

    rankFilterInput.classList.remove('greyed-out');
    rankThresholdInput.classList.remove('greyed-out');

    scoreThresholdLowInput.classList.remove('greyed-out');
    scoreThresholdHighInput.classList.remove('greyed-out');
    rankThresholdLowInput.classList.remove('greyed-out');
    rankThresholdHighInput.classList.remove('greyed-out');
}

// Function used to disable the input field for entering the name 
// it also reduces the opacity of the input field and label
// as well as changes the colour of the label and input field
// to be more grey

function disableNameLabel() {
    // Add the greyed-out class to make labels grey
    nameLabel.classList.add('greyed-out');
    nameInput.classList.add('greyed-out');
}


// Function used to enable the input field for entering the name 
// it also brings the opacity back to 1 for the input field and label
// as well as changes the colour of the label and input field
// back to normal b
function enableNameLabel() {
    // Remove the greyed-out class to restore default label styling
    nameLabel.classList.remove('greyed-out');
    nameInput.classList.remove('greyed-out');
}

// This function is called when the user types in the name input field
function toggleFieldsOnNameInput() {
    // this io used to only allow alphabet characters, apostrophes and hyphens in the name input field
    this.value = this.value.replace(/[^a-zA-Z\s\-\']/g, '');


if (nameInput.value.trim() !== "") {
        // We checked to see if the name field has a value, then disabled other inputs
        // this is because if a user is searching by name, it's not useful to filter by rank or score
        scoreFilterInput.disabled = true;
        scoreThresholdInput.disabled = true;
        rankFilterInput.disabled = true;
        rankThresholdInput.disabled = true;

        scoreThresholdLowInput.disabled = true;
        scoreThresholdHighInput.disabled = true;
        rankThresholdLowInput.disabled = true;
        rankThresholdHighInput.disabled = true;

        //this calls function that greys out and reduces opacity of the rank and score labels and input fields
        greyoutScoreAndRank();
} else {
        // If name field is cleared, enable all the score and rank input options 
        // this is because if the user is not searching by name, they can may want to filter by rank or score
        scoreFilterInput.disabled = false;
        scoreThresholdInput.disabled = false;
        rankFilterInput.disabled = false;
        rankThresholdInput.disabled = false;

        scoreThresholdLowInput.disabled = false;
        scoreThresholdHighInput.disabled = false;
        rankThresholdLowInput.disabled = false;
        rankThresholdHighInput.disabled = false;

        // this calls the function that brings the opacity back to 1 and removes the greyed out class
        // bringing default styling back to rank and score labels and input fields
        makeScoreAndRankNormal();
    }
}

// this function is called when the user types in any of the other input fields (related to score and rank)
function toggleFieldsOtherInputs() {
// checks to see if anything is entered in any of the score and rank input fields 
if (scoreThresholdInput.value.trim().length !==0 || rankThresholdInput.value.trim().length !==0 || scoreThresholdLowInput.value.trim().length !==0 || scoreThresholdHighInput.value.trim().length !==0 || rankThresholdLowInput.value.trim().length !==0 || rankThresholdHighInput.value.trim().length !==0) { 
        // If any of the score and rank input fields has a value, it disable the name input field
        // and then calls the function to grey out and reduce opacity of name input field and label
        nameInput.disabled = true;
        disableNameLabel();
} 
else {
    // If there is no value entered in any of the score and rank input fields, it enables the name input field
    // and calls the function to bring the opacity back to 1 and remove the greyed out class
    nameInput.disabled = false;
    enableNameLabel();
}
}


// Add event listener to the name input field which calls the function whenever an input detected
nameInput.addEventListener('input', toggleFieldsOnNameInput);

// Add event listener to the other input fields which calls the function whenever an input detected
scoreThresholdInput.addEventListener('input', toggleFieldsOtherInputs);
scoreThresholdHighInput.addEventListener('input', toggleFieldsOtherInputs);
scoreThresholdLowInput.addEventListener('input', toggleFieldsOtherInputs);

rankThresholdInput.addEventListener('input', toggleFieldsOtherInputs);
rankThresholdHighInput.addEventListener('input', toggleFieldsOtherInputs);
rankThresholdLowInput.addEventListener('input', toggleFieldsOtherInputs);

// adds an event listener to the submit button on the search form so that when the user clicks the submit button it calls this internal function
document.getElementById('search-form').addEventListener('submit', function(e) {
e.preventDefault();

// Get the form values from the html elements
const name = document.getElementById('name').value.trim();
const scoreFilter = document.getElementById('score').value;
const scoreThreshold = document.getElementById('score-threshold').value.trim();
const rankFilter = document.getElementById('rank').value;
const rankThreshold = document.getElementById('rank-threshold').value.trim();

// does the same for the form values used for when the between filter is selected
// meaning the user can enter a range for score or rank
const scoreThresholdLow = document.getElementById('score-threshold-low').value.trim();
const scoreThresholdHigh = document.getElementById('score-threshold-high').value.trim();
const rankThresholdLow = document.getElementById('rank-threshold-low').value.trim();
const rankThresholdHigh = document.getElementById('rank-threshold-high').value.trim();


// Check if at least one of name, scoreThreshold, or rankThreshold is provided
if (name === '' && scoreThreshold === '' && rankThreshold === '' &&
    scoreThresholdLow === '' && scoreThresholdHigh === '' &&
    rankThresholdLow === '' && rankThresholdHigh === '') {
    showPopup("Please enter something for name, score or rank to start your search.");
    return;
}

// If "between" is selected for both score and rank filters, ensure neither are left empty and if they are say to fill in 
if (scoreFilter === 'between' && rankFilter === 'between') {
    if ((scoreFilter === 'between' && (scoreThresholdLow === '' || scoreThresholdHigh === '')) &&
        (rankFilter === 'between' && (rankThresholdLow === '' || rankThresholdHigh === ''))) {
        showPopup("Please fill in both the score and rank thresholds");
        return;
    }
}

// If "between" for score is selected: both scoreThresholdLow and scoreThresholdHigh must be filled not just one 
if (scoreFilter === 'between') {
    if ((scoreThresholdLow === '' && scoreThresholdHigh !== '') || (scoreThresholdLow !== '' && scoreThresholdHigh === '')) {
        showPopup("Please enter both low and high score thresholds.");
        return;
    }
}

// If "between" for rank is selected: both rankThresholdLow and rankThresholdHigh must be filled not just one 
if (rankFilter === 'between') {
    if ((rankThresholdLow === '' && rankThresholdHigh !== '') || (rankThresholdLow !== '' && rankThresholdHigh === '')) {
        showPopup("Please enter both low and high rank thresholds.");
        return;
    }
}


// creates query paramaters we going to use to attach to URL link - avoids need to manually construct it all 
const queryParams = new URLSearchParams({
    name: name,
    scoreFilter: scoreFilter,
    scoreThreshold: scoreFilter !== 'between' ? scoreThreshold : '', // Send blank if between
    rankFilter: rankFilter,
    rankThreshold: rankFilter !== 'between' ? rankThreshold : '' // Send blank if between
});

// If "between" is selected, send separate parameters for the low and high thresholds for the score by appending them onto the parameters 
if (scoreFilter === 'between') {
    queryParams.append('scoreThresholdLow', scoreThresholdLow);
    queryParams.append('scoreThresholdHigh', scoreThresholdHigh);
}

// If "between" is selected, send separate parameters for the low and high thresholds for the rank by appending them onto the parameters 

if (rankFilter === 'between') {
    queryParams.append('rankThresholdLow', rankThresholdLow);
    queryParams.append('rankThresholdHigh', rankThresholdHigh);
}


// Redirect to results page with the selected parameters
// Which will first be recieved by our app.py file endpoint 
window.location.href = `/result?${queryParams.toString()}`;

});

//adds an event listener that detects when the dropdown menu for score filter is changed
// does the same for the rank filter
// calls a function that clears the low and high score thresholds if "between" is not selected
scoreFilterInput.addEventListener('change', handleScoreFilterChange);
rankFilterInput.addEventListener('change', handleRankFilterChange);

function handleScoreFilterChange() {
    const scoreFilter = document.getElementById('score').value;
    
    // If "between" is not selected, clear the low and high score thresholds
    if (scoreFilter !== 'between') {
        scoreThresholdHighInput.value = '';
        scoreThresholdLowInput.value = '';
        if (rankFilterInput.value !== 'between') {
            toggleFieldsOtherInputs()
        }
    }
}

function handleRankFilterChange() {
    const rankFilter = document.getElementById('rank').value;
    
    // If "between" is not selected, clear the low and high rank thresholds
    if (rankFilter !== 'between') {
        rankThresholdHighInput.value = '';
        rankThresholdLowInput.value = '';
        if (scoreFilterInput.value !== 'between') {
            toggleFieldsOtherInputs()
        }
    }
}


// Show the custom pop-up with a message
function showPopup(message) {
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popup-message');
    
    popupMessage.textContent = message;
    popup.classList.remove('hidden');
    popup.style.display = 'block'; 
}

// Hide the custom pop-up
function hidePopup() {
    const popup = document.getElementById('popup');
    popup.classList.add('hidden');
    popup.style.display = 'none'; 
}

// makes close button click event listener to hide the popup when detect button is clicked
document.getElementById('close-popup').addEventListener('click', hidePopup);


// adds event listener to the dropdown menu for score filter  change
// if it is changed to "between", show both the high and low threshold inputs and hide the single threshold input
// for the reverse the high and low threshold inputs are hidden and the single threshold input is shown
document.getElementById('score').addEventListener('change', function() {
    const scoreBetweenFields = document.getElementById('score-between-fields');
    if (this.value === 'between') {
        scoreBetweenFields.style.display = 'block';
        document.getElementById('score-threshold').style.display = 'none';  // Hide single threshold input
    } else {
        scoreBetweenFields.style.display = 'none';
        document.getElementById('score-threshold').style.display = 'block';  // Show single threshold input
    }
});
// adds event listener to the dropdown menu for rank filter  change
// if it is changed to "between", show both the high and low threshold inputs and hide the single threshold input
// for the reverse the high and low threshold inputs are hidden and the single threshold input is shown
document.getElementById('rank').addEventListener('change', function() {
    const rankBetweenFields = document.getElementById('rank-between-fields');
    if (this.value === 'between') {
        rankBetweenFields.style.display = 'block';
        document.getElementById('rank-threshold').style.display = 'none';  // Hide single threshold input
    } else {
        rankBetweenFields.style.display = 'none';
        document.getElementById('rank-threshold').style.display = 'block';  // Show single threshold input
    }
});