const closeAlerts = document.querySelectorAll(".close-alert");

for (let closeAlert of closeAlerts) {
  closeAlert.onclick = (e) => {
    e.target.parentNode.remove();
    /*console.log(e);*/
  };
}
