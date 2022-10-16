<template>
  <div>
    <v-row>
      <v-col xl="2" lg="3" md="4" sm="6" xs="12"
        v-for="message, index in messages"
        :key="'message-' + index"
      >
        <v-card
          class="mx-auto"
          max-width="374"
          height="600"
        >
          <template slot="progress">
            <v-progress-linear
              color="deep-purple"
              height="10"
              indeterminate
            ></v-progress-linear>
          </template>

          <client-only placeholder="Loading...">
            <v-carousel v-if="message.photos && message.photos.length"
              :height="250"
              :hide-delimiters="true"
              :show-arrows-on-hover="true">
              <v-carousel-item
                v-for="photo in message.photos"
                :key="photo.id"
                :src="photo.path"
                height="250"
              ></v-carousel-item>
            </v-carousel>
            <v-img
              v-else
              height="250"
              src="/media/noimage.png"
            ></v-img>
          </client-only>

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

          <v-divider class="mx-4"></v-divider>

          <v-card-actions>
            <v-btn
              color="indigo"
              text
              :to="`/estate/author/${message.telegram_author_id}/message/${message.id}`"
            >Подробнее</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'MessageList',
  data: () => ({
    loading: false,
    selection: 1,
  }),
  props: {
    pagination: {
      type: Object,
      default: () => {},
    },
    messages: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
  computed: {

  },
  mounted() {
    /* eslint-disable no-console */
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
    reserve () {
        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
      },
  }
}
</script>

<style lang="scss">

</style>
