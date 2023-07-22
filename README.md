# bots vs bots

To prevent r/Scotland being invaded by the 4chan botnet, we'll create our own botnet

# instaling

- install python
  - go to <https://www.python.org/downloads/release/python-3106/> and download python 3.10.6 at the bottom of the page
    - if you're feeling lucky go to <https://www.python.org/downloads/> and click the yellow button instead to download the latest version, it'll probably work just fine but i cant be arsed testing it and i know 3.10.6 works anyway
  - run the installer
- download this repo by clicking the \[<> Code ↓] dropdown in the top right of this page and click "Download ZIP"
  - then unpack it into your downloads folder or wherevr
  - if you have github desktop then use that instead
- open a terminal in the folder (probably called bots-vs-bots-main) by doing right click > open in terminal or whatevr
- in the terminal run `pip3 install -r requirements.txt` or `pip install -r requirements.txt` or `python -m pip install -r requirements.txt`, whichever one works first
  - if none of them work, uh idk good luck lmao

# configuringggn

1. rename config.example.json to config.json
   - its got some options in it that show where the file is stored and where the uh the artwrok is on the canvas
2. go into the file
3. go to where it says
	```json
	"workers": {
		"worker1username": {
			"password": "password",
			"start_coords": [5, 19]
		},
		"worker2username": {
			"password": "password",
			"start_coords": [0, 0]
		}
	}
	```
4. change worker1username to your reddit bot's username and change password to your reddit password
   - oh yea i forgot to say make a bot account or get one you had from ages ago
   - you can use your main reddit account password if you are crazy enough to trust anything i say, hey i'm just a text file
  - if you only got one bot account just remove the `"worker2username": { ... }` *ANd dont forget* to remove the comma at the end of the line before it
5. if you do have a bunch of accounts, duplicate the `"worker1username": { ... },` block until you have enough to match the number of bot accounts you have
	- i dont think itll work well if you have a lot of bots, changing `"using_tor": false,` to `"using_tor": true,` might fix it but it will slow the startup down to a crawl probably lmao
6. fuck around with start_coords, \[0, 0] is the top left pixel of the image, \[5, 19] is 5 pixels down 19 across, which is the top left corner of the 4chan invasion if you wanna specifically target that for now
   - remember the image has 4 pixels o transparent space on the left right and 5 pixels on da bottom, so \[4, 0] is the top left corner of the unicorn area
   - just set them to wherever u think is best✅✅you can set them differently for each bot

# how to, uh, how to run

idk mate im too tired for this shite

- `python main.py`
- or `python3 main.py`
- or failing that, open main.py in the IDLE (type it in the taskbar or apps bar or whatever until it comes up) then press f5
  - the console output will look fucked up if you have to do it this way dont worry bout that

# faq

Question can i run this with WSL  
Answer yes and it will probably work better

Question can i run this with Docker  
Answer fuck you

Question theres an error what do i do  
Answer i dont fecking know mate i amnt have the slightest clue

Question why is Python 3.10.6 the best version  
Answer i picked it at random (its the version i already had installed anyway and changing python versions is a pain in the arse)

Question can someone help me fix my fridge it's a Samsung RS27T5561SR  
Answer please turn it off and on again make sure to clean it througholry

Question can i run this with kubernetes  
Answer an icbm will impact your residence at 11:28 pm local time on September 18 2023


**THis concludes our q and a**


# see here

thanks to <https://github.com/WorldObservationLog/reddit-place-script-2023> for all of the code

