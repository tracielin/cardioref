// define variable
var searchResults = document.getElementById("search-results");
var searchBox = document.getElementById("search");
// var hidden =  document.getElementById("hidden");

// add event listener to the search box
searchBox.addEventListener("input", function() {
  // if no results found, search results are empty
  if (!this.value) {
    searchResults.innerHTML = "";
    return;
  }

  //   if (!this.value) {
  //     hidden.innerHTML =
  //   '.hidden:not([data-index*="' +
  //   this.value.toLowerCase() +
  //   '"]) { display: block ; }';
  //   return;
  // }

  // if characters typed in search box don't match any data-index, hide with display: none

  searchResults.innerHTML =
    '.searchable:not([data-index*="' +
    this.value.toLowerCase() +
    '"]) { display: none; }';
});

// Credits: http://www.redotheweb.com/2013/05/15/client-side-full-text-search-in-css.html
