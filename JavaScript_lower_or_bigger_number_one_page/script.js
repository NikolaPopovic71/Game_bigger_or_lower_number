const toggle = document.getElementById("toggle");

toggle.addEventListener("change", function () {
  document.body.classList.toggle("night-mode");
});

let sn = 5; // this is starting number
let c = 0; // this is counter for number of guessed numbers

let buttonBigger = document.getElementById("bigger");
let buttonLower = document.getElementById("lower");
let numberDisplay = document.getElementById("number_display");
let finalMessage = document.getElementById("final_message");
let buttonReset = document.getElementById("reset_game");
let endMessage = document.getElementById("end_message"); // Add this to specifically target the end message

function generateDifferentRandomNumber() {
  let random_number;
  do {
    random_number = Math.floor(Math.random() * 10) + 1; // Generates a number from 1 to 10
  } while (random_number === sn); // Keep generating until it's different from sn
  return random_number; // Return the new, different number
}

function bigger() {
  let random_number = generateDifferentRandomNumber();

  if (random_number > sn) {
    numberDisplay.textContent = random_number;
    sn = random_number;
    c += 1;
  } else {
    numberDisplay.textContent = `${random_number} is a lower number`;
    end_game();
  }
}

buttonBigger.addEventListener("click", bigger);

function lower() {
  let random_number = generateDifferentRandomNumber();

  if (random_number < sn) {
    numberDisplay.textContent = random_number;
    sn = random_number;
    c += 1;
  } else {
    numberDisplay.textContent = `${random_number} is a bigger number`;
    end_game();
  }
}

buttonLower.addEventListener("click", lower);

function end_game() {
  finalMessage.style.display = "block";
  endMessage.innerHTML =
    c === 0
      ? `Ups! You had ${c} hits! <br>You seem to be a great lover!<br>Would you like to play a new game?`
      : `Congratulations!<br>You had ${c} hits!<br>Would you like to play a new game?`;
  buttonBigger.removeEventListener("click", bigger);
  buttonLower.removeEventListener("click", lower);
  buttonReset.style.display = "inline-block"; // Make sure this line remains to show the reset button
}

function resetGame() {
  sn = 5;
  c = 0;
  numberDisplay.textContent = "5";
  finalMessage.style.display = "none";

  // Re-add event listeners for a new game
  buttonBigger.addEventListener("click", bigger);
  buttonLower.addEventListener("click", lower);
}

buttonReset.onclick = resetGame;
