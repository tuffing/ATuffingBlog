//lazy load in the next article when the user is near the end

//Ths share link is thee bottom of the article so wen that comes into view it is thoeritcally the best time to load it
let newestLoaded = document.querySelector('.article-post .share-post:last-child');
let triggered = false;

var elementInViewport = function (element) {
    //adapted from https://gomakethings.com/how-to-test-if-an-element-is-in-the-viewport-with-vanilla-javascript/
    var bounding = element.getBoundingClientRect();
    return (bounding.top >= 0 && bounding.left >= 0 
        && bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
};


var appendNewArticle = function(json) {
    if (json.length == 0) {
        return;
    }

    //takes an existing article as a template, an switches out the relevent parts with the new ones;
    let template = document.querySelector('.article-post:first-child').cloneNode(true);

    //("headline", "machine_name", "tags", "body", "pub_date", "teaser", "author", "header_image", "header_image_small")

    //header
    template.querySelector('h1').innerHTML = json[0]['headline']
    //@TODO links
    //@TODO banner

    //byline
    //@TODO pubdate
    //@TODO author

    //content
    //@TODO body

    //footer
    //@TODO tags
    //@TODO share links
    
    document.querySelector('.left-col:first-child').append(template)
}

var fetchNextArticle = function() {
    let count = document.querySelectorAll('.article-post').length;
    fetch(`/api/v1/articles/recent/?start_index=${count}&format=json`).then(response => {
        if (response.ok) {
          return Promise.resolve(response);
        }
        else {
          return Promise.reject(new Error('Failed to load')); 
        }
    })
    .then(response => response.json()) // parse response as JSON
    .then(data => {
        // success
        appendNewArticle(data);
    })
    .catch(function(error) {
        console.log(`Error: ${error.message}`);
    });
    
}


window.addEventListener('scroll', function (event) {
    if (elementInViewport(newestLoaded) && !triggered) {
        //alert(newestLoaded.innerHTML);
        fetchNextArticle();
        triggered = true;
    }
}, false);