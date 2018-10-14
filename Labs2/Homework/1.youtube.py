from youtube_dl import YoutubeDL

#Ex1
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

#Ex2
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#Ex3
options = {
    'format':'bestaudio/audio',
   }
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

#Ex4

options = {
    'default_search':'ytsearch',
    'max_downloads': 1,
}
dl = YoutubeDL(otions)
dl.download(['con dien TAMKA PKL'])

#Ex5
options = {
    'default_search':'ytsearch',
    'max_downloads': 1,
}
dl = YoutubeDL(options)
dl.download(['Nho mua Sai Gon Lam Truong'])

