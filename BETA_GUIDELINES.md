# Bento
Thanks for giving Bento a try.  
We would like you to follow these steps prior to the user interview.
 - Install Bento: ```pip3 install bento-cli``` 
 - Initialize Bento: ```bento init``` (please provide your email when prompted)
 - Run Bento: ```bento check```
 - Whitelist results: ```bento archive```
 - Disable unwanted rules: ```bento disable r2c.eslint arrow-parens``` (this will disable the eslint arrow-parens rule)

## Notes
Bento doesn't do any style checking (whitespace, etc.) and also doesn't ship any code off of your machine. You can read more about our privacy policy [here](https://github.com/returntocorp/bento/PRICACY.md).


More detailed instructions can be found [here](https://github.com/returntocorp/bento).  

To initialize Bento, choose a Python or Javascript project that is managed by git (Bento understands git).  

During the initialization, when prompted, please enter the same email address you used for the interview so we can distinguish your session from other users.   

Once you ran ```bento check```, feel free to fix issues, ignore warnings, or disable specific checks (ex: ```bash bento disable r2c.eslint arrow-parens```). Just use Bento as many times as you'd like to use. 🤞

We are curious if you'll like the ```bento archive``` feature as much as we do. This command will add all current findings to the whitelist, by creating a .bento-whitelist.yml file. It provides a clean slate for your project, so you can keep coding. You can work through the imperfections in your project over time. 

## License
Copyright (c) [r2c](https://r2c.dev ).

![r2c logo](https://r2c.dev/r2c-logo-silhouette.png?gh)