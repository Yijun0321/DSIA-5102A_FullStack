<h1>Mon équipe</h1>


<script>
    async function getEquipe() {
        try {
            const response = await fetch('https://localhost:5000/Equipe');
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
    getEquipe();
</script>