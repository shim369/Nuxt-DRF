<script setup>
import { useUserStore } from '@/store/user'

const userStore = useUserStore()

function logout() {
    userStore.removeToken()
}
</script>

<template>
    <div class="bg-black-orign">
        <header class="w-full bg-[#0f0f0f] p-6 flex items-center justify-between">
            <NuxtLink to="/" class="lilita-one text-xl text-[#E01A00] md:text-3xl">Portfolio</NuxtLink>

            <div class="flex items-center space-x-4">
                <NuxtLink to="/" class="text-white">Home</NuxtLink>
                <NuxtLink to="/projects" class="text-white">Projects</NuxtLink>

                <template v-if="userStore.user.isAuthenticated">
                    <NuxtLink to="/admin"
                        class="btn-red-rounded">
                        Admin</NuxtLink>
                    <NuxtLink to="/post"
                        class="btn-red-rounded">
                        Post Project</NuxtLink>
                    <a v-on:click="logout"
                        class="btn-red-rounded">
                        Log out</a>
                </template>

                <template v-else>
                    <NuxtLink to="/login"
                        class="btn-red-rounded">
                        Log in</NuxtLink>
                    <NuxtLink to="/signup"
                        class="btn-red-rounded">
                        Sign up</NuxtLink>
                </template>

            </div>
        </header>
        <div class="min-h-screen text-white">
            <slot />
        </div>
        <footer class="flex justify-center p-5 text-[#747474]">
            &copy; 2023 Portfolio
        </footer>
    </div>
</template>

<style scoped>
.bg-black-orign {
    background-image: radial-gradient(circle at center center, transparent, rgb(33, 33, 33)), repeating-linear-gradient(135deg, rgb(33, 33, 33) 0px, rgb(33, 33, 33) 2px, transparent 2px, transparent 10px, rgb(33, 33, 33) 10px, rgb(33, 33, 33) 11px, transparent 11px, transparent 21px), repeating-linear-gradient(45deg, rgb(47, 47, 47) 0px, rgb(47, 47, 47) 4px, transparent 4px, transparent 8px), linear-gradient(90deg, rgb(33, 33, 33), rgb(33, 33, 33));
}
</style>