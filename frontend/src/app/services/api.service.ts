import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, throwError, fromEvent, map } from 'rxjs';
import { environment } from 'src/environments/environment';

export interface ChartData {
  timestamp: string;
  total_players: number;
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

  private socket: WebSocket | undefined;

  constructor(private http: HttpClient) { }

  connectSocket(type: string) {
    const url = `ws://localhost:8001/ws/${type}/`;
    this.socket = new WebSocket(url);
  }

  disconnectSocket(type: string) {
    this.socket?.close();
  }

  getLiveSocketData(type: string): Observable<any> {
    if (!this.socket) {
      throw new Error('WebSocket connection is not established. Please connect first.');
    }

    return fromEvent<MessageEvent>(this.socket, 'message').pipe(
      map(event => JSON.parse(event.data))
    );
  }

  // Soon to be deprecated
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
