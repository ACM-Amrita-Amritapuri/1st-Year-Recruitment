<p align="center">
<!-- 
<a href="https://aseam.acm.org/">
    <img src="" alt="Logo" width=30%>
  </a>
-->
  <h1 align="center">SIG Cyber</h1>
</p>

* Cybersecurity, often referred to as information security, is the practice of protecting computer systems, networks, data, and digital assets from unauthorized access, attacks, damage, or theft.
* The followinng task sets will help you to get your basic skill set to be in our world.
* If you face any difficulty you can ask your doubts in discord.

#### How to submit what you have done

* Create a folder for each task in the GitHub Repository you have created([refer](../README.md#creating-your-submission-repo)), i.e, Cyber Task 2 and Cyber Task 3.
* Create a word document, pdf or markdown file on how you did each level/tasks.
* Format for the document is given [here](./Format.pdf).
* You can add screenshots too.

## Cyber Task 0 - Installing a Linux System

**Objective:** The objective of this task is to set up a Linux environment using any one of the three methods: dual booting alongside an existing operating system, creating a virtual machine, or installing Windows Subsystem for Linux (WSL) on a Windows machine.

The **safest way** is to use virtual machine.

**NOTE:** This task can be skipped is you are using a MAC.

### **Method 1: Dual Boot Installation**

**NOTE:** Only do dual boot if you have Windows 10 Home or Windows 11 Home

1. Choose a Linux distribution ( I would say go for [Ubuntu](https://ubuntu.com/download/desktop) as it is easy to use ).
2. Prepare a bootable USB drive with the chosen Linux distribution using a tool like [Rufus](https://rufus.ie/en/)
3. Boot your computer from the USB drive and follow the installation wizard.
4. During installation, choose the option to install Linux alongside your existing operating system.
5. Configure partitioning, timezone, keyboard layout, and user account details.
6. Complete the installation process and reboot your computer.
7. Now we are ready to go.

**FOR HELP you can refer [here](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/), or refer youtube. **

### **Method 2: Virtual Machine Installation**

1. Download and install a virtualization software such as [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Download the ISO image of your chosen Linux distribution ( I would say go for [Ubuntu](https://ubuntu.com/download/desktop) as it is easy to use ).
3. Create a new virtual machine and configure settings such as memory, storage, and networking.
4. Install Linux on the virtual machine using the downloaded ISO image.
5. Follow the installation steps, configure settings, and set up user accounts.
6. After install we are ready to go.

FOR HELP you can refer [here](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview), or refer youtube.

### **Method 3: Windows Subsystem for Linux (WSL) Installation**

1. Ensure you have Windows 10 or later with WSL support.
2. Open command prompt and run the command to enable WSL: `wsl --install`.
3. Visit the Microsoft Store and search for your desired Linux distribution (e.g., Ubuntu).
4. Install the Linux distribution from the Store.
5. Launch the installed distribution, set up a user account.
6. Now we are ready to go.

FOR HELP you can refer [here](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview), or refer youtube.

## Cyber Task 1 - Learn how to use the Linux Terminal.

Learning how to use the Linux terminal is an essential skill for anyone working with Linux systems. The terminal, also known as the command-line interface (CLI), allows you to interact with the operating system using text-based commands.

Here is a [tutorial](https://ubuntu.com/tutorials/command-line-for-beginners), or just watch youtube.

Here is a [cheet sheet](./Linux.pdf) for you.

## Cyber Task 2 - Bandit (Levels 0 to 10)

The Bandit challenge is designed to help individuals learn and practice Linux command-line skills, basic security concepts, and ethical hacking techniques. The challenge consists of multiple levels, each with its own set of tasks and puzzles that need to be solved using the terminal.

There are up to 34 levels, if you want to explore a bit more you can continue playing.

**Getting Started with Bandit:**

1. **Access the Challenge:** Visit the Bandit challenge page on the OverTheWire website: [Bandit](https://overthewire.org/wargames/bandit/)
2. **Connect to the Server:** The challenge is hosted on a remote server. You can connect to it using SSH (Secure Shell). For example, to connect to Level 0, you would use the following command:

   ```bash
   ssh bandit0@bandit.labs.overthewire.org -p 2220
   ```

   The `-p 2220` specifies the port number to connect to.
3. **Play the Game:** Each level has a specific task or puzzle to solve. You'll need to navigate through directories, read files, and use your Linux command-line skills to find the solution. The solution often involves finding a password for the next level.
4. **Level Up:** After solving a level, you'll typically gain access to the password for the next level. Use this password to log in to the next level's server.
5. **Learn as You Go:** The challenges gradually introduce new concepts and techniques, allowing you to learn and practice as you progress.

**Tips for Success:**

* Read the challenge instructions and hints carefully.
* Experiment with Linux commands and concepts to solve the tasks.
* Don't hesitate to search online for explanations of commands or concepts you're unfamiliar with.
* Keep track of your progress and passwords as you move through the levels.
* Take your time to understand each level before moving on to the next one.

The Bandit challenge is a great way to develop practical Linux command-line skills and gain a basic understanding of cybersecurity concepts. It's suitable for beginners and provides a hands-on learning experience in a controlled environment.

## Cyber Task 3 - Natas (Levels 0 to 10)

"Natas" is another beginner-friendly Capture The Flag (CTF) challenge created by OverTheWire. Similar to the Bandit challenge, Natas focuses on teaching web application security concepts and ethical hacking techniques. The challenge consists of multiple levels, each with its own set of web-based tasks and puzzles that need to be solved by exploiting vulnerabilities in the web application.

There are up to 34 levels, if you want to explore a bit more you can continue playing.

**Getting Started with Natas:**

1. **Access the Challenge:** Visit the Natas challenge page on the OverTheWire website: [Natas](https://overthewire.org/wargames/natas/)
2. **Connect to the Server:** The challenge is web-based, so you'll need a web browser to access and interact with the levels.
3. **Play the Game:** Each level provides a web page with a specific task or puzzle. To solve each level, you'll need to find vulnerabilities in the web application and exploit them to retrieve sensitive information, access restricted areas, or accomplish other objectives.
4. **Level Up:** After solving a level, you'll typically gain access to the password for the next level. Use this password to move on to the next level.
5. **Learn as You Go:** The challenges progressively introduce more complex web security concepts. You'll learn about common vulnerabilities such as SQL injection, cross-site scripting (XSS), and more.

**Tips for Success:**

* Carefully read the challenge instructions and hints.
* Experiment with the web application's functionality and input fields to identify potential vulnerabilities.
* Research web security concepts and techniques to understand how to exploit common vulnerabilities.
* Keep track of the information you discover and the actions you take to solve each level.
* Approach each challenge with a curious and investigative mindset.

"Natas" offers an interactive and educational way to learn about web security and penetration testing. By solving the challenges, you'll gain hands-on experience in identifying and exploiting vulnerabilities commonly found in web applications. It's a valuable resource for individuals interested in entering the field of cybersecurity.

## Cyber Optional Tasks

Create an acount in [PicoCTF](https://picoctf.org/).

Go to [CLassroom](https://play.picoctf.org/classrooms) and join with invite code ```C87QwQUxl```.

### Cryptography Task Set :

**Learn**

* Learn basic conversions starting from Base-64, Hex etc.
* Use Caesar Cipher and ROT Cipher

**Implement**

* Mod 26 ([pico gym](https://play.picoctf.org/practice/challenge/144))
* Mind your P’s and Q’s ([pico gym](https://play.picoctf.org/practice/challenge/162))
* Wave a flag ([pico gym](https://play.picoctf.org/practice/challenge/170))
* Nice netcat ([pico gym](https://play.picoctf.org/practice/challenge/156))

### Forensics Task Set :

**Learn**

* Learn and use [forensically](https://29a.ch/photo-forensics/#forensic-magnifier) beta tool
* Learn more about binwalk, strings and exif-tool in terminal

**Implementation**

* Information ([pico gym](https://play.picoctf.org/practice/challenge/186))
* Matryoshka doll ([pico gym](https://play.picoctf.org/practice/challenge/129?category=4&page=1))

### Reversing Task Set :

**Learn**

* Learn about stack and go through all its basic functionalities
* Learn about basics to c programming and implement following programs:

1. Swapping two numbers using functions
2. Menu driven calculator using functions

* Get to know about x86 assembly language

**Implement**

* Transformation([pico gym](https://play.picoctf.org/practice/challenge/104?category=3&page=1))

