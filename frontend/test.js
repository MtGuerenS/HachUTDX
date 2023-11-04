// Generate random values for the input parameters
const randomValue = () => Math.floor(Math.random() * 10000);
const grossMonthlyIncome = randomValue();
const creditCardPayment = randomValue();
const carPayment = randomValue();
const studentLoanPayment = randomValue();
const appraisedValue = randomValue();
const downPayment = randomValue();
const loanAmount = randomValue();
const mortgagePayment = randomValue();
const creditScore = Math.floor(Math.random() * 800); // Random credit score between 0 and 800

// Create the input data for the validation request
const validationData = {
  gross_monthly_income: grossMonthlyIncome,
  credit_card_payment: creditCardPayment,
  car_payment: carPayment,
  student_loan_payment: studentLoanPayment,
  appraised_value: appraisedValue,
  down_payment: downPayment,
  loan_amount: loanAmount,
  mortgage_payment: mortgagePayment,
  credit_score: creditScore,
};

// Send the validation request to Flask
fetch('http://127.0.0.1:5000/api/validate-buy', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(validationData),
})
  .then((response) => response.json())
  .then((data) => {
    console.log('Validation Response:', data);
  })
  .catch((error) => {
    console.error('Validation Error:', error);
  });

// Create a random prompt for GPT-3
const randomPrompt = 'Generate a creative story about a flying elephant.';

// Create the input data for the GPT-3 request
const gptData = {
  user_input: randomPrompt,
};

// Send the GPT-3 request to Flask
fetch('http://127.0.0.1:5000/api/chat-with-gpt', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(gptData),
})
  .then((response) => response.json())
  .then((data) => {
    console.log('GPT-3 Response:', data);
  })
  .catch((error) => {
    console.error('GPT-3 Error:', error);
  });
