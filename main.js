/** @global Mustache **/
(function () {
    /**
     * Queued list of scripts urls and functions to be loaded or executed sequentially
     *
     * @type {string[]|Function[]}
     */
    var appScripts = [
        'https://code.jquery.com/jquery-2.2.0.min.js',
        'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js',
        'https://cdn.bootcss.com/bootbox.js/4.4.0/bootbox.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.min.js',
        appMainScript,
    ];

    // Load or executes scripts sequentially
    appLoadScripts(appScripts);

    /**
     * Loads or executes scripts urls or functions sequentially.
     *
     * @param scripts {string[]|Function[]} a queued array of script urls, or/and functions or mix of the two types.
     */
    function appLoadScripts(scripts) {
        // insert the first script in the queue
        insertScript(scripts.shift());

        /**
         * Loads or executes the provided script
         *
         * @param _script {string|Function} a script url or a function
         */
        function insertScript(_script) {
            // if the provided `_script` is a function, then execute it (call it)
            if (typeof _script === 'function') {
                _script();
                // after executing the script we shouldn't proceed to other instructions as
                // this is a function and not a url of the script
                return;
            }

            // if the provided script is not a function, it's assumed to be a string url of the script
            // so we are creating a DOM script element and set its source to the provided url
            // and then add it to the end of the document
            var script = document.createElement('script');
            script.src = _script;
            // listening to the onLoad event so we can load other, next, scripts after
            // this script is loaded
            script.onload = scriptLoaded;
            document.body.appendChild(script);
        }

        /**
         * A listener for the script onLoad event.
         * Used to load or execute the next script in the queue
         */
        function scriptLoaded() {
            // detects if all script has been loaded
            // so we stop trying to load next scripts
            if (scripts.length < 1)
                return;

            // inserts the next script in the queue
            insertScript(scripts.shift());
        }
    }

    /**
     * Contains scripts that are going to be executed after loading all required
     * external scripts
     */
    function appMainScript() {
        (function ($) {
            // retrieve the template of the movie dialog
            var dialogTemplate = $('#movie-dialog-template').html();

            // parse the template to speed up performance
            Mustache.parse(dialogTemplate);

            $('.movie').click(function () {
                // retrieve movie data
                var movie = $(this).data();

                // list of rendered properties
                var renders = {
                    rate: renderRate(movie.rate),
                    cast: renderCast(movie.cast),
                };

                // show movie dialog
                bootbox.dialog({
                    title: movie.title + ' (' + movie.year + ')',

                    // render and return the dialog template
                    message: Mustache.render(dialogTemplate,
                        // overwrite movie data that require rendering
                        // with the rendered one
                        // using `{}` as the target to prevent overriding the original movie data
                        $.extend({}, movie, renders)),
                });
            });

            $('.poster-source').click(function (e) {
                // to prevent passing the click event
                // to the `.movie` click listener
                e.stopPropagation();
            });

            /**
             * Renders the rating number into stars
             *
             * @param rate {number} Movie rate
             * @returns {string} Rendered movie rate (HTML string)
             */
            function renderRate(rate) {
                /**
                 * This will allow us to detect when there is a half-full star
                 * for example if `rate` is 4 then `_tempRate` will evaluate to `4`
                 * therefore, when we compare them they'll be equal which will indicated
                 * that there is no half-full star.
                 * but if `rate` was 3.5 for instance. Then `_tempRate` will evaluate to `4`
                 * which is not equal to `rate` and it means that there is a half-full rose
                 *
                 * @type {number}
                 */
                var _tempRate = Math.ceil(rate);

                /**
                 * Indicates whether there is a half star or not.
                 *
                 * Note: if `_tempRate` does not equal `rate`, that means there is a half-full star.
                 *      @see _tempRate
                 *
                 * @type {boolean}
                 */
                var halfStar = (_tempRate !== rate);

                /**
                 * HTML string contains the rendered stars
                 * @type {string}
                 */
                var stars = '';

                for (var i = 0; i < (halfStar ? rate - 1 : rate); i++) {
                    stars += '<i class="fa fa-star"></i> ';
                }

                if (halfStar) {
                    stars += '<i class="fa fa-star-half-full"></i>';
                }

                return stars;
            }

            /**
             * Renders movie cast string into a list
             *
             * @param castString {string} string that contains cast info. In this example pattern `'cast name a:1, cast name b:0'`
             * @returns {string} Rendered movie cast (HTML string)
             */
            function renderCast(castString) {
                // The `castString` contains cast information array separated by `,`
                // therefore spliting them by `,` will gives an array of cast information in each element
                var cast = castString.split(',');

                /**
                 * HTML string contains the rendered cast
                 * @type {string}
                 */
                var renderedCast = '';

                cast.forEach(function (cstInfo) {
                    // `cstInfo` holds cast information represented as `cast name:[1|0])
                    // where 1 means the person is starring in the movie and 0 is not
                    // therefore when we split it by `:` this will give us an array
                    // of two elements. The first element is the cast name, and the
                    // second is a flag to determine whether or not the cast is starring
                    // in the movie
                    var cst = cstInfo.split(':');

                    // open the wrapper div tag and put cast name
                    renderedCast += '<div class="col-sm-4 col-xs-6">' + cst[0];

                    // check if cast is starring
                    if (cst[1] === '1') {
                        // add star next to the cast name
                        renderedCast += ' <i class="fa fa-star"></i>';
                    }

                    // close the div tag
                    renderedCast += '</div>';
                });

                return renderedCast;
            }
        })(jQuery);
    }
})();