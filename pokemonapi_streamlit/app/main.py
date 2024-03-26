import streamlit as st
from api.pokeapi import fetch_pokemon_data

def display_pokemon_info(data, limit):
    st.title("PokeAPI Data")
    st.write("Welcome to the PokeAPI Explorer!")

    if data:
        st.write("Available Endpoints:")
        for endpoint, url in data.items():
            st.write(f"- {endpoint}: {url}")

        # Allow the user to set the limit for the number of items to display
        for endpoint, url in data.items():
            if st.checkbox(f"Show {endpoint}"):
                st.write(f"Showing {limit} items for {endpoint}:")
                items_response = fetch_pokemon_data(url)
                items = items_response["results"][:limit]
                for item in items:
                    st.write(f"- {item['name']}")
    else:
        st.error("Failed to fetch data from the PokeAPI. Please try again later.")

def main():
    pokemon_data = fetch_pokemon_data()
    if pokemon_data:
        limit = st.slider("Select the limit of items to display:", 1, 20, 10)
        display_pokemon_info(pokemon_data, limit)

if __name__ == "__main__":
    main()
