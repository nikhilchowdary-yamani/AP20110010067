const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.get('/numbers', async (req, res) => {
  const urls = req.query.url;

  if (!urls) {
    res.status(400).json({ error: 'No URLs provided' });
  }

  const requests = urls.map(url => axios.get(url));

  try {
    const responses = await Promise.allSettled(requests);

    const numbers = [];
    responses.forEach(response => {
      if (response.status === 'fulfilled' && response.value.data && Array.isArray(response.value.data.numbers)) {
        numbers.push(...response.value.data.numbers);
      }
    });

    const uniqueNumbers = [...new Set(numbers)];
    const sortedNumbers = uniqueNumbers.sort((a, b) => a - b);

    res.json({ numbers: sortedNumbers });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(port, () => {
  console.log(`number-management-service is running on port ${port}`);
});
