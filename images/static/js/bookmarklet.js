(function(){
    var jquery_version = '2.1.4';
    var site_url = 'http://127.0.0.1:8000/';
    var static_url = site_url + 'static/'
    var min_width = 100;
    var min_height = 100;

    function bookmarklet() {
        // load css
        var css = $('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
        });
        $('head').append(css);

        // load html
        box_html = "<div id='bookmarklet'><a href='#' id='close'>&times;</a>"+
                        "<h1>Select an image to bookmark</h1><div class='images'></div></div>";
        $('body').append(box_html);
        // close event
        $('#bookmarklet #close').click(function(event) {
            $('#bookmarklet').remove();
        });

        jQuery.each(jQuery('img[src$="jpg"]'), function(index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height){
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('<a href="#"><img src="'+
                image_url +'" /></a>');
            }
        });

        // when an image is selected
        $('#bookmarklet .images a').click(function(event) {
            selected_image = $(this).children('img').attr('src');
            // hide bookmarklet
            $('#bookmarklet').hide();
            // open windows to submit an image
            window.open(
                site_url + 'images/create/?url='
                + encodeURIComponent(selected_image)
                + '&title='
                + encodeURIComponent(jQuery('title').text()),
                '_blank'
            );
        });
    }

    if(typeof window.jQuery != 'undefined'){
        bookmarklet()
    } else {
        // check for conflicts
        var conflicts = typeof window.$ != 'undefined';
        // create a script to point to google api
        var script = document.createElement('script');
        script.setAttribute('src',
            'https://ajax.googleapis.com/ajax/libs/jquery/' + jquery_version + '/jquery.min.js'
        );
        // append the script to head for processing
        document.getElementsByTagName('head')[0].appendChild(script);
        // waits until the script is loading
        var attempts = 30;
        (function(){
            // check again if jQuery is defined
            if (typeof window.jQuery == 'undefined') {
                if (--attempts > 0) {
                    // call himself in few milliseconds
                    window.setTimeout(arguments.callee, 250);
                } else {
                    // too much attempts
                    alert('Error while loading jQuery' + script);
                }
            } else {
                bookmarklet()
            }
        })();
    }
})();
