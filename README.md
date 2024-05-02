# SEO Topic Cluster Creation
This is my process for creating content clusters, topical maps, whatever you want to call them. Ultimately this is how I plan content. 

[See More Of My SEO Work](https://rkseo.xyz)

## Context
As of the last few years, the idea of topical authority has been playing a larger role in SEO as time goes on. As a result, having a quality system for creating a topical map or clustering keywords became a pressing need in my day to day. 

As I thought about the best way to cluster lists of keywords, I thought about all sorts of crazy ideas before I realized the answer was under my nose. 

"The answer is always on the first page of Google" - Kyle Roof 
	(or Matt Diggity... I'm not going to lie as I write this I have no idea which one said that. So my apologies to whoever it was....)

Any one page will rank for a variety of keywords. So if we can take a list of keywords and scrape the first result, and use the URL to group keywords, Google is effectively mapping out clusters of content for us. From there we can make more refined groups that can be targeted with a single page, and use that to create maps or silo structures within a topic. 
## Process Overview
1. Create Your List Of Keywords: Take a primary topic, let's say it's coffee. Use that as your seed keyword and cast a relatively wide net, gathering as may keywords as you want, digging into sub-topics of coffee as well (such as brewing methods, beans, roasting, etc.)
2. Scrape Results: For all of these keywords, scrape the 1st result from Google via their API or *other potentially frowned upon methods.*
3. Sort Results: Group this output by URL
4. Organize Results: Manually pull keywords into lists underneath a potential article or page. Sort all the keywords into these groupings. 
5. Create Silos: Once you've got a list of articles, create a silo with whatever parameters you'd like. 
## Strategy and Implementation

### Gathering Your List of Keywords
The first step is simply gathering a large list of keywords that you want to analyze. In this step you can cast a fairly wide net as it's pretty easy to exclude irrelevant keywords at a later step. It saves you some time to not worry about picking through specific keywords at this point of the process. 

It's really as simple as taking your seed keyword and putting it into your keyword research tool of choice with some select filters, and exporting the full list. 

In order to narrow down the list I'd recommend filtering out the following low hanging fruit. Below are my parameters that I use in Semrush, but this is likely applicable to most if not all other KW research tools. 
- Monthly Search Volume > 0
- Language: English
- Broad Match (sometimes nice but sometimes includes too many irrelevant keywords)

Additionally you can look to exclude keywords that are common occurrences in the results, that you know you won't want to target. In the instance of coffee, maybe you don't want to target keywords discussing coffee shops for example. Therefore you can exclude instances including "shop". I typically just skim through a few pages and see what I can get filtered out easily.  

From here we can niche down into sub topics or related keywords. In our coffee example, maybe we want to also go with keywords related to V60, Aeropress, or other brewing devices. Think of other terms that are interchangeable or closely related to the keyword, but don't have your actual seed keyword in it. 

If you want to take it further can go after the 0 MSV terms, and even go scrape PAA Questions and drill down into related keywords. This is what I'd do if I'm making a *truly comprehensive and exhaustive* topic map. That being said,  at least for the first attack on a cluster I personally don't feel it's worth it and opt to enact Pareto's Principle as my defense here. But do as you wish.

Some additional sources of keywords / phrases: 
- Google related searches, out a few tiers potentially. 
- Google PAA questions
- Answer The Public
- Bing, Yahoo, and other search engines related searches if you really want to go that deep
### Scrape Results
This is where the theory of "Google has already grouped these for you" comes in. If you can scrape the search results for each keyword here, by grouping keywords with the same page ranking 1st you've got preliminary clusters of keywords. 

The recommended and truly noble way to do this is with the [Google Search API](https://developers.google.com/custom-search/v1/overview) (or another SERP API / tool). However I'm not going to lie when you do things at scale it can get pricy and you can still run into limits. 

As an alternative there's a more grey hat option I don't technically endorse - and that's just scraping the results yourself. Google doesn't want you scraping their results and it's [technically against their TOS](https://medium.com/@sachin.kumarr9904/the-legality-of-google-scraping-and-google-news-api-what-you-need-to-know-20c0d5b93bbc). That being said [Bing did it in 2011.](https://searchengineland.com/google-bing-is-cheating-copying-our-search-results-62914). So do with that information what you will. 

I've put together an *educational purposes* scraper that does just this. Imperfectly might I add as sometimes you've got to run keywords multiple times. But it'll get the job done. 

[Google 1st Result Scraper]()
### Sorting and Organizing Your Keyword and URL Results
This step is the most hands on and where you start to actually build your cluster. Once you've got all your keywords and results, you can make a simple count function in excel to see how many times a URL is appearing in your list. Then sort columns in this order: Count high to low, URL alphabetical, MSV high to low. 
![[Pasted image 20240111142746.png]]

This sorts so that the pages responsible for the most of the keywords are at the top of your page, and so that within each page keywords are sorted high to low. The URL alphabetical sort then means that if two pages have the same number of ranking keywords in the list, you'll still keep those pages separate. 

Then you can begin going through your list one page at a time. I will pull all the keywords from a group into a new tab, and basically give them a label for what page or type of content I aim to write to target that group of words. As you go down your list, it is very easy to identify groupings of keywords that may not be relevant to your topic based on what page is ranking for that term. 

You'll also likely find that as you go down the list, you'll take smaller groups and combine them due to search intent and nature of the article being similar enough to combine onto a single page. 

This is where the 'art' of SEO comes into play a bit. I'm just aiming to generally group these to the best of my ability on the first pass. I will then keep this full list with their articles and set up a simple formula where I can dump in some google search console data to check their rankings. 

And then from there once I've gone through the entire list, you can cluster your new list of articles in to silos with primary keywords. 

This keyword database is a nifty way to figure out if a keyword needs a separate page to rank on it. IF you have 10 keywords, and 9 of them all rank somewhere in the top 20, but 1 keyword sits outside the top 50, that's essentially google telling you that keyword isn't relevant enough to that page.  

### Creating Silos
From here you've got a list of articles that you'll want to write. At this point I like to organize them into a silo structure and assign them a primary keyword. 

I organize my internal linking and silo structure according to Kyle Roof's silo structure at least to start. As for the primary keyword, I assign this based on my website's current keyword volume authority tier. This is based on my implementation of the Avalanche Technique (but I haven't put together my repository on that yet so check back later or shoot me a message).

And bingo, you've got a pretty robust cluster built out. 

#### Results and Insights
- Example Spreadsheet With All Steps of the Process
#### Resources Mentioned / Used
- Google Search API
- Google Result Scraper
- Semrush
- Kyle Roof & Matt Diggity






