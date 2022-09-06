const html = document.querySelector("html")

let page = 0

let pages = []

function updatePage() {
    pages = [
        `<head>
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="start">
            <div class="start">
                <h1 class="start">Website maken</h1>
                <p class="start">Door Sem</p>
            </div>
        </body>`,
        `<head>
        
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="title">
            <div class="title">
                <h1>Inleiding</h1>
            </div>
            <div class="ul">
                <ul> 
                    <li>Waarom deze challenge?</li>
                </ul>
            </div>
        </body>`,
        `<head>
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="title">
            <div class="title">
                <h1>Inhoud</h1>
            </div>
            <div class="ul">
                <ul>
                    <li>Doelen</li>
                    <li>Stappenplan</li> 
                    <li>Samenvatting</li>
                    <li>Mijn Website</li>
                </ul>
            </div>
        </body>`,
        `<head>
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="title">
            <div class="title">
                <h1>Doelen</h1>
            </div>
            <div class="ul">
                <ul>
                    <li>HTML leren</li>
                    <li>CSS leren</li>
                    <li>JavaScript leren</li>
                </ul>
            </div>
        </body>`,
        `<head>
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="title">
            <div class="title">
                <h1>Stappenplan</h1>
            </div>
            <div class="ul">
                <ul>
                    <li>JavaScript cursus afronden</li>
                    <li>HTML en CSS cursus afronden</li>
                    <li>Website maken</li>
                    <ul>
                        <li>Navigation bar maken</li>
                        <li>Agenda widget toevoegen</li>
                        <li>Snelkoppelingen toevoegen</li>
                        <li>Games toevoegen</li>
                        <li>Notitiesysteem maken</li>
                    </ul>
                </ul>
            </div>
        </body>`,
        `<head>
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="title">
            <div class="title">
                <h1>Samenvatting</h1>
            </div>
            <div class="ul">
                <ul>
                    <li>Cursus op scrimba</li>
                    <li>JavaScript vond ik erg leuk</li>
                    <li>HTML cursus was niet nodig</li>
                    <li>CSS vond ik het lastigst</li>
                </ul>
            </div>
        </body>`,
        `<head>
            <title>page ${page}</title>
            <style>html{visibility: hidden;opacity:0;}</style>
            <link rel="stylesheet" href="/Presentaties/PresentatieWorkspace/style.css">
            <script src="script.js"></script>
        </head>
        <body class="start">
            <div class="start" style="margin-top:250px;">
                <h1 class="start"> <a style="text-decoration:none; color:black;" href="../../JavaScript/Workspace/index.html" target="_blank">Mijn Website</a></h1>
            </div>
        </body>`,
    ]
    html.innerHTML = pages[page]
}

updatePage()

document.addEventListener("keydown", function(e) {
    console.log(e.keyCode)
    if (e.keyCode === 39 && page < pages.length-1) {
        page += 1
        updatePage()
    }
    if (e.keyCode === 37 && page > 0) {
        page -= 1
        updatePage()
    }
})