import Vue from 'vue'
import filters from '../filters'

for (const name in filters) {
  Vue.filter(name, filters[name]);
}
