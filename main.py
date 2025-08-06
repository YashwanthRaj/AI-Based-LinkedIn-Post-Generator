import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

def main():
    st.title("LinkedIn Post Generator")
    col1, col2 = st.columns(2)

    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length", options=["Short", "Medium", "Long"])

    if st.button("Generate"):
        post = generate_post(selected_tag, selected_length)
        st.write(post)



if __name__ == "__main__":
    main()