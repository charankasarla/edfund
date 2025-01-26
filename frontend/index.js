let isOpen = true;
const toggle_sidebar = document.getElementById("toggle_sidebar");
const sidebar = document.getElementById("left_sidebar");
const parent_sidebar = document.querySelector(".sidebar-left");

function toggleSidebar() {
  console.log("sidebar", parent_sidebar);

  if (!isOpen) {
    sidebar.classList.remove("close");
    parent_sidebar.style.width = "300px";
    toggle_sidebar.classList = "fa-solid fa-bars";
    isOpen = true;
  } else {
    sidebar.classList.add("close");
    parent_sidebar.style.width = "0";
    toggle_sidebar.classList = "fa-solid fa-times";
    isOpen = false;
  }
}

function adjustPageScale() {
  const width = window.innerWidth;
  let scale = 1;

  if (width >= 992 && width <= 1600) {
    scale = 0.9;
  } else if (width >= 700 && width <= 767) {
    scale = 0.8;
  } else if (width >= 600 && width < 700) {
    scale = 0.75;
  } else if (width <= 600) {
    scale = 0.5;
  }

  document.body.style.transform = `scale(${scale})`;
  document.body.style.transformOrigin = "top left";
  // Adjust container width to prevent horizontal scrollbar
  document.body.style.width = `${100 / scale}%`;
}
