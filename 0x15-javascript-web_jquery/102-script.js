$(document).ready(function() {
  $('#INPUTbtn_translate').click(function() {
    const codeLang = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${codeLang}/`,
	    function(data) {
      $('#DIVhello').text(data.hello);
    });
  });
});
