<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">Post Project</h1>

        <form class="space-y-4">

            <div>
                <label>Title</label>
                <input type="text" class="w-full mt-2 p-4">
            </div>

            <div>
                <label>Description</label>
                <textarea type="text" class="w-full mt-2 p-4"></textarea>
            </div>

            <div>
                <label>Image URL</label>
                <input type="text" class="w-full mt-2 p-4">
            </div>

            <div>
                <label>Skills</label>
                <select class="w-full mt-2 p-4">
                    <option value="">Select Skills</option>
                    <option value="Skill 1">Skill 1</option>
                    <option value="Skill 2">Skill 2</option>
                    <option value="Skill 3">Skill 3</option>
                </select>
            </div>

            <div>
                <label>URL</label>
                <input type="text" class="w-full mt-2 p-4">
            </div>

            <div>
                <label>GitHub</label>
                <input type="text" class="w-full mt-2 p-4">
            </div>

            <button class="py-4 px-6 text-white bg-[#E01A00]">Submit</button>
        </form>
    </div>
</template>