import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('classifier.pkl', 'rb'))

def predict_fire_probability(Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, Convex_Area, Equiv_Diameter, Eccentricity, Solidity, Extent, Roundness, Aspect_Ratio, Compactness):
    input_data = np.array([[Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, Convex_Area, Equiv_Diameter, Eccentricity, Solidity, Extent, Roundness, Aspect_Ratio, Compactness]]).astype(np.float64)
    prediction = model.predict_proba(input_data)
    predicted_probability = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(predicted_probability)

def main():
    st.title("Pumpkin Seed Prediction ML App")
    html_temp = """
    <div style="background-color:#025246;padding:10px">
    <h2 style="color:white;text-align:center;">Pumpkin Seed Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Area = st.text_input("Area")
    Perimeter = st.text_input("Perimeter")
    Major_Axis_Length = st.text_input("Major Axis Length")
    Minor_Axis_Length = st.text_input("Minor Axis Length")
    Convex_Area = st.text_input("Convex Area")
    Equiv_Diameter = st.text_input("Equivalent Diameter")
    Eccentricity = st.text_input("Eccentricity")
    Solidity = st.text_input("Solidity")
    Extent = st.text_input("Extent")
    Roundness = st.text_input("Roundness")
    Aspect_Ratio = st.text_input("Aspect Ratio")
    Compactness = st.text_input("Compactness")

    safe_html = """  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;">Seed Type Urgup Sivrisi</h2>
       </div>
    """
    danger_html = """  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">Seed Type- Cercevelik</h2>
       </div>
    """

    if st.button("Predict"):
        output = predict_fire_probability(Area, Perimeter, Major_Axis_Length, Minor_Axis_Length, Convex_Area, Equiv_Diameter, Eccentricity, Solidity, Extent, Roundness, Aspect_Ratio, Compactness)
        st.success('The probability of seed place is'.format(output))

        if output > 0.5:
            st.markdown(danger_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()