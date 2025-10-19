```json
{
  "id": "9897e33a284c57ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293819,
  "host_pid": "9e6742732c60:1",
  "hash": "460aa883809a1e787de6121a9ceb40afc1b6239e8fc8f2e13df4f8b37a2e9b4f",
  "cid": "QmV1460aa883809a1e787de6121a9ceb40afc1b6239e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293819,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293819
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "8d7779aa1b4a0f3526a2fbc16c4e4db6318bab07fc064ecd6217968b2968e304"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 111518570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}