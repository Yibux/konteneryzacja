<script setup lang="ts">
import { mdiHome, mdiInformationOutline, mdiCheckboxMultipleMarkedCircle, mdiMenu } from '@mdi/js'
import { onMounted, computed, ref } from 'vue'
import router from '@/router'
import { useDisplay } from 'vuetify'

const isLoggedIn = ref(false)
const { name } = useDisplay()

const isDesktop = computed(() => {
  switch (name.value) {
    case 'xs':
    case 'sm':
      return false
    default:
      return true
  }
})
</script>

<template>
  <v-navigation-drawer v-if="isDesktop" permanent>
    <v-list>
      <v-list-item v-if="!isLoggedIn"
        ><v-btn
          variant="elevated"
          class="ml-1"
          color="primary"
          @click="() => router.push('/SignUp')"
          >{{ $t('SignUp') }}</v-btn
        ></v-list-item
      >

      
    </v-list>

    <v-divider class="my-2"></v-divider>

    <v-list density="compact" nav>
      <v-list-item to="/" nav :title="$t('Home')">
        <template #prepend> <v-icon size="large" :icon="mdiHome" class="mr-4"></v-icon></template>
      </v-list-item>

      <v-list-item to="/dashboard" nav :title="$t('Todo')">
        <template #prepend
          ><v-icon size="large" :icon="mdiCheckboxMultipleMarkedCircle" class="mr-4"></v-icon
        ></template>
      </v-list-item>

      <v-list-item to="/about" nav :title="$t('About')">
        <template #prepend
          ><v-icon size="large" :icon="mdiInformationOutline" class="mr-4"></v-icon
        ></template>
      </v-list-item>
    </v-list>

    <v-select
      v-model="$i18n.locale"
      :items="['Polski', 'English']"
      :value="$i18n.locale"
      :label="$t('LangLabel')"
      variant="solo"
    >
    </v-select>
  </v-navigation-drawer>

  <v-toolbar v-else>
    

    <v-spacer></v-spacer>

    <div class="w-35">
      <v-select
        v-model="$i18n.locale"
        rounded
        class="mr-4 mt-4"
        :items="['Polski', 'English']"
        :value="$i18n.locale"
        :label="$t('LangLabel')"
        density="compact"
        variant="solo"
      >
      </v-select>
    </div>

    <v-menu>
      <template #activator="{ props }">
        <v-btn color="primary" dark v-bind="props" :icon="mdiMenu"> </v-btn>
      </template>

      <v-list density="compact" nav>
        <v-list-item to="/" nav :title="$t('Home')">
          <template #prepend> <v-icon size="large" :icon="mdiHome" class="mr-4"></v-icon></template>
        </v-list-item>

        <v-list-item to="/dashboard" nav :title="$t('Todo')">
          <template #prepend
            ><v-icon size="large" :icon="mdiCheckboxMultipleMarkedCircle" class="mr-4"></v-icon
          ></template>
        </v-list-item>

        <v-list-item to="/about" nav :title="$t('About')">
          <template #prepend
            ><v-icon size="large" :icon="mdiInformationOutline" class="mr-4"></v-icon
          ></template>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-toolbar>
</template>
