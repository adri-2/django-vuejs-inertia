<template>
    <div class="p-4">
      <h1 class="text-2xl">Bienvenue, {{ username }}</h1>
    </div>
  </template>
  
  <script setup>
  defineProps({
    username: String
  })
  </script>
  