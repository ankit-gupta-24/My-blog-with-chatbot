if ($(window).width() > 992) {
    $(window).scroll(function(){  
       if ($(this).scrollTop() > 40) {
          $('#navbar_top').addClass("fixed-top");
          // add padding top to show content behind navbar
        //   $("#main").css('padding-top',$('#navbar_top').outerHeight()+'px');
          $('body').css('padding-top', $('.navbar').outerHeight() + 'px');
        }else{
          $('#navbar_top').removeClass("fixed-top");
           // remove padding top from body
        //    $("#main").css('padding-top','0');
          $('body').css('padding-top', '0');
        }   
    });
  }