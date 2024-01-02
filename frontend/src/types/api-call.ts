export interface Response<T> {
  items: [T];
  count: number;
}

export interface Filter {
  key: string;
  value: string | number | boolean | Date;
}

export interface SearchParams {
  limit?: number;
  offset?: number;
  filters?: [Filter];
}
