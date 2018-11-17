/*
@TODO
- page reload - load to the right place
- more than one lazy load

*/

//lazy load in the next article when the user is near the end

//Ths share link is thee bottom of the article so wen that comes into view it is thoeritcally the best time to load it
//let newestLoaded = document.querySelector('.homepage .article-post .share-post:last-child');
let newestLoaded = document.querySelector('.article-post');
let triggered = false;

let pageOriginalPath = window.location.pathname;
let pageOriginalTitle = document.title;
let firstArticle = document.querySelector('.article-post header .title');
if (firstArticle) {
    var activeArticlePath, firstArticlePath = firstArticle.getAttribute('href');
}

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


/**
* Returns the dom object matching the select representing what is probably the primary object
*
* We define this as the object closest to the horizontal center line of the view port. 
*
* We'll do this by calculating how close an object is to this line (0 being on top or overlapping). 
* 
* This will return the LAST object found that is also the closest AKA if two items overlapping, this wil return the second.
* 
**/
var elementPrimaryItemInViewBySelector = function (selector) {
    let currentClosest = null;
    let closestToCenterScore = 0;
    let pageHeight = (window.innerHeight || document.documentElement.clientHeight);
    let centerLine = pageHeight / 2;

    document.querySelectorAll(selector).forEach(function(object) {
        let bounding = object.getBoundingClientRect();

        //if it's the active article or not on screen we skip it
        if (!(bounding.right <= (window.innerWidth || document.documentElement.clientWidth) && bounding.left >= 0)
            || bounding.bottom < 0 || bounding.top > pageHeight) {
            return;
        }

        if (bounding.top < centerLine && bounding.bottom > centerLine) {
            score = 0;
        }
        else if (bounding.top > centerLine) {
            score = bounding.top - centerLine
        }
        else {
            score = centerLine - bounding.bottom
        }

        if (currentClosest == null || score <= closestToCenterScore) {
            currentClosest = object;
            closestToCenterScore = score;
        }
    });


    return currentClosest;
};


var fetchNextArticle = function() {
    let count = document.querySelectorAll('.article-post').length;
    let exclude= ""
    if (pageOriginalPath != '/') {
        //on an individual articles page the article won't be part of of the query our api runs
        //therefore the offset needs to exclude it
        count--;
        exclude = pageOriginalPath.replace(/\/$/, "").replace(/^\//, "");
    }

    fetch(`/fetchArticlesOffset/${count}/${exclude}`).then(response => {
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

//If an article is about half way up the view it's probably the one they're reading
//Mark it - need to detect scrolling up and down
var setActiveUrl = function() {
    let activeArticle = elementPrimaryItemInViewBySelector('.article-post');

    if (activeArticle == null)
        return;

    let title = activeArticle.querySelector('header a.title h1').innerHTML;
    let url = activeArticle.querySelector('header a.title').getAttribute('href');

    if (url != activeArticlePath && url == firstArticlePath) {
        window.history.replaceState({"path": pageOriginalPath,"title":pageOriginalTitle}, pageOriginalTitle, pageOriginalPath);
        activeArticlePath = url;
    }
    else if (url != activeArticlePath) {
        window.history.replaceState({"path": url,"title":title}, title, url);
        activeArticlePath = url;
    }
}

if (document.querySelectorAll('.homepage, .article').length) {
    window.addEventListener('scroll', function (event) {
        //check to see if we should lazy load another article
        if (!triggered && xPercentOfElementAboveViewportFold(newestLoaded, .5)) {
            //alert(newestLoaded.innerHTML);
            fetchNextArticle();
            triggered = true;
        }

        setActiveUrl()

    }, false);
}
