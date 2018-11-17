/*
@TODO
- page reload - load to the right place
- more than one lazy load

*/

//lazy load in the next article when the user is near the end

//Ths share link is thee bottom of the article so wen that comes into view it is thoeritcally the best time to load it
//let newestLoaded = document.querySelector('.homepage .article-post .share-post:last-child');
let newestLoaded = document.querySelector('.homepage .article-post');
let triggered = false;
let documentReady = false;

/**
* Returns true if x% of an element is above the fold
**/
var xPercentOfElementAboveViewportFold = function (element, percentageX) {
    var bounding = element.getBoundingClientRect();

    let horizontalCheck = bounding.right <= (window.innerWidth || document.documentElement.clientWidth) && bounding.left >= 0;
    let percentageXLocation = ((bounding.bottom - bounding.top) * percentageX) + bounding.top;
    let verticalCheck = percentageXLocation <= (window.innerHeight || document.documentElement.clientHeight);

    return horizontalCheck && verticalCheck;
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

        triggered = false;
        //newestLoaded = wrapper.querySelector('.share-post:last-child');
        newestLoaded = wrapper;
    })
    .catch(function(error) {
        console.log(`Error: ${error.message}, likely no more articles`);
    });
    
}

if (document.querySelectorAll('.homepage').length) {
    window.addEventListener('scroll', function (event) {
        if (!triggered && xPercentOfElementAboveViewportFold(newestLoaded, .5)) {
            //alert(newestLoaded.innerHTML);
            fetchNextArticle();
            triggered = true;
        }
    }, false);
}
