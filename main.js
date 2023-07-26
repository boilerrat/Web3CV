// Fetch data from passport.json
fetch('passport.json')
  .then(response => response.json())
  .then(data => {
    // Get the table body where the data will be appended
    const credentialDataElement = document.getElementById('credentialData');

    // Iterate over each stamp in the data
    data.stamps.forEach(stamp => {
      const row = document.createElement('tr');

      const providerCell = document.createElement('td');
      providerCell.textContent = stamp.provider;
      row.appendChild(providerCell);

      const issuanceDateCell = document.createElement('td');
      issuanceDateCell.textContent = stamp.credential.issuanceDate;
      row.appendChild(issuanceDateCell);

      const expiryDateCell = document.createElement('td');
      expiryDateCell.textContent = stamp.credential.expirationDate;
      row.appendChild(expiryDateCell);

      const credentialTypeCell = document.createElement('td');
      credentialTypeCell.textContent = stamp.credential.type.join(', ');
      row.appendChild(credentialTypeCell);

      const proofTypeCell = document.createElement('td');
      proofTypeCell.textContent = stamp.credential.proof.type;
      row.appendChild(proofTypeCell);

      credentialDataElement.appendChild(row);
    });
  })
  .catch(error => console.error('Error:', error));
