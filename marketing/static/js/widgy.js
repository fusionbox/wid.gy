$(document).ready(function(){


  //|
  //| Homepage Anchor Jumps
  //|
  $("header a").bind("click", function(event){
    var target = $(this).attr('href');
    var targetPos = $(target).offset().top - 60;
    
    $('html, body').animate({
        scrollTop: targetPos
    }, 1000);
    
    event.preventDefault();
    return false;
  });
  
  //|
  //| Scroll-Based Functions
  //|
  var headerHeight = $("header").height();
  var arbitrarySpacer = 300;
  
  function runAtScrollPosition() {
    var distanceFromTop = $(window).scrollTop();
    
    // if we've scrolled past the header
    if (distanceFromTop >= headerHeight - 25) {
      $("body").addClass("bop-it");
    }
    else {
      $("body").removeClass("bop-it");
    }
    
    // highlight the top nav
    
    // for each section
      // get the top
      // compare against the current scroll position
      // if it's within some parameter, grab the ID and highlight the matching top nav
      
    $("body > section").each(function(){
      var myOffset = $(this).offset().top + headerHeight - arbitrarySpacer;
      var myHeight = $(this).height();
      var totalHeight = myOffset + myHeight;
      var myId = $(this).attr("id");
      
      if (myOffset < distanceFromTop && distanceFromTop < totalHeight) {
        $("header a").removeClass("here");
        $("header a[href='#" + myId + "']").addClass("here");
      }
    });
  }

  var throttled = _.throttle(runAtScrollPosition, 100);
  $(window).delay(3000).scroll(throttled);


  //|
  //| Set Feature Tooltip Positions 
  //|
  calculateTooltipWidths();
  $(window).resize(function(){
    calculateTooltipWidths();
  });
  
  function calculateTooltipWidths(){
    $("td span.feature").each(function(){
      var newWidth = $("section.features .inner").width() - 50; // descriptionn span's horizontal padding
      var newTop = $(this).height() + 32;
      $(this).next("span.description").css("width", newWidth + "px");
      $(this).next("span.description").css("top", newTop + "px");
    });
  }

  //|
  //| convert external links
  //|
  $("a[href*='http://']:not([href*='"+location.hostname+"']), a[rel='external']").attr("target","_blank");
  
  
});
