# Scrape imdb.com for top 1500 action titles based on US boxoffice

#import required libraries
from urllib.request import urlopen 
from bs4 import BeautifulSoup as Soup

#create a csv file to store data
filename = "imdb_action_1500.csv"
f = open(filename,"w")

#titles for the respective columns retrived
headers = "title,director,release,certificate,runtime,genre,rating,summary,gross\n"

f.write(headers)

#loop through the pages on the site
for i in range(1,1500,50):
	url = "https://www.imdb.com/search/title/?title_type=feature&genres=action&sort=boxoffice_gross_us,desc&start={}&explore=genres&ref_=adv_nxt".format(i)
	uClient = urlopen(url)
	page_html = uClient.read()
	uClient.close()

    #parse the retrived page data
	page_soup = Soup(page_html,"html.parser")
	containers = page_soup.findAll("div",{"class":"lister-item-content"})

    #retrive all the values from page
	for container in containers:
		title_container = container.findAll("h3",{"class":"lister-item-header"})
		title_c = title_container[0].a
		title = title_c.text

		year_c = container.findAll("span",{"class":"lister-item-year text-muted unbold"})
		release = year_c[0].text.replace('(','').replace(')','')
		try:
			certificate_c = container.findAll("span",{"class":"certificate"})
			certificate = certificate_c[0].text
		except:
			certificate = "NA"

		runtime_c = container.findAll("span",{"class":"runtime"})
		runtime = runtime_c[0].text

		genre_c = container.findAll("span",{"class":"genre"})
		genre = genre_c[0].text.strip()

		rating_c = container.findAll("div",{"class":"inline-block ratings-imdb-rating"})
		rating = rating_c[0].text.strip()

		summary_c = container.findAll("p",{"class":"text-muted"})
		summary = summary_c[1].text.strip()

		try:
			gross_c = container.findAll("span",{"name":"nv"})
			gross = gross_c[1].text
		except:
			gross = "NA"

		director_c = container.findAll("p",{"class":""})
		director_container = director_c[0].a
		director = director_container.text

		print("title: "+title)
		print("director: "+director)
		print("release: "+release)
		print("certificate: "+certificate)
		print("runtime: "+runtime)
		print("genre: "+genre)
		print("rating: "+rating)
		print("summary: "+summary)
		print("gross: "+gross)

        #write the retrived data to csv file
		f.write(title.replace(",","")+","+director.replace(",","")+","+release+","+certificate.replace(",","")+","+runtime + ","+genre.replace(",","")+","+rating+","+summary.replace(",","")+","+gross.replace(",","")+"\n")
		
f.close()





