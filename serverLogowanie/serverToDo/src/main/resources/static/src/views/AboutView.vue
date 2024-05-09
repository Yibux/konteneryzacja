<script setup lang="ts">
const techArray = ['vue', 'firebase', 'i18n', 'vite', 'vitepwa', 'vuetify'] as string[]
</script>

<template>
  <div class="about" align="center" style="min-height: 65vh">
    <h1 class="my-4">{{ $t('AboutView.Title') }}</h1>

    <v-divider></v-divider>

    <h4 class="mt-4">{{ $t('AboutView.Text') }}</h4>

    <div align="left" class="ml-15 mt-4">
      <ul>
        <li v-for="(tech, index) in techArray" :key="index">
          {{ tech }}
        </li>
      </ul>
    </div>
  </div>
</template>
