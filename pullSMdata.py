import urllib

def get_insta_followers(username):
	url = "http://www.instagram.com/"+username+"/"
	f = urllib.urlopen(url)
	html_text = f.read()

	followers = html_text.find(" followers")
	area = html_text[(followers-50):followers]
	closeTag = area.find("</span>")
	openTag = area.find('">', (closeTag-10), closeTag) + 2
	followerNum = area[openTag:closeTag]
	followerNum = int(followerNum.translate(None, ','))

	return followerNum