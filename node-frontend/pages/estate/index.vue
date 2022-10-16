<template>
  <v-row justify="center" align="center" class="tasklist--container">
    <v-col cols="12">
      <h1 class="title text-uppercase text-left pt-4 pb-12">Поиск недвижимость в странах СНГ из телеграм-каналов</h1>

      <v-row align="end" no-gutters>
        <v-col cols="6" md="3">
          <v-select
            :value="activeCountry"
            :items="countries"
            :menu-props="{ bottom: true, offsetY: true }"
            item-text="name"
            item-value="id"
            label="Выберите страну"
            class="mt-2"
            dense
            hide-details
            solo
            single-line
            @change="changeCountry"
          ></v-select>
        </v-col>
        <v-col cols="6" md="3">
          <v-select
            :value="activeCity"
            :items="filteredCities"
            :menu-props="{ bottom: true, offsetY: true }"
            item-text="name"
            item-value="id"
            label="Выберите город"
            class="mt-2 ml-2"
            dense
            hide-details
            solo
            single-line
            @change="changeCity"
          ></v-select>
        </v-col>

        <v-col cols="7" md="4">
          <v-range-slider
            v-model="priceRange"
            :min="0"
            :max="priceMax"
            step="100"
            :label="$vuetify.breakpoint.mobile ? '' : 'Цена'"
            :prepend-icon="$vuetify.breakpoint.mobile ? '' : 'mdi-currency-usd'"
            thumb-label="always"
            hide-details
            @end="applyFilter(false)"
          ></v-range-slider>
        </v-col>

        <v-col cols="5" md="2">
          <v-select
            v-model="sortByValue"
            :items="sortValues"
            :menu-props="{ bottom: true, offsetY: true }"
            label="Сортировать по"
            class="mt-2 ml-2 pa-0"
            dense
            hide-details
            solo
            single-line
            @change="applyFilter(false)"
          ></v-select>
        </v-col>

        <!-- <v-col cols="3">
          <v-btn primary class="float-right" @click="applyFilter">Сброс</v-btn>
        </v-col> -->
      </v-row>

      <h2 v-if="pagination && pagination.total > 0"
        class="title text-uppercase text-left pt-4 pb-2">Найдено {{ pagination.total }} {{ pagination.total | plural(['объявление', 'объявления', 'объявлений']) }}</h2>

      <MessageList :messages="messages" />

      <client-only placeholder="Loading...">
        <v-pagination
          v-if="pagination"
          class="mt-4"
          :value="pagination.current_page"
          :length="pagination.last_page"
          :total-visible="7"
          @input="paginationChange"></v-pagination>
      </client-only>
    </v-col>

    <v-snackbar
      v-model="errorShow"
      color="red accent-2"
      right>
      <p>{{ errorMessage }}</p>
      <v-btn color="accent" class="float-right" @click.native="errorShow = false">Закрыть</v-btn>
    </v-snackbar>
  </v-row>
</template>

<script>
import MessageList from '@/components/estate/MessageList.vue'

const DEFAULT_COUNTRY_ID = 1
const DEFAULT_CITY_ID = 1

// TODO: create mixin for process url params when page loaded first time
export default {
  name: 'EstateIndexPage',
  components: {
    MessageList
  },
  // layout: 'defau',
  // auth: AUTH_ENABLED,
  data() {
    return {
      countries: [],
      cities: [],
      filteredCities: [],
      activeCountry: null,
      activeCity: null,
      errorShow: '',
      errorMessage: '',
      pagination: null,
      messages: [],
      sortValues: [
        { text: 'Сортировать по дате', value: '-updated_at' },
        { text: 'Сортировать по возратснию цены (↑)', value: 'price' },
        { text: 'Сортировать по убыванию цены (↓)', value: '-price' },
      ],
      priceMax: 0,
      priceRange: [0, 0],
      sortByValue: '-updated_at',
    }
  },
  created() {
    this.parseUrlParams(this.$route.query)
  },
  async fetch() {
    try {
      this.hideError()
      let query = this.$route.query

      if (this.activeCountry === null && this.activeCity === null) {
        this.activeCountry = DEFAULT_COUNTRY_ID
        this.activeCity = DEFAULT_CITY_ID
      }

      query.country_id = this.activeCountry
      query.city_id = this.activeCity


      const queryString = Object.keys(query).map(key => key + '=' + query[key]).join('&');

      const url = this.$isServer
        ? `${this.$config.backendUrl}/api/estate/messages?${queryString}`
        : `${this.$config.appUrl}/api/estate1/messages?${queryString}`
      const response = await this.$axios.get(url)

      if (!response.data) {
        throw new Error('No data')
      }

      this.messages = response.data.data
      this.pagination = response.data.meta
      this.countries = response.data.meta.countries
      this.cities = response.data.meta.cities

      this.filteredCities = this.cities.filter((city) => city.country_id === this.activeCountry)

      if (response.data.meta && response.data.meta.price_max > 0) {
        this.priceMax = response.data.meta.price_max
        if (this.priceRange[1] === 0) {
          this.priceRange = [this.priceRange[0], response.data.meta.price_max]
        }
      }
    } catch (error) {
      console.error('🚀 ~ file: index.vue ~ line 28 ~ fetch ~ error', error)
      this.showError('Что-то пошло не так, попробуйте позже ¯\_(ツ)_/¯')
    }
  },
  watch: {
    '$route.query': '$fetch',
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
    parseUrlParams(query) {
      // Promise.all([
        this.parseSortBy(query)
        this.parseFilter(query)
      // ])
    },

    parseSortBy(query) {
      if (query['sort']) {
        this.sortByValue = query['sort']
      }
    },

    parseFilter(query) {
      if (query['filter[price_min]'] && query['filter[price_max]']) {
        this.priceRange = [parseInt(query['filter[price_min]']), parseInt(query['filter[price_max]'])]
      } else if (query['filter[price_min]']) {
        this.priceRange = [parseInt(query['filter[price_min]']), this.priceRange[1]]
      } else if (query['filter[price_max]']) {
        this.priceRange = [this.priceRange[0], parseInt(query['filter[price_max]'])]
      }

      if (query['country_id']) {
        this.activeCountry = parseInt(query['country_id'])
      }
      if (query['city_id']) {
        this.activeCity = parseInt(query['city_id'])
      }
    },

    paginationChange(page) {
      this.$router.push({
        path: this.$route.path,
        query: {
          ...this.$route.query,
          page,
        },
      })
      this.$vuetify.goTo(60)
    },

    changeCountry(countryId) {
      this.activeCountry = countryId
      this.activeCity = null
      this.filteredCities = this.cities.filter(city => city.country_id === countryId)

      if (this.filteredCities && this.filteredCities.length === 1) {
        this.activeCity = this.filteredCities[0].id
        this.applyFilter(true)
      }
    },

    changeCity(cityId) {
      this.activeCity = cityId
      this.priceRange = [0, 0]
      this.priceMax = 0
      this.applyFilter(true)
    },

    applyFilter(reset = false) {
      let query = {
        ...this.$route.query,
        page: 1,
        'country_id': this.activeCountry,
        'city_id': this.activeCity,
        'filter[price_min]': this.priceRange[0],
        'filter[price_max]': this.priceRange[1],
        'sort': this.sortByValue
      }

      if (reset) {
        this.priceRange = [0, 0]
        delete query['filter[price_min]']
        delete query['filter[price_max]']
      }

      this.$router.push({
        path: this.$route.path,
        query,
      })
    },

    showError(message) {
      this.errorShow = true;
      this.errorMessage = message;
    },

    hideError() {
      this.errorShow = false;
      this.errorMessage = '';
    },
  },
}
</script>

<style scoped>
</style>
