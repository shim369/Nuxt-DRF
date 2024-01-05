<script setup>
import { ref } from 'vue'

const isOpen = ref(false);

const toggleNav = () => {
    isOpen.value = !isOpen.value;
};
</script>

<template>
    <header class="w-full bg-[#0f0f0f] p-6 flex items-center justify-between">
        <NuxtLink to="/" class="lilita-one text-xl text-[#E01A00] md:text-3xl">Portfolio</NuxtLink>

        <nav class="pc-nav flex items-center space-x-4">
            <NavLinks />
        </nav>

        <div :class="['nav-icon', { 'active': isOpen }]" @click="toggleNav">
            <span></span>
            <span></span>
            <span></span>
        </div>

        <nav :class="['sp-nav', { 'panelactive': isOpen }]">
            <NavLinks />
        </nav>

        <div :class="['circle', { 'circleactive': isOpen }]"></div>
    </header>
</template>

<style>
.sp-nav {
    display: none;
}

.sp-nav a {
    display: none;
}

.sp-nav.panelactive {
    position: fixed;
    z-index: 998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
}

.sp-nav.panelactive a {
    display: block;
    text-decoration: none;
    color: #fff;
    margin-bottom: 40px;
    text-transform: capitalize;
}

.nav-icon {
    position: fixed;
    top: 10px;
    right: 10px;
    z-index: 998;
    cursor: pointer;
    width: 50px;
    height: 50px;
    display: none;
    background: transparent;
    padding: 10px;
}

.nav-icon span {
    display: inline-block;
    transition: all .4s;
    position: absolute;
    left: 14px;
    height: 3px;
    border-radius: 2px;
    background: #E01A00;
    width: 45%;
}

.nav-icon span:nth-of-type(1) {
    top: 15px;
}

.nav-icon span:nth-of-type(2) {
    top: 23px;
}

.nav-icon span:nth-of-type(3) {
    top: 31px;
}

.nav-icon.active {
    z-index: 9999;
}

.nav-icon.active span {
    transition: all .4s;
}

.nav-icon.active span:nth-of-type(1) {
    top: 18px;
    left: 14px;
    transform: translateY(6px) rotate(-45deg);
    width: 45%;
}

.nav-icon.active span:nth-of-type(2) {
    opacity: 0;
}

.nav-icon.active span:nth-of-type(3) {
    top: 30px;
    left: 14px;
    transform: translateY(-6px) rotate(45deg);
    width: 45%;
}

@media screen and (max-width: 800px) {
    .pc-nav {
        display: none;
    }

    .sp-nav {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .nav-icon {
        display: block;
    }
}

.circle {
    position: fixed;
    z-index: 100;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: #0f0f0fe3;
    transform: scale(0);
    bottom: -50px;
    left: calc(50% - 50px);
    transition: all .2s;
}

.circle.circleactive {
    transform: scale(50);
}
</style>