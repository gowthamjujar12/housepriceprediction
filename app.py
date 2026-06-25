# import joblib
# import streamlit as st 
# import pandas as pd

# st.set_page_config(page_icon="🏠",page_title="House_Price_Prediction",layout="wide")
# with open("Rf_model.joblib","rb")as file:
#     model=joblib.load(file)
    
# df=pd.read_csv("cleaned_df.csv")
# with st.sidebar:
#     st.title("House Price Prediction App")
#     st.image("house_logo.png",width=300)
    
# st.header("House Price Prediction")
# st.image("house_logo.png")

# with st.container(border=True):
#     col1,col2=st.columns(2)
# with col1:
#     location=st.selectbox("Location:",options=df['location'].unique())
#     sqft=st.number_input("Sq.ft",min_value=300)
# with col2:
#     bath=st.selectbox("Bath",options=sorted(df["bath"].unique()))
#     bhk=st.selectbox("BHK",options=sorted(df['bhk'].unique()))
    
# def get_encoded_loc(location):  
#     for loc,encoded in zip(df['location'],df['encoded_loc']):
#         if location==loc:
#             return encoded

# encoded_loc=get_encoded_loc(location)

# if st.button("Predict"):
#     inp_data=[[sqft,bath,bhk,encoded_loc]]
#     pred=model.predict(inp_data)
#     pred=float(f'{pred[0]:2f}')
#     st.title(f"Predicted Price: Rs.{pred*100000}")
    
import joblib
import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.stButton > button:hover {
    background-color: #45a049;
}

.prediction-box {
    background-color: #f0f2f6;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
}

.title-text {
    text-align: center;
    color: #1E3A8A;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #
with open("Rf_model.joblib", "rb") as file:
    model = joblib.load(file)

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("cleaned_df.csv")

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.title("🏠 House Price Prediction")
    st.image("house_logo.png", width=250)
    st.markdown("---")
    st.write(
        """
        Predict house prices based on:
        - Location
        - Area (Sq.ft)
        - Bathrooms
        - BHK
        """
    )

# ---------------- HEADER ---------------- #
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("house_logo.png", width=250)

st.markdown(
    "<h1 class='title-text'>🏠 House Price Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Estimate the value of your property instantly</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT SECTION ---------------- #
st.subheader("📋 Enter Property Details")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        location = st.selectbox(
            "📍 Select Location",
            options=sorted(df["location"].unique())
        )

        sqft = st.number_input(
            "📐 Area (Sq.ft)",
            min_value=300
        )

    with col2:
        bath = st.selectbox(
            "🛁 Number of Bathrooms",
            options=sorted(df["bath"].unique())
        )

        bhk = st.selectbox(
            "🛏 Number of Bedrooms (BHK)",
            options=sorted(df["bhk"].unique())
        )

# ---------------- LOCATION ENCODING ---------------- #
def get_encoded_loc(location):
    for loc, encoded in zip(df["location"], df["encoded_loc"]):
        if location == loc:
            return encoded

encoded_loc = get_encoded_loc(location)

# ---------------- PREDICTION ---------------- #
if st.button("🔮 Predict House Price"):

    inp_data = [[sqft, bath, bhk, encoded_loc]]

    pred = model.predict(inp_data)

    pred = float(f"{pred[0]:.2f}")

    price = pred * 100000

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class='prediction-box'>
            <h2>🏡 Estimated House Price</h2>
            <h1>₹ {price:,.0f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- FOOTER ---------------- #
st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit | Machine Learning House Price Prediction"
)