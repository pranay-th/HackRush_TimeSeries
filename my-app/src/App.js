const express = require('express');
const {PrismaClient} = require('@prisma/client'); 
const prisma = new PrismaClient();
const app = express();
const port = 3000;

app.get('/api/drug-sales', async (req, res) => {
  try{
    const data = await prisma.drug_sales.findMany();
    res.json(data);
  }catch(error){
    res.status(500).json({error: 'failed to fetch drug sales data'});
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
