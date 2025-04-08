$(document).ready( () => {
	
	// runs when an h2 heading is clicked
    $("#faqs h2").click( evt => {
		const target = evt.currentTarget;

		$(target).toggleClass("minus");

		if ($(target).attr("class") != "minus") {
		   	$(target).next().slideUp(1000, "easeInBounce");
	   	}
	   	else {
	        $(target).next().slideDown(1000, "easeOutBounce");
		   }

    });
    
    
});
