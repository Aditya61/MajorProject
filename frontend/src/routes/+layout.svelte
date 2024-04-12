<script>
    import "../app.css";
    import logo from "../lib/assets/logo.webp";
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<header class="flex flex-wrap justify-between p-2 gap-4">
    <div class="flex flex-wrap">
        <img class="h-20 w-auto" src={logo} alt="IBM">
        <div class="p-1">
            <h1 class="text-3xl font-serif font-extrabold py-1 px-2">Major Project</h1>
            <h2 class="text-xl font-serif font-bold text-purple-600 shadow-inner shadow-purple-700 px-2">Customer Behavior Analysis</h2>
        </div>
    </div>
    <div class="flex flex-wrap gap-5">
        <button class="px-4 h-12 bg-orange-100 rounded-sm"><a href="http://localhost:5173/">Home</a></button>
        <button class="px-4 h-12 bg-orange-100 rounded-sm"><a href="http://localhost:5173/Individual">Individual Dashboard</a></button>
        <button class="px-4 h-12 bg-orange-100 rounded-sm"><a href="http://localhost:5173/Grouped">Grouped Dashboard</a></button>
        <div class="bg-orange-100 rounded-full h-12 w-12"></div>
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