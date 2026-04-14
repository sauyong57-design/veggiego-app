import streamlit as st

st.set_page_config(
    page_title="VeggieGo Healthy Corner",
    page_icon="🥬",
    layout="centered",
)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #f6fff7 0%, #ffffff 50%, #f7fff4 100%) !important;
        color: #0f172a !important;
    }

    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #f6fff7 0%, #ffffff 50%, #f7fff4 100%) !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    div[data-testid="stSidebar"] {
        display: none;
    }

    .block-container {
        max-width: 460px;
        padding-top: 0.7rem;
        padding-bottom: 2rem;
    }

    .app-shell {
        background: white;
        border-radius: 32px;
        border: 1px solid #dfe7df;
        box-shadow: 0 16px 40px rgba(0,0,0,0.10);
        overflow: hidden;
        margin-bottom: 18px;
    }

    .grab-header {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #00b14f 0%, #16c35b 45%, #39d66f 100%);
        color: white !important;
        padding: 24px 18px 34px 18px;
    }

    .grab-header * {
        color: white !important;
    }

    .grab-header::before {
        content: "";
        position: absolute;
        bottom: -45px;
        left: -20px;
        width: 120%;
        height: 90px;
        background: rgba(255,255,255,0.18);
        border-radius: 50%;
        transform: rotate(-2deg);
    }

    .grab-header::after {
        content: "";
        position: absolute;
        bottom: -60px;
        right: -30px;
        width: 90%;
        height: 100px;
        background: rgba(255,255,255,0.10);
        border-radius: 50%;
        transform: rotate(4deg);
    }

    .app-title {
        position: relative;
        z-index: 2;
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 4px;
        line-height: 1.05;
        letter-spacing: -0.3px;
    }

    .app-subtitle {
        position: relative;
        z-index: 2;
        font-size: 15px;
        opacity: 0.98;
        line-height: 1.45;
        max-width: 95%;
    }

    .pill-row {
        position: relative;
        z-index: 2;
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-top: 14px;
    }

    .pill {
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.28);
        color: white !important;
        padding: 7px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        backdrop-filter: blur(4px);
    }

    .section-card {
        background: white !important;
        color: #0f172a !important;
        padding: 16px;
        border-radius: 22px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 14px;
        border: 1px solid #e7eee7;
    }

    .section-card * {
        color: #0f172a !important;
    }

    .soft-green {
        background: linear-gradient(135deg, #ecfdf3, #d8fae6) !important;
    }

    .soft-yellow {
        background: linear-gradient(135deg, #fffce8, #fde68a) !important;
    }

    .soft-blue {
        background: linear-gradient(135deg, #eef7ff, #d9ebff) !important;
    }

    .soft-orange {
        background: linear-gradient(135deg, #fff6ee, #ffd8b5) !important;
    }

    .metric-card {
        padding: 14px;
        border-radius: 18px;
        text-align: center;
        font-weight: 700;
        min-height: 96px;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.35);
    }

    .metric-label {
        font-size: 13px;
        color: #334155 !important;
        margin-top: 6px;
        font-weight: 700;
    }

    .metric-value {
        font-size: 24px;
        color: #0f172a !important;
        font-weight: 800;
        line-height: 1.1;
    }

    .meal-card {
        background: white !important;
        color: #0f172a !important;
        border-radius: 24px;
        padding: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        margin-bottom: 12px;
    }

    .meal-card * {
        color: #0f172a !important;
    }

    .meal-title {
        font-size: 20px;
        font-weight: 800;
        margin-top: 4px;
        line-height: 1.2;
        letter-spacing: -0.2px;
    }

    .meal-meta {
        color: #475569 !important;
        font-size: 14px;
        margin: 6px 0 8px 0;
        font-weight: 600;
    }

    .meal-desc {
        font-size: 15px;
        color: #1f2937 !important;
        line-height: 1.55;
    }

    .badge {
        display: inline-block;
        padding: 6px 11px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    .badge-green {
        background: #dcfce7;
        color: #166534 !important;
    }

    .badge-blue {
        background: #dbeafe;
        color: #1d4ed8 !important;
    }

    .badge-orange {
        background: #ffedd5;
        color: #c2410c !important;
    }

    .reward-card {
        border-radius: 20px;
        padding: 15px;
        background: linear-gradient(135deg, #faf5ff, #ede9fe) !important;
        border: 1px solid #ddd6fe;
        margin-bottom: 10px;
        color: #0f172a !important;
    }

    .reward-card * {
        color: #0f172a !important;
    }

    .small-muted {
        color: #475569 !important;
        font-size: 14px;
        line-height: 1.5;
    }

    .featured-banner {
        border-radius: 24px;
        padding: 17px;
        background: linear-gradient(135deg, #0f172a, #334155);
        color: white !important;
        margin-bottom: 14px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.15);
    }

    .featured-banner * {
        color: white !important;
    }

    .image-card {
        background: white !important;
        border-radius: 24px;
        padding: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 18px rgba(0,0,0,0.05);
        margin-bottom: 12px;
    }

    .bottom-note {
        color: #475569 !important;
        font-size: 13px;
        text-align: center;
        margin-top: 12px;
        font-weight: 600;
    }

    .stButton > button {
        border-radius: 16px !important;
        font-size: 15px !important;
        font-weight: 800 !important;
        padding: 0.78rem 1rem !important;
        border: none !important;
        background: linear-gradient(135deg, #00b14f, #16c35b) !important;
        color: white !important;
        box-shadow: 0 8px 18px rgba(0, 177, 79, 0.18) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #009846, #12b356) !important;
        color: white !important;
    }

    label, p, h1, h2, h3, h4, h5, h6, span, div, li {
        color: #0f172a;
    }

    .stSelectbox label, .stSlider label, .stRadio label {
        font-size: 15px !important;
        font-weight: 800 !important;
        color: #0f172a !important;
    }

    .stMarkdown p, .stMarkdown li {
        font-size: 15px !important;
        color: #1f2937 !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background: white !important;
        color: #0f172a !important;
        border: 1px solid #d1d5db !important;
    }

    div[role="radiogroup"] > label {
        background: #ffffff !important;
        border: 1px solid #dbe4db !important;
        border-radius: 999px;
        padding: 7px 12px;
        margin-right: 6px;
        color: #0f172a !important;
    }
            /* Fix dropdown main box */
    .stSelectbox div[data-baseweb="select"] > div {
        background: white !important;
        color: #0f172a !important;
        border: 1px solid #d1d5db !important;
    }

/* Fix dropdown menu (expanded list) */
    div[data-baseweb="popover"] {
        background: white !important;
    }

    div[data-baseweb="menu"] {
        background: white !important;
        color: #0f172a !important;
    }

    /* Fix each option */
    div[role="option"] {
        background: white !important;
        color: #0f172a !important;
    }

    /* Hover effect */
    div[role="option"]:hover {
        background: #ecfdf5 !important;
        color: #0f172a !important;
    }
</style>
""", unsafe_allow_html=True)
import streamlit as st

st.set_page_config(
    page_title="VeggieGo Healthy Corner",
    page_icon="🥬",
    layout="centered",
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background: linear-gradient(180deg, #f5fff7 0%, #ffffff 50%, #f7fff4 100%);
    }

    .block-container {
        max-width: 460px;
        padding-top: 0.7rem;
        padding-bottom: 2rem;
    }

    div[data-testid="stSidebar"] {
        display: none;
    }

    .app-shell {
        background: white;
        border-radius: 32px;
        border: 1px solid #dfe7df;
        box-shadow: 0 16px 40px rgba(0,0,0,0.10);
        overflow: hidden;
        margin-bottom: 18px;
    }

    .grab-header {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #00b14f 0%, #16c35b 45%, #39d66f 100%);
        color: white;
        padding: 24px 18px 34px 18px;
    }

    .grab-header::before {
        content: "";
        position: absolute;
        bottom: -45px;
        left: -20px;
        width: 120%;
        height: 90px;
        background: rgba(255,255,255,0.18);
        border-radius: 50%;
        transform: rotate(-2deg);
    }

    .grab-header::after {
        content: "";
        position: absolute;
        bottom: -60px;
        right: -30px;
        width: 90%;
        height: 100px;
        background: rgba(255,255,255,0.10);
        border-radius: 50%;
        transform: rotate(4deg);
    }

    .app-title {
        position: relative;
        z-index: 2;
        font-size: 32px;
        font-weight: 800;
        margin-bottom: 4px;
        line-height: 1.05;
        letter-spacing: -0.3px;
    }

    .app-subtitle {
        position: relative;
        z-index: 2;
        font-size: 15px;
        opacity: 0.98;
        line-height: 1.45;
        max-width: 95%;
    }

    .pill-row {
        position: relative;
        z-index: 2;
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-top: 14px;
    }

    .pill {
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.28);
        color: white;
        padding: 7px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        backdrop-filter: blur(4px);
    }

    .section-card {
        background: white;
        padding: 16px;
        border-radius: 22px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 14px;
        border: 1px solid #e7eee7;
    }

    .soft-green {
        background: linear-gradient(135deg, #ecfdf3, #d8fae6);
    }

    .soft-yellow {
        background: linear-gradient(135deg, #fffce8, #fde68a);
    }

    .soft-blue {
        background: linear-gradient(135deg, #eef7ff, #d9ebff);
    }

    .soft-orange {
        background: linear-gradient(135deg, #fff6ee, #ffd8b5);
    }

    .metric-card {
        padding: 14px;
        border-radius: 18px;
        text-align: center;
        font-weight: 700;
        min-height: 96px;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.35);
    }

    .metric-label {
        font-size: 13px;
        color: #334155;
        margin-top: 6px;
        font-weight: 700;
    }

    .metric-value {
        font-size: 24px;
        color: #0f172a;
        font-weight: 800;
        line-height: 1.1;
    }

    .meal-card {
        background: white;
        border-radius: 24px;
        padding: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        margin-bottom: 12px;
    }

    .meal-title {
        font-size: 20px;
        font-weight: 800;
        color: #0f172a;
        margin-top: 4px;
        line-height: 1.2;
        letter-spacing: -0.2px;
    }

    .meal-meta {
        color: #475569;
        font-size: 14px;
        margin: 6px 0 8px 0;
        font-weight: 600;
    }

    .meal-desc {
        font-size: 15px;
        color: #1f2937;
        line-height: 1.55;
    }

    .badge {
        display: inline-block;
        padding: 6px 11px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    .badge-green {
        background: #dcfce7;
        color: #166534;
    }

    .badge-blue {
        background: #dbeafe;
        color: #1d4ed8;
    }

    .badge-orange {
        background: #ffedd5;
        color: #c2410c;
    }

    .reward-card {
        border-radius: 20px;
        padding: 15px;
        background: linear-gradient(135deg, #faf5ff, #ede9fe);
        border: 1px solid #ddd6fe;
        margin-bottom: 10px;
    }

    .small-muted {
        color: #475569;
        font-size: 14px;
        line-height: 1.5;
    }

    .featured-banner {
        border-radius: 24px;
        padding: 17px;
        background: linear-gradient(135deg, #0f172a, #334155);
        color: white;
        margin-bottom: 14px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.15);
    }

    .image-card {
        background: white;
        border-radius: 24px;
        padding: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 18px rgba(0,0,0,0.05);
        margin-bottom: 12px;
    }

    .bottom-note {
        color: #475569;
        font-size: 13px;
        text-align: center;
        margin-top: 12px;
        font-weight: 600;
    }

    .stButton > button {
        border-radius: 16px !important;
        font-size: 15px !important;
        font-weight: 800 !important;
        padding: 0.78rem 1rem !important;
        border: none !important;
        background: linear-gradient(135deg, #00b14f, #16c35b) !important;
        color: white !important;
        box-shadow: 0 8px 18px rgba(0, 177, 79, 0.18) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #009846, #12b356) !important;
        color: white !important;
    }

    .stSelectbox label, .stSlider label, .stRadio label {
        font-size: 15px !important;
        font-weight: 800 !important;
        color: #0f172a !important;
    }

    .stMarkdown p, .stMarkdown li {
        font-size: 15px !important;
        color: #1f2937 !important;
    }

    div[role="radiogroup"] > label {
        background: #ffffff;
        border: 1px solid #dbe4db;
        border-radius: 999px;
        padding: 7px 12px;
        margin-right: 6px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# DATA
# -----------------------------
LEVELS = {
    1: {
        "name": "No Taste",
        "summary": "Almost invisible vegetables",
        "description": "Meals are mild and beginner-friendly, with vegetables hidden or softened in flavour.",
        "color": "soft-green"
    },
    2: {
        "name": "Hidden Veggies",
        "summary": "Veg inside familiar meals",
        "description": "Vegetables are mixed into familiar foods so the meal still feels normal and comforting.",
        "color": "soft-blue"
    },
    3: {
        "name": "Getting Used To It",
        "summary": "Balanced taste adaptation",
        "description": "Vegetables become more noticeable, but meals are still easy to enjoy.",
        "color": "soft-yellow"
    },
    4: {
        "name": "Stronger Veg",
        "summary": "Confident veggie meals",
        "description": "Meals now have stronger and more visible vegetable flavours for confident users.",
        "color": "soft-orange"
    },
}

FOOD_MENUS = [
    {
        "Meal": "Cheesy Veggie Mac & Cheese",
        "Level": 1,
        "Shop": "VeggieGo Kitchen",
        "ETA": "20–30 min",
        "Calories": 480,
        "Points": 18,
        "Description": "Creamy, comforting mac and cheese packed with hidden vegetables."
    },
    {
        "Meal": "Sweet Corn Veggie Fritters",
        "Level": 1,
        "Shop": "VeggieGo Kitchen",
        "ETA": "15–25 min",
        "Calories": 360,
        "Points": 16,
        "Description": "Crispy outside, soft inside, and perfect for beginners."
    },
    {
        "Meal": "Veggie Paneer Wrap",
        "Level": 2,
        "Shop": "VeggieGo Kitchen",
        "ETA": "20–30 min",
        "Calories": 430,
        "Points": 20,
        "Description": "High-protein wrap loaded with vegetables and familiar flavours."
    },
    {
        "Meal": "Hidden Veg Tomato Pasta",
        "Level": 2,
        "Shop": "VeggieGo Kitchen",
        "ETA": "20–30 min",
        "Calories": 500,
        "Points": 20,
        "Description": "Vegetables blended into a rich tomato sauce that still tastes familiar."
    },
    {
        "Meal": "Veggie Stir Fry with Tofu",
        "Level": 3,
        "Shop": "VeggieGo Kitchen",
        "ETA": "25–35 min",
        "Calories": 510,
        "Points": 24,
        "Description": "Colourful vegetables with tofu in a savoury stir fry."
    },
    {
        "Meal": "Lentil Veggie Bowl",
        "Level": 3,
        "Shop": "VeggieGo Kitchen",
        "ETA": "25–35 min",
        "Calories": 530,
        "Points": 24,
        "Description": "Hearty, wholesome bowl that keeps you full for longer."
    },
    {
        "Meal": "Quinoa Veggie Power Bowl",
        "Level": 4,
        "Shop": "VeggieGo Kitchen",
        "ETA": "25–35 min",
        "Calories": 540,
        "Points": 28,
        "Description": "Superfood bowl loaded with nutrients and stronger vegetable flavours."
    },
    {
        "Meal": "Veggie Thai Curry with Rice",
        "Level": 4,
        "Shop": "VeggieGo Kitchen",
        "ETA": "25–35 min",
        "Calories": 560,
        "Points": 28,
        "Description": "Aromatic Thai-style curry with visible vegetables and rich flavour."
    },
]

DRINK_RECIPES = [
    {"Drink": "Orange Carrot Tomato", "Ingredients": "2 oranges, 2 carrots, 1 tomato"},
    {"Drink": "Pineapple Cucumber Mint", "Ingredients": "1 cup pineapple, 1/2 cucumber, mint leaves"},
    {"Drink": "Watermelon Mint Lime", "Ingredients": "2 cups watermelon, mint leaves, 1/2 lime"},
    {"Drink": "Orange Spinach Apple", "Ingredients": "2 oranges, 1 handful spinach, 1 apple"},
    {"Drink": "Kiwi Spinach Apple", "Ingredients": "2 kiwis, 1 handful spinach, 1 apple"},
    {"Drink": "Apple Carrot Ginger", "Ingredients": "2 apples, 2 carrots, small piece ginger"},
    {"Drink": "Mango Carrot Orange", "Ingredients": "1 mango, 1 carrot, 1 orange"},
    {"Drink": "Beetroot Apple Orange", "Ingredients": "1/2 beetroot, 1 apple, 1 orange"},
]

MEAL_KITS = {
    "Cheesy Veggie Mac & Cheese Kit": {
        "shop": "NTUC Online",
        "points": 20,
        "ingredients": ["Macaroni", "Carrot", "Cauliflower", "Cheese", "Milk", "Butter"]
    },
    "Veggie Paneer Wrap Kit": {
        "shop": "RedMart",
        "points": 22,
        "ingredients": ["Wraps", "Paneer", "Bell pepper", "Spinach", "Carrot", "Sauce"]
    },
    "Lentil Veggie Bowl Kit": {
        "shop": "GrabMart",
        "points": 24,
        "ingredients": ["Lentils", "Rice", "Carrot", "Spinach", "Broccoli", "Seasoning"]
    },
    "Quinoa Veggie Power Bowl Kit": {
        "shop": "Little Farms",
        "points": 26,
        "ingredients": ["Quinoa", "Avocado", "Kale", "Chickpeas", "Carrot", "Lemon dressing"]
    }
}

REWARDS = {
    "Free Delivery": 80,
    "Free Coffee": 100,
    "$5 NTUC Voucher": 120,
    "Healthy Combo Unlock": 180,
    "$10 NTUC Voucher": 220,
}

FOOD_IMAGES = {
    1: "food_level1.png",
    2: "food_level2.png",
    3: "food_level3.png",
    4: "food_level4.png",
}

# -----------------------------
# STATE
# -----------------------------
if "points" not in st.session_state:
    st.session_state.points = 96
if "streak" not in st.session_state:
    st.session_state.streak = 4
if "last_message" not in st.session_state:
    st.session_state.last_message = "Welcome to VeggieGo Healthy Corner."

# -----------------------------
# HELPERS
# -----------------------------
def get_badges(points, streak):
    badges = []
    if points >= 50:
        badges.append("Veg Starter")
    if points >= 100:
        badges.append("Healthy Habit")
    if points >= 180:
        badges.append("Pantry Champion")
    if streak >= 5:
        badges.append("5-Day Streak")
    return ", ".join(badges) if badges else "No badges yet"

def get_next_reward(points):
    for reward, cost in REWARDS.items():
        if points < cost:
            return f"{reward} ({cost} pts)"
    return "All rewards unlocked"

def meals_for_exact_level(level):
    return [meal for meal in FOOD_MENUS if meal["Level"] == level]

def add_points(amount, message):
    st.session_state.points += amount
    st.session_state.streak += 1
    st.session_state.last_message = message

def render_header():
    st.markdown("""
    <div class="app-shell">
      <div class="grab-header">
        <div class="app-title">🥬 VeggieGo</div>
        <div class="app-subtitle">Healthy Corner integrated into a delivery app experience</div>
        <div class="pill-row">
          <div class="pill">Combined browse + order</div>
          <div class="pill">Refined UI</div>
          <div class="pill">Recipe + meal kit rewards</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

def render_metrics():
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="metric-card soft-green">
            <div class="metric-value">{st.session_state.points}</div>
            <div class="metric-label">Points</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card soft-yellow">
            <div class="metric-value">{st.session_state.streak}🔥</div>
            <div class="metric-label">Streak</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-card soft-blue">
            <div class="metric-value" style="font-size:15px;">{get_next_reward(st.session_state.points)}</div>
            <div class="metric-label">Next Reward</div>
        </div>
        """, unsafe_allow_html=True)

def render_meal_card(meal):
    st.markdown(f"""
    <div class="meal-card">
        <div>
            <span class="badge badge-green">Level {meal['Level']}</span>
            <span class="badge badge-blue">Food</span>
            <span class="badge badge-orange">+{meal['Points']} pts</span>
        </div>
        <div class="meal-title">{meal['Meal']}</div>
        <div class="meal-meta">{meal['Shop']} · {meal['ETA']} · {meal['Calories']} kcal</div>
        <div class="meal-desc">{meal['Description']}</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# APP
# -----------------------------
render_header()
render_metrics()

st.markdown(f"""
<div class="section-card">
    <b style="font-size:16px;">Latest activity</b><br>
    <span class="small-muted">{st.session_state.last_message}</span>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "Navigation",
    ["Home", "Healthy Corner", "Recipes", "Meal Kits", "Rewards"],
    horizontal=True
)

if page == "Home":
    st.markdown("""
    <div class="featured-banner">
        <b style="font-size:20px;">Healthy Corner inside delivery apps</b><br>
        <span style="font-size:15px; opacity:0.95; line-height:1.5;">
        VeggieGo helps users choose veggie meals gradually by matching meals to their current level, while still rewarding recipe usage and meal kit purchases.
        </span>
    </div>
    """, unsafe_allow_html=True)

elif page == "Healthy Corner":
    st.subheader("Healthy Corner")
    level = st.slider("Choose level", 1, 4, 1)

    info = LEVELS[level]
    st.markdown(f"""
    <div class="section-card {info['color']}">
        <h4 style="margin-top:0; font-size:22px;">Level {level}: {info['name']}</h4>
        <div class="small-muted"><b>{info['summary']}</b></div>
        <div style="margin-top:8px; font-size:15px; color:#1f2937; line-height:1.5;">{info['description']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image(FOOD_IMAGES[level], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Menus for this level")
    current_meals = meals_for_exact_level(level)

    for meal in current_meals:
        render_meal_card(meal)
        if st.button(f"Order {meal['Meal']}", key=f"order_{meal['Meal']}", use_container_width=True):
            add_points(
                meal["Points"],
                f"Ordered {meal['Meal']} and earned {meal['Points']} points."
            )
            st.success(st.session_state.last_message)
            st.rerun()

elif page == "Recipes":
    st.subheader("Drink Recipes")

    st.markdown('<div class="image-card">', unsafe_allow_html=True)
    st.image("veggie_drinks.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    for drink in DRINK_RECIPES:
        st.markdown(f"""
        <div class="meal-card">
            <div>
                <span class="badge badge-blue">Drink Recipe</span>
                <span class="badge badge-orange">+10 pts</span>
            </div>
            <div class="meal-title">{drink['Drink']}</div>
            <div class="meal-desc"><b>Ingredients:</b> {drink['Ingredients']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"I used recipe: {drink['Drink']}", key=f"recipe_{drink['Drink']}", use_container_width=True):
            add_points(10, f"Used recipe {drink['Drink']} and earned 10 points.")
            st.success(st.session_state.last_message)
            st.rerun()

elif page == "Meal Kits":
    st.subheader("Meal Kits")

    st.markdown("""
    <div class="section-card soft-green">
        <b style="font-size:18px;">Choose a meal kit</b><br>
        <span class="small-muted">Tap a kit to view ingredients and earn points when you order it.</span>
    </div>
    """, unsafe_allow_html=True)

    if "selected_kit" not in st.session_state:
        st.session_state.selected_kit = list(MEAL_KITS.keys())[0]

    for kit_name in MEAL_KITS.keys():
        if st.button(kit_name, key=f"kit_{kit_name}", use_container_width=True):
            st.session_state.selected_kit = kit_name

    selected_kit = st.session_state.selected_kit
    kit = MEAL_KITS[selected_kit]

    st.markdown(f"""
    <div class="section-card soft-green">
        <b style="font-size:18px;">{selected_kit}</b><br>
        <span class="small-muted">Partner shop: {kit['shop']}</span><br>
        <span class="small-muted">Reward on purchase: +{kit['points']} pts</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Ingredients")
    for ingredient in kit["ingredients"]:
        st.markdown(f"- {ingredient}")

    if st.button("Order Meal Kit", type="primary", key="order_meal_kit", use_container_width=True):
        add_points(kit["points"], f"Ordered {selected_kit} and earned {kit['points']} points.")
        st.success(st.session_state.last_message)
        st.rerun()

elif page == "Rewards":
    st.subheader("Rewards")
    st.markdown(f"""
    <div class="section-card soft-yellow">
        <b style="font-size:17px;">Current badges:</b> {get_badges(st.session_state.points, st.session_state.streak)}<br>
        <span class="small-muted">Earn points from food orders, recipe usage, and meal kit purchases.</span>
    </div>
    """, unsafe_allow_html=True)

    for reward, cost in REWARDS.items():
        st.markdown(f"""
        <div class="reward-card">
            <b style="font-size:17px;">{reward}</b><br>
            <span class="small-muted">{cost} points needed</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Redeem {reward}", key=reward, use_container_width=True):
            if st.session_state.points >= cost:
                st.session_state.points -= cost
                st.session_state.last_message = f"Successfully redeemed {reward}."
                st.success(st.session_state.last_message)
                st.rerun()
            else:
                st.error(f"Not enough points. You need {cost - st.session_state.points} more points.")

st.markdown('<div class="bottom-note">VeggieGo prototype · refined healthy delivery mobile UI</div>', unsafe_allow_html=True)