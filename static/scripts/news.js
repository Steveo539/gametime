
function requestArticles(sources, keywords, pageSize)
{
	url =
		'https://newsapi.org/v2/top-headlines?' +
		'sources=' + sources + '&' +
		'q=' + keywords + '&' +
		'pageSize=' + pageSize + '&' +
		'apiKey=be707787636945f1ae6ce3f65a4e2a28';
		  
	request = new Request(url);
	fetch(request)
		.then(function(response){return response.json();})
		.then(function(data){renderArticles(data.articles);})
}

function renderArticles(articles)
{
	if (articles.length != 0) {
		document.getElementById('news').innerHTML += "<h3>News</h3>";
		for (i in articles)
		{
			renderArticle(articles[i]);
		}
	}
}

function renderArticle(article)
{
	if (article.title == null || article.description == null
			|| article.url == null || article.urlToImage == null)
	{
		return;
	}
	
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