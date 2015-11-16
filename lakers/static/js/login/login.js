/**
 * Created by bug on 15/11/2.
 */

+function () {

  // login
  $(function() {
    $(document).on('click', '.btn-submit-login', function(e) {
      e.preventDefault();
      var username = $(':input[name="username"]').val();
      var password = $(':input[name="password"]').val();
      $.ajax({
        type: "POST",
        url: "/api/login/",
        data: {
          username: username,
          password: password
        },
        success: function(jsn) {
          if (jsn.success === true) {
            window.location.replace('/');
          } else {
            alert(jsn.message.password + ' -- ' + jsn.message.username)
          }
        }
      });
    });
  });

}();


