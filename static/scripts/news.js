
var url = 'https://newsapi.org/v2/top-headlines?' +
          'sources=bbc-sport&' +
		  'pageSize=5&' +
          'apiKey=be707787636945f1ae6ce3f65a4e2a28';
		  
var request = new Request(url);
fetch(request)
	.then(function(response){return response.json();})
	.then(function(data){renderArticles(data.articles);})

function renderArticles(articles)
{
	renderArticle(articles[0]);
	renderArticle(articles[1]);
	renderArticle(articles[2]);
	renderArticle(articles[3]);
	renderArticle(articles[4]);
}

function renderArticle(article)
{
	document.getElementById('news').innerHTML +=
	'<div>' +
		'<a href="' + article.url + '">' +
			'<img src ="' + article.urlToImage + '"/>' +
		'</a>' +
		'<a href="' + article.url + '">' +
			'<h1>' + article.title + '</h1>' +
		'</a>' +
		'<p>' + article.description + '</p>'+
	'</div>'
}