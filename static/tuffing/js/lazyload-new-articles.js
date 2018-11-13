//lazy load in the next article when the user is near the end

//Ths share link is thee bottom of the article so wen that comes into view it is thoeritcally the best time to load it
let newestLoaded = document.querySelector('.homepage .article-post .share-post:last-child');
let triggered = false;

var elementInViewport = function (element) {
    //adapted from https://gomakethings.com/how-to-test-if-an-element-is-in-the-viewport-with-vanilla-javascript/
    var bounding = element.getBoundingClientRect();
    return (bounding.top >= 0 && bounding.left >= 0 
        && bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
};


var fetchNextArticle = function() {
    let count = document.querySelectorAll('.article-post').length;
    fetch(`/fetchArticlesOffset/${count}/`).then(response => {
        if (response.ok) {
          return Promise.resolve(response);
        }
        else {
          return Promise.reject(new Error('Failed to load')); 
        }
    })
    .then(response => response.text()) // parse response as JSON
    .then(data => {
        // success
        var wrapper = document.createElement('article');
        wrapper.className = 'article-post';
        wrapper.innerHTML = data;
        document.querySelector('.left-col:first-child').append(wrapper);
    })
    .catch(function(error) {
        console.log(`Error: ${error.message}`);
    });
    
}

if (document.querySelectorAll('.homepage').length) {
    window.addEventListener('scroll', function (event) {
        if (elementInViewport(newestLoaded) && !triggered) {
            //alert(newestLoaded.innerHTML);
            fetchNextArticle();
            triggered = true;
        }
    }, false);
}