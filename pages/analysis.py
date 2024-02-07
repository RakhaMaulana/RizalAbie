import streamlit as st
import os
import matplotlib.pyplot as plt

st.set_page_config(
        page_title="Analysis",
        page_icon="scientist"
    )

st.title("Analysis of Dataset")
# Define the train_classes dictionary
train_classes = {
    'Uninfected': len(os.listdir('train/Uninfected')),
    'Parasitized': len(os.listdir('train/Parasitized'))
}

test_classes = {
    'Uninfected': len(os.listdir('test/Uninfected')),
    'Parasitized': len(os.listdir('test/Parasitized'))
}

# Create the bar chart
fig1, ax1 = plt.subplots()
ax1.bar(train_classes.keys(), train_classes.values(), width=0.5)
ax1.set_title("Number of Images by Class (Train)")
ax1.set_xlabel('Class Name')
ax1.set_ylabel('Amount')

st.write("The amount of train set")
# Display the bar chart using Streamlit
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2.bar(test_classes.keys(), test_classes.values(), width=0.5)
ax2.set_title("Number of Images by Class (Test)")
ax2.set_xlabel('Class Name')
ax2.set_ylabel('Amount')

st.write("The amount of test set")
st.pyplot(fig2)