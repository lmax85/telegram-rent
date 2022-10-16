<template>
  <v-row justify="center" align="center">
    <v-card
      v-if="message"
      class="mt-12 mx-auto"
    >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>

      <v-carousel v-if="message.photos && message.photos.length"
        :hide-delimiters="true"
        :show-arrows-on-hover="true">
        <v-carousel-item
          v-for="photo in message.photos"
          :key="photo.id"
          :src="photo.path"
        ></v-carousel-item>
      </v-carousel>

      <v-img
        v-else
        height="250"
        src="/media/noimage.png"
      ></v-img>

      <v-card-title>
        <a :href="'https://t.me/' + message.author.username"
          class="d-inline-flex align-start flex-nowrap overflow-hidden text--grey text-decoration-none"
          style="color: black;"
          target="_blank">
          <v-avatar
            color="indigo"
            size="36"
            class="mr-1"
          >
            <img
              v-if="message.author.avatar_path"
              :src="message.author.avatar_path"
              :alt="getAuthorTitle(message.author)"
            >
            <span v-else class="white--text text-h5">{{ getAuthorTitle(message.author, true) }}</span>
          </v-avatar>
          <div class="text-truncate">{{ getAuthorTitle(message.author) }}</div>
        </a>
      </v-card-title>
      <a :href="'https://t.me/' + message.group.username"
          class="caption float-right mt-n4 mr-2 overflow-hidden"
          style="color: black;"
          target="_blank">
        <div>{{ getAuthorTitle(message.group) }}</div>
      </a>

      <v-card-text>
        <div class="d-flex justify-space-between align-end my-2 text-subtitle-1 black--text">
          <div>
            <strong>$ {{ message.price }}</strong>
          </div>
          <div class="caption grey--text float-right">{{ message.updated_at | formatDate('DD.MM.YYYY') }}</div>
        </div>

        <div class="overflow-hidden" style="height: 150px;">{{ message.text }}</div>
      </v-card-text>
    </v-card>
  </v-row>
</template>

<script>
export default {
  name: 'EstateAuthorMessagePage',
  components: {

  },
  data() {
    return {
      message: null,
    }
  },
  async created() {
  },
  async fetch() {
    const params = this.$route.params

    try {
      const url = this.$isServer
        ? `${this.$config.backendUrl}/api/estate/authors/${params.author_id}/messages/${params.id}`
        : `${this.$config.appUrl}/api/estate/authors/${params.author_id}/messages/${params.id}`

      const response = await this.$axios.get(url)

      if (!response.data) {
        throw new Error('No data')
      }

      this.message = response.data.data
      // this.pagination = response.data.meta
      // this.countries = response.data.meta.countries
      // this.cities = response.data.meta.cities

      // this.filteredCities = this.cities.filter((city) => city.country_id === this.activeCountry)

      // if (response.data.meta && response.data.meta.price_max > 0) {
      //   this.priceMax = response.data.meta.price_max
      //   if (this.priceRange[1] === 0) {
      //     this.priceRange = [this.priceRange[0], response.data.meta.price_max]
      //   }
      // }
    } catch (error) {
      console.error('🚀 ~ file: index.vue ~ line 28 ~ fetch ~ error', error)
    }
  },
  watch: {
  },
  filters: {
    plural(n, forms) {
        let idx;
        // @see http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html
        if (n % 10 === 1 && n % 100 !== 11) {
            idx = 0; // many
        } else if (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) {
            idx = 1; // few
        } else {
            idx = 2; // one
        }
        return forms[idx] || '';
    }
  },
  methods: {
    getAuthorTitle(author, isShort = false) {
      let title = ''

      if (author.title) {
        title = author.title
      } else if (author.first_name && author.last_name) {
        title = `${author.first_name} ${author.last_name}`
      } else if (author.first_name) {
        title = author.first_name
      } else if (author.last_name) {
        title = author.last_name
      } else {
        title = author.username
      }

      return isShort ? title[0] : title
    },
  },
}
</script>

<style scoped>
</style>
