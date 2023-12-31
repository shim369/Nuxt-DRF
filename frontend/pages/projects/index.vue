<template>
    <div class="grid md:grid-cols-4 gap-6 py-10 px-6">
        <aside class="md:col-span-1 px-6 py-6">
            <div class="flex space-x-4">
                <input type="search" placeholder="Find project" class="w-full px-6 py-4">
                <button class="px-6 py-6 text-white bg-[#E01A00] border-2 border-[#E01A00] hover:bg-transparent hover:text-[#E01A00] hover:border-2 hover:border-[#E01A00]">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                    </svg>
                </button>
            </div>
            <hr class="my-6 opacity-30">
            <h3 class="mt-6 text-xl text-white">Skills</h3>
            <div class="mt-6 space-y-4">
                <p class="py-4 px-6 text-white">Skill 1</p>
                <p class="py-4 px-6 text-white">Skill 2</p>
                <p class="py-4 px-6 text-white">Skill 3</p>
            </div>
        </aside>
        <main class="md:col-span-3">
            <ul class="space-y-4">
                <project />
                <project />
                <project />
            </ul>
        </main>
    </div>
</template>