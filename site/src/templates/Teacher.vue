<template>
  <syllabus-layout class="teacher">
    <h1 class="syllabus-page-title">{{ $page.teacher.name }}</h1>
    <p class="teacher-subjects-count">
      講義数
      <span class="syllabus-page-title-count">{{ subjects.length }}</span>
    </p>

    <syllabus-list :items="subjects" />
  </syllabus-layout>
</template>

<page-query>
query Teacher($id: String!) {
  teacher: teacher(id: $id) {
    name
    subjects {
      node {
        id
        title
      }
    }
  }
}
</page-query>

<script>
export default {
  metaInfo() {
    return {
      title: this.$page.teacher.name
    };
  },
  computed: {
    subjects() {
      let subjects = this.$page.teacher.subjects.node.map(({ title, id }) => {
        return {
          id,
          name: title,
          url: `/subject/${id}`
        };
      });
      return subjects;
    }
  }
};
</script>

<style lang="scss" scoped>
.teacher {
  &-subjects {
    &-count {
      color: $theme-green;
      text-align: center;
    }
  }
}
</style>
