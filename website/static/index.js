document.addEventListener("DOMContentLoaded", function () {
  M.AutoInit();
});

/* Close alerts */
const closeAlerts = document.querySelectorAll(".close-alert");

for (let closeAlert of closeAlerts) {
  closeAlert.onclick = (e) => {
    e.target.parentNode.remove();
  };
}

/* Delete todos */
const delButtons = document.querySelectorAll(".delTodo");

for (let delButton of delButtons) {
  delButton.onclick = (e) => {
    const todoId = e.target.dataset["id"];
    fetch(`/delete-todo/${todoId}`, { method: "DELETE" })
      .then(() => {
        window.location.href = "/todo";
      })
      .catch((e) => {
        console.log("error", e);
      });
  };
}

/* Checkboxes */
const checkBoxes = document.querySelectorAll(".check-completed");

for (let checkBox of checkBoxes) {
  checkBox.onchange = (e) => {
    const todoId = e.target.dataset["id"];
    const checked = e.target.checked;

    fetch(`/update-todo/${todoId}`, {
      method: "POST",
      body: JSON.stringify({
        completed: checked,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }).then(() => {
      window.location.href = "/todo";
    });
  };
}

/* Auto resize text area */

const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute(
    "style",
    "height:" + tx[i].scrollHeight + "px;overflow-y:hidden;"
  );
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = "auto";
  this.style.height = this.scrollHeight + "px";
}
