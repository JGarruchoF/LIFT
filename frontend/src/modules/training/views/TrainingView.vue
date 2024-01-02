<script setup lang="ts">
import { ref } from "vue";

import { IonPage, IonContent, IonCard, IonCardContent } from "@ionic/vue";

const previousTrainings = ref<TrainingSession[]>([]);
async function fetchPreviousTrainings() {
  previousTrainings.value = await getServiceByBasename("TrainingSessionService").getUserTrainings({
    limit: 5,
    offset: 0,
  });
}
fetchPreviousTrainings();
</script>

<template>
  <IonPage>
    <IonContent class="ion-padding">
      <IonCard>
        <IonCardContent></IonCardContent>
      </IonCard>
    </IonContent>
  </IonPage>
</template>

<script lang="ts">
import { getServiceByBasename } from "@/services/index.ts";

import type { TrainingSession } from "@/modules/training/types/training-session.ts";

export default {
  name: "TrainingView",
};
</script>