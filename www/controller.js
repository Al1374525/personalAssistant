$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage);
    
    function DisplayMessage(message) {

        $("#siri-message").text(message);
        $('.siri-message').textillate('start');
         // Add logic to re-enable input or retry after error
    if (message === "I didn't catch that. Please try again.") {
        console.log("Enabling retry options...");
        // Example: Automatically listen again after a short delay
        setTimeout(() => {
            eel.allCommands(1); // Retry command listening
        }, 3000);
    }

    }
    

    

    //Display Hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        
    }

});