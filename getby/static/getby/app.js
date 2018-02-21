'use strict'

// --- Make ajax call every n in milliseconds --- \\

(setTimeout(function() {
  update();
}, 50))();
function update() {
  $.ajax({
    type: 'GET',
    url: '', // URL to your view that serves new info
    success: function(data) {
      $('#matrix').html(data);
    }
  });
}
