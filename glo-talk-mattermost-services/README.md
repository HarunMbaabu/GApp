# Glo Talk Mattermost Services

A complete Flask landing page and inquiry web application for **Glo Talk**, a professional service provider that helps organizations install, configure, migrate to, secure, and support self-hosted Mattermost.

> Mattermost is an open-source collaboration platform. Glo Talk is not Mattermost and does not present itself as the owner or seller of Mattermost. Glo Talk provides professional setup and support services around self-hosted Mattermost deployments.

## Features

- Premium SaaS-style landing page
- Sticky responsive navigation with mobile hamburger menu
- Self-hosted Mattermost service positioning
- Feature, package, process, comparison, use-case, FAQ, and CTA sections
- Detailed pricing/packages page
- Payment/inquiry form without real payment gateway integration
- Contact form with beginner-friendly validation
- Success confirmation page
- Health check endpoint at `/health`
- SVG logo and favicon created with no paid assets
- SEO, Open Graph, Twitter card, accessibility, and responsive design basics
- Vercel-ready Flask configuration

## Tech Stack

- Python Flask
- HTML5 templates
- CSS3 with custom properties, grid, flexbox, and responsive media queries
- Vanilla JavaScript
- SVG assets
- Vercel Python runtime

## Folder Structure

```text
glo-talk-mattermost-services/
├── app.py
├── requirements.txt
├── vercel.json
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── pricing.html
│   ├── payment.html
│   ├── success.html
│   └── contact.html
└── public/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── main.js
    └── images/
        ├── logo.svg
        └── favicon.svg
```

## Local Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run locally

```bash
python app.py
```

Open the local Flask URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## Vercel Deployment

This project includes a `vercel.json` file that routes all requests to `app.py` using Vercel's Python runtime.

Deploy with the Vercel CLI:

```bash
vercel
```

Or connect the GitHub repository to Vercel and deploy from the dashboard.

## Routes

- `/` - Landing page
- `/pricing` - Detailed package page
- `/payment` - Payment/inquiry form
- `/success` - Confirmation page
- `/contact` - Contact page
- `/health` - JSON health check

## Environment Variables

No environment variables are required for the current static inquiry version.

Recommended future variables:

```text
SECRET_KEY=replace-with-a-secure-random-value
MAIL_SERVER=smtp.example.com
MAIL_USERNAME=your-email-user
MAIL_PASSWORD=your-email-password
MPESA_CONSUMER_KEY=your-mpesa-key
MPESA_CONSUMER_SECRET=your-mpesa-secret
STRIPE_SECRET_KEY=your-stripe-secret
```

## Future Payment Integration Notes

The `/payment` page is intentionally an inquiry form. After a customer submits requirements, the Glo Talk team can confirm the scope and share payment instructions or an invoice.

Future integrations can include:

- M-Pesa STK Push
- Stripe/Card payments
- Bank transfer invoice generation
- PayPal if required for international customers
- CRM or email notification workflows

## Future Improvements

- Add a reusable base template to reduce repeated HTML
- Store inquiries in a database or CRM
- Send email notifications for form submissions
- Add analytics and conversion tracking
- Add blog or resource pages for self-hosted collaboration education
- Add case studies and testimonials
- Replace placeholder contact details with production business details
- Add automated unit and integration tests

## Screenshots

Screenshots placeholder:

- Landing page desktop screenshot
- Landing page mobile screenshot
- Pricing page screenshot
- Payment/inquiry form screenshot

## Contact Placeholder

- Email: `hello@example.com`
- Phone: `+254 700 000 000`
- Location: Nairobi, Kenya
