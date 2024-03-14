<script>
    import "../app.css";
    import logo from "../lib/assets/logo.webp";
</script>

<header class="flex flex-wrap p-2 gap-4">
    <img class="h-20 w-auto" src={logo} alt="IBM">
    <div class="p-1">
        <h1 class="text-3xl font-serif font-extrabold py-1 px-2">Major Project</h1>
        <h2 class="text-xl font-serif font-bold text-purple-600 shadow-inner shadow-purple-700 px-2">Customer Behavior Analysis</h2>
    </div>
</header>
<slot />
<footer class="bg-purple-700 shadow-inner shadow-purple-800 h-48 p-4 w-full flex flex-wrap justify-between">
    <div>
        <p class="text-white font-serif font-bold text-xl p-1">Created by :</p>
        <p class="text-white font-serif px-1">Aditya Narayan Panda</p>
        <p class="text-white font-serif px-1">M.S.L.V. Saranya</p>
        <p class="text-white font-serif px-1">Sonali Nanda</p>
        <p class="text-white font-serif px-1">Bhandari Sree Shivani</p>
    </div>
    <div class="py-9">
        <p class="text-white font-serif font-bold text-xl p-1 text-right">Guided by :</p>
        <p class="text-white font-serif px-1">Dr. Chinmaya Kumar Nayak</p>
    </div>
</footer>