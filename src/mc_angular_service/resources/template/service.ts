import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { {pascal_case} } from "./{pascal_case}";
import { first } from "rxjs";


@Injectable({
  providedIn: 'root',
})
export class {pascal_case}Service {
  apiUrl = environment.apiUrl;
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})
  
  constructor(private http: HttpClient) {}

  findAll() {
    return this.http.get<{pascal_case}[]>(`${this.apiUrl}/{kebab_case}`)
    .pipe(first())
    
  }

  findOne(id: string) {
    return this.http.get<{pascal_case}>(`${this.apiUrl}/{kebab_case}/${id}`)
    .pipe(first())
  }

  update(item: {pascal_case}) {
    return this.http.put<{pascal_case}>(`${this.apiUrl}/{kebab_case}/${item.id}`, item, {headers: this.httpHeaders})
    .subscribe((res) => {console.error(res)})
  }

  delete(item: {pascal_case}) {
    return this.http.delete<{pascal_case}>(`${this.apiUrl}/{kebab_case}/${item.id}`, item, {headers: this.httpHeaders})
    .subscribe((res) => {console.error(res)})
  }
}
