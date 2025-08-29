
define e = Character("Eileen")
define a = Character("Lucy")
define u = Character("You")
define m = Character("Mother")
define i = Character("Recruiter")
define d = Character("David") 
define y = Character("Alice")


label start:

    play music "ciaconna theme.mp3"

    show eileen vhappy:
        xalign 0.0
        yalign 0.5

    "Welcome to your scam simulation, please pick the experience you want."

    menu:
        "Welcome to your scam simulation, please pick the experience you want."
        
        "Job scam":
            jump choice1_jobscam

        "Love scam":
            jump choice1_lovescam

        "Discount item scam":
            jump choice1_discountscam 

label choice1_jobscam:

    jump scenariojobscam

label choice1_lovescam:

    jump scenariolovescam

    e "random"

label choice1_discountscam:

    jump scenariodiscountscam

label scenariojobscam:

        hide eileen vhappy

        stop music

        "You are a fresh graduate after years of education, and you posted your resume on Jobstreet expecting some replies."

        "After a few days, you received a interview invitation from a company named {b}Bright Future Solutions{/b}"

        play music "sunflower-slow-drag.ogg" fadeout 1

        scene bg room d

        u "Finally a company contacted me!Seems like it's one that focuses on customer service."

        u "The salary is RM4500... And it includes dorms and even employee training, it gives so much than other companies."
    
        "You contacted the recruiter"

        show hayato calm

        i "Greetings, We received your resume on JobStreet, and we find that you are very fiiting for the job"

        menu:
            "Thanks for the compliment":
                i "We truly believe in your ability"
                   
            "Are you sure about that?":
                i "You're a funny one, continuing on"
                   
        u "Really? I actually do not have much work experience."

        show hayato calm arm raised

        i "That is not a problem. We welcome fresh graduates. The company provides full training, all you need is basic computer skills and English"

        u "Sounds good. May I ask where the job is located?"

        show hayato calm 

        i "Our headquarters is overseas. We mainly serve the Southeast Asian market. But do not worry, we will arrange transportation and a pre-departure briefing in Kuala Lumpur"

        menu:
            "Overseas? This is a major business huh?":

                show hayato calm arm raised

                i "Of course! Only fitting for someone of your caliber."

            "Overseas? Guess that means I'm earning big!":

                show hayato calm arm raised

                i "Please be assured that you will be compensated properly for your efforts."
        
        u "But still, I did not expect it to be an international job."

        show hayato calm

        i "Yes, our company is quite large. The salary and benefits are much better than local firms. Housing in serviced apartments is very comfortable"

        u "I see. Do I need to attend an interview?"

        i "Of course. We will conduct an online interview through Zoom. You can join whenever you are ready."

        "After a lengthy interview..."

        hide hayato calm

        u "*Thinking* Wow, the questions were pretty professional. They even asked me for a lot of personal information. It felt very legitimate."

        show hayato calm

        i "Congratulations, you've passed the interview! We'll send you the offer letter soon."

        menu:
            "Really? That's amazing!":
                i "You abilities made this an easy decision."
            
            "Wow, That was really quick.":
                i "We would not want to miss someone as skillful as you."

        show hayato calm arm raised

        i "Be assured, There's not much you need to prepare. Just bring your passport. The company will handle your flight ticket and accommodation."

        u "That sounds really convenient... but are you sure I don't need to report to the office first?"

        i "No need. Everything is arranged in batches. You'll just depart together with other new hires"

        menu:
            "New hires? I thought I was the only one":

                show hayato calm 

                i "We are an international company, we always need more recruits"

            "How many others are there?":

                show hayato calm
               
                i "That much is confidential, I cannot reveal that to you."

        u "Why do I have to fly abroad so quickly? I've never even seen the company office...(Thinking)"

        i "Don't worry. We've been working with JobStreet for years. All our job postings are from legitimate channels."

        u "(Hesitant) Should I take this opportunity or not...?"

        hide hayato calm

        menu:
            "Pick your choice"
        
            "Believe in the job offer":
                jump badending1

            "Fact check the company":
                jump goodending1

            "Ask for other's opinion":
                jump neutralending1

label badending1:

    u "Great! I finally found my ideal job!"

    show eileen concerned

    e "Are you sure it's safe? Why do you not need to report to the company first?"

    menu:

        "It'll be fine I'm sure":

            u "Don't worry, it's a posting from a legitimate website, so it should be fine"
            
    e "If you're sure..."

    scene bg airports
    
    "(A few days later, You received a flight ticket and instructions, preparing to depart.)"

    "You chose to believe, unaware that you were walking right into a trap."

    scene bg kkplace

    play music "tower_clock.ogg" fadeout 1.0

    "You fell for the scam, and will now be forced to work for their organisation for a long while. {b}BAD ENDING {/b}"

    "Press again to return to the main menu"

    return 

label goodending1:

    u "It sounds pretty good, But I have to confirm the details again"

    "You looked up the name of the company, and find out that there were news reports pointing out that it was a scam company"

    show company

    u "Thankfully I checked beforehand, I almost got scammed!"

    hide company

    show eileen happy

    e "Nice work, we have to be more careful when facing these lucrative job offers next time!"

    "With calm reasoning and fact-checking, You successfully avoided becoming another victim in the scam. {b}GOOD ENDING {/b}"

    "Press again to return to the main menu"

    return

label neutralending1:
   
    u "Let me ask my parent's opinion first"
    
    m "Overseas work? Sounds dangerous, it's best if you consider this carefully before deciding"

    u "Hmmm... That is true, let me look for local jobs first."
    
    "You decided to put this \"opportunity\"on the side, you didn't get scammed, but also loss a chance to warn yourself and others {b}NEUTRAL ENDING {/b}" 

    "Press again to return to the main menu"
    
    return 

label scenariolovescam:

    hide eileen vhappy

    stop music

    "Xin Hui meets David, a foreign engineer, on a dating app. At first, they chat casually, but over time their relationship grows closer. Eventually, the scammer uses the excuse of investment funds being stuck to ask her for money"

    "Two months after they first messaged..."

    play music "hard as life.mp3"

    show bg office
    
    show male_neutral 
    
    play audio "discord_sound_effect.mp3" 

    d "Hi Xin Hui, It's me David, nice to see you online again."

    u "Hello! I was expecting you to come online at this time as well."

    show male_happy

    d "Ya, I'm usually busy with work, so I don't have many other times I can be on here."

    u "Haha, so is an engineer's life always boring?"

    hide male_happy

    show male_smile

    d "You could say that. It's either the construction site or the office every day."

    u "if so, why did you decide to talk to me at first?"

    hide male_smile
    
    show male_blush

    d "I saw in your profile that you enjoy reading and coffee the same as me. I thought it would be nice to get to know you."

    u "Oh, so you like those too."

    hide male_blush

    show male_smile

    d "Yes, especially coffee. I often go alone, but I really wish I had someone to join me."

    u "Haha, me too. I often sit in cafes alone for hours."

    hide male_smile

    show male_confused

    d "Xin Hui, you're often online at night. Do you work late like I do?"

    u "Haha, yeah. I've had a lot of projects lately, so I usually work until pretty late."

    hide male_confused

    show male_smile

    d "Then we're in the same boat. My engineering projects are exhausting deadlines every day."

    u "Sounds tough. What do you usually do after work?"

    hide male_smile

    show male_sad 

    d "Mostly just go back to my place, grab a quick meal. I don't have many friends here"

    u "No wonder you came to a dating app."

    hide male_sad

    show male_happy

    d "Exactly. Meeting you is a nice change, it feels good having someone to talk to."

    u "You're actually quite talkative. I kind of enjoy chatting like this too."

    d "Thanks. Without you, I'd probably just be staring at my laptop every night."

    u "Haha, that sounds like an exaggeration."

    hide male_happy

    show male_blush

    d "It's not. I really think you're special."

    u "Special? How so?"

    hide male_blush

    show male_smile

    d "You speak with honesty, not like some people who just reply casually. I really value that."

    u "You sound quite serious."

    hide male_smile

    show male_happy 

    d "I am. I've always hoped to meet someone I can truly walk through life with."

    u "Aren't you moving too fast? We've only just met not too long ago."

    hide male_happy

    show male_blush

    d "Maybe it's because my work life is so monotonous. I really look forward to having someone in my life."

    u "Hmm... I get that."

    hide male_blush

    show male_smile

    d "I'm planning to visit Malaysia soon. If all goes well, I'd love to meet you in person."

    u "Really? That sounds a bit sudden."

    hide male_smile

    show male_neutral 

    d "Yes, it was already in my plans. But something came up recently."

    u "What happened?"

    hide male_neutral

    show male_cry

    d "A friend introduced me to an investment opportunity. I put some money in, but now the funds are stuck with bank procedures. It's delaying my trip to Malaysia."

    u "Wow... that sounds complicated."

    show male_confused

    d "It is a little troublesome. If I can just cover the shortfall quickly, I'll be able to come see you sooner."

    u "So... what are you going to do?"

    show male_neutral

    d "Honestly, I didn't expect to share this with you. But I really want to meet you as soon as possible. Could you help me out a little? I'll pay you back the moment I arrive."

    u "......"

    stop music fadeout 1.0

    hide male_neutral

    show bg pure black

    menu:
        "Pick your choice"
        
        "Transfer the Money":
            jump badending2

        "Expose the scam":
            jump goodending2

        "Block the person hesitantly":
            jump neutralending2

label badending2:

    show bg office

    show male_neutral 
     
    u "Alright, I'll transfer some money to help you. I hope you really mean what you say."

    show male_evil

    d "Thank you, Xin Hui. You're really so kind."

    show bg pure black

    show transaction

    "Xin Hui makes the transfer and waits for a reply."

    "A few days later"

    u "David, when will you come? I've already sent you the money."

    "A few days later, David's account disappears, and his profile picture turns grey."
    
    u "...Did he block me?"

    "Xin Hui lost her savings, and also her trust. The romance scam succeeded once again. {b}BAD ENDING{/b}"

    return

label goodending2:

    show bg office

    show male_neutral

    u "Wait, this sounds suspicious. Didn't you say you had a stable job? How could you be short of money?"

    show male_cry

    d "It's just a temporary issue, why can't you believe me?"

    u "A real friend wouldn't ask me for money, especially someone I just met."

    show male_angry

    d "...Are you doubting me?"

    u "It's no doubt that I know you're scamming me. I'm going to report to you."

    show male_disgust

    play sound "discord-leave-noise.mp3"

    hide male male_disgust

    show bg pure black

    "(David's account vanishes instantly.)"

    "Xin Hui realized the scam in time and avoided financial loss. {b}GOOD ENDING{/b}" 

    return

label neutralending2:

    show male_neutral

    show bg office

    u "I think we'd better stop talking"

    show male_surprised

    d "Xin Hui, you've misunderstood me, I really just need a little help!"

    u "Sorry, I don't want to get involved in this kind of thing."

    show bg pure black 

    hide male_surpised

    show yippie

    "(Xin Hui opens the settings and blocks him.)"
   
    "Though Xin Hui still felt uncertain, she chose to protect herself. {b}NEUTRAL ENDING{/b}"

    return 

label scenariodiscountscam:

    hide eileen vhappy

    stop music

    "You had just graduated and wanted to buy a new smartphone. While scrolling on Instagram, you came across an ad from a page called Gadget Store. The page looked professional, with thousands of followers and many customer unboxing photos."

    "Everything seemed trustworthy and legitimate."

    play music "from the start.mp3"

    show bg room a

    u "Wow, an iPhone 14 Pro for only RM1999? That's half the market price."

    show alice_happy

    y "Hello~ We're Gadget Store. It's our anniversary sale, a limited-time offer!"

    u "Really? Isn't one at least RM3999 right now?"

    hide alice_happy

    show alice_default

    y "Because we get our stock directly from the factory, with no middlemen. That's why our prices are much lower."

    u "So how do I purchase it? Do I order through Shopee?"

    y "Shopee charges higher fees. Ordering directly on IG is faster, plus you'll get a free warranty card"

    u "I see your account has a few thousand followers."

    hide alice_default

    show alice_happy

    y "Yes, and you can also check our customer reviews and unboxing videos."

    menu:
        "Wow, that's alot of photos":
            y "See, we are trustworthy~"

        "I've seen that video somewhere...":
            y "Really? I guess you must've scrolled upon us at some point."

    u "Can I do cash on delivery? I'm worried bank transfer might be risky."

    hide alice_happy

    show alice_worried

    y "Sorry, new customers must pay in advance. But don't worry, we have a solid reputation, and all our products are genuine."

    u "How long will it take to receive the phone?"

    hide alice_worried

    show alice_default

    y "We ship within 3 days after payment, and you'll receive it within 7 days"

    menu:
        "Does it come with a warranty?":

            y " Yes, we'll provide an e-warranty card with one year coverage"

        "Seems weirdly efficient...":

            hide alice_default

            show alice_doubt

            y "We've been trusted sellers for years, of course we have efficiency."

    show alice_default

    u "Sounds pretty good… should I give it a try?"

    hide alice_default

    show alice_happy

    y "Only 2 units left in stock! If you want one, it's best to transfer today!"

    u "So fast? Already almost sold out?"

    hide alice_happy

    show alice_default

    y "Yes, iPhones are always in high demand. Many customers are waiting"

    u "(Inner Thoughts) Ugh, I'm torn… but the price is really tempting…"

    show bg pure black 

    stop music fadeout 1.0
    menu:
        "Pick your choice"
        
        "Transfer Immediately":
            jump badending3

        "Double-Check Seller Information":
            jump goodending3

        "Insist on Self-Pickup":
            jump neutralending3
             

label badending3:

    show bg room a

    u "Alright, I'll just transfer first since I'm going to buy it anyway!"

    hide alice_default

    show alice_embarrassed

    y "Thank you for your purchase!"

    hide alice_embarrassed
    
    show bg pure black

    show transaction2

    "(After transferring, the seller left your messages on “read” and the next day, the account disappeared completely.)"

    u "Oh no! I've been scammed..."

    "Because of chasing a bargain, You lost RM1999. {b}BAD ENDING{/B}"

    return

label goodending3:

    show bg room a

    hide alice_default

    show complains

    "(You looked up the store's name on Google and found many complaints on forums and Facebook about this IG seller being a scam.)"

    u "Luckily I checked first! I almost got scammed."

    hide complains

    show eileen happy

    e "See? These days, you really have to fact-check before shopping online!"

    show bg pure black

    "Through fact-checking, You avoided financial loss. {b}GOOD ENDING{/b}"  

    return

label neutralending3:

    show bg room a

    u "I'm in KL, can I pick it up directly from your store?"

    hide alice_default

    show alice_doubt

    y "Sorry, we only have a warehouse, not open to the public."

    u "No physical shop? That feels suspicious… better not."

    hide alice_doubt

    show bg pure black

    "Although Ah Jie didn't get the phone, he trusted his instincts and avoided being scammed. {b}NEUTRAL ENDING{/b}"

    return

    


   