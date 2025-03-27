document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("spamForm");
    const resultContainer = document.getElementById("resultContainer");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
  
      const inputType = document.getElementById("input_type").value;
      const userInput = document.getElementById("user_input").value.trim();
      
      let resultText = "";
      let resultClass = "";
  
      // Simple dummy logic for spam detection:
      // For emails: if the input contains "spam", mark as Spam, else Ham.
      // For website URLs: if the input contains "phish", mark as Phishing, else Legitimate.
      if (!userInput) {
        resultText = "Please enter some text!";
        resultClass = "spam";
      } else {
        if (inputType === "email") {
          if (/spam/i.test(userInput)) {
            resultText = "Spam";
            resultClass = "spam";
          } else {
            resultText = "Ham";
            resultClass = "ham";
          }
        } else if (inputType === "website") {
          if (/phish/i.test(userInput)) {
            resultText = "Phishing";
            resultClass = "spam";
          } else {
            resultText = "Legitimate";
            resultClass = "legitimate";
          }
        }
      }
  
      // Display the result in the resultContainer
      resultContainer.innerHTML = `
        <div class="result ${resultClass}">
          ${inputType.charAt(0).toUpperCase() + inputType.slice(1)} Result: ${resultText}
        </div>
      `;
    });
  });
  