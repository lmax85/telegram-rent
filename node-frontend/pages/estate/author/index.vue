<template>
  <v-row justify="center" align="center" class="tasklist--container">
    {{ $route.params }}
  </v-row>
</template>

<script>
export default {
  name: 'EstateAuthorPage',
  components: {

  },
  data() {
    return {
      message: null,
    }
  },
  async created() {
  },
  async fetch({ params }) {
    // try {
    //   const url = this.$isServer
    //     ? `http://host.docker.internal:7100/api/messages?${queryString}`
    //     : `http://localhost:7100/api/messages?${queryString}`
    //   // console.log("🚀 ~ file: index.vue ~ line 27 ~ fetch ~ url", url)
    //   const response = await this.$axios.get(url)
    //   // console.log("🚀 ~ file: _id.vue ~ line 131 ~ fetch ~ response.data", response.data)

    //   if (!response.data) {
    //     throw new Error('No data')
    //   }

    //   this.messages = response.data.data
    //   this.pagination = response.data.meta
    //   this.countries = response.data.meta.countries
    //   this.cities = response.data.meta.cities

    //   this.filteredCities = this.cities.filter((city) => city.country_id === this.activeCountry)

    //   if (response.data.meta && response.data.meta.price_max > 0) {
    //     this.priceMax = response.data.meta.price_max
    //     if (this.priceRange[1] === 0) {
    //       this.priceRange = [this.priceRange[0], response.data.meta.price_max]
    //     }
    //   }
    // } catch (error) {
    //   console.error('🚀 ~ file: index.vue ~ line 28 ~ fetch ~ error', error)
    // }
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
