# Scrape imdb.com for top 1500 action titles based on US boxoffice

#import required libraries
from urllib.request import urlopen 
from bs4 import BeautifulSoup as Soup

#create a csv file to store data
filename = "imdb_action_data.csv"
f = open(filename,"w")

#titles for the respective columns retrived
headers = "Title,Directors and Actors,Release,Certificate,Runtime,Genre,Rating,Metascore,Summary,Gross\n"

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
		try:
			title_container = container.findAll("h3",{"class":"lister-item-header"})
			title_c = title_container[0].a
			title = title_c.text
		except:
			title = "NA"

		try:
			year_c = container.findAll("span",{"class":"lister-item-year text-muted unbold"})
			release = year_c[0].text.replace('(','').replace(')','')
		except:
			release = "NA"

		try:
			certificate_c = container.findAll("span",{"class":"certificate"})
			certificate = certificate_c[0].text
		except:
			certificate = "NA"

		try:
			runtime_c = container.findAll("span",{"class":"runtime"})
			runtime = runtime_c[0].text
		except:
			runtime = "NA"

		try:
			genre_c = container.findAll("span",{"class":"genre"})
			genre = genre_c[0].text.strip()
		except:
			genre = "NA"

		try:	
			rating_c = container.findAll("div",{"class":"inline-block ratings-imdb-rating"})
			rating = rating_c[0].text.strip()
		except:
			rating = "NA"

		try:	
			rating_m = container.findAll("div",{"class":"inline-block ratings-metascore"})
			Metascore = rating_m[0].span.text
		except:
			Metascore = "NA"

		try:
			summary_c = container.findAll("p",{"class":"text-muted"})
			summary = summary_c[1].text.strip()
		except:
			summary = "NA"
		
		try:
			gross_c = container.findAll("span",{"name":"nv"})
			gross = gross_c[1].text
		except:
			gross = "NA"

		try:
			director_c = container.findAll("p",{"class":""})
			director_container = director_c[0]
			dir_act = director_container.text.replace('\n','-')
		except:
			dir_act = "NA"

		print("title: "+title)
		print("Directors and Actors: "+dir_act)
		print("release: "+release)
		print("certificate: "+certificate)
		print("runtime: "+runtime)
		print("genre: "+genre)
		print("rating: "+rating)
		print("Metascore: "+Metascore)
		print("summary: "+summary)
		print("gross: "+gross)

        #write the retrived data to csv file
		f.write(title.replace(",","")+","+dir_act.replace(",","")+","+release+","+certificate.replace(",","")+","+runtime + ","+genre.replace(",","")+","+rating+","+Metascore+","+summary.replace(",","")+","+gross.replace(",","")+"\n")
		
f.close()





