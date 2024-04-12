<script>
    function analyze()
    {
        const id = document.getElementById("Cid").value;
        window.location.href = `http://localhost:5173/Individual/${id}`
    }
</script>




<div class="w-full h-96 bg-slate-300 flex flex-wrap justify-around">
    <div class="h-40 p-8 w-auto">
        <center>
            <h1 class="font-semibold">Enter Customer ID :</h1><br>
            <input id="Cid" type="text" class="h-8 w-48 px-2 rounded-sm"><br><br>
            <button on:click={analyze} class="h-10 w-40 border-2 m-2 hover:bg-purple-500 border-black bg-[#8ED1CD] rounded-sm font-semibold">Analyze</button>
        </center>
    </div>
</div>