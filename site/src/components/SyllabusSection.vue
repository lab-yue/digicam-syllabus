<template>
  <section class="subject-section" v-if="isNotEmpty">
    <h2 class="syllabus-page-statistics-title subject-margin">{{title}}</h2>
    <div class="subject-section-txt">
      <p v-if="typeof content === 'string'" class="subject-txt">{{content}}</p>
      <ul v-else-if="Array.isArray(content)">
        <li v-for="line in content" :key="line">
          <p class="subject-txt">{{line}}</p>
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
export default {
  props: ["title", "content"],
  computed: {
    isNotEmpty() {
      if (Array.isArray(this.content)) {
        return this.content.length;
      } else {
        return this.content;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.subject {
  &-margin:not(:first-child) {
    margin-top: 4rem;
  }
  &-section {
    &-txt {
      color: #555;
      border-radius: 5px;
      padding: 1rem;
      background-color: #f2f6f5;
      font-size: 1.2rem;
    }
  }
  &-txt {
    margin: 0;
    white-space: pre-line;
    word-break: break-word;
    line-height: 1.5;
  }
}

@media screen and (max-width: 640px) {
  .subject {
    &-txt {
      font-size: 1rem;
    }
  }
}
</style>
