<template>
  <router-view></router-view>
</template>
<script>

import HelloWorld from "@/components/HelloWorld.vue";
import VedioPlay from "@/components/VideoPlay.vue";

export default {
  components: {
    HelloWorld,
    VedioPlay,
    // Test,
  },
  setup() {
  }
};
</script>
