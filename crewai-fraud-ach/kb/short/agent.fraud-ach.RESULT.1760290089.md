```json
{
  "id": "fd99b780d26339f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290089,
  "host_pid": "9e6742732c60:1",
  "hash": "87df0829dc35d077301c08e58bacb9afb4bb29493c26b9dc4a800b0a5fca06b7",
  "cid": "QmV187df0829dc35d077301c08e58bacb9afb4bb2949",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290089,
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
      "evaluated_at": 1760290089
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
  "sig": "4e13eb81748a9d9f554f11b09b4d236430c86aba609071177d7f2519b9048063"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466150314
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 61074216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760284979, 'matching_hash': '93cc3488fa8b8da9'}}}