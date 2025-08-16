# TravellerBuddy

A smart AI-powered travel assistant built using **Gemini** for natural language understanding and **Gradio** for a sleek, interactive user interface.

---
![Traveller Buddy](https://socialify.git.ci/SatyamPrakash09/TravellerBuddy/image?custom_description=A+smart+AI-powered+travel+assistant+built+using+Gemini+for+natural+language+understanding+and+Gradio+for+a+sleek%2C+interactive+user+interface.&custom_language=Python&description=1&font=Source+Code+Pro&language=1&name=1&theme=Dark)
---

## Overview

- **Purpose**: TravellerBuddy acts as your virtual travel companion—chat or describe your plans, and it responds with suggestions, itinerary ideas, or travel tips.
- **Powered By**:
  - **Gemini** – AI model handling user queries and generating recommendations.
  - **Gradio** – Simplifies frontend deployment with a browser-based interactive UI.

---

## Project Structure

```text
TravellerBuddy/
├── TravellerBuddy.py      # Core logic combining Gemini with Gradio
├── index.html             # HTML frontend
├── script.js              # JavaScript logic
├── styles.css             # Styling
├── requirements.txt       # Python dependencies
├── .gitignore
└── LICENSE                # MIT License
````

---

## Features

* **Conversational Travel Planning** – Ask about destinations, itineraries, packing tips, weather insights, etc.
* **Instant Web Interface** – Built with Gradio; interact via your browser with no complex setup.
* **Fast Prototyping** – Ideal for experimenting with AI responses and user flows.

---

## Getting Started

### Prerequisites

* Python 3.x
* (Optional but recommended) Virtual environment

### Setup & Run Locally

```bash
git clone https://github.com/SatyamPrakash09/TravellerBuddy.git
cd TravellerBuddy

# (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the application
python TravellerBuddy.py
```

Open your browser and go to the Gradio URL—usually `http://127.0.0.1:7860/`.

---

## Usage Tips

* Try prompts like:

  * “Suggest a 3-day itinerary for Tokyo.”
  * “What should I pack for a beach trip in Goa?”
* Be specific: include location, duration, preferences, budget, etc.
* Customize the UI via `index.html`, `script.js`, and `styles.css`.

---

## Architecture Overview

```
[ Gradio Web UI ] ←→ [ TravellerBuddy.py — Gemini AI ]
```

1. User interacts via Gradio.
2. Gradio sends queries to Python backend.
3. Gemini processes the queries.
4. Responses are returned and displayed in the UI.

---

## Technologies Used

* **Python**
* **Gradio**
* **Gemini** (open-access model)

---

## Future Enhancements

* Add location-specific itinerary suggestions.
* Enable voice input/output.
* Support saving/exporting itineraries (PDF, calendar events).
* Deploy via Hugging Face Spaces, Gradio Hub, or similar.
* Improve UI with better styles, loading indicators, and error handling.

---

## Contributing

Contributions are welcome! Please follow:

1. Fork the repo.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and test.
4. Commit your changes:

   ```bash
   git commit -m "Add meaningful description"
   ```
5. Push to your fork:

   ```bash
   git push origin feature/your-feature
   ```
6. Open a pull request—happy to review!

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact / Support

Feel free to open an issue for questions or help.
