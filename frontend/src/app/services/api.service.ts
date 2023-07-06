import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';

export interface ChartData {
  timestamp: string;
  total_players: number;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getLiveData(type: string, filter: string): Observable<any> {
    return this.http.get<any>(`${environment.API_URL}/${type}/lasthour/${filter}`)
      .pipe(
        catchError(this.handleError)
      );
  }

  getStatistics(type: string): Observable<any> {
    return this.http.get<any>(`${environment.API_URL}/${type}/latestbatch`)
      .pipe(
        catchError(this.handleError)
      );
  }
  
  private handleError(error: { status: any; error: any; }) {
    // You can transform error response here if needed
    console.error(
      `Backend returned code ${error.status}, ` +
      `body was: ${error.error}`
    );
  
    // Return an observable with a user-facing error message
    return throwError(
      'Something bad happened; please try again later.');
  }
}
