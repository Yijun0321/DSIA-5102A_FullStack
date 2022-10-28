<script>
    console.log("hello from terminal");


    //fetch('https://jsonplaceholder.typicode.com/todos/1')
    //    .then(response => response.json())
    //    .then(data => console.log(data));


    const num1 = 1;
    let num2 = 2;
    async function fetchProducts() {
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
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
    fetchProducts();


    let user = { loggedIn: false };
    function toggle() {
		user.loggedIn = !user.loggedIn;
	}


    let data2;
    async function getRequest() {
        try {
            const response2 = await fetch('https://jsonplaceholder.typicode.com/todos');
            if (!response2.ok) {
                throw new Error(`HTTP error: ${response2.status}`);
            }
            data2 = await response2.json();
            //console.log(data2[0]);
        }
        catch (error) {
            console.error(`Could not get products: ${error}`);
        }
    }
</script>

<div class="flex justify-center justify-items-center grid grid-flow-row auto-rows-max p-10">
    <p>Hello there</p>
    <a class="underline" href="https://svelte.dev/tutorial/basics">Link to Svelte tutorial</a>
    <a class="underline" href="https://tailwindcss.com/docs/text-color">Link to Tailwind CSS docs</a>
    <button class="m-3 p-3 text-white bg-green-400" on:click={toggle}>button</button>
    <p>{user.loggedIn}</p>
    <button class="m-3 p-3 text-white bg-green-400" on:click={getRequest}>button2</button>
    
    {#if data2}
	{data2}
    {/if}
</div>