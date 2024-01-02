import TrainingServices from "@/modules/training/services/index.ts";

export const serviceCatalog = {
  ...TrainingServices,
};

export function getServiceByBasename(serviceBasename: string) {
  const service = serviceCatalog[serviceBasename][0];
  if (!service) {
    throw new Error(`Service '${serviceBasename}' not found. Available services: ${Object.keys(serviceCatalog)}.`);
  }
  return service;
}
