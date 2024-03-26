import streamlit as st
from api.pokeapi import fetch_pokemon_data

def display_pokemon_info(data):
    st.title("PokeAPI Data")
    st.write("Welcome to the PokeAPI Explorer!")

    if data:
        st.write("Available Endpoints:")
        for endpoint, url in data.items():
            st.write(f"- {endpoint}: {url}")
    else:
        st.error("Failed to fetch data from the PokeAPI. Please try again later.")

def main():
    pokemon_data = fetch_pokemon_data()
    display_pokemon_info(pokemon_data)

if __name__ == "__main__":
    main()
