# Copy for 50 Dynamo AI posts. Facts only: ₹4/min, 24×7, first ring, Hindi, English and regional
# languages, WhatsApp follow-up, team alert, transfer to a person, recording + summary, sheet/CRM,
# outbound call-back within a minute, setup + testing by the team, new number, login with
# transcripts/recordings, 10-min free trial, 2,000-min minimum, 10% extra minutes on 2,000+.
# Headline: text after "|" goes on a new line in the accent style.

POSTS = [
# ---------- 1. STATEMENT ----------
dict(t="statement", th="grad", h="Missed call =|missed customer.",
     sub="Dynamo AI picks up every call on the first ring, 24×7."),
dict(t="statement", th="navy", h="Your best salesperson|shouldn't be on hold.",
     sub="Let Dynamo AI take the first call, note what the customer wants and pass the ready ones to your team."),
dict(t="statement", th="light", h="The lead from your ad called.|Who picked up?",
     sub="Dynamo AI answers in Hindi, English and regional languages, and saves every detail."),
dict(t="statement", th="grad", h="Ads bring calls.|Who answers them?",
     sub="You pay for every click. Make sure every call gets a reply. ₹4 per minute."),
dict(t="statement", th="navy", h="Sunday is a holiday.|Not for your phone.",
     sub="Dynamo AI answers on Sundays, festivals and late nights, when your team is off."),

# ---------- 2. NOTIFICATIONS ----------
dict(t="notif", th="grad", h="Site visit booked|at 11:20 PM.", tag="Real estate",
     cards=[("phone","Dynamo AI answered","Incoming call · English","11:18 PM"),
            ("note","Call summary saved","2BHK enquiry. Wants a site visit on Sunday.","11:20 PM"),
            ("bell","Team alert sent","Lead shared on your team's WhatsApp","11:20 PM")]),
dict(t="notif", th="light", h="Appointment request|before you open.", tag="Clinics",
     cards=[("phone","Dynamo AI answered","Incoming call · Hindi","7:05 AM"),
            ("note","Request saved","Wants an evening slot with the doctor","7:06 AM"),
            ("bell","Front desk alerted","Your staff confirms the slot","7:06 AM")]),
dict(t="notif", th="navy", h="Admission enquiry|during class hours.", tag="Coaching",
     cards=[("phone","Dynamo AI answered","Incoming call · Hindi","11:40 AM"),
            ("note","Call summary saved","Class 11 science batch. Asked about fees.","11:43 AM"),
            ("chat","WhatsApp follow-up sent","Batch details shared with the parent","11:43 AM")]),
dict(t="notif", th="grad", h="COD order confirmed|before dispatch.", tag="D2C brands",
     cards=[("phone","Dynamo AI called the customer","Outbound call · Hindi","10:02 AM"),
            ("check","Order confirmed","Address and delivery time checked","10:03 AM"),
            ("note","Sheet updated","Marked ready to ship","10:03 AM")]),
dict(t="notif", th="light", h="Form filled at 4:12.|Called back at 4:13.", tag="Auto dealers",
     cards=[("phone","Dynamo AI called back","New lead from your Instagram ad","4:13 PM"),
            ("note","Call summary saved","Wants a test ride on Saturday morning","4:15 PM"),
            ("check","Lead added to your CRM","Sales team sees it right away","4:15 PM")]),

# ---------- 3. CHAT (call transcripts, illustrative) ----------
dict(t="chat", th="navy", h="What a call with|Dynamo AI sounds like.", foot="Recording and summary saved",
     lines=[("c","नमस्ते, प्लॉट के रेट जानने थे।"),("d","ज़रूर! आप किस एरिया में देख रहे हैं?"),
            ("c","मानसरोवर में, 200 गज़ तक।"),("d","नोट कर लिया। हमारी टीम कल सुबह 10 बजे आपको कॉल करेगी।")]),
dict(t="chat", th="light", h="It takes the request.|Your staff confirms.", foot="Front desk alerted",
     lines=[("c","Is the doctor available tomorrow?"),("d","I can note your request. May I have your name and a good time to call back?"),
            ("c","Rohit. After 5 PM."),("d","Done, Rohit. The clinic team will call you to confirm the slot.")]),
dict(t="chat", th="grad", h="Want a real person?|One line is enough.", foot="Call transferred to your sales head",
     lines=[("c","Can I talk to the owner?"),("d","Of course. Connecting you now, please stay on the line."),
            ("s","Transferring the call…")]),
dict(t="chat", th="navy", h="Your lead gets a call|within a minute.", foot="Lead added to your sheet",
     lines=[("d","Hi Neha, this is the AI assistant for Sunrise Homes. You just filled our form. Is this a good time?"),
            ("c","Yes, tell me."),("d","Great. Which locality and budget are you looking at?")]),
dict(t="chat", th="light", h="COD orders,|confirmed by call.", foot="Order marked confirmed",
     lines=[("d","नमस्ते! आपका ₹1,499 का ऑर्डर कैश ऑन डिलीवरी है। क्या पता सही है?"),
            ("c","हाँ, पता सही है।"),("d","धन्यवाद! आपका ऑर्डर आज ही भेज दिया जाएगा।")]),

# ---------- 4. MYTH vs FACT ----------
dict(t="myth", th="light", myth="AI calls sound robotic.",
     fact="Don't take our word for it. Hear it yourself: 10 minutes free at dynamoasi.com/app."),
dict(t="myth", th="navy", myth="Setting up AI needs a tech team.",
     fact="Our team sets it up and tests it with you before it goes live. You don't write a line of code."),
dict(t="myth", th="grad", myth="AI will replace my staff.",
     fact="It takes the first call and the late-night ones. Your team talks to customers who are ready, and any caller can be transferred to a person."),
dict(t="myth", th="light", myth="My customers won't talk to an English bot.",
     fact="Dynamo AI talks in Hindi, English and regional languages, in the language your customer uses."),
dict(t="myth", th="navy", myth="AI is too expensive for a small business.",
     fact="₹4 per minute of call time. No salary, no seat fee. Plans start at 2,000 minutes."),

# ---------- 5. BIG NUMBER ----------
dict(t="number", th="grad", n="₹4", h="per minute of call time.", sub="No salary. No seat fee. You pay only for the minutes your calls use."),
dict(t="number", th="navy", n="1 min", h="to call back a new lead.", sub="Someone fills your ad or website form. Dynamo AI calls them within a minute."),
dict(t="number", th="light", n="10 min", h="free trial.", sub="Hear it answer your kind of call before you pay anything. dynamoasi.com/app"),
dict(t="number", th="grad", n="+10%", h="extra minutes, free.", sub="Take 2,000 minutes or more and get 10% extra minutes on us."),
dict(t="number", th="navy", n="1st", h="ring. Every time.", sub="Day, night, Sunday or Diwali. No caller hears it ring out."),

# ---------- 6. CHECKLIST ----------
dict(t="list", th="light", h="After every call,|you get:", mark="check",
     items=["The full call recording","A 2-line summary","The lead in your sheet or CRM","A WhatsApp follow-up to the customer","An alert to your team"]),
dict(t="list", th="navy", h="Is your business|missing calls?", mark="box",
     items=["Calls after closing time","Calls on Sundays and festivals","Leads from ads not called back fast","Staff on leave or at lunch","One number for many branches"],
     note="Ticked even one? Try Dynamo AI free."),
dict(t="list", th="grad", h="What you|won't need:", mark="cross",
     items=["A tech team","Coding","Night-shift hiring","Salary or seat fees"]),
dict(t="list", th="light", h="Live in|4 steps.", mark="num",
     items=["Tell us about your business and common questions","Our team sets up your agent and a new number","We test it with you","Go live and check every call in your login"]),
dict(t="list", th="navy", h="Dynamo AI is a|good fit if you:", mark="check",
     items=["Get most of your leads by phone","Run ads that say “Call now”","Miss calls after hours","Confirm COD orders by phone","Want every call recorded and noted"]),

# ---------- 7. WITHOUT / WITH ----------
dict(t="split", th="light", sit="A customer calls at 9 PM",
     no="It rings out. They call the next shop.", yes="Answered. Details saved. WhatsApp follow-up sent."),
dict(t="split", th="navy", sit="A lead fills your ad form",
     no="Someone calls back the next morning.", yes="Dynamo AI calls back within a minute."),
dict(t="split", th="grad", sit="Your receptionist is on leave",
     no="The phone goes unattended.", yes="Calls are answered as usual."),
dict(t="split", th="light", sit="After the call",
     no="Notes on a paper slip, if any.", yes="Recording, summary and your sheet updated."),
dict(t="split", th="navy", sit="Getting a caller for your business",
     no="Hire, train, cover leaves, pay a salary.", yes="₹4 per minute of calls. Set up by our team."),

# ---------- 8. QUESTION ----------
dict(t="question", th="grad", h="When did your business last miss a call?", opts=["During lunch","After closing","On a Sunday","No idea"]),
dict(t="question", th="light", h="Your customers call in which language?", opts=["Hindi","English","A regional language","All of these"]),
dict(t="question", th="navy", h="Who answers your phone at 10 PM?", opts=["Me","Nobody","Voicemail","Dynamo AI"]),
dict(t="question", th="light", h="How fast do you call back a new lead?", opts=["Within 5 minutes","Within an hour","The next day","Not sure"]),
dict(t="question", th="grad", h="Which missed call hurts the most?", opts=["A new enquiry","A booking","An order confirmation","A regular customer"]),

# ---------- 9. INDUSTRY ----------
dict(t="industry", th="navy", ico="home", ind="real estate", h="Every property enquiry, answered.",
     items=["Answers calls from your property ads","Notes budget, location and BHK","Books site visits for your team"]),
dict(t="industry", th="light", ico="plus", ind="clinics and labs", h="Never miss an appointment request.",
     items=["Takes appointment requests 24×7","Shares timings and address","Passes every request to your front desk"]),
dict(t="industry", th="grad", ico="book", ind="coaching institutes", h="Admission season, fully covered.",
     items=["Answers fee and batch enquiries","Calls back every form fill within a minute","Follows up with parents on WhatsApp"]),
dict(t="industry", th="navy", ico="car", ind="auto and EV dealers", h="Turn calls into test rides.",
     items=["Answers model and showroom questions","Books test rides","Hands hot leads to your sales team"]),
dict(t="industry", th="light", ico="cart", ind="D2C brands", h="Confirm COD orders without a call team.",
     items=["Calls customers to confirm COD orders","Checks address and delivery time","Updates your sheet after every call"]),

# ---------- 10. TIPS ----------
dict(t="tip", th="light", n=1, h="Call new leads while they still remember filling your form.", sub="Speed decides who gets the conversation first."),
dict(t="tip", th="grad", n=2, h="Put one number on every ad, and make sure it always gets answered.", sub="A number that rings out wastes the ad."),
dict(t="tip", th="navy", n=3, h="Write down the 10 questions customers ask most.", sub="That list is the start of a great call script, for people or for AI."),
dict(t="tip", th="light", n=4, h="Never end a call without a next step.", sub="A visit, a callback time or a WhatsApp follow-up. Something specific."),
dict(t="tip", th="navy", n=5, h="Listen to 5 call recordings every week.", sub="You'll hear what customers really ask, and where you lose them."),
]
assert len(POSTS) == 50, len(POSTS)
