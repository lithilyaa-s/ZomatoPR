def load_css():
    return """
    <style>

    /* =====================================================
       IMPORT FONT
    ===================================================== */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]{
        font-family:'Inter',sans-serif;
    }

    /* =====================================================
       APP
    ===================================================== */

    .stApp{
        background:#0F1117;
        color:#FFFFFF;
    }

    #MainMenu,
    footer,
    header{
        visibility:hidden;
    }

    section[data-testid="stSidebar"]{
        display:none;
    }

    .block-container{
        max-width:1200px;
        padding-top:2rem;
        padding-bottom:3rem;
    }

    /* =====================================================
       HERO
    ===================================================== */

    .hero-title{
        font-size:48px;
        font-weight:700;
        text-align:center;
        color:white;
        margin-bottom:8px;
    }

    .hero-subtitle{
        text-align:center;
        color:#9CA3AF;
        font-size:18px;
        margin-bottom:45px;
    }

    /* =====================================================
       CARDS
    ===================================================== */

    .card{

        background:#161B22;

        border:1px solid #262C36;

        border-radius:18px;

        padding:24px;

        margin-bottom:20px;
    }

    .card-title{
        font-size:15px;
        color:#9CA3AF;
        margin-bottom:12px;
    }

    .card-value{
        font-size:34px;
        font-weight:700;
        color:white;
    }

    /* =====================================================
       PREDICTION
    ===================================================== */

    .prediction{

        background:#161B22;

        border:1px solid #D4A017;

        border-radius:18px;

        text-align:center;

        padding:30px;

        margin-top:30px;
    }

    .prediction-label{
        color:#9CA3AF;
        font-size:16px;
    }

    .prediction-value{

        font-size:60px;

        color:#D4A017;

        font-weight:700;
    }

    /* =====================================================
       BUTTON
    ===================================================== */

    .stButton>button{

        width:100%;

        height:54px;

        border-radius:14px;

        border:none;

        background:#D4A017;

        color:black;

        font-weight:600;

        font-size:17px;

    }

    .stButton>button:hover{

        background:#E8B923;

    }

    /* =====================================================
       INPUTS
    ===================================================== */

    .stTextArea textarea,
    .stSelectbox,
    .stNumberInput{

        border-radius:12px;

    }

    </style>
    """