<h1>Pokemon #1 Pound</h1>
<p>Index: 1</p>
<p>Name: Pound</p>
<p>Type: Normal</p>
<p>Category: Physical</p>
<p>Contest: Tough</p>
<p>PP: 35</p>
<p>Power: 40</p>
<p>Accuracy: 100</p>
<p>Generation: 1</p>

<button class="m-3 p-3 text-white bg-green-400" on:click={setEquipe}>Mettre dans mon équipe</button>

<script>
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

    function setEquipe(Index) {

    }
</script>