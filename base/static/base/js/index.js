// This code will add a new exercise to the website when the user clicks on the "Add Exercise" button.

var exercises = document.getElementById("exercises");
var addExerciseButton = document.getElementById("add-exercise-button");

addExerciseButton.addEventListener("click", function() {
  var newExercise = document.createElement("li");
  newExercise.innerHTML = "New Exercise";
  exercises.appendChild(newExercise);
});
