<template>
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
</template>

<script>
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
  }
};
</script>
