import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm';

// Replace with your actual Supabase URL from GitHub secrets
const SUPABASE_URL = 'https://qflhgztoxamhdhlxjpjc.supabase.co';

// Replace with your public Supabase API key from GitHub secrets (assuming public access)
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFmbGhnenRveGFtaGRobHhqcGpjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjA4Mzg5MTksImV4cCI6MjAzNjQxNDkxOX0.BWDSmZFBrQVSZV0wK6XWGaAZky51VxrRG_wfwG3FWZc';

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

// Function to fetch a random drink
async function fetchRandomDrink() {
  const { data, error } = await supabase
    .from('drinks')
    .select('*')
    .order('random()')
    .single();

  if (error) {
    console.error('Error fetching random drink:', error);
    return;
  }

  // Update the landing drink section with the fetched drink data
  updateLandingDrink(data);
}

// Function to update the landing drink section
function updateLandingDrink(drink) {
  const landingDrinkElement = document.getElementById('landing-drink');
  landingDrinkElement.innerHTML = `
    <h2>${drink.name}</h2>
    <img src="${drink.picture}" alt="${drink.name}">
  `;
}

// Function to populate the drink name dropdown (replace with your actual logic)
async function populateDrinkNames() {
  const { data, error } = await supabase
    .from('drinks')
    .select('name');

  if (error) {
    console.error('Error fetching drink names:', error);
    return;
  }

  const drinkNameDropdown = document.getElementById('search-by-name');
  data.forEach(drink => {
    const option = document.createElement('option');
    option.value = drink.name;
    option.text = drink.name;
    drinkNameDropdown.appendChild(option);
  });
}

// Function to populate the ingredient dropdown (replace with your actual logic)
async function populateIngredients() {
  const { data, error } = await supabase
    .from('ingredients')
    .select('name');

  if (error) {
    console.error('Error fetching ingredients:', error);
    return;
  }

  const ingredientDropdown = document.getElementById('search-by-ingredient');
  data.forEach(ingredient => {
    const option = document.createElement('option');
    option.value = ingredient.name;
    option.text = ingredient.name;
    ingredientDropdown.appendChild(option);
  });
}

// Function to handle search by name selection (replace with your actual logic)
function handleSearchByName(event) {
  const selectedName = event.target.value;
  // Implement logic to search drinks by name and display results
}

// Function to handle search by ingredient selection (replace with your actual logic)
function handleSearchByIngredient(event) {
  const selectedIngredient = event.target.value;
  // Implement logic to search drinks by ingredient and display results
}

// Function to generate a random drink (replace with your SQL logic)
async function generateRandomDrink() {
  // Replace with your actual SQL code to generate a random drink
  // This might involve querying the database and combining ingredients
  console.log('Generate random drink logic not implemented yet!');
}

// Call functions on page load
window.addEventListener('DOMContentLoaded', async () => {
  await populateDrinkNames();
  await populateIngredients();
  await fetchRandomDrink();

  // Add event listeners for search and generate buttons
  document.getElementById('search-by-name').addEventListener('change', handleSearchByName);
  document.getElementById('search-by-ingredient').addEventListener('change', handleSearchByIngredient);
  document.getElementById('generate-button').addEventListener('click', generateRandomDrink);
});
