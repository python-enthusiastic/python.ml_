import pyqrcode

# source path

link = "https://www.youtube.com/channel/UCOrJa9hT27ASrtX-X83Q11g"
# genrate QR code
url = pyqrcode.create(link)
# creating and save the file
url.svg("immutableyoutubeqr.svg",scale=8)

 # copyreg="_python.cs"_