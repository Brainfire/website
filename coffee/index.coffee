Chirp = Chirp || {}

do ($=jQuery, chirp=Chirp) ->
  chirp.fetchTweets = (user,count,renderCallback) ->
    url = "http://search.twitter.com/search.json"
    searchParams = 
      q: "from:#{user}"
      rpp: count
      result_type: "mixed"
    
    $.ajax {
      url: url,
      type: "GET",
      data: searchParams,
      dataType: "jsonp",
      success: (search) ->
        renderCallback(search.results)
    }

$ =>
  Chirp.fetchTweets 'brainfirellc', 3, (tweets) =>
    for tweet in tweets
      do (tweet) ->
        DAY = 1000 * 60 * 60  * 24

        d1 = new Date(tweet.created_at)
        d2 = new Date

        days_passed = Math.round((d2.getTime() - d1.getTime()) / DAY)
        
        $('#tweet-list').append $("<dd class='tweet'><p>#{tweet.text}</p><p class='right'>#{days_passed} days ago</p></dd>")