document.getElementById('findLunch').addEventListener('click', function() {
    const diet = document.getElementById('diet').value;
    const cuisine = document.getElementById('cuisine').value;
    const budget = document.getElementById('budget').value;

    console.log('Sending request with:', { diet, cuisine, budget });

    fetch('http://127.0.0.1:5000/get_lunch', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ diet, cuisine, budget }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('result').style.display = 'block';
            document.getElementById('lunchName').textContent = data.name;
            document.getElementById('lunchImage').src = data.image_url;
            document.getElementById('lunchDetails').textContent = `Diet: ${data.diet} | Cuisine: ${data.cuisine} | Budget: ${data.budget}`;
            document.getElementById('recipeLink').href = data.recipe_url;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('newSuggestion').addEventListener('click', function() {
    document.getElementById('result').style.display = 'none';
});