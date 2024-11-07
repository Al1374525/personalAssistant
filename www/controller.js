$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $("#siri-message ").text(message); //Update the text content
        $('.siri-message').textillate('start'); //Animate if needed

    }

    //eel.expose(DisplayMessage);

    //Display Hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

});