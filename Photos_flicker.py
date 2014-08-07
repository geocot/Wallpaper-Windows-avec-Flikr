import flickr

flickr.API_KEY=""
flickr.API_SECRET= ""
photos = flickr.photos_search(text="lune")
flickr.Photo.getURL(photos[0])

#Get flicker photo
