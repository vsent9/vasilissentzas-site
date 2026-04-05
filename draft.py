<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artist Portfolio</title>

    <!-- Cormorant Garamond -->
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&display=swap" rel="stylesheet">

    <!-- Inter (για μικρά κείμενα) -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap" rel="stylesheet">

    <style>
        body {
            margin: 0;
            background: #ffffff;
            color: #111;
            font-family: 'Inter', sans-serif;
        }

        header {
            padding: 40px 60px;
            font-family: 'Cormorant Garamond', serif;
            font-size: 32px;
            letter-spacing: 1px;
        }

        .hero {
            height: 90vh;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            opacity: 0;
            animation: fadeIn 2s ease forwards;
        }

        .hero img {
            max-width: 70%;
            height: auto;
            margin-bottom: 30px;
        }

        .hero h1 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 48px;
            font-weight: 400;
            margin: 0;
        }

        .hero p {
            font-size: 18px;
            margin-top: 10px;
            opacity: 0.7;
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }

        .section {
            padding: 120px 60px;
            opacity: 0;
            animation: fadeIn 1.5s ease forwards;
            animation-delay: 1s;
        }

        .section h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 36px;
            margin-bottom: 20px;
        }

        .section p {
            max-width: 600px;
            line-height: 1.6;
        }
    </style>
</head>

<body>

<header>
    Το Όνομά Σου
</header>

<section class="hero">
    <img src="your-image.jpg" alt="Featured Artwork">
    <h1>Sculpture · Printmaking · Digital Art</h1>
    <p>Ένας κόσμος που αποκαλύπτεται σταδιακά.</p>
</section>

<section class="section">
    <h2>Ανακάλυψε το έργο</h2>
    <p>
        Η δουλειά μου κινείται ανάμεσα στη γλυπτική, τη χαρακτική και το digital art.
        Κάθε έργο είναι μια εξερεύνηση υλικών, υφών και αφηγήσεων.
    </p>
</section>

</body>
</html>
