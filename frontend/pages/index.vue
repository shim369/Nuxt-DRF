<template>
    <div class="py-40 px-6 bg-[#1a1a1a] text-center">
        <h1 class="text-5xl text-white">My portfolio site</h1>
    </div>
    <div class="grid md:grid-cols-4 gap-6 py-10 px-6 text-white">
        <main class="md:col-span-3">
            <ul class="mb-8">
                <li class="flex flex-col mb-8 w-full p-5 bg-[#3a3a3a] md:flex-row" key="">

                    <img src="" alt="" class="w-full md:w-1/4 h-auto max-h-[300px] object-cover" width="300" height="200" />
                    <div class="w-full md:w-3/4 ml-0 mt-5 md:ml-5 md:mt-0">
                        <h2 class="text-2xl border-b-2 border-[#fff]">title</h2>
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
                                    <td class="bg-[#2b2a2a] p-4 break-all"><a href="" target="_blank"
                                            rel="noopener noreferrer" class="underline hover:no-underline">demo_link</a>
                                    </td>
                                </tr>
                                <tr>
                                    <th class="bg-[#2b2a2a] p-4">GitHub</th>
                                    <td class="bg-[#2b2a2a] p-4 break-all"><a href="" target="_blank"
                                            rel="noopener noreferrer"
                                            class="underline hover:no-underline">article.github_repo
                                        </a></td>
                                </tr>
                            </tbody>
                        </table>
                        <nuxt-link to="/projects/1"
                            class="bg-[#E01A00] py-2 px-4 text-white float-right rounded-full border-2 border-[#E01A00] hover:bg-transparent hover:text-[#E01A00] hover:border-2 hover:border-[#E01A00]">Detail</nuxt-link>
                    </div>
                </li>
            </ul>
        </main>
        <aside class="md:col-span-1">
            <div class="p-5 bg-[#3a3a3a]">
                <h2 class="text-2xl mb-4 border-b-2 border-[#fff]">Profile</h2>
                <div class="mb-20">
                    <div class="py-8">
                        <img src="/pongki2.jpg" alt=""
                            class="rounded-full max-w-[150px] w-[100%] max-h-[150px] h-[100%] m-auto mb-6" />
                    </div>
                    <p class="text-center">S-Ohtani</p>
                    <p class="text-center">Passionate developer</p>
                </div>

                <h2 class="text-2xl mb-4 border-b-2 border-[#fff]">Skills</h2>
                <div class="mb-8 flex flex-row break-all">
                    <p class="mr-2">Python</p>
                    <p>JavaScript</p>
                </div>
            </div>
        </aside>
    </div>
</template>