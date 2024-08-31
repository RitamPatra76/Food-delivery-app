import streamlit as st

# Add Font Awesome link
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div style="background-color: #00695c; padding: 15px; border-radius: 10px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="display: flex; align-items: center;">
            <div style="background-color: #ff9800; padding: 5px 15px; border-radius: 5px; color: white; font-weight: bold;">
                Work
            </div>
            <div style="margin-left: 10px; color: white;">
                Ms Ramaiah University Of Applied Sciences
            </div>
        </div>
        <div>
            <i class="fas fa-user-circle" style="color: white; font-size: 30px;"></i>
            <button style="background-color: #ff5722; color: white; padding: 5px 15px; border-radius: 5px; border: none;">Buy One</button>
        </div>
    </div>
    <div style="margin-top: 10px; display: flex; align-items: center;">
        <input type="text" placeholder="Search for 'Biryani'" style="width: 100%; padding: 10px; border-radius: 5px; border: none; background-color: white; color: black;">
        <i class="fas fa-microphone" style="color: black; margin-left: 10px;"></i>
    </div>
</div>
""", unsafe_allow_html=True)

# Promotional Banner
st.markdown("""
<div style="background-color: #c62828; padding: 20px; margin-top: 20px; border-radius: 10px; color: white;">
    <h3 style="margin: 0;">Salary In? Forks Out!</h3>
    <h2 style="margin: 0; font-size: 28px;">Unlimited: Party Discounts & More</h2>
    <div style="display: flex; justify-content: space-around; margin-top: 20px;">
        <div>
            <i class="fas fa-utensils" style="color: white; font-size: 50px;"></i>
            <p>Biryani</p>
            <p>From ₹99</p>
        </div>
        <div>
            <i class="fas fa-bacon" style="color: white; font-size: 50px;"></i>
            <p>Rolls & Shawarmas</p>
            <p>From ₹59</p>
        </div>
        <div>
            <i class="fas fa-drumstick-bite" style="color: white; font-size: 50px;"></i>
            <p>North Indian</p>
            <p>From ₹69</p>
        </div>
        <div>
            <i class="fas fa-bread-slice" style="color: white; font-size: 50px;"></i>
            <p>South Indian</p>
            <p>From ₹69</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Offers Section
st.markdown("""
<div style="background-color: #ffe0b2; padding: 20px; margin-top: 20px; border-radius: 10px;">
    <h3 style="color: #bf360c;">KFC Menu at ₹179*</h3>
    <p style="color: #5d4037;">Relish hearty delights</p>
    <button style="background-color: #d32f2f; color: white; padding: 10px; border-radius: 5px; border: none;">Order Now</button>
</div>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<div style="background-color: #ffffff; padding: 10px; margin-top: 20px; border-radius: 10px; display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <i class="fas fa-home" style="color: #008577; font-size: 30px;"></i>
        <p style="color: #008577;">Home</p>
    </div>
    <div style="text-align: center;">
        <i class="fas fa-utensils" style="color: #008577; font-size: 30px;"></i>
        <p style="color: #008577;">Food</p>
    </div>
    <div style="text-align: center;">
        <i class="fas fa-shopping-cart" style="color: #008577; font-size: 30px;"></i>
        <p style="color: #008577;">Eatlist</p>
    </div>
    <div style="text-align: center;">
        <i class="fas fa-compass" style="color: #008577; font-size: 30px;"></i>
        <p style="color: #008577;">Explore</p>
    </div>
    <div style="text-align: center;">
        <i class="fas fa-redo" style="color: #008577; font-size: 30px;"></i>
        <p style="color: #008577;">Reorder</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Additional styles to match the desired theme
st.markdown("""
<style>
    body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    h3, h2, p {
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)
