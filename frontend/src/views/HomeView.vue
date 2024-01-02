<template>
  <IonPage>
    <IonContent class="ion-padding">
      <IonGrid>
        <IonRow>
          <IonCol
            ><IonAvatar>
              <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
            </IonAvatar>
          </IonCol>
          <IonCol></IonCol>
        </IonRow>
      </IonGrid>
      <h1 class="ion-text-start">Last Sessions</h1>
      <IonCard>
        <IonCardContent><WeeklySessionsChart /></IonCardContent>
      </IonCard>
      <h1 class="ion-text-start">Achivements</h1>
      <h1 class="ion-text-start">Goals</h1>
    </IonContent>
  </IonPage>
</template>

<script setup lang="ts">
import { IonPage, IonContent, IonGrid, IonRow, IonCol, IonAvatar, IonCard, IonCardContent } from "@ionic/vue";
</script>

<script>
import WeeklySessionsChart from "@/components/WeeklySessionsChart.vue";

export default {
  name: "HomeView",
  components: { WeeklySessionsChart },
};
</script>
