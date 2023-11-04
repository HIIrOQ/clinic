$(document).ready(function(){
	
	$("a[href*='#']").on('click',function(){
		   var target=$(this).attr("href");
		   var tar=target.split("#");
		   targetSection=tar[1];
		   if (!targetSection || targetSection == '') {
                return;
            }else
			{
				targetSection = '#' + targetSection;
				var targetOffset = Math.floor($(targetSection).offset().top );
				var targetOffset1 = targetOffset - 65;
				//scroll			 
				$('html,body').animate({scrollTop: targetOffset1}, 1200, function() {
					
					$(window).scroll();
					
				});
				return false;
			}
		})
		
	$('.jw-animate').each(function() {
        var $curr = $(this);
        var $currOffset = $curr.attr('data-gen-offset');
        if ($currOffset === '' || $currOffset === 'undefined' || $currOffset === undefined) {
            $currOffset = 'bottom-in-view';
        }
        if ($currOffset === 'none') {
            $curr.trigger('jw-animate');
        } else {
            $curr.waypoint(function() {
                $curr.trigger('jw-animate');
            }, {triggerOnce: true, offset: $currOffset});
        }
    });  
	   // ewebcraft Animate General - Bind
    $('.jw-animate-gen').each(function() {
        var $curr = $(this);
        $curr.on('jw-animate', function() {
            $curr.css('opacity', '');
            $curr.addClass('animated ' + $curr.data('gen'));
        });
    });
    // ewebcraft Animate General
    $('.jw-animate-gen').each(function() {
        var $curr = $(this);
        var $currOffset = $curr.attr('data-gen-offset');
        if ($currOffset === '' || $currOffset === 'undefined' || $currOffset === undefined) {
            $currOffset = 'bottom-in-view';
        }
        $curr.waypoint(function() {
            $curr.trigger('jw-animate');
        }, {triggerOnce: true, offset: $currOffset});
    });

	$('#header').affix({
	  offset: {
		top:100,
		bottom: function () {
		  return (this.bottom = $('#footer').outerHeight(true))
		}
	  }
	})

});
	
