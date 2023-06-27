from pathlib import Path
import streamlit as st
from PIL import Image
import requests

current_dir = Path.cwd()

PAGE_TITLE = "CV | Szymon Krasnodębski"
PAGE_ICON = "\U0001F4BB"

css_code = """
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');


* {font-family: 'Readex Pro';}

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

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.markdown("<style>{}</style>".format(css_code), unsafe_allow_html=True)

st.markdown("<script>{}</script>".format(javascript_code), unsafe_allow_html=True)

loader = st.empty()
loader.markdown("""<div class="loader"></div>""", unsafe_allow_html=True)

st.markdown(google_analytics_script, unsafe_allow_html=True)



resume_file = current_dir / "assets" / "cv_szymon_krasnodebski.pdf"
profile_pic = current_dir / "assets" / "pic2.png"
pdf_symbol = "\U0001F4C4"
NAME = "Szymon Krasnodębski"
DESCRIPTION = """Sprzedawca E-commerce | Doradca Klienta"""
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
profile_pic = Image.open(profile_pic)
st.write("#")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)
with col2:
    st.title(NAME)
    st.write(f'<p style="font-size:22px;">{DESCRIPTION}</p>', unsafe_allow_html=True)
    st.download_button(
        label=pdf_symbol + " Pobierz PDF",
        data=PDFbyte,
        file_name="cv_szymon_krasnodebski.pdf",
        mime="application/octet-stream",
    )
    st.write("\U0001F4F1 " + PHONE)
    st.markdown('<span style="white-space: nowrap;">\u2709 {}</span>'.format(EMAIL), unsafe_allow_html=True)
    col3, col4 = st.columns([1, 20])
    with col3:
        st.image(linkedin_image, width=20)
    with col4:
        st.markdown(f"[Linkedin]({linkedin_link})")
st.write("#")
st.subheader("Doświadczenie i kwalifikacje")
st.write(
    """
- \u2713 2 lata doświadczenia w branży odzieżowej
- \u2713 Zawsze na bieżąco z aktualnymi trendami
- \u2713 Bogate doświadczenie w obsłudze klienta
- \u2713 Łącznie ponad 600 pozytywnych ocen na takich portalach jak: Vinted, Grailed, OLX, Allegro, Ebay, Vestiaire Collective
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
    
st.write("#")
st.subheader("Umiejętności")
st.write(
    """
- \U0001F464\U0000200D\U0001F4AC\U0000200D\U0001F464 Nawiązywanie kontaktu z klientem, 
pozyskiwanie nowych klientów 
oraz tworzenie bazy klientów
- \U0001F454 Znajomość branży odzieżowej - rozróżnianie replik od oryginalnych produktów, zawsze na bieżąco z aktualnymi trendami
- \U0001F9D1\u200D\U0001F4BB Podstawy programowania i umiejętności informatyczne: Python, JS, CSS, HTML, Excel
- \U0001F4B3 Obsługa kasy i terminalu płatniczego
- \U0001F69A Wysokie kwalifikacje logistyczne
- \U0001F1EC\U0001F1E7 Język angielski - poziom rozszerzony maturalny
- \U0001F697 Prawo jazdy kat. B
"""
)

st.write("#")
st.subheader("Portfolio/Projekty Front-endowe")
st.write("---")

with st.expander("Sklep Internetowy E-commerce Website Concept"):
    st.markdown("""<iframe src="https://e-commerce-website-bidlit-1445e3fe9c04.herokuapp.com/" width="1400" height="1080" style="position:relative; left:-350px;"></iframe>""", unsafe_allow_html=True)


with st.expander("DZIK ENERGY Website Slider Concept"):
  st.markdown('<iframe src="https://dzik-energy-slider-3a343de5cd11.herokuapp.com/" width="1400" height="800" style="position:relative; left:-350px;"></iframe>', unsafe_allow_html=True)


st.write("#")
st.subheader("Doświadczenie zawodowe")
st.write("---")
st.write("**Własna działalność | BidLit Szymon Krasnodębski**")
st.write("07/2020 - Teraz")
st.write(
    """
- \u25B6 Sprzedaż internetowa/E-commerce - sprzedaż detaliczna odzieży i akcesoriów
- \u25B6 Prowadzenie strony internetowej
- \u25B6 Międzynarodowa wysyłka towarów
- \u25B6 Stały kontakt z klientem w języku polskim i angielskim
- \u25B6 Zarządzanie i optymalizacja wydajnością pracy
- \u25B6 Sprowadzanie/Importowanie towarów z zagranicy
- \u25B6 Nawiązywanie relacji z dostawcami
- \u25B6 Dbanie o estetykę ogłoszeń i sprzedawanych produktów
- \u25B6 Rozwój działalności, otwartość na nowe propozcyje i rozwiązania
"""
)

st.write("---")
st.write("#")
st.write("**Junior/Praktykant ds. Logistyki | Prymat Sp. z o.o.**")
st.write("04/2021 - 06/2021")
st.write(
    """
- \u25B6 Wypisywanie listów przewozowych
- \u25B6 Podstawy obsługi programu SAP
- \u25B6 Dbanie o porządek i przejrzystość w dokumentach logistycznych
- \u25B6 Przyjmowanie zleceń od klientów
- \u25B6 Aktualizowanie danych w Excelu
- \u25B6 Pomoc fizyczna w magazynie
- \u25B6 Praca w grupie pod presją czasową
- \u25B6 Wydawanie towarów do transportu
"""
)
st.write("---")
st.write('<span style="font-size: 12px;">Wyrażam zgodę na przetwarzanie moich danych osobowych dla potrzeb niezbędnych do realizacji procesu rekrutacji zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (RODO).</span>', unsafe_allow_html=True)
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
                                    headers={"Referer": "https://cv-szymon-krasnodebski.onrender.com/"})
            
            if response.status_code == 200:
                st.success("Wiadomość wysłana \U0001F44D")
            else:
                st.error("Wystąpił błąd podczas wysyłania wiadomości")
        except Exception as e:
            st.error(f"Wystąpił błąd podczas wysyłania wiadomości: {e}")
    else:
        st.warning("Proszę wypełnić wszystkie pola")

loader.empty()
