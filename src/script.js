const url = 'https://www.komplett.no/product/1251458'

fetch(url, {mode: 'no-cors'})
    .then(response => {
        if (!response.ok) {
            console.log(response)
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Here's a list of repos!
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
