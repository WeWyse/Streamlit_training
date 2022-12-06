import streamlit as st

from utils.persist import load_widget_state


def set_session_states():
    if "page" not in st.session_state:
        # Initialize session state.
        st.session_state.update(
            {
                # Default page.
                "page": "Beginner",
                # Default widget values.
                "text": False,
                "button": False,
                "checkbox": False,
                "radio": False,
                "select": False,
                "slider": False,
                "input": False,
                "media": False,
                "columns": False,
                "load": False,
                "expander": False,
                "form": False,
                "metric": False,
                "dataframe": False,
                "pprofiling": False,
                "lottie": False,
                "aggrid": False,
                "sessionstate": False,
                "theme": False,
                "cache": False,
                "multipages": False,
                "leon": False,
                "keyvault": False,
                "ex1": False,
                "ex2": False,
                "ex3": False,
                "ex4": False,
                "ex5": False,
                "ex6": False,
                "ex7": False,
                "ex8": False,
                "ex9": False,
                "ex10": False,
            }
        )


def homepage_content():
    cols = st.columns((3, 5, 3))
    cols[1].image("data/streamlit_logo.png", width=500)
    st.subheader("Introduction")
    st.markdown(
        "Welcome to this training dedicated to Streamlit! The objectives "
        "of this training  are to:"
    )
    st.markdown(
        """
    - Introduce you to Streamlit,
    - Show you a large range of Streamlit features, from basic to advanced ones,
    - Allow you to test these features and play with Streamlit.
    """
    )

    st.subheader("What is Streamlit?")
    st.markdown(
        "Streamlit is an open-source app framework that allows you to "
        "create webapps in Python code, with no front-end experience, very quickly. "
        "You can find examples of Streamlit dashboard [here](https://streamlit.io/gallery). "
        "Concretely, Streamlit will offer you the ability to share your data works and ideas "
        "and to be able to launch on-demand computation or scripts via a webapp."
    )

    st.subheader("Training ")
    st.markdown(
        "During this training, you will be free to navigate through the pages presenting "
        "many Streamlit capabilities by level of difficulty/importance/abstraction. We advise you to:"
    )
    st.markdown(
        """
        1. Read and learn about Streamlit capabilities according to your level of knowledge,
        2. Try and learn in the Editor section where you can directly type Streamlit code,
        3. Complete some of the ideas in the Exercises section,
        4. Pass the final exam deploying your very first Streamlit to Leon.
        """
    )
    st.markdown("And obviously **ASK ANY QUESTION AT ANY TIME**! We will be glad to help you.")


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    load_widget_state()
    set_session_states()
    homepage_content()
