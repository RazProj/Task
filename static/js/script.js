document.addEventListener("DOMContentLoaded", function () {
    // Fetch the data from Flask's /data route
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('data-container');

            // Populate the HTML with the fetched data
            const table = document.createElement('table');
            const thead = document.createElement('thead');
            const tbody = document.createElement('tbody');

            const headerRow = document.createElement('tr');
            const urlHeader = document.createElement('th');
            urlHeader.innerText = 'URL';
            const dataHeader = document.createElement('th');
            dataHeader.innerText = 'Data Enriched';
            headerRow.appendChild(urlHeader);
            headerRow.appendChild(dataHeader);
            thead.appendChild(headerRow);

            // Loop through each country in the JSON data
            data.forEach((country, countryIndex) => {
                // Add a separator row between countrys (except before the first country)
                if (countryIndex > 0) {
                    const separatorRow = document.createElement('tr');
                    const separatorCell = document.createElement('td');
                    separatorCell.colSpan = 2; // Make the separator span both columns
                    separatorCell.style.borderTop = '4px solid #000'; // Add thick line
                    separatorRow.appendChild(separatorCell);
                    tbody.appendChild(separatorRow);
                }

                // Loop through each url in the country
                country.forEach((url) => {
                    const row = document.createElement('tr');
                    const urlCell = document.createElement('td');
                    urlCell.innerHTML = `<a href="${url.url}" target="_blank">${url.url}</a>`;
                    const dataCell = document.createElement('td');
                    dataCell.innerHTML = `
                        <strong>Name:</strong> ${url.name}<br>
                        <strong>Employees:</strong> ${url.est_emp}<br>
                        <strong>Industry:</strong> ${url.industry || 'N/A'}<br>
                        <strong>Country:</strong> ${url.country}
                    `;
                    row.appendChild(urlCell);
                    row.appendChild(dataCell);
                    tbody.appendChild(row);
                });
            });

            table.appendChild(thead);
            table.appendChild(tbody);
            container.appendChild(table);
        })
        .catch(error => console.error('Error fetching data:', error));
});
