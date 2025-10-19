```json
{
  "id": "b471bfca25d62720",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287839,
  "host_pid": "9e6742732c60:1",
  "hash": "44ead2268184aa93e625939e730e9030615cc865fccdd753cc3028569a42adde",
  "cid": "QmV144ead2268184aa93e625939e730e9030615cc865",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287839,
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
      "evaluated_at": 1760287839
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
  "sig": "ad43e719e6557e59acea5d407245c9d7540a0ecdd44763e8c714d5363f43f26d"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 063100274960966
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': 'f5e3b3cd48fefc81'}}}764, 'matching_hash': '6b9326523c35dc7b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.57, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9380590}}}