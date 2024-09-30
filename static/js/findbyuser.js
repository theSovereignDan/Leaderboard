//gets the values for the inputs (comes from HTML form elements)
const nameInput = document.getElementById('name');
const sortInput = document.getElementById('sort');
const orderInput = document.getElementById('order');
const qualifiedorallInput = document.getElementById('qualified-or-all');

// function to show a popup when the user not entered in a name (to inform them to do so)
function showPopup(message) {
    //links to the pop-up html elements
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popup-message');

    popupMessage.textContent = message; //assigns the pop up message value passed through
    popup.classList.remove('hidden'); //makes the pop up not hidden

    popup.style.display = 'block'; 
}
// Function to show a popup
function showPopup(message) {
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popup-message');
    popupMessage.textContent = message;
    popup.classList.remove('hidden');
    popup.style.display = 'block';
}

// function to hide the popup and go back to the find submissions by user page 
function hidePopup() {
    const popup = document.getElementById('popup');
    popup.classList.add('hidden'); // hides it 
    popup.style.display = 'none';
}

//adds event listener so that when you click the close pop up button it calls the above function
document.getElementById('close-popup').addEventListener('click', hidePopup);

// adds event listener so that when you click the submit button it calls this internal function 
document.getElementById('search-form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get the entered name, filter, order, qualifiedorall values from the inputs 
    const name = nameInput.value.trim();
    const sort = sortInput.value;
    const order = orderInput.value;
    const qualifiedorall = qualifiedorallInput.value;
    

    // checks if the user has entered a name and if they have not displays the pop up over the search for user submissions screen
    if (name === '') {
        showPopup("Please enter a name to proceed.");
        return;
    }

    // creates query paramaters we going to use to attach to URL link - avoids need to manually construct it all 
    const queryParams = new URLSearchParams({
        name: name,
        sort: sort,
        order: order,
        qualifiedorall: qualifiedorall
    });

    // Redirect to user submissions page with the selected parameters
    // Which will first be recieved by our app.py file endpoint 
    window.location.href = `/user-submissions?${queryParams.toString()}`;
});