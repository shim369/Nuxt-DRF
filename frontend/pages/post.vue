<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/store/user'

const userStore = useUserStore()
const router = useRouter()

onMounted(() => {
    if (!userStore.user.isAuthenticated) {
        router.push('/login')
    }
})
let { data: projectsSkills } = await useFetch('http://127.0.0.1:8000/api/v1/projects/skills/')
let skill = ref('')
let title = ref('')
let description = ref('')
let image_url = ref('')
let demo_link = ref('')
let github_repo = ref('')
let errors = ref([])

async function submitForm() {
    console.log('submitForm')

    errors.value = []

    if (image_url.value == '') { errors.value.push('The image url field is missing') }
    if (title.value == '') { errors.value.push('The title field is missing') }
    if (description.value == '') { errors.value.push('The description field is missing') }
    if (skill.value == '') { errors.value.push('You must select a skill') }
    if (demo_link.value == '') { errors.value.push('The link field is missing') }
    if (github_repo.value == '') { errors.value.push('The github field is missing') }

    if (errors.value.length == 0) {
        await $fetch('http://127.0.0.1:8000/api/v1/projects/create/', {
            method: 'POST',
            headers: {
                'Authorization': 'token ' + userStore.user.token,
                'Content-Type': 'application/json'
            },
            body: {
                skill: skill.value,
                title: title.value,
                description: description.value,
                image_url: image_url.value,
                demo_link: demo_link.value,
                github_repo: github_repo.value,
            }
        })
            .then(response => {
                console.log('response', response)

                router.push({ path: '/admin' })
            })
            .catch(error => {
                if (error.response) {
                    for (const property in error.response._data) {
                        errors.value.push(`${property}: ${error.response._data[property]}`)
                    }
                    console.log(JSON.stringify(error.response))
                } else if (error.message) {
                    errors.value.push('Something went wrong. Please try again')

                    console.log(JSON.stringify(error))
                }
            })
    }
}
</script>
<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">Post Project</h1>

        <form v-on:submit.prevent="submitForm" class="space-y-4">

            <div>
                <label>Image URL</label>
                <input v-model="image_url" type="text" class="w-full mt-2 p-4 text-black">
            </div>

            <div>
                <label>Title</label>
                <input v-model="title" type="text" class="w-full mt-2 p-4 text-black">
            </div>

            <div>
                <label>Description</label>
                <textarea v-model="description" type="text" class="w-full mt-2 p-4 text-black"></textarea>
            </div>

            <div>
                <label>Skill</label>
                <select v-model="skill" class="w-full mt-2 p-4 text-black">
                    <option value="">Select Skill</option>
                    <option v-for="skill in projectsSkills" v-bind:key="skill.id" v-bind:value="skill.id">
                        {{ skill.title }}
                    </option>
                </select>
            </div>

            <div>
                <label>URL</label>
                <input v-model="demo_link" type="text" class="w-full mt-2 p-4 text-black">
            </div>

            <div>
                <label>GitHub</label>
                <input v-model="github_repo" type="text" class="w-full mt-2 p-4 text-black">
            </div>

            <div v-if="errors.length" class="mb-6 py-4 px-6 bg-[#f84934] text-white">
                <p v-for="error in errors" v-bind:key="error">
                    {{ error }}
                </p>
            </div>

            <button class="py-4 px-6 text-white bg-[#E01A00]">Submit</button>
        </form>
    </div>
</template>