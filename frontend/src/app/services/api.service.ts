import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError, Subject, Observer } from 'rxjs';
import { environment } from 'src/environments/environment';

export interface BarChartData {
  name: string,
  timestamps: Array<string>,
  min_players: Array<number>,
  max_players: Array<number>
}

export interface ChartData {
  timestamp: string;
  total_players: number;
  total_servers: number;
}

export interface LatestBatch {
  id: number;
  batch_id: string;
  timestamp: string;
  name: string;
  total_players: number;
  total_servers: number;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private ws: WebSocket | null = null;

  constructor(private http: HttpClient) { }

  public connect(url: string): Observable<any> {
    this.ws = new WebSocket(url);
    return new Observable((subscriber) => {
      this.ws!.onmessage = (event) => subscriber.next(event);
      this.ws!.onerror = (event) => subscriber.error(event);
      this.ws!.onclose = (event) => subscriber.complete();
      return () => this.ws!.close();
    });
  }

  public disconnect(): void {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }

  public getPlayerStatistics(range: string): Observable<any> {
    return this.http.get<any>(`${environment.API_URL}/playerstatistics/${range}`)
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
