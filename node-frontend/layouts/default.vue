<template>
  <v-app dark>
    <v-app-bar
      fixed
      app
    >
      <nuxt-link to="/" class="text-decoration-none indigo--text">
        <v-toolbar-title v-text="title" />
      </nuxt-link>
      <v-spacer />
      <v-btn
        icon
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>mdi-information-outline</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-navigation-drawer
      v-model="rightDrawer"
      :right="true"
      temporary
      fixed
      :width="$vuetify.breakpoint.xs ? '80%' : '50%'"
    >
      <div class="pa-8">
        <h2 class="mb-4">Some awesome info about project</h2>
      </div>
    </v-navigation-drawer>
    <v-footer>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data () {
    return {
      clipped: false,
      drawer: false,
      miniVariant: false,
      rightDrawer: false,
      title: 'Telegram Rent'
    }
  }
}
</script>
