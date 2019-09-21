<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto subject-title">
      <v-card-title>
        All
        <span class="subject-length">{{ subjects.length }}</span>
        Subjects
        <v-spacer />
        <v-text-field v-model="searchText" append-icon="search" label="講義名検索"></v-text-field>
      </v-card-title>
      <syllabus-card :links="subjects" :card_col="3" />
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout>
    <h2 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{ subjects.length }}</span>
      Subjects
    </h2>

    <input
      class="syllabus-input"
      placeholder="講義名検索"
      v-model="searchText"
    />

    <transition-group name="syllabus-tags" tag="nav">
      <syllabus-button :link="link" v-for="link in subjects" :key="link.id" />
    </transition-group>
  </syllabus-layout>
  -->
</template>

<script>
import SyllabusCard from "../components/SyllabusCard";

export default {
  metaInfo: {
    title: "Subjects"
  },
  data() {
    return {
      page_col: 3,
      searchText: ""
    };
  },
  computed: {
    subjects() {
      let subjects = this.$page.allSubject.edges.map(edge => {
        const { title, id } = edge.node;
        return {
          id,
          name: title,
          url: `/subject/${id}`
        };
      });

      if (this.searchText) {
        subjects = subjects.filter(subject =>
          subject.name.includes(this.searchText)
        );
      }
      return subjects;
    }
  },
  components: {
    SyllabusCard
  }
};
</script>

<page-query>
query {
  allSubject {
    edges {
      node {
        id
        title
      }
    }
  }
}
</page-query>

<style lang="scss" scoped>
.subject {
  &-title {
    padding: 30px 40px;
  }
  &-length {
    margin: 5px;
    font-size: 1.2em;
    color: rgb(0, 147, 226);
  }
}
</style>
