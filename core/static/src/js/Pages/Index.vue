<template>
    <div>
      <h1>Django+inertia+vue</h1>
      hello vue {{ tevents }} ...
    </div>
  </template>
  
  <script setup>
  // ✅ On déclare la prop correctement avec `defineProps`
  const props = defineProps({
    tevents: String
  })
  </script>
  