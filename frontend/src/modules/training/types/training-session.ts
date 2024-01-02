import type { TimeStampedModel } from "@/modules/base/types/time-stamped.ts";
import type { User } from "@/modules/users/types/user.ts";

export interface TrainingSession extends TimeStampedModel {
  user: User;
  finished: boolean;
  duration?: number;
}
