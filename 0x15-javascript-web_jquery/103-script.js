$(document).ready(function() {
  $('#INPUTbtn_translate').click(function() {
    translate();
  });

  $('#INPUTlanguage_code').keypress(function(event) {
    if (event.which === 13) {
      event.preventDefault();
      translate();
    }
  });

  function translate() {
    const codeLang = $('#INPUTlanguage_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${codeLang}/`,
	    function(data) {
      $('#DIVhello').text(data.hello);
    });
  }
});
