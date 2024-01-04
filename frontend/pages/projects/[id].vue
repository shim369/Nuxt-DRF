<script setup>
const route = useRoute()

const { data: project } = await useFetch('http://127.0.0.1:8000/api/v1/projects/' + route.params.id + '/')

useSeoMeta({
    title: project.value.title,
    description: project.value.description
})
</script>
<template>
    <div class="py-10 px-6 max-w-[800px] w-[90%] m-auto bg-[#3a3a3a] mt-10 border-b-8 border-[#e82c2c]">
        <div class="m-auto md:col-span-3">
            <h1 class="mb-6 text-2xl">{{ project.title }}</h1>
            <img :src="project.image_url" class="max-h-[400px] w-full object-cover" :alt="project.title">
            <div class="mt-6 text-xl">{{ project.content }}</div>
            <div class="mt-10">
                <a :href="project.demo_link" target="_blank" rel="noopener noreferrer"
                    class="bg-[#2b2a2a] py-1 px-3 inline-block hover:bg-transparent border-2 border-[#2b2a2a] hover:text-[#fff] hover:border-2 hover:border-[#2b2a2a] mr-2">Site</a>
                <a :href="project.github_repo" target="_blank" rel="noopener noreferrer"
                    class="bg-[#2b2a2a] py-1 px-3 inline-block hover:bg-transparent border-2 border-[#2b2a2a] hover:text-[#fff] hover:border-2 hover:border-[#2b2a2a]">GitHub</a>
            </div>
        </div>
    </div>
</template>