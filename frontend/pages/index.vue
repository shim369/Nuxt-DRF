<script setup>
const { data: projects } = await useFetch('http://127.0.0.1:8000/api/v1/projects/newest/')

// console.log(projects.value)

useSeoMeta({
    title: 'My portfolio site',
    description: 'My portfolio site'
})
</script>
<template>
    <div class="py-40 px-6 bg-[#1a1a1a] text-center">
        <h1 class="text-transparent lilita-one text-4xl text-stroke font-bold mb-2 md:text-8xl">WEB DEVELOPMENT</h1>
        <p class="lilita-one text-xl text-[#6b6b6b]">My Portfolio site</p>
    </div>
    <div class="grid md:grid-cols-4 gap-6 py-10 px-6 text-white">
        <main class="md:col-span-3">
            <ul class="space-y-4">
                <project
                    v-for="project in projects"
                    v-bind:key="project.id"
                    v-bind:project="project"
                />
            </ul>
        </main>
        <aside class="md:col-span-1">
            <div class="p-5 bg-[#3a3a3a]">
                <h2 class="text-2xl mb-4 border-b-2 border-[#000] pb-2">Profile</h2>
                <div class="mb-20">
                    <div class="py-8">
                        <img src="/pongki2.jpg" alt=""
                            class="rounded-full max-w-[150px] w-[100%] max-h-[150px] h-[100%] m-auto mb-6" />
                    </div>
                    <p class="text-center">S-Ohtani</p>
                    <p class="text-center">Passionate developer</p>
                </div>

                <h2 class="text-2xl mb-4 border-b-2 border-[#000] pb-2">Skills</h2>
                <div class="mb-8 flex flex-row break-all">
                    <p class="mr-2">Python</p>
                    <p>JavaScript</p>
                </div>
            </div>
        </aside>
    </div>
</template>

<style>
.text-stroke {
    -webkit-text-stroke: 1px #E01A00;
}
</style>