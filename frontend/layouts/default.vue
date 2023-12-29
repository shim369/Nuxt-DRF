<template>
    <header class="w-full bg-[#0f0f0f] p-6 flex items-center justify-between">
        <NuxtLink to="/" class="text-xl text-white md:text-3xl">Portfolio</NuxtLink>

        <div class="flex items-center space-x-4">
            <NuxtLink to="/" class="text-white">Home</NuxtLink>
            <NuxtLink to="/projects" class="text-white">Projects</NuxtLink>
        </div>
    </header>
    <div class="min-h-screen text-white">
        <slot />
    </div>
    <footer class="flex justify-center p-5 text-[#fff]">
        Copright (c) 2023 - Portfolio
    </footer>
</template>