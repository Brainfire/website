# Scroll to top
$('#back-to-top').bind "click", (event) =>
  do event.preventDefault
  $('html, body').animate { 'scrollTop': 0 }

$('#questions').bind "click", (event) =>
  do event.preventDefault
  do window.Zenbox.show();