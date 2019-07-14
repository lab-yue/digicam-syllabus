<template>
  <syllabus-layout>
    <h2 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{subjects.length}}</span> Subjects
    </h2>

    <input class="syllabus-input" placeholder="講義名検索" v-model="searchText" />

    <transition-group name="syllabus-tags" tag="nav">
      <syllabus-button :link="link" v-for="link in subjects" :key="link.id" />
    </transition-group>
  </syllabus-layout>
</template>

<script>
export default {
  metaInfo: {
    title: "Subjects"
  },
  data() {
    return {
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
  }
};
</script>

<page-query>
query {
    allSubject {
    edges{
      node{
        id
        title
      }
    }
  }
}
</page-query>


<style lang="scss" scoped>
</style>
