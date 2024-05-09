<script lang="ts" setup>
import { RouterView } from 'vue-router'
import NavigationBar from '@/components/NavigationBar.vue'
</script>

<template>
  <v-app>
    <v-main>
      <NavigationBar></NavigationBar>

      <v-row class="ma-2" justify="center">
        <v-col cols="12" sm="9" md="6">
          <v-card>
            <RouterView />
          </v-card>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>
