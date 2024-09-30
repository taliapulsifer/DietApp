// 'document' refers to the html document you are working with
// 'addEventListener' is a function that listens for an event (like a button click)
// 'DOMContentLoaded' is the event for the listener. This means we are listening for when the html is fully loaded
document.addEventListener("DOMContentLoaded", function ()
{
    // waterElement is assigned to the element with the .water class in the html
    const waterElement = document.querySelector('.water');
    // Get the total calories and parse into an int for later calculations
    const totalCalories = parseInt(waterElement.dataset.totalCalories, 10);
    // The user's goal calories ** This needs to be changed so the user can add their own goal**
    const goalCalories = 2000;

    //Calculate the percentage of calories consumed. This function 'min' ensures that the percentage never exceeds 1000
    const percentage = Math.min((totalCalories / goalCalories) * 100, 100)

    // Set the height of the water element
    waterElement.style.height = `${percentage}%`;

});

    // This function delays the execution of the code inside the body by the specified amount of time
    //setTimeout(() =>{
        // This adds a CSS transition effect to the .water element
        //waterElement.style.transition = "height 1.5 ease-in-out"
        // This sets the final height of the .water element based on the calculated percentage
       // waterElement.style.height = `${percentage}`
            //This is the second parameter for the setTimeout, in this case 100 milliseconds
    //}, 100);