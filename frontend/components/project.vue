
import type { Style } from '#build/components';
<script setup>
const props = defineProps({
    my: {
        type: [Boolean]
    }
})
</script>
<template>
    <li class="flex flex-col w-full p-5 bg-[#3a3a3a] md:flex-row" key="">
        <img src="" alt="" class="w-full md:w-1/4 h-auto max-h-[300px] object-cover" width="300" height="200" />
        <div class="w-full md:w-3/4 ml-0 mt-5 md:ml-5 md:mt-0">
            <h2 class="text-2xl border-b-2 border-[#000] pb-2">title</h2>
            <p class="mt-4 mb-6">description</p>
            <table class="w-full border-separate mb-3">
                <tbody>
                    <tr>
                        <th class="bg-[#2b2a2a] p-4 w-[20%]">TECH</th>
                        <td class="bg-[#2b2a2a] p-4 break-all">
                            <ul class="flex">
                                <li key="tech" class="mr-2">tech
                                </li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <th class="bg-[#2b2a2a] p-4">URL</th>
                        <td class="bg-[#2b2a2a] p-4 break-all"><a href="" target="_blank" rel="noopener noreferrer"
                                class="underline hover:no-underline">demo_link</a>
                        </td>
                    </tr>
                    <tr>
                        <th class="bg-[#2b2a2a] p-4">GitHub</th>
                        <td class="bg-[#2b2a2a] p-4 break-all"><a href="" target="_blank" rel="noopener noreferrer"
                                class="underline hover:no-underline">article.github_repo
                            </a></td>
                    </tr>
                </tbody>
            </table>
            <div class="space-x-4 flex justify-end">
                <nuxt-link to="/projects/1"
                    class="bg-[#E01A00] py-2 px-4 text-white rounded-full border-2 border-[#E01A00] hover:bg-transparent hover:text-[#E01A00] hover:border-2 hover:border-[#E01A00]">Detail</nuxt-link>
                <nuxt-link to="/projects/1"
                    class="bg-[#E01A00] py-2 px-4 text-white rounded-full border-2 border-[#E01A00] hover:bg-transparent hover:text-[#E01A00] hover:border-2 hover:border-[#E01A00]"
                    v-if="my">Edit</nuxt-link>
                <nuxt-link to="/projects/1"
                    class="bg-[#E01A00] py-2 px-4 text-white rounded-full border-2 border-[#E01A00] hover:bg-transparent hover:text-[#E01A00] hover:border-2 hover:border-[#E01A00]"
                    v-if="my">Delete</nuxt-link>
            </div>
        </div>
    </li>
</template>