from pathlib import Path
import streamlit as st
from PIL import Image
import requests
import base64

current_dir = Path.cwd()

PAGE_TITLE = "CV | Szymon Krasnodębski"
PAGE_ICON = "👨‍💻"

css_code = """
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');


* {font-family: 'Readex Pro';}
 body {
        cursor: default !important;
    }

a {
    text-decoration: none;
    color: white !important;
    font-weight: 500;
}

a:hover {
    color: #d33682 !important;
    text-decoration: none;
}

ul {list-style-type: none;}

hr {
    margin-top: 0px;
    margin-bottom: 5%;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.loader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: opacity 0.75s, visibility 0.75s;
    z-index: 9999;
}
.loader::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.25));
}

.loader-hidden {
    opacity: 0;
    visibility: hidden;
}
    
.loader::after {
    content: "";
    width: 35px;
    height: 35px;
    border: 7.5px solid #dddddd;
    border-top-color: #021f26;
    border-radius: 50%;
    animation: loading 0.75s ease infinite;
}

@keyframes loading {
    from {
        transform: rotate(0turn);
    }
    to {
        transform: rotate(1turn);
    }
}

"""


javascript_code = """
    window.addEventListener("load", () => {
        const loader = document.querySelector(".loader");

        loader.classList.add("loader-hidden");

        setTimeout(() => {
            document.body.removeChild(loader);
        }, 750);
    });
"""


google_analytics_script = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-D1E02SED5V"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-D1E02SED5V');
    </script>
"""


javascript_code2 = """
<script type="text/javascript">
  function handleError(element) {
    element.src='https://www.youtube.com/embed/aUBMSPN18es?autoplay=1&mute=1&controls=0&showinfo=0&loop=1&playlist=aUBMSPN18es';
  }
</script>
"""

html_code2 = """
<div style="position: relative; z-index: 2;">
    <div style="position: absolute; z-index: 1; top: 30px; left: 160px;">
        <iframe src="https://www.youtube.com/embed/aUBMSPN18es?autoplay=1&mute=1&controls=0&showinfo=0&loop=1&playlist=aUBMSPN18es" style="width: 360px; height: 760px; border-radius: 30px;" frameborder="0" onError="handleError(this)"></iframe>
    </div>
    <div style="background-image: url('data:image/png;base64,{}'); width: 1076px; height: 1628px; position: relative; transform: scale(0.428); top:-400px; left:-200px; z-index: 2; pointer-events: none;"></div>
</div>
"""


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.markdown("<style>{}</style>".format(css_code), unsafe_allow_html=True)

st.markdown("<script>{}</script>".format(javascript_code), unsafe_allow_html=True)

loader = st.empty()
loader.markdown("""<div class="loader"></div>""", unsafe_allow_html=True)

st.markdown(google_analytics_script, unsafe_allow_html=True)


iphone = current_dir / "assets" / "iphone.png"

def get_image_base64(iphone):
    with open(iphone, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf8")
    
image_base64 = get_image_base64(iphone)
final_code = javascript_code2 + html_code2.format(image_base64)

resume_file = current_dir / "assets" / "resume_szymon_krasnodebski.pdf"
matura_file = current_dir / "assets" / "matura2023.pdf"
dyplom_file = current_dir / "assets" / "dyplom_oke.pdf"
profile_pic = current_dir / "assets" / "pic2.png"
pdf_symbol = "📄"
pdf_symbol2 = "📑"
NAME = "Szymon Krasnodębski"
DESCRIPTION = """Retail E-commerce <br> Junior Full-Stack Developer"""
STUDIES = """Student na wydziale Inżynierii Mechanicznej w WAT na kierunku Mechanika i Budowa Maszyn"""
EMAIL = "szymon.natalian.krasnodebski@gmail.com"
PHONE = "536 579 591"
LINKEDIN = {"Linkedin": "http://www.linkedin.com/in/szymon-krasnodębski"}
SOCIAL_MEDIA = {
    "Vinted": "https://www.vinted.pl/member/90985178-bidlit",
    "Grailed": "https://www.grailed.com/BidLit",
    "OLX": "https://www.olx.pl/oferty/user/H6WHx/",
    "Allegro": "https://allegrolokalnie.pl/uzytkownik/BidLit",
    "Ebay": "https://www.ebay.pl/usr/bidlit",
    "Vestiaire": "https://www.vestiairecollective.com/members/profile-17490614.shtml#sell"
}
image_path = current_dir / "assets" / "linkedin.png"
linkedin_image = Image.open(image_path)
linkedin_image = linkedin_image.resize((16, 16))
linkedin_link = "http://www.linkedin.com/in/szymon-krasnodębski"
Vinted = Image.open(current_dir / "assets" / "vinteddd.png")
Vinted = Vinted.resize((16, 16))
Grailed = Image.open(current_dir / "assets" / "graileddd.jpg")
Grailed = Grailed.resize((16, 16))
Olx = Image.open(current_dir / "assets" / "olxxx.png")
Olx = Olx.resize((16, 16))
Allegro = Image.open(current_dir / "assets" / "allegrooo.png")
Allegro = Allegro.resize((16, 16))
Ebay = Image.open(current_dir / "assets" / "ebayyy.png")
Ebay = Ebay.resize((16, 16))
Vestiaire = Image.open(current_dir / "assets" / "vestiaireee.png")
Vestiaire = Vestiaire.resize((16, 16))
image_mapping = {
    "Vinted": Vinted,
    "Grailed": Grailed,
    "OLX": Olx,
    "Allegro": Allegro,
    "Ebay": Ebay,
    "Vestiaire": Vestiaire
}
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(matura_file, "rb") as pdf_file2:
    PDFbyte2 = pdf_file2.read()

with open(dyplom_file, "rb") as pdf_file3:
    PDFbyte3 = pdf_file3.read()
profile_pic = Image.open(profile_pic)
st.write("#")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)
with col2:
    st.title(NAME)
    st.write(f'<p style="font-size:22px;">{DESCRIPTION}</p>', unsafe_allow_html=True)
    st.write(f'<p style="font-size:14px;">{STUDIES}</p>', unsafe_allow_html=True)
    st.download_button(
        label=pdf_symbol + " Pobierz PDF",
        data=PDFbyte,
        file_name="cv_szymon_krasnodebski.pdf",
        mime="application/octet-stream",
    )
    st.download_button(
        label=pdf_symbol2 + " Świadectwo dojrzałości",
        data=PDFbyte2,
        file_name="swiadectwo_dojrzalosci_szymon_krasnodebski.pdf",
        mime="application/octet-stream",
    )
    # st.download_button(
    #     label=pdf_symbol + "Dyplom zawodowy",
    #     data=PDFbyte3,
    #     file_name="dyplom_zawodowy_szymon_krasnodebski.pdf",
    #     mime="application/octet-stream",
    # )
    st.write("\U0001F4F1 " + PHONE)
    st.markdown('<span style="white-space: nowrap;">\u2709 {}</span>'.format(EMAIL), unsafe_allow_html=True)
    col3, col4 = st.columns([1, 20])
    with col3:
        st.image(linkedin_image, width=20)
    with col4:
        st.markdown(f"[Linkedin]({linkedin_link})")
st.write("#")
st.subheader("Doświadczenie i kwalifikacje")
st.write("---")
st.write(
    """
- \u2713 3 lata doświadczenia w branży odzieżowej, IT/E-commerce
- \u2713 Zawsze na bieżąco z aktualnymi trendami
- \u2713 Bogate doświadczenie w obsłudze klienta, tworzeniu aplikacji i stron internetowych
- \u2713 Zaawansowane umiejętności w automatyzacji procesów w biznesie
"""
)

st.write("#")
st.subheader("Umiejętności")
st.write("---")
st.write(
    """
- 🧑‍💻 Programowanie i umiejętności informatyczne: Python, JavaScript, Node.js, Express.js, React, React Native, TypeScript, HTML, CSS, Microsoft Clipchamp, DaVinci Resolve, MySQL, Excel
- 🖱️ Znajomość branży IT - na bieżąco z nowinkami i nowoczesnymi rozwiązaniami technologicznymi
- ⚙️ Umiejętność stosowania specjalistycznych API i narzędzi informatycznych w celu efektywnej automatyzacji procesów w biznesie
- ⌨️ Doświadczenie w tworzeniu: responsywnych interfejsów użytkownika, UX/UI Design, aplikacji mobilnych w React Native, aplikacji webowych, integracji z bazami danych MySQL
- \U0001F1EC\U0001F1E7 Język angielski - poziom rozszerzony maturalny (B2+); Matura pisemna 82%, ustna 93%
"""
)

st.write("#")
st.subheader("Portfolio/Projekty Front-endowe spersonalizowane dla firmy WK Sp. z o.o.")
st.write("---")

with st.expander("Sklep Internetowy (Website Concept) - WKDZIK®"):
    st.markdown("""<iframe src="https://wkdzik-d33ce975e6fa.herokuapp.com/" width="1500px" height="900px" style="position:relative; left:-400px; border-radius:20px;"></iframe>""", unsafe_allow_html=True)


with st.expander("Aplikacja Android/iOS (App Concept, prezentacja wideo) - WKDZIK®"):
        
        st.write("#")
        st.markdown(
            """
            <style>
            .text2 {
                text-align: center;
                font-size: 16px;
            }
            </style>
            <div class="text2">Jeśli wideo się nie odtwarza proszę odświeżyć stronę lub odnaleźć w serwisie YouTube: <br> https://www.youtube.com/watch?v=aUBMSPN18es</div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("#")
        st.markdown(
            """
            <style>
            .center-text {
                text-align: center;
                font-size: 12px;
            }
            </style>
            <div class="center-text">Żeby przewijać lub zatrzymywać wideo, należy kliknąć w wideo, następnie za pomocą klawiatury <br> (J - do tyłu, K - pauza, L - do przodu)</div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(final_code, unsafe_allow_html=True)


st.write("#")
st.subheader("Doświadczenie zawodowe")
st.write("---")
st.write("**Własna działalność | BidLit Szymon Krasnodębski**")
st.write("07/2020 - 06/2023")
st.write(
    """
- \u25B6 Sprzedaż internetowa/E-commerce - sprzedaż detaliczna odzieży i akcesoriów
- \u25B6 Tworzenie i prowadzenie własnej strony internetowej
- \u25B6 Zarządzanie stanami magazynowymi
- \u25B6 Międzynarodowa wysyłka towarów
- \u25B6 Stały kontakt z klientem w języku polskim i angielskim
- \u25B6 Zarządzanie i optymalizacja wydajnością pracy
- \u25B6 Sprowadzanie/Importowanie towarów z zagranicy
- \u25B6 Nawiązywanie relacji z dostawcami
- \u25B6 Dbanie o estetykę ogłoszeń i sprzedawanych produktów
- \u25B6 Rozwój działalności, otwartość na nowe propozcyje i rozwiązania
- \u25B6 3 lata doświadczenia w branży odzieżowej
- \u25B6 Bogate doświadczenie w obsłudze klienta
- \u25B6 Łącznie ponad 700 pozytywnych ocen na takich platformach jak: Vinted, Grailed, OLX, Allegro, Ebay, Vestiaire Collective
"""
)

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    image_col, text_col = cols[index].columns([1, 5])
    with image_col:
        st.image(image_mapping[platform], width=20)
    with text_col:
        st.markdown(f"[{platform}]({link})")

st.write("---")
st.write('<span style="font-size: 12px;">Wyrażam zgodę na przetwarzanie moich danych osobowych przez WK Sp. z o.o. dla potrzeb niezbędnych do realizacji procesu rekrutacji zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (RODO).</span>', unsafe_allow_html=True)
st.write("#")
st.write("#")
st.write("#")
st.write("#")

st.header("Zostaw wiadomość")
email = st.text_input("E-mail")
message = st.text_area("Wiadomość")
submit = st.button("Wyślij")
if submit:
    if email and message:
        try:
            data = {
                "email": email,
                "message": message
            }
            response = requests.post(f"https://formspree.io/f/xlekywoy",
                                    data=data,
                                    headers={"Referer": "https://resume-szymon-krasnodebski.onrender.com/"})
            
            if response.status_code == 200:
                st.success("Wiadomość wysłana \U0001F44D")
            else:
                st.error("Wystąpił błąd podczas wysyłania wiadomości")
        except Exception as e:
            st.error(f"Wystąpił błąd podczas wysyłania wiadomości: {e}")
    else:
        st.warning("Proszę wypełnić wszystkie pola")

loader.empty()