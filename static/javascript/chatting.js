// Load the bot responses from a JSON file
var botResponses = {};

function loadBotResponses() {
  var xhr = new XMLHttpRequest();
  xhr.overrideMimeType("application/json");
  xhr.open("GET", "\static\keyword.json", true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      botResponses = JSON.parse(xhr.responseText);
    }
  };
  xhr.send();
}

loadBotResponses();

// Handle button click events
var buttons = document.getElementsByClassName("btn-quick-reply");
var chatBox = document.querySelector(".chat-box");

for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", handleButtonClick);
}

function handleButtonClick(event) {
  var buttonName = event.target.id;
  var lastOutgoingMsg = chatBox.lastElementChild.previousElementSibling;

  // Display the user's message
  var userMsgDiv = document.createElement("div");
  userMsgDiv.classList.add("chat", "outgoing");
  userMsgDiv.innerHTML = `
    <img src="/static/images/user.png" alt="" />
    <div class="details">
      <p class="user-msg">${buttonName}</p>
    </div>
  `;
  chatBox.appendChild(userMsgDiv);

  // Display the bot's response
  var botResponse = botResponses[buttonName];
  var botMsgDiv = document.createElement("div");
  botMsgDiv.classList.add("chat", "incoming");
  botMsgDiv.innerHTML = `
    <img src="/static/images/bot.png" alt="" />
    <div class="details">
      <p class="bot-msg">${botResponse}</p>
    </div>
  `;
  chatBox.appendChild(botMsgDiv);

  // Scroll to the bottom of the chat box
  chatBox.scrollTop = chatBox.scrollHeight;
}
