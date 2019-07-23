<template>
  <syllabus-layout class="teacher">
    <h1 class="syllabus-page-title">
      All
      <span class="syllabus-page-title-count">{{teachers.length}}</span>Teachers
    </h1>

    <input class="syllabus-input" placeholder="名前検索" v-model="searchText" />

    <transition-group name="syllabus-tags" tag="nav">
      <syllabus-button :link="link" v-for="link in teachers" :key="link.name" />
    </transition-group>
  </syllabus-layout>
</template>

<script>
export default {
  metaInfo: {
    title: "Teachers"
  },
  data() {
    return {
      searchText: ""
    };
  },
  computed: {
    teachers() {
      let teachers = this.$page.allTeacher.edges.map(edge => {
        const { name, id, subjects } = edge.node;
        return {
          extra: subjects.totalCount,
          name,
          url: `/teacher/${id}`
        };
      });

      if (this.searchText) {
        teachers = teachers.filter(teacher =>
          teacher.name.includes(this.searchText)
        );
      }
      return teachers;
    }
  }
};
</script>

<page-query>
query {
  allTeacher {
    edges {
      node {
        id
        name
        subjects{
          totalCount
        }
      }
    }
  }
}
</page-query>

<style lang="scss" scoped>
</style>
