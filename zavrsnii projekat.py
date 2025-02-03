import tkinter as tk
import calendar
from tkinter import messagebox
import webbrowser

# Historical events
historical_events = {
    
    "1960": [
        "The 'Kitchen Debate' takes place between U.S. Vice President Richard Nixon and Soviet Premier Nikita Khrushchev at the American National Exhibition in Moscow.",
        "The U.S. launches the first weather satellite, TIROS-1.",
        "The African continent sees the independence of many countries, including Senegal and Madagascar.",
        "The first recorded use of the term 'Third World' is made by French demographer Alfred Sauvy."
    ],
    "1961": [
        "President John F. Kennedy delivers his inaugural address, stating, 'Ask not what your country can do for you—ask what you can do for your country.'",
        "The Berlin Wall is constructed, dividing East and West Berlin.",
        "Yuri Gagarin becomes the first human to travel into space aboard Vostok 1.",
        "The Bay of Pigs invasion occurs when U.S.-backed Cuban exiles attempt to overthrow Fidel Castro’s government but fail."
    ],
    "1962": [
        "The Cuban Missile Crisis occurs, bringing the world to the brink of nuclear war.",
        "The United States successfully tests its first communication satellite, Telstar 1.",
        "The U.S. bans all trade with Cuba.",
        "Marilyn Monroe dies of a drug overdose."
    ],
    "1963": [
        "President John F. Kennedy is assassinated in Dallas, Texas.",
        "Dr. Martin Luther King Jr. delivers his 'I Have a Dream' speech during the March on Washington.",
        "The Beatles release their first album, 'Please Please Me'.",
        "The U.S. and the Soviet Union sign the Limited Test Ban Treaty."
    ],
    "1964": [
        "The Civil Rights Act is passed in the United States.",
        "The Gulf of Tonkin incident leads to increased U.S. involvement in the Vietnam War.",
        "The Ford Mustang is introduced.",
        "The Beatles appear on The Ed Sullivan Show."
    ],
    "1965": [
        "The United States increases its military involvement in Vietnam.",
        "The Voting Rights Act is passed in the United States.",
        "The first spacewalk is conducted by Soviet cosmonaut Alexei Leonov.",
        "The U.S. begins bombing North Vietnam."
    ],
    "1966": [
        "The Cultural Revolution begins in China.",
        "The first human heart transplant is successfully carried out in South Africa.",
        "The National Organization for Women (NOW) is founded in the U.S.",
        "The United Nations peacekeeping force is deployed to the Congo."
    ],
    "1967": [
        "The Six-Day War takes place between Israel and its neighboring Arab states.",
        "The United States begins using Agent Orange in the Vietnam War.",
        "The first successful heart transplant is performed by Dr. Christiaan Barnard.",
        "The first human flight into space by a woman, Valentina Tereshkova, occurs."
    ],
    "1968": [
        "The assassination of Dr. Martin Luther King Jr. sparks riots across the U.S.",
        "The Tet Offensive in Vietnam marks a turning point in the war.",
        "The Soviet Union invades Czechoslovakia to suppress the Prague Spring.",
        "The first Special Olympics is held in Chicago."
    ],
    "1969": [
        "The Apollo 11 mission lands on the moon, and Neil Armstrong becomes the first human to walk on the lunar surface.",
        "The Woodstock Festival takes place, becoming a symbol of the counterculture movement.",
        "The Beatles' final studio album, 'Abbey Road,' is released.",
        "The Internet's precursor, ARPANET, is established."
    ],
    "1970": [
        "The first Earth Day is celebrated, marking the beginning of the environmental movement.",
        "The Kent State shootings occur during a protest against the U.S. invasion of Cambodia.",
        "The first portable cell phone is demonstrated by Martin Cooper of Motorola.",
        "The Soviet Union launches the first space station, Salyut 1."
    ],
    "1971": [
        "Intel introduces the first microprocessor, the 4004.",
        "The U.S. dollar is taken off the gold standard by President Richard Nixon.",
        "The Pentagon Papers are leaked, revealing classified U.S. government information about the Vietnam War.",
        "The United Nations votes to admit the People's Republic of China, replacing Taiwan."
    ],
    "1972": [
        "President Nixon visits China, marking a significant step toward normalization of relations.",
        "The Watergate scandal begins with the break-in at the Democratic National Committee headquarters.",
        "The Munich Olympics are marred by a terrorist attack in which 11 Israeli athletes are taken hostage and killed.",
        "The U.S. signs the SALT I agreement with the Soviet Union to limit nuclear arms."
    ],
    "1973": [
        "The U.S. ends its involvement in the Vietnam War with the signing of the Paris Peace Accords.",
        "The Arab oil embargo causes a worldwide energy crisis.",
        "The U.S. Supreme Court legalizes abortion with the Roe v. Wade decision.",
        "The Yom Kippur War occurs between Israel and a coalition of Arab states."
    ],
    "1974": [
        "President Richard Nixon resigns following the Watergate scandal.",
        "The first portable home computer, the Altair 8800, is introduced.",
        "The U.S. continues to experience the effects of the oil crisis.",
        "The Soviet Union invades Afghanistan, beginning a long and costly war."
    ],
    "1975": [
        "The Vietnam War officially ends with the fall of Saigon.",
        "The Khmer Rouge takes control of Cambodia, leading to a genocide.",
        "The Helsinki Accords are signed, promoting human rights and international cooperation.",
        "The first test-tube baby, Louise Brown, is born."
    ],
    "1976": [
        "The United States celebrates its bicentennial, marking 200 years since the Declaration of Independence.",
        "The first commercial Concorde supersonic flight takes place.",
        "The Soviet Union launches the Soyuz 11 space mission, which tragically results in the deaths of three cosmonauts.",
        "The first fully functional computer mouse is demonstrated by Xerox PARC."
    ],
    "1977": [
        "The first Star Wars film is released, becoming a cultural phenomenon.",
        "The Soviet Union and the U.S. sign the SALT II agreement, limiting nuclear weapons.",
        "The U.S. Energy Crisis leads to long lines at gas stations.",
        "The Great Blizzard of 1977 hits the Northeastern United States."
    ],
    "1978": [
        "The Camp David Accords are signed, leading to peace between Israel and Egypt.",
        "The first test-tube baby, Louise Brown, is born.",
        "The Jonestown massacre occurs in Guyana, with over 900 people dying in a mass suicide.",
        "The U.S. adopts the Star Wars missile defense program under President Ronald Reagan."
    ],
    "1979": [
        "The Iranian Revolution leads to the overthrow of the Shah and the establishment of the Islamic Republic of Iran.",
        "The Soviet Union invades Afghanistan, leading to a prolonged conflict.",
        "The U.S. Embassy in Tehran is seized by militants, leading to a hostage crisis.",
        "The Three Mile Island nuclear accident occurs in Pennsylvania, raising concerns about nuclear energy."
    ],
    "1980": [
        "The U.S. boycotts the Moscow Olympics in protest of the Soviet invasion of Afghanistan.",
        "Mount St. Helens erupts in Washington state, causing widespread damage.",
        "The election of Ronald Reagan as U.S. president signals a shift to conservative policies.",
        "The World Health Organization announces that smallpox has been eradicated."
    ],
    "1981": [
        "President Ronald Reagan is shot in an assassination attempt but survives.",
        "The first personal computer, the IBM PC, is introduced.",
        "The Space Shuttle program is launched with the launch of Columbia.",
        "The AIDS epidemic begins to spread globally."
    ],
    "1982": [
        "The Falklands War between the United Kingdom and Argentina ends with British victory.",
        "The first artificial heart transplant is successfully performed.",
        "Michael Jackson's 'Thriller' album is released, becoming the best-selling album of all time.",
        "The U.S. economy enters a severe recession."
    ],
    "1983": [
        "The Internet's domain name system (DNS) is introduced.",
        "The U.S. invades Grenada to overthrow the communist government.",
        "The first video game console, the Nintendo Entertainment System (NES), is released.",
        "President Reagan proposes the Strategic Defense Initiative (SDI), also known as 'Star Wars.'"
    ],
    "1984": [
        "Apple introduces the Macintosh computer, changing personal computing forever.",
        "The Summer Olympics are held in Los Angeles, showcasing American culture and sports dominance.",
        "The U.S. economy begins to recover from the early 1980s recession.",
        "The Iran-Contra affair begins to unfold, involving illegal arms deals to fund Nicaraguan rebels."
    ],
    "1985": [
        "Mikhail Gorbachev becomes the leader of the Soviet Union and initiates reforms with perestroika and glasnost.",
        "The Live Aid concert is held to raise money for famine relief in Ethiopia.",
        "The first wireless cell phone call is made by Martin Cooper of Motorola.",
        "The first 'Back to the Future' film is released, becoming a box-office hit."
    ],
    "1986": [
        "The Chernobyl nuclear disaster occurs in the Soviet Union, leading to widespread radioactive contamination.",
        "The Space Shuttle Challenger explodes shortly after launch, killing all seven crew members.",
        "The Iran-Contra hearings begin, revealing the U.S. government's covert activities.",
        "The U.S. adopts the Anti-Drug Abuse Act, strengthening drug enforcement."
    ],
    "1987": [
        "The stock market crashes on Black Monday, leading to a global financial crisis.",
        "The U.S. and the Soviet Union sign the Intermediate-Range Nuclear Forces Treaty.",
        "The first 'The Simpsons' short is aired on The Tracey Ullman Show.",
        "The 'Tiananmen Square' protests begin in China, though they are later suppressed by the government."
    ],
    "1988": [
        "The Iran–Iraq War ends after nearly a decade of conflict.",
        "The Soviet Union withdraws from Afghanistan, ending its involvement in the war there.",
        "The U.S. presidential election sees George H.W. Bush defeat Michael Dukakis.",
        "Pan Am Flight 103 is bombed over Lockerbie, Scotland, killing 270 people."
    ],
    "1989": [
        "The Berlin Wall falls, signaling the end of the Cold War.",
        "The Tiananmen Square protests take place in China, with a violent government crackdown.",
        "The Exxon Valdez oil spill occurs in Alaska, causing environmental devastation.",
        "The U.S. invades Panama to depose General Manuel Noriega."
    ],
    "1990": [
        "Germany reunifies after the fall of the Berlin Wall.",
        "Nelson Mandela is released from prison in South Africa, leading to the end of apartheid.",
        "The Hubble Space Telescope is launched.",
        "The World Wide Web is created by Tim Berners-Lee."
    ],
    "1991": [
        "The Soviet Union dissolves, officially ending the Cold War.",
        "The Gulf War begins with U.S.-led coalition forces liberating Kuwait from Iraqi occupation.",
        "The World Wide Web is made publicly available, sparking the digital revolution.",
        "The European Union is formally established with the Maastricht Treaty."
    ],
    "1992": [
        "The U.S. signs the North American Free Trade Agreement (NAFTA).",
        "The Rio Earth Summit takes place, focusing on global environmental issues.",
        "Bill Clinton is elected President of the United States.",
        "The Bosnian War begins, leading to a brutal conflict in the Balkans."
    ],
    "1993": [
        "The Oslo Accords are signed, beginning the peace process between Israel and the Palestinians.",
        "The European Union is officially established by the Maastricht Treaty.",
        "The World Trade Center in New York is bombed by terrorists, killing six people.",
        "The North American Free Trade Agreement (NAFTA) is signed."
    ],
    "1994": [
        "Nelson Mandela is elected president of South Africa, ending apartheid.",
        "The Rwandan Genocide begins, resulting in the deaths of over 800,000 people.",
        "The World Trade Organization (WTO) is established.",
        "The Channel Tunnel, connecting the UK and France, is opened."
    ],
    "1995": [
        "The Oklahoma City bombing kills 168 people, one of the deadliest terrorist attacks in U.S. history.",
        "The Java programming language is introduced by Sun Microsystems.",
        "The World Trade Organization (WTO) is established, replacing the General Agreement on Tariffs and Trade (GATT).",
        "The movie 'Toy Story' is released, becoming the first fully computer-animated feature film."
    ],
    "1996": [
        "The Taliban seizes control of Afghanistan, establishing a repressive regime.",
        "The Centennial Olympic Games are held in Atlanta, Georgia.",
        "The Internet boom begins with the rise of websites like Yahoo, Amazon, and eBay.",
        "Dolly the sheep is cloned, marking a significant breakthrough in genetics."
    ],
    "1997": [
        "Princess Diana dies in a car crash in Paris, leading to worldwide mourning.",
        "The Kyoto Protocol is adopted to combat global climate change.",
        "The Asian financial crisis hits, affecting several countries in East Asia.",
        "The Hong Kong handover occurs, with British rule ending and China taking control."
    ],
    "1998": [
        "The Good Friday Agreement is signed, marking a significant peace process in Northern Ireland.",
        "The Monica Lewinsky scandal leads to the impeachment of U.S. President Bill Clinton.",
        "Google is founded, changing the way people use the Internet.",
        "France wins the FIFA World Cup in front of a home crowd."
    ],
    "1999": [
        "The euro is introduced as the official currency in 11 European countries.",
        "The Y2K scare leads to widespread fears of computer system failures.",
        "The U.S. conducts airstrikes in Kosovo as part of the NATO intervention during the Kosovo War.",
        "The Columbine High School massacre occurs, changing discussions about gun control and school safety."
    ],
    "2000": 
    ["The dot-com bubble bursts, leading to a significant downturn in the tech sector.",
     "George W. Bush is elected as the 43rd President of the United States after a contested election.",
     "The first human genome is sequenced, marking a major milestone in genetics.",
     "The International Space Station (ISS) is officially opened for international collaboration.",

    ],
    "2001": [
        "The September 11 terrorist attacks occur in the U.S., leading to the deaths of nearly 3,000 people and triggering the War on Terror.",
        "The U.S. invades Afghanistan to overthrow the Taliban regime.",
        "Wikipedia is launched as a free online encyclopedia.",
        "The U.S. stock market suffers a sharp decline due to the aftermath of 9/11."
    ],
    "2002": [
        "The Euro currency is introduced in 12 European Union countries.",
        "The U.S. Department of Homeland Security is created in response to the 9/11 attacks.",
        "The U.S. invades Iraq, citing weapons of mass destruction as a key reason for military action.",
        "The first film in the 'Lord of the Rings' trilogy, 'The Fellowship of the Ring,' is released."
    ],
    "2003": [
        "The U.S. invades Iraq, leading to the toppling of Saddam Hussein's regime.",
        "The human genome is sequenced for the first time.",
        "The Space Shuttle Columbia disaster occurs, killing all seven crew members.",
        "The European Union expands to include 10 new countries, mostly from Eastern Europe."
    ],
    "2004": [
        "The Indian Ocean tsunami occurs, killing over 230,000 people across 14 countries.",
        "Facebook is launched by Mark Zuckerberg and his college roommates.",
        "The U.S. re-elects George W. Bush as president.",
        "The Madrid train bombings kill 191 people and injure over 2,000 in Spain."
    ],
    "2005": [
        "Hurricane Katrina devastates New Orleans, causing over 1,800 deaths and widespread damage.",
        "The first YouTube video is uploaded, marking the beginning of the video-sharing era.",
        "The U.S. withdraws from the Kyoto Protocol, citing economic concerns.",
        "Angela Merkel becomes the first female Chancellor of Germany."
    ],
    "2006": [
        "North Korea conducts its first nuclear test, leading to global condemnation.",
        "Twitter is launched, providing a new platform for short-form social media communication.",
        "The Iraq War continues, with U.S. forces involved in fighting insurgent groups.",
        "The FIFA World Cup is held in Germany, with Italy emerging as the winner."
    ],
    "2007": [
        "The global financial crisis begins to take shape with the subprime mortgage crisis in the U.S.",
        "The iPhone is released by Apple, revolutionizing the smartphone industry.",
        "The Virginia Tech shooting occurs, killing 32 people and injuring many more.",
        "The global economy begins to experience significant instability."
    ],
    "2008": [
        "Barack Obama is elected the first African American president of the United States.",
        "The global financial crisis hits, leading to widespread recession and major bailouts for financial institutions.",
        "The Beijing Olympics are held, showcasing China's rising global influence.",
        "The Large Hadron Collider (LHC) is completed, beginning a new era of scientific experimentation."
    ],
    "2009": [
        "The H1N1 (Swine Flu) pandemic begins, infecting millions globally.",
        "The U.S. economy shows signs of recovery from the financial crisis, although many challenges remain.",
        "Michael Jackson, the 'King of Pop,' dies unexpectedly at the age of 50.",
        "Barack Obama is inaugurated as the 44th president of the United States."
    ],
    "2010": [
        "The Deepwater Horizon oil spill occurs in the Gulf of Mexico, becoming one of the largest environmental disasters in history.",
        "The European debt crisis begins to threaten the stability of the Eurozone.",
        "Haiti is devastated by a powerful earthquake, killing over 230,000 people.",
        "Apple introduces the iPad, creating a new category of tablet computers."
    ],
    "2011": [
        "Osama bin Laden, the mastermind behind the 9/11 attacks, is killed by U.S. Navy SEALs in Pakistan.",
        "The Arab Spring begins with protests against authoritarian regimes in the Middle East and North Africa.",
        "The U.S. military ends its combat operations in Iraq after nearly nine years.",
        "Steve Jobs, co-founder of Apple Inc., dies from cancer."
    ],
    "2012": [
        "The Costa Concordia cruise ship sinks off the coast of Italy, killing 32 people.",
        "The U.S. re-elects Barack Obama for a second term.",
        "Hurricane Sandy hits the U.S. East Coast, causing extensive damage and flooding.",
        "The Mayan calendar 'end of the world' prediction proves to be a hoax."
    ],
    "2013": [
        "Edward Snowden leaks classified documents revealing the extent of U.S. surveillance programs.",
        "The Boston Marathon bombing kills three people and injures hundreds.",
        "Pope Francis is elected as the leader of the Roman Catholic Church.",
        "The Syrian Civil War escalates, with international involvement and humanitarian crises."
    ],
    "2014": [
        "Russia annexes Crimea, leading to international sanctions and condemnation.",
        "The Ebola outbreak spreads across West Africa, killing thousands.",
        "The Islamic State (ISIS) emerges as a powerful force in Iraq and Syria.",
        "The Malaysia Airlines Flight MH370 disappears, sparking one of the greatest mysteries in aviation history."
    ],
    "2015": [
        "The Paris Agreement on climate change is adopted by 195 countries.",
        "Same-sex marriage is legalized across the United States following a Supreme Court ruling.",
        "The Syrian refugee crisis intensifies as millions flee the civil war.",
        "The Iran nuclear deal is signed, aiming to limit Iran's nuclear program in exchange for sanctions relief."
    ],
    "2016": [
        "The United Kingdom votes to leave the European Union in a referendum, known as Brexit.",
        "Donald Trump is elected the 45th president of the United States in a stunning upset over Hillary Clinton.",
        "The Zika virus outbreak becomes a global health emergency.",
        "The Paris Agreement on climate change enters into force."
    ],
    "2017": [
        "Donald Trump is inaugurated as the 45th president of the United States.",
        "The #MeToo movement gains momentum, raising awareness of sexual harassment and assault.",
        "The total solar eclipse occurs across the United States.",
        "The North Korean missile crisis escalates with multiple missile tests."
    ],
    "2018": [
        "The U.S. announces its withdrawal from the Iran nuclear deal, leading to increased tensions.",
        "The Camp Fire in California becomes the deadliest and most destructive wildfire in the state's history.",
        "The World Health Organization announces that the Ebola outbreak in the Democratic Republic of Congo is contained.",
        "The 2018 Winter Olympics are held in Pyeongchang, South Korea."
    ],
    "2019": [
        "The Notre-Dame Cathedral in Paris is severely damaged by a fire.",
        "The U.S. formally impeaches President Donald Trump over abuse of power and obstruction of Congress.",
        "The COVID-19 pandemic begins in Wuhan, China, spreading globally.",
        "Greta Thunberg leads climate strikes around the world, pushing for urgent action on climate change."
    ],
    "2020": [
        "The COVID-19 pandemic spreads globally, leading to widespread lockdowns and economic disruption.",
        "Black Lives Matter protests erupt across the U.S. and globally following the killing of George Floyd.",
        "Joe Biden is elected president of the United States, defeating incumbent Donald Trump.",
        "The Australian wildfires burn millions of acres, killing or displacing thousands of animals."
    ]
}



# Function to open Wikipedia for the given query
def search_wikipedia(query):
    if query.strip():  # Ensure the query is not empty
        formatted_query = query.replace(" ", "_")
        url = f"https://en.wikipedia.org/wiki/{formatted_query}"
        webbrowser.open(url)  # Open the URL in the default web browser
    else:
        messagebox.showwarning("Error", "Please enter a search term.")
# Login function
def handle_login():
    username = username_entry.get()
    year_of_birth = year_entry.get()

    if username and year_of_birth.isdigit():
        year_of_birth = int(year_of_birth)

        # Welcome window
        welcome_window = tk.Toplevel(app)
        welcome_window.title("Welcome")
        welcome_window.geometry("600x300")
        welcome_window.configure(bg="#d3deeb")

        # Welcome messages
        tk.Label(welcome_window, text=f"Hello, {username}!", font=("Times New Roman", 20), bg="#d3deeb", fg="black").pack(pady=20)
        tk.Label(welcome_window, text="This is a sort of Wikipedia for history.", font=("Times New Roman", 20), bg="#d3deeb", fg="black").pack(pady=10)
        tk.Label(welcome_window, text="Search years, explore events, fun facts, quizzes,", font=("Times New Roman", 20), bg="#d3deeb", fg="black").pack(pady=5)
        tk.Label(welcome_window, text="and a calendar with significant historical events.", font=("Times New Roman", 20), bg="#d3deeb", fg="black").pack(pady=5)

        # Close button
        def close_and_open_fullscreen():
            welcome_window.destroy()
            open_fullscreen_window(year_of_birth)

        tk.Button(welcome_window, text="Close", font=("Times New Roman", 20), bg="#ffc1c1", fg="black", command=close_and_open_fullscreen).pack(pady=20)
    else:
        messagebox.showwarning("Error", "Enter a valid username and year of birth.")

# Open fullscreen window with historical events
def open_fullscreen_window(year_of_birth):
    fullscreen_window = tk.Toplevel(app)
    fullscreen_window.title("Full Screen")
    fullscreen_window.attributes('-fullscreen', True)
    fullscreen_window.configure(bg="#d3deeb")

    # Create the top panel with buttons
    top_frame = tk.Frame(fullscreen_window, bg="#c8e6c9")
    top_frame.pack(fill="x", side="top")

    # Button functions for the top panel
    def exit_app():
        fullscreen_window.quit()

    # Add buttons to the top panel
    tk.Button(top_frame, text="Exit", font=("Times New Roman", 16), bg="#ffc1c1", fg="black", command=exit_app).pack(side="right", padx=10)

    # Get events for the year of birth
    events = historical_events.get(str(year_of_birth), ["No historical event available for this year."])

    # Content of the fullscreen window
    tk.Label(fullscreen_window, text="Welcome to the History Exploration App!", font=("Times New Roman", 80), bg="#d3deeb", fg="black").pack(pady=50)
    tk.Label(fullscreen_window, text=f"In the year {year_of_birth}:", font=("Times New Roman", 64), bg="#d3deeb", fg="black").pack(pady=20)

    # Create a label for each event
    event_labels = []
    for event in events:
        event_label = tk.Label(fullscreen_window, text=event, font=("Times New Roman", 48), bg="#d3deeb", fg="black")
        event_labels.append(event_label)
        event_label.pack(pady=5)

    # Go to app button
    def go_to_app():
        fullscreen_window.destroy()
        open_second_fullscreen_window()  # Open the second fullscreen window

    tk.Button(fullscreen_window, text="Go to App", font=("Times New Roman", 40), bg="#c8e6c9", fg="black", command=go_to_app).pack(pady=50)

    # label to show fun facts
    def show_fun_facts():
        fun_facts = fun_facts_by_year.get(str(year_of_birth), ["No fun facts available for this year."])
        fun_facts_window = tk.Toplevel(fullscreen_window)
        fun_facts_window.title("Fun Facts")
        fun_facts_window.geometry("600x400")
        fun_facts_window.configure(bg="#d3deeb")

        tk.Label(fun_facts_window, text=f"Fun Facts for {year_of_birth}:", font=("Times New Roman", 24), bg="#d3deeb", fg="black").pack(pady=20)

        for fact in fun_facts:
            tk.Label(fun_facts_window, text=fact, font=("Times New Roman", 18), bg="#d3deeb", fg="black").pack(pady=5)

   


def open_second_fullscreen_window():
    second_fullscreen_window = tk.Toplevel(app)
    second_fullscreen_window.title("Second Full Screen")
    second_fullscreen_window.attributes('-fullscreen', True)
    second_fullscreen_window.configure(bg="#d3deeb")

    # Create the top panel with buttons
    top_frame = tk.Frame(second_fullscreen_window, bg="#c8e6c9")
    top_frame.pack(fill="x", side="top")

    # Button functions for the top panel on the second fullscreen window
    def open_calendar():
        open_fullscreen_for_calendar()

    def open_quiz():
        open_fullscreen_for_quiz()

    def open_fun_facts():
        open_fullscreen_for_fun_facts()

    # Add buttons to the top panel with expanded width
    tk.Button(top_frame, text="Calendar", font=("Times New Roman", 40), bg="#a5d6a7", fg="black", command=open_calendar).pack(side="left", fill="x", expand=True, padx=10, pady=10)
    tk.Button(top_frame, text="Quiz", font=("Times New Roman", 40), bg="#a5d6a7", fg="black", command=open_quiz).pack(side="left", fill="x", expand=True, padx=10, pady=10)
    tk.Button(top_frame, text="Fun Facts", font=("Times New Roman", 40), bg="#a5d6a7", fg="black", command=open_fun_facts).pack(side="left", fill="x", expand=True, padx=10, pady=10)
   

    # Search bar in the middle of the second fullscreen window
    search_frame = tk.Frame(second_fullscreen_window, bg="#d3deeb")
    search_frame.pack(pady=150)

    tk.Label(search_frame, text="Search for Historical Facts:", font=("Times New Roman", 40), bg="#d3deeb", fg="black").pack(pady=20)
    search_entry = tk.Entry(search_frame, font=("Times New Roman", 30), width=30)
    search_entry.pack(pady=20)

    def perform_search():
        query = search_entry.get()
        search_wikipedia(query)

    tk.Button(search_frame, text="Search", font=("Times New Roman", 30), bg="#c8e6c9", fg="black", command=perform_search).pack(pady=20)

        # Close button for second fullscreen window
    def close_second_fullscreen():
        second_fullscreen_window.destroy()

    tk.Button(second_fullscreen_window, text="Exit Fullscreen", font=("Times New Roman", 40), bg="#ffc1c1", fg="black", command=close_second_fullscreen).pack(pady=50)

historical_event_cal = {
    (1, 1): "In 1801, the Act of Union created the United Kingdom of Great Britain and Ireland.",
    (1, 2): "In 1492, the Catholic Monarchs entered Granada, completing the Reconquista.",
    (1, 3): "In 1521, Martin Luther was excommunicated by Pope Leo X.",
    (1, 4): "In 2004, NASA's Spirit rover landed on Mars.",
    (1, 5): "In 1914, Henry Ford introduced a $5-per-day wage for workers.",
    (1, 6): "In 1838, Samuel Morse successfully tested the telegraph.",
    (1, 7): "In 1789, the first US presidential election was held.",
    (1, 8): "In 1815, the Battle of New Orleans took place during the War of 1812.",
    (1, 9): "In 2007, Apple announced the first iPhone.",
    (1, 10): "In 1920, the League of Nations was established.",
    (1, 11): "In 1935, Amelia Earhart became the first person to fly solo from Hawaii to California.",
    (1, 12): "In 1969, Led Zeppelin released their debut album.",
    (1, 13): "In 1910, the first public radio broadcast took place.",
    (1, 14): "In 1954, Marilyn Monroe married Joe DiMaggio.",
    (1, 15): "In 1929, Martin Luther King Jr. was born.",
    (1, 16): "In 1605, the first edition of 'Don Quixote' was published.",
    (1, 17): "In 1773, Captain James Cook became the first person to cross the Antarctic Circle.",
    (1, 18): "In 1919, the Paris Peace Conference began after World War I.",
    (1, 19): "In 1809, Edgar Allan Poe was born.",
    (1, 20): "In 1981, Ronald Reagan was inaugurated as the 40th US president.",
    (1, 21): "In 1976, Concorde began commercial service.",
    (1, 22): "In 1905, the Bloody Sunday massacre occurred in Russia.",
    (1, 23): "In 1849, Elizabeth Blackwell became the first female doctor in the US.",
    (1, 24): "In 1984, Apple introduced the Macintosh computer.",
    (1, 25): "In 1924, the first Winter Olympics opened in Chamonix, France.",
    (1, 26): "In 1788, Australia was colonized by British settlers on the First Fleet.",
    (1, 27): "In 1945, the Soviet army liberated Auschwitz concentration camp.",
    (1, 28): "In 1986, the Challenger space shuttle disaster occurred.",
    (1, 29): "In 1886, the first gasoline-powered car was patented by Karl Benz.",
    (1, 30): "In 1948, Mahatma Gandhi was assassinated in New Delhi.",
    (1, 31): "In 1865, the US Congress passed the 13th Amendment, abolishing slavery.",
    (2, 1): "In 1884, the first volume of the Oxford English Dictionary was published.",
    (2, 2): "In 1922, James Joyce's 'Ulysses' was published.",
    (2, 3): "In 1959, rock and roll stars Buddy Holly, Ritchie Valens, and J.P. Richardson died in a plane crash.",
    (2, 4): "In 1945, the Yalta Conference began with Churchill, Roosevelt, and Stalin.",
    (2, 5): "In 1919, Charlie Chaplin, Mary Pickford, and Douglas Fairbanks founded United Artists.",
    (2, 6): "In 1952, Queen Elizabeth II ascended the throne after the death of her father, King George VI.",
    (2, 7): "In 1964, The Beatles arrived in the US for the first time.",
    (2, 8): "In 1904, the Russo-Japanese War began.",
    (2, 9): "In 1825, the US House of Representatives elected John Quincy Adams as president.",
    (2, 10): "In 1996, world chess champion Garry Kasparov lost a game to IBM's Deep Blue.",
    (2, 11): "In 1990, Nelson Mandela was released from prison after 27 years.",
    (2, 12): "In 1809, Abraham Lincoln was born.",
    (2, 13): "In 1935, Bruno Hauptmann was convicted for the kidnapping of the Lindbergh baby.",
    (2, 14): "In 1929, the Saint Valentine's Day Massacre occurred in Chicago.",
    (2, 15): "In 1898, the USS Maine exploded in Havana Harbor, leading to the Spanish-American War.",
    (2, 16): "In 1923, archaeologist Howard Carter opened the tomb of King Tutankhamun.",
    (2, 17): "In 1864, the USS H.L. Hunley became the first submarine to sink a warship.",
    (2, 18): "In 1930, Pluto was discovered by Clyde Tombaugh.",
    (2, 19): "In 1945, the Battle of Iwo Jima began during World War II.",
    (2, 20): "In 1962, John Glenn became the first American to orbit the Earth.",
    (2, 21): "In 1848, Karl Marx and Friedrich Engels published 'The Communist Manifesto.'",
    (2, 22): "In 1732, George Washington was born.",
    (2, 23): "In 1945, the US flag was raised on Iwo Jima's Mount Suribachi.",
    (2, 24): "In 1920, the Nazi Party was founded in Germany.",
    (2, 25): "In 1964, Muhammad Ali defeated Sonny Liston to become the world heavyweight champion.",
    (2, 26): "In 1815, Napoleon Bonaparte escaped from exile on the island of Elba.",
    (2, 27): "In 1933, Germany's Reichstag building was set on fire.",
    (2, 28): "In 1953, Watson and Crick discovered the structure of DNA.",
    (2, 29): "In 1940, Hattie McDaniel became the first African American to win an Oscar.",
     (3, 1): "In 1872, Yellowstone became the first US national park.",
    (3, 2): "In 1933, the movie 'King Kong' premiered in New York City.",
    (3, 3): "In 1931, 'The Star-Spangled Banner' was adopted as the US national anthem.",
    (3, 4): "In 1789, the US Constitution went into effect.",
    (3, 5): "In 1946, Winston Churchill delivered his 'Iron Curtain' speech.",
    (3, 6): "In 1957, Ghana became the first African nation to gain independence from colonial rule.",
    (3, 7): "In 1965, the Selma to Montgomery marches began in Alabama.",
    (3, 8): "In 1917, the Russian February Revolution began.",
    (3, 9): "In 1959, the Barbie doll debuted at the American International Toy Fair.",
    (3, 10): "In 1876, Alexander Graham Bell made the first telephone call.",
    (3, 11): "In 2011, the Fukushima nuclear disaster occurred in Japan.",
    (3, 12): "In 1930, Mahatma Gandhi began the Salt March in India.",
    (3, 13): "In 1781, Uranus was discovered by astronomer William Herschel.",
    (3, 14): "In 1879, Albert Einstein was born.",
    (3, 15): "In 44 BC, Julius Caesar was assassinated on the Ides of March.",
    (3, 16): "In 1926, Robert Goddard launched the first liquid-fueled rocket.",
    (3, 17): "In 461 AD, Saint Patrick, the patron saint of Ireland, died.",
    (3, 18): "In 1965, Alexei Leonov became the first person to walk in space.",
    (3, 19): "In 2003, the Iraq War began with a US-led invasion.",
    (3, 20): "In 1995, a sarin gas attack occurred on the Tokyo subway.",
    (3, 21): "In 1960, South African police killed 69 people in the Sharpeville massacre.",
    (3, 22): "In 1765, the British Parliament passed the Stamp Act.",
    (3, 23): "In 1839, the first recorded use of 'OK' appeared in a Boston newspaper.",
    (3, 24): "In 1882, Robert Koch discovered the bacterium that causes tuberculosis.",
    (3, 25): "In 1957, the Treaty of Rome established the European Economic Community.",
    (3, 26): "In 1979, the Israel-Egypt Peace Treaty was signed.",
    (3, 27): "In 1998, the FDA approved Viagra as a treatment for erectile dysfunction.",
    (3, 28): "In 1930, the cities of Constantinople and Angora were officially renamed Istanbul and Ankara.",
    (3, 29): "In 1974, the Terracotta Army was discovered in Xi'an, China.",
    (3, 30): "In 1981, US President Ronald Reagan survived an assassination attempt.",
    (3, 31): "In 1889, the Eiffel Tower was officially opened in Paris.",
    (4, 1): "In 1976, Apple Computer was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne.",
    (4, 2): "In 1917, the United States entered World War I.",
    (4, 3): "In 1968, Dr. Martin Luther King Jr. was assassinated in Memphis, Tennessee.",
    (4, 4): "In 1969, the Boeing 747 made its first flight.",
    (4, 5): "In 1982, the Falklands War began between Argentina and the United Kingdom.",
    (4, 6): "In 1917, the U.S. declared war on Germany during World War I.",
    (4, 7): "In 1994, the Rwandan genocide began.",
    (4, 8): "In 1973, the World Trade Center in New York was bombed.",
    (4, 9): "In 1865, Confederate General Robert E. Lee surrendered to Ulysses S. Grant at Appomattox Court House, ending the Civil War.",
    (4, 10): "In 1912, the RMS Titanic set sail on its maiden voyage.",
    (4, 11): "In 1968, the Civil Rights Act was passed in the U.S.",
    (4, 12): "In 1961, Yuri Gagarin became the first human in space.",
    (4, 13): "In 1970, the Apollo 13 mission was launched.",
    (4, 14): "In 1865, President Abraham Lincoln was shot by John Wilkes Booth.",
    (4, 15): "In 1912, the RMS Titanic hit an iceberg and sank.",
    (4, 16): "In 1962, the first U.S. satellite was launched from Cape Canaveral.",
    (4, 17): "In 1990, Jesse Owens, the famous Olympic gold medalist, died.",
    (4, 18): "In 1906, the San Francisco earthquake occurred.",
    (4, 19): "In 1995, the Oklahoma City bombing occurred.",
    (4, 20): "In 1999, the Columbine High School shooting occurred.",
    (4, 21): "In 1836, the Battle of San Jacinto took place during the Texas Revolution.",
    (4, 22): "In 1970, the first Earth Day was celebrated.",
    (4, 23): "In 1616, William Shakespeare and Miguel de Cervantes died.",
    (4, 24): "In 1916, the Easter Rising took place in Ireland.",
    (4, 25): "In 1953, Francis Crick and James Watson published their discovery of the structure of DNA.",
    (4, 26): "In 1986, the Chernobyl nuclear disaster occurred in the Soviet Union.",
    (4, 27): "In 1961, the United States launched its first weather satellite.",
    (4, 28): "In 1930, the cities of Constantinople and Angora were officially renamed Istanbul and Ankara.",
    (4, 29): "In 1945, Benito Mussolini was executed by Italian partisans.",
    (4, 30): "In 1997, the final episode of 'The X-Files' was aired on Fox.",
    (5, 1): "In 1886, the Haymarket affair took place in Chicago, marking the beginning of the labor movement in the U.S.",
    (5, 2): "In 2011, Osama bin Laden, the mastermind behind the September 11 attacks, was killed by U.S. Navy SEALs in Pakistan.",
    (5, 3): "In 1979, Margaret Thatcher became the first female Prime Minister of the United Kingdom.",
    (5, 4): "In 1961, Freedom Riders began their campaign to desegregate interstate buses in the southern U.S.",
    (5, 5): "In 1862, the Battle of Puebla took place, commemorated as Cinco de Mayo.",
    (5, 6): "In 1937, the Hindenburg disaster occurred when the German zeppelin caught fire while attempting to land in New Jersey.",
    (5, 7): "In 1945, Nazi Germany surrendered to the Allies, ending World War II in Europe.",
    (5, 8): "In 1945, Victory in Europe (VE) Day was celebrated, marking the end of World War II in Europe.",
    (5, 9): "In 1974, the U.S. House of Representatives began the impeachment proceedings against President Richard Nixon.",
    (5, 10): "In 1994, Nelson Mandela was inaugurated as South Africa's first black president.",
    (5, 11): "In 1960, the U.S. launched its first weather satellite.",
    (5, 12): "In 1967, the Six-Day War ended with Israel's victory and occupation of the West Bank and Gaza Strip.",
    (5, 13): "In 1917, the United States entered World War I.",
    (5, 14): "In 1948, the state of Israel was declared, leading to the Arab-Israeli War.",
    (5, 15): "In 1972, the Watergate scandal began when five men broke into the Democratic National Committee headquarters.",
    (5, 16): "In 1966, the Cultural Revolution began in China, led by Mao Zedong.",
    (5, 17): "In 1954, the U.S. Supreme Court issued the Brown v. Board of Education ruling, declaring racial segregation in schools unconstitutional.",
    (5, 18): "In 1980, Mount St. Helens erupted in Washington, causing widespread damage and loss of life.",
    (5, 19): "In 1993, the Intel Corporation released the Pentium microprocessor.",
    (5, 20): "In 1927, Charles Lindbergh completed the first solo nonstop flight across the Atlantic Ocean.",
    (5, 21): "In 1881, the American Red Cross was founded by Clara Barton.",
    (5, 22): "In 1990, the World Health Organization removed homosexuality from its list of mental illnesses.",
    (5, 23): "In 1967, the Nigerian Civil War (Biafran War) began.",
    (5, 24): "In 1965, the first U.S. spacewalk occurred when astronaut Ed White left his spacecraft.",
    (5, 25): "In 1977, Star Wars premiered in theaters, becoming a cultural phenomenon.",
    (5, 26): "In 1998, Indonesia's President Suharto resigned after 31 years in power during a time of economic crisis.",
    (5, 27): "In 1937, the Golden Gate Bridge was opened to vehicular traffic in San Francisco.",
    (5, 28): "In 1930, the Chrysler Building was completed in New York City.",
    (5, 29): "In 1953, Sir Edmund Hillary and Tenzing Norgay became the first to reach the summit of Mount Everest.",
    (5, 30): "In 1431, Joan of Arc was burned at the stake in Rouen, France.",
    (6, 1): "In 1967, The Beatles released their album Sgt. Pepper’s Lonely Hearts Club Band.",
    (6, 2): "In 1953, Queen Elizabeth II was crowned in Westminster Abbey, London.",
    (6, 3): "In 1965, Edward White became the first American astronaut to conduct a spacewalk.",
    (6, 4): "In 1989, the Tiananmen Square Massacre occurred in Beijing, China.",
    (6, 5): "In 1968, Senator Robert F. Kennedy was assassinated in Los Angeles.",
    (6, 6): "In 1944, D-Day occurred as Allied forces landed on the beaches of Normandy, France.",
    (6, 7): "In 1494, Spain and Portugal signed the Treaty of Tordesillas, dividing the New World.",
    (6, 8): "In 1789, James Madison introduced the Bill of Rights to the U.S. Congress.",
    (6, 9): "In 1815, the Congress of Vienna officially ended, reshaping Europe after Napoleon’s defeat.",
    (6, 10): "In 1692, the first person, Bridget Bishop, was hanged for witchcraft in Salem, Massachusetts.",
    (6, 11): "In 1776, the Continental Congress appointed a committee to draft the Declaration of Independence.",
    (6, 12): "In 1987, President Ronald Reagan gave his famous ‘Tear down this wall!’ speech in Berlin.",
    (6, 13): "In 323 BC, Alexander the Great died in Babylon.",
    (6, 14): "In 1777, the United States adopted the Stars and Stripes as its national flag.",
    (6, 15): "In 1215, King John of England sealed the Magna Carta at Runnymede.",
    (6, 16): "In 1963, Valentina Tereshkova became the first woman in space.",
    (6, 17): "In 1972, the Watergate break-in occurred, leading to President Nixon’s resignation.",
    (6, 18): "In 1815, Napoleon was defeated at the Battle of Waterloo.",
    (6, 19): "In 1865, Union troops arrived in Texas, marking the end of slavery in the U.S. (Juneteenth).",
    (6, 20): "In 1789, the Tennis Court Oath was taken during the French Revolution.",
    (6, 21): "In 1788, New Hampshire became the ninth state to ratify the U.S. Constitution, making it official.",
    (6, 22): "In 1941, Nazi Germany launched Operation Barbarossa, invading the Soviet Union.",
    (6, 23): "In 2016, Britain voted to leave the European Union (Brexit referendum).",
    (6, 24): "In 1314, the Scots defeated the English at the Battle of Bannockburn.",
    (6, 25): "In 1950, the Korean War began as North Korea invaded South Korea.",
    (6, 26): "In 1945, the United Nations Charter was signed in San Francisco.",
    (6, 27): "In 1954, the world's first nuclear power station opened in Obninsk, USSR.",
    (6, 28): "In 1914, Archduke Franz Ferdinand was assassinated, triggering World War I.",
    (6, 29): "In 2007, Apple released the first iPhone.",
    (6, 30): "In 1908, the Tunguska event, a massive explosion, occurred over Siberia.",
    (7, 1): "In 1863, the Battle of Gettysburg began during the American Civil War.",
    (7, 2): "In 1964, President Lyndon B. Johnson signed the Civil Rights Act into law.",
    (7, 3): "In 1863, the Battle of Gettysburg ended with Pickett’s Charge.",
    (7, 4): "In 1776, the United States declared independence from Britain.",
    (7, 5): "In 1687, Isaac Newton published Principia Mathematica.",
    (7, 6): "In 1415, Jan Hus was burned at the stake for heresy.",
    (7, 7): "In 2005, the London bombings killed 52 people.",
    (7, 8): "In 1497, Vasco da Gama set sail for India.",
    (7, 9): "In 1850, President Zachary Taylor died in office.",
    (7, 10): "In 1925, the Scopes Monkey Trial began in Tennessee.",
    (7, 11): "In 1804, Alexander Hamilton was fatally shot by Aaron Burr in a duel.",
    (7, 12): "In 1995, the Srebrenica massacre occurred during the Bosnian War.",
    (7, 13): "In 1985, Live Aid concerts were held to fight famine in Africa.",
    (7, 14): "In 1789, the French Revolution began with the storming of the Bastille.",
    (7, 15): "In 1975, the Apollo-Soyuz Test Project marked U.S.-Soviet cooperation in space.",
    (7, 16): "In 1969, Apollo 11 was launched, beginning the first moon landing mission.",
    (7, 17): "In 1918, Tsar Nicholas II and his family were executed by the Bolsheviks.",
    (7, 18): "In 1918, Nelson Mandela was born in South Africa.",
    (7, 19): "In 1848, the Seneca Falls Convention, the first women's rights convention, was held.",
    (7, 20): "In 1969, Neil Armstrong and Buzz Aldrin walked on the Moon.",
    (7, 21): "In 1861, the First Battle of Bull Run occurred in the American Civil War.",
    (7, 22): "In 1796, Cleveland, Ohio, was founded by Moses Cleaveland.",
    (7, 23): "In 1995, Comet Hale-Bopp was discovered.",
    (7, 24): "In 1911, Machu Picchu was rediscovered by Hiram Bingham.",
    (7, 25): "In 1894, the First Sino-Japanese War began.",
    (7, 26): "In 1948, President Truman desegregated the U.S. military.",
    (7, 27): "In 1953, the Korean War armistice was signed, ending active combat.",
    (7, 28): "In 1914, World War I officially began when Austria-Hungary declared war on Serbia.",
    (7, 29): "In 1981, Prince Charles and Lady Diana were married in St. Paul's Cathedral.",
    (7, 30): "In 1930, Uruguay won the first-ever FIFA World Cup.",
    (7, 31): "In 1971, Apollo 15 astronauts drove the first Lunar Roving Vehicle on the Moon.",
    (8, 1): "In 1981, MTV launched, marking the start of the 24-hour music video era.",
    (8, 2): "In 1990, Iraq invaded Kuwait, leading to the Gulf War.",
    (8, 3): "In 1492, Christopher Columbus set sail from Spain on his first voyage.",
    (8, 4): "In 1914, Germany invaded Belgium, starting World War I.",
    (8, 5): "In 1962, Marilyn Monroe was found dead in her Los Angeles home.",
    (8, 6): "In 1945, the U.S. dropped an atomic bomb on Hiroshima, Japan.",
    (8, 7): "In 1974, Philippe Petit walked a tightrope between the Twin Towers.",
    (8, 8): "In 2008, the Beijing Olympics opened with a spectacular ceremony.",
    (8, 9): "In 1945, the U.S. dropped an atomic bomb on Nagasaki, Japan.",
    (8, 10): "In 1792, the French monarchy was effectively overthrown.",
    (8, 11): "In 1965, the Watts Riots began in Los Angeles.",
    (8, 12): "In 1981, IBM released its first personal computer.",
    (8, 13): "In 1961, East Germany began building the Berlin Wall.",
    (8, 14): "In 1945, Japan announced its surrender in World War II.",
    (8, 15): "In 1947, India gained independence from Britain.",
    (8, 16): "In 1977, Elvis Presley was found dead in his home.",
    (8, 17): "In 1962, Peter Fechter was shot trying to cross the Berlin Wall.",
    (8, 18): "In 1920, the 19th Amendment was ratified, granting U.S. women the right to vote.",
    (8, 19): "In 2003, a deadly bombing targeted the UN headquarters in Baghdad.",
    (8, 20): "In 1977, NASA launched the Voyager 2 spacecraft.",
    (8, 21): "In 1911, the Mona Lisa was stolen from the Louvre.",
    (8, 22): "In 1642, the English Civil War began.",
    (8, 23): "In 2005, Hurricane Katrina formed over the Bahamas.",
    (8, 24): "In 79 AD, Mount Vesuvius erupted, burying Pompeii.",
    (8, 25): "In 1944, Paris was liberated from Nazi control.",
    (8, 26): "In 1920, the 19th Amendment was formally adopted.",
    (8, 27): "In 1883, Krakatoa erupted in one of the most violent eruptions in history.",
    (8, 28): "In 1963, Martin Luther King Jr. delivered his 'I Have a Dream' speech.",
    (8, 29): "In 2005, Hurricane Katrina devastated New Orleans.",
    (8, 30): "In 1999, East Timor voted for independence from Indonesia.",
    (8, 31): "In 1997, Princess Diana died in a car crash in Paris.",
    (9, 1): "In 1939, Germany invaded Poland, starting World War II.",
    (9, 2): "In 1945, Japan formally surrendered in World War II.",
    (9, 3): "In 1783, the Treaty of Paris was signed, ending the American Revolution.",
    (9, 4): "In 1957, Arkansas National Guard troops blocked school desegregation.",
    (9, 5): "In 1972, Palestinian terrorists attacked the Munich Olympics.",
    (9, 6): "In 1901, President William McKinley was shot.",
    (9, 7): "In 1813, the U.S. won the Battle of Lake Erie in the War of 1812.",
    (9, 8): "In 1966, Star Trek premiered on television.",
    (9, 9): "In 1948, North Korea was officially established.",
    (9, 10): "In 2008, the Large Hadron Collider was switched on.",
    (9, 11): "In 2001, terrorist attacks destroyed the World Trade Center and hit the Pentagon.",
    (9, 12): "In 1962, JFK delivered his 'We choose to go to the Moon' speech.",
    (9, 13): "In 1993, Israel and Palestine signed the Oslo Accords.",
    (9, 14): "In 1812, Napoleon entered Moscow during his Russian campaign.",
    (9, 15): "In 1935, the Nuremberg Laws were enacted in Nazi Germany.",
    (9, 16): "In 1620, the Mayflower set sail for America.",
    (9, 17): "In 1787, the U.S. Constitution was signed.",
    (9, 18): "In 1970, Jimi Hendrix was found dead in London.",
    (9, 19): "In 1893, New Zealand became the first country to grant women the right to vote.",
    (9, 20): "In 1519, Ferdinand Magellan set sail to circumnavigate the globe.",
    (9, 21): "In 1937, J.R.R. Tolkien's The Hobbit was published.",
    (9, 22): "In 1862, Abraham Lincoln issued the preliminary Emancipation Proclamation.",
    (9, 23): "In 1846, the planet Neptune was discovered.",
    (9, 24): "In 1948, Honda Motor Company was founded.",
    (9, 25): "In 1957, Central High School in Little Rock was desegregated.",
    (9, 26): "In 1969, The Beatles released Abbey Road.",
    (9, 27): "In 1825, the first public steam railway opened in England.",
    (9, 28): "In 1066, William the Conqueror invaded England.",
    (9, 29): "In 2008, SpaceX launched its first successful rocket.",
    (9, 30): "In 1791, Mozart's opera The Magic Flute premiered in Vienna."
    (11, 1): "In 1512, the Sistine Chapel ceiling was opened to the public.",
    (11, 2): "In 1930, the Indian freedom fighter Jawaharlal Nehru was elected as the first President of the Indian National Congress.",
    (11, 3): "In 1978, the first Camp David Accords were signed between Israel and Egypt.",
    (11, 4): "In 2008, Barack Obama was elected as the first African American president of the United States.",
    (11, 5): "In 1917, the Balfour Declaration was issued by the British government.",
    (11, 6): "In 1991, the Soviet Union launched the Soyuz TM-10 mission.",
    (11, 7): "In 1973, the Yom Kippur War officially ended.",
    (11, 8): "In 1942, the Allied forces launched Operation Torch in North Africa.",
    (11, 9): "In 1989, the Berlin Wall came down, symbolizing the end of the Cold War.",
    (11, 10): "In 1969, Sesame Street aired for the first time.",
    (11, 11): "In 1918, World War I ended with the signing of an armistice.",
    (11, 12): "In 1954, Ellis Island closed its doors after processing over 12 million immigrants.",
    (11, 13): "In 1927, the Holland Tunnel, connecting New Jersey and New York, opened.",
    (11, 14): "In 1969, Apollo 12 launched for the second manned mission to the Moon.",
    (11, 15): "In 1971, the D.B. Cooper hijacking took place.",
    (11, 16): "In 1983, the U.S. invaded Grenada in Operation Urgent Fury.",
    (11, 17): "In 1869, the Suez Canal opened.",
    (11, 18): "In 1978, the Jonestown Massacre occurred in Guyana.",
    (11, 19): "In 1863, Abraham Lincoln delivered the Gettysburg Address.",
    (11, 20): "In 1975, King Juan Carlos of Spain became the head of state.",
    (11, 21): "In 1942, the Battle of Stalingrad began during WWII.",
    (11, 22): "In 1963, President John F. Kennedy was assassinated.",
    (11, 23): "In 1945, the first United Nations General Assembly opened.",
    (11, 24): "In 1963, Jack Ruby shot and killed Lee Harvey Oswald.",
    (11, 25): "In 1927, the first Macy's Thanksgiving Day Parade was held.",
    (11, 26): "In 1977, Elvis Presley performed his last concert.",
    (11, 27): "In 1978, Harvey Milk and George Moscone were assassinated.",
    (11, 28): "In 1929, the Hoover Dam was dedicated.",
    (11, 29): "In 1972, Atari released the first commercially successful arcade video game.",
    (11, 30): "In 1954, the first-ever broadcast of the The Twilight Zone took place.",

    (12, 1): "In 1955, Rosa Parks was arrested for refusing to give up her seat on a bus in Montgomery, Alabama.",
    (12, 2): "In 1942, the first controlled nuclear chain reaction took place in Chicago.",
    (12, 3): "In 1967, the first heart transplant was performed in South Africa.",
    (12, 4): "In 1991, the Soviet Union officially recognized the independence of the Baltic States.",
    (12, 5): "In 1933, the 21st Amendment to the U.S. Constitution repealed Prohibition.",
    (12, 6): "In 1917, the Halifax Explosion, one of the largest man-made explosions, occurred.",
    (12, 7): "In 1941, the attack on Pearl Harbor occurred, leading the U.S. into World War II.",
    (12, 8): "In 1980, John Lennon was assassinated outside his apartment in New York City.",
    (12, 9): "In 1993, the Oslo Accords were signed between Israel and Palestine.",
    (12, 10): "In 1948, the Universal Declaration of Human Rights was adopted by the United Nations.",
    (12, 11): "In 1913, Henry Ford introduced the moving assembly line.",
    (12, 12): "In 1991, the first web browser, WorldWideWeb, was created by Tim Berners-Lee.",
    (12, 13): "In 2000, the United States Supreme Court ruled in Bush v. Gore.",
    (12, 14): "In 1911, the first air flight across the English Channel occurred.",
    (12, 15): "In 2001, the first Harry Potter movie, 'Harry Potter and the Sorcerer's Stone,' premiered.",
    (12, 16): "In 1773, the Boston Tea Party took place.",
    (12, 17): "In 1903, the Wright brothers made the first powered flight in Kitty Hawk.",
    (12, 18): "In 1865, the 13th Amendment to the U.S. Constitution, abolishing slavery, was ratified.",
    (12, 19): "In 1998, the U.S. House of Representatives impeached President Bill Clinton.",
    (12, 20): "In 1957, the first successful launch of a U.S. satellite, Vanguard TV3, occurred.",
    (12, 21): "In 1968, Apollo 8 became the first manned spacecraft to orbit the Moon.",
    (12, 22): "In 1807, the U.S. passed the Embargo Act, which restricted trade with foreign nations.",
    (12, 23): "In 1986, Voyager 2 made its closest approach to Uranus.",
    (12, 24): "In 1914, World War I's 'Christmas Truce' occurred.",
    (12, 25): "In 1776, George Washington crossed the Delaware River during the American Revolution.",
    (12, 26): "In 2004, the Indian Ocean earthquake and tsunami killed over 230,000 people.",
    (12, 27): "In 1932, the first issue of the famous comic book 'Action Comics' was published.",
    (12, 28): "In 1895, the first motion picture theater opened in Paris.",
    (12, 29): "In 1845, U.S. President James K. Polk announced that the United States would annex Texas.",
    (12, 30): "In 1927, the first talking motion picture, 'The Jazz Singer,' premiered.",
    (12, 31): "In 1999, the world celebrated the turn of the millennium with huge celebrations worldwide."
}

def open_fullscreen_for_calendar():
    calendar_window = tk.Toplevel(app)
    calendar_window.title("Calendar Full Screen")
    calendar_window.attributes('-fullscreen', True)
    calendar_window.configure(bg="#d3deeb")

    # Year to display the calendar
    year = 2025  # Replace with the current year dynamically if needed
    tk.Label(calendar_window, text=f"Full Year Calendar - {year}",
             font=("Times New Roman", 50), bg="#d3deeb", fg="black").pack(pady=20)

    # Frame for the calendar grid
    grid_frame = tk.Frame(calendar_window, bg="#d3deeb")
    grid_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def show_event_popup(month, day):
        """Show a popup with the event for the given date."""
        event = historical_event_cal.get((month, day), f"No historical event recorded for {month}/{day}.")
        messagebox.showinfo(f"Event on {month}/{day}", event)

    # Loop through months and arrange them in a grid (4 months per row)
    for month in range(1, 13):
        row = (month - 1) // 4  # Determine the row (0, 1, 2)
        col = (month - 1) % 4   # Determine the column (0, 1, 2, 3)

        # Month frame
        month_frame = tk.Frame(grid_frame, bg="#c8e6c9", relief="solid", borderwidth=2)
        month_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Month name
        month_name = calendar.month_name[month]
        tk.Label(month_frame, text=month_name, font=("Times New Roman", 28),
                 bg="#c8e6c9", fg="black").pack(pady=5)

        # Create buttons for each day of the month
        days_frame = tk.Frame(month_frame, bg="#c8e6c9")
        days_frame.pack()

        # Get the month's calendar as a matrix (weeks x days)
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            week_frame = tk.Frame(days_frame, bg="#c8e6c9")
            week_frame.pack()
            for day in week:
                if day == 0:  # Empty day
                    tk.Label(week_frame, text=" ", width=3, font=("Times New Roman", 16), bg="#c8e6c9").pack(side="left")
                else:  # Create a button for the day
                    tk.Button(week_frame, text=f"{day}", font=("Times New Roman", 16), width=3, bg="#a5d6a7",
                              command=lambda m=month, d=day: show_event_popup(m, d)).pack(side="left", padx=2, pady=2)

    # Configure grid to expand evenly
    for i in range(3):  # Rows (3 rows for 12 months)
        grid_frame.rowconfigure(i, weight=1)
    for j in range(4):  # Columns (4 months per row)
        grid_frame.columnconfigure(j, weight=1)

    # Exit button
    def close_calendar():
        calendar_window.destroy()

    tk.Button(calendar_window, text="Exit Fullscreen", font=("Times New Roman", 40), bg="#ffc1c1", fg="black",
              command=close_calendar).pack(pady=20)

# Open a fullscreen window for Quiz
def open_fullscreen_for_quiz():
    quiz_window = tk.Toplevel(app)
    quiz_window.title("Quiz Full Screen")
    quiz_window.attributes('-fullscreen', True)
    quiz_window.configure(bg="#d3deeb")

    quizzes = [
        {
            "question": "Who was the first human to travel into space?",
            "options": ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "John Glenn"],
            "answer": "Yuri Gagarin"
        },
        {
            "question": "In which year was the Berlin Wall constructed?",
            "options": ["1959", "1961", "1963", "1965"],
            "answer": "1961"
        },
        {
            "question": "What was the name of the first satellite launched into space?",
            "options": ["Explorer 1", "Sputnik 1", "Voyager 1", "Hubble"],
            "answer": "Sputnik 1"
        },
        {
            "question": "Who delivered the 'I Have a Dream' speech?",
            "options": ["Malcolm X", "Martin Luther King Jr.", "John F. Kennedy", "Nelson Mandela"],
            "answer": "Martin Luther King Jr."
        },
        {
            "question": "What event is considered the start of World War II?",
            "options": ["The attack on Pearl Harbor", "The invasion of Poland", "The signing of the Treaty of Versailles", "The assassination of Archduke Franz Ferdinand"],
            "answer": "The invasion of Poland"
        }
    ]

    def show_results():
        correct_count = sum([1 for i in range(len(quizzes)) if user_answers[i].get() == quizzes[i]["answer"]])
        messagebox.showinfo("Quiz Results", f"You answered {correct_count} out of {len(quizzes)} questions correctly!")

    # Add user answers storage
    user_answers = [tk.StringVar(value="") for _ in quizzes]

    # Quiz frame
    quiz_frame = tk.Frame(quiz_window, bg="#d3deeb")
    quiz_frame.pack(pady=20)

    for idx, quiz in enumerate(quizzes):
        question_label = tk.Label(quiz_frame, text=f"Q{idx + 1}. {quiz['question']}", font=("Times New Roman", 20), bg="#d3deeb", fg="black")
        question_label.pack(anchor="w", pady=10)

        for option in quiz["options"]:
            option_button = tk.Radiobutton(quiz_frame, text=option, variable=user_answers[idx], value=option,
                                           font=("Times New Roman", 18), bg="#d3deeb", fg="black", anchor="w")
            option_button.pack(anchor="w")

    # Submit button
    tk.Button(quiz_window, text="Submit", font=("Times New Roman", 20), bg="#a5d6a7", fg="black", command=show_results).pack(pady=10)

    # Exit to Main Menu button
    def exit_to_second_window():
        quiz_window.destroy()
        open_second_fullscreen_window()  # Open the second fullscreen window

    tk.Button(quiz_window, text="Exit to Main Menu", font=("Times New Roman", 20), bg="#ffc1c1", fg="black", command=exit_to_second_window).pack(pady=10)

# Open a fullscreen window for Fun Facts with space between text and left side and centered exit button
def open_fullscreen_for_fun_facts():
    fun_facts_window = tk.Toplevel(app)
    fun_facts_window.title("Fun Facts Full Screen")
    fun_facts_window.attributes('-fullscreen', True)
    fun_facts_window.configure(bg="#FFF1EE")  # Set the background color to #FFF1EE
    
    # Create a frame to hold the fun facts content
    frame = tk.Frame(fun_facts_window, bg="#FFF1EE")  # Set the background color for the frame
    frame.pack(fill="both", expand=True, padx=50, pady=20)  # Add 5cm padding (about 50 pixels on each side)
    
    # List of fun facts
    fun_facts = [
        "The Battle of Cannae (216 BCE): During the Second Punic War, Hannibal's Carthaginian army destroyed a much larger Roman",
        "force using a double-envelopment strategy.",
        "The Trojan War: The famous Trojan War may have been based on real events, but the city of Troy",
        "was believed to be a myth until it was excavated in the 19th century.",
        "The Mongol Postal System: The Mongol Empire had a highly efficient postal system,",
        "using mounted couriers to carry messages across vast distances.",
        "Ancient Egypt's Toothpaste: Ancient Egyptians used a form of toothpaste made from",
        "crushed eggshells and powdered pumice, mixed with mint or frankincense.",
        "The Great Fire of Rome (64 CE): Emperor Nero allegedly fiddled while Rome burned, though this is likely a myth.",
        "Cleopatra’s Language Skills: Cleopatra VII, the last active ruler of the Ptolemaic Kingdom of Egypt, spoke at least nine languages.",
        "Roman Concrete: Ancient Roman concrete was incredibly durable. In fact, some Roman harbors built with it are still standing today.",
        "The Samurai's Origin: The samurai, Japan's iconic warrior class,",
        "originally started as government-employed farmers and guards before evolving into an elite military force.",
        "The First Use of Chemical Warfare: The Ancient Greeks used a substance called 'Greek fire' during naval battles in the 7th century.",
        "The Library of Alexandria: The Library of Alexandria in Egypt, one of the largest libraries of the ancient world,",
        "contained hundreds of thousands of scrolls and texts.",
        "The Empire of Mali: The Mali Empire, in West Africa, was one of the wealthiest empires in history, and its ruler,",
        "Mansa Musa, is considered the richest person to have ever lived.",
        "Napoleon Bonaparte was once attacked by a horde of rabbits during a hunting event he organized.",
        "The first known vending machine was invented in the first century by Hero of Alexandria to dispense holy water.",
  

    ]
    
    # Display each fun fact with a larger font size inside the frame
    for fact in fun_facts:
        tk.Label(frame, text=fact, font=("Times New Roman", 25), bg="#FFF1EE", fg="black", anchor="w", justify="left").pack(pady=10, fill="x")
    
    # Center the Exit Fullscreen button at the bottom
    def close_fun_facts():
        fun_facts_window.destroy()

    # Create the Exit Fullscreen button and center it
    exit_button = tk.Button(fun_facts_window, text="Exit Fullscreen", font=("Times New Roman", 25), bg="#ffc1c1", fg="black", command=close_fun_facts)
    exit_button.pack(side="bottom", pady=20)


    tk.Button(fun_facts_window, text="Exit Fullscreen", font=("Times New Roman", 40), bg="#ffc1c1", fg="black", command=close_fun_facts).pack(pady=50)

# Main window setup
app = tk.Tk()
app.title("History Exploration App")
app.geometry("400x400")
app.configure(bg="#d3deeb")

# Username and year input
tk.Label(app, text="Enter your name:", font=("Times New Roman", 14), bg="#d3deeb").pack(pady=10)
username_entry = tk.Entry(app, font=("Times New Roman", 14))
username_entry.pack(pady=10)

tk.Label(app, text="Enter your year of birth:", font=("Times New Roman", 14), bg="#d3deeb").pack(pady=10)
year_entry = tk.Entry(app, font=("Times New Roman", 14))
year_entry.pack(pady=10)

# Login button
tk.Button(app, text="Login", font=("Times New Roman", 16), bg="#c8e6c9", fg="black", command=handle_login).pack(pady=20)

# Run the app
app.mainloop()         
