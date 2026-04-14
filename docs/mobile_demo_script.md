## Mobile Demo script:

### Intro:
Hello, my name is Christian Hernandez and this is a demo video for the functionality of our JagBot on mobile platforms. For this video, I'll be using my Galaxy S24 to test the website. This test is just to determine if the frontend we have set up can work well on mobile devices. Apologies if the audio quality is not very good, like I said I'll be recording from my phone. Also, in the interest of not doxing my IP address, the top of the screen will be cropped out.

### How I got it running:
To be able to access the webpage from my phone, I first cloned the repo into my IDE, then went through the steps for starting the API server on the ReadME. Once the API server is up and able to receive and send responses, we can move on to setting up the frontend. We'll follow its instructions up until it gives us the npm command to start the server. The command used to start the server is normally "npm run dev", but for mobile testing we'll be using "npm run dev -- --host". The "--" after npm will pass the "--host" argument to VITE, which will operate the server on my house's wi-fi network instead of just the local host. If I didn't do this, I wouldn't be able to access the JagBot page from my phone. This also changes the URL that'll be typed in to connect to the server, but that contains my IP and, like I said, I don't wanna dox myself. 

### Runnin the test:
Now, time to move on to the actual demonstration. For this demo, I'm gonna be asking three questions covering three different categories of information. The first will be a question about advising, the second will be a question related to services on campus, and the third will be a question designed to be refused. For the first question, we'll ask, "How many credit hours are required to graduate with a bachelor's degree?" --Say something about the response--. Our second question will be, "What mental health services are available through the school?". --Note about response--. And our final question, designed to be refused, is "What is the dean's favorite menu item from Chick-fil-A?" And as we can see, it doesn't know how to answer that.

---

## Backup Questions

1. What is the minimum GPA required to stay outside of academic probation?

category - Advising

2. Who should I talk to about any financial aid questions?

category - Services provided

3. Where is the nearest Whataburger to campus?

category - Failure
