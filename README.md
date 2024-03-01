
<html>

<body>
    <h1>Vaccination Check GUI Python</h1>

    <p>This is a simple Python GUI application built to manage vaccination records using MySQL as the database backend.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Check-in Tab:</strong> Allows users to input vaccination details such as ID, first name, last name, etc., and submit them to the database.</li>
        <li><strong>Immunity Check Tab:</strong> Enables users to check the vaccination status of individuals by their ID.</li>
        <li><strong>Import and Export Tab:</strong> Provides functionality to import vaccination records from a CSV file into the database and export records from the database to a CSV file.</li>
    </ul>

    <h2>Prerequisites</h2>
    <p>Before running this application, ensure you have the following installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>MySQL</li>
        <li>Required Python packages listed in <code>requirements.txt</code></li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
    </ol>
    <pre><code>git clone https://github.com/yourusername/vaccination-check-gui.git</code></pre>
    <ol start="2">
        <li>Navigate to the project directory:</li>
    </ol>
    <pre><code>cd vaccination-check-gui</code></pre>
    <ol start="3">
        <li>Install dependencies:</li>
    </ol>
    <pre><code>pip install -r requirements.txt</code></pre>
    <ol start="4">
        <li>Run the application:</li>
    </ol>
    <pre><code>python main.py</code></pre>

    <h2>Usage</h2>
    <ol>
        <li>Open the application.</li>
        <li>Fill in the required details in the Check-in tab and submit the form to add records to the database.</li>
        <li>Use the Immunity Check tab to verify the vaccination status of individuals by their ID.</li>
        <li>Import existing vaccination records from a CSV file using the Import button in the Import and Export tab.</li>
        <li>Export records from the database to a CSV file using the Export button in the Import and Export tab.</li>
    </ol>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. Feel free to modify and distribute it according to the terms of the license.</p>
</body>
</html>
