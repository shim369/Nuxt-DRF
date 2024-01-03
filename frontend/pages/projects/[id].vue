<script setup>
const route = useRoute()

const { data: project } = await useFetch('http://127.0.0.1:8000/api/v1/projects/' + route.params.id + '/')

useSeoMeta({
    title: project.value.title,
    description: project.value.description
})
</script>
<template>
    <div class="py-10 px-6 grid md:grid-cols-4 gap-3">
        <div class="md:col-span-3">
            <h1 class="mh-6 text-3xl">{{ project.title }}</h1>
            <img :src="project.image_url" alt="">
            <p>{{ project.description }}</p>
            <p>{{ project.demo_link }}</p>
            <p>{{ project.github_repo }}</p>
        </div>
    </div>
</template>