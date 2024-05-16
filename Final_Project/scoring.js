const { createClient } = require('@supabase/supabase-js');

// Create a single Supabase client for interacting with your database
const supabase = createClient('https://bfsqoukxpynbbcxuozyr.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmc3FvdWt4cHluYmJjeHVvenlyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3NjA3NTQsImV4cCI6MjAzMTMzNjc1NH0.aNpGGnO4w_90OL3iLR7H2OVWLLJeAIn5Izi1x4IN3H8');

async function fetchData() {
  try {
    const { data, error } = await supabase.from('score').select('*');
    
    if (error) {
      console.error('Error fetching data:', error.message);
    } else {
      console.log('Data:', data);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

// Call the function to fetch data
fetchData();
