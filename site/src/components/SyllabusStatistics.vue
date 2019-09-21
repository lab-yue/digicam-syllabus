<template>
  <div>
    <template v-for="(field,index) of Object.keys(info)">
      <v-card class="s-card" :key="`${field}-${index}`">
        <v-card-title>{{upper(field)}}</v-card-title>
        <syllabus-card v-if="field != 'teacher'" :links="info[field]" :card_col="3" />
        <syllabus-card v-if="field === 'teacher'" :links="info[field]" :card_col="4" />
      </v-card>
    </template>
  </div>
  <!--
  <div>
    <div
      class="syllabus-page-statistics-wrapper"
      v-for="(field,index) of Object.keys(info)"
      :key="`${field}-${index}`"
    >
      <h2 class="syllabus-page-statistics-title">{{upper(field)}}</h2>
      <syllabus-button :link="link" v-for="link in info[field]" :key="link.id" />
    </div>
  </div>
  -->
</template>

<script>
import SyllabusCard from "../components/SyllabusCard";

import { collectSubjectInfo } from "../helpers";
export default {
  props: ["subjects", "keys"],
  computed: {
    info() {
      return collectSubjectInfo(this.subjects, this.keys);
    }
  },
  methods: {
    upper(str) {
      return str.slice(0, 1).toUpperCase() + str.slice(1);
    }
  },
  components: {
    SyllabusCard
  }
};
</script>

<style lang="scss" scoped>
.s {
  &-card {
    box-shadow: none;
    margin: 0 20px;
  }
}
</style>