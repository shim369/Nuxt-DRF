<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/store/user'

const userStore = useUserStore()
const router = useRouter()
let projects = ref()

onMounted(() => {
  if (!userStore.user.isAuthenticated) {
    router.push('/login')
  } else {
    getProjects()
  }
})

async function getProjects() {
    await $fetch('http://127.0.0.1:8000/api/v1/projects/admin', {
        headers: {
            'Authorization': 'token ' + userStore.user.token,
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        projects.value = response
    })
    .catch(error => {
        console.log('error', error)
    })
}
</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">Admin</h1>

        <ul class="space-y-4">
            <project
                v-for="project in projects"
                :key="project.id"
                :project="project"
                :admin="true"
            />
        </ul>
    </div>
</template>