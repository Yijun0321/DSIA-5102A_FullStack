<h1>Liste de Pokemon</h1>

<div class="flex justify-center justify-items-center grid grid-flow-row auto-rows-max p-10">
    <p>Trouver les informations de Pokémon dans la liste</p>
    <script>getPokemonAll()</script>
    <a href="/Pokemon">Pokemon #1 Pound</a>

    <p>Trouver les pokémon dans mon équipe</p>
    <a href="/Equipe">Mon équipe</a>
</div>

<script>
    fetch('https://localhost:5000/Pokemon')
        .then(response => response.json())
        .then(data => console.log(data));
    
    async function getPokemonAll() {
        try {
            const response = await fetch('https://localhost:5000/Pokemon');
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }
            const data = await response.json();
            console.log(data.title);
        }
        catch (error) {
            console.error(`Could not get products: ${error}`);
        }
    }
    getPokemonAll();

    async function getPokemonByIndex(Index) {
        try {
            var siteAdresse = 'https://localhost:5000/Pokemon/'.concat(Index.toString())
            const response = await fetch(siteAdresse);
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }
            const data = await response.json();
            console.log(data.title);
        }
        catch (error) {
            console.error(`Could not get products: ${error}`);
        }
    }
    getPokemonByIndex(1);
</script>