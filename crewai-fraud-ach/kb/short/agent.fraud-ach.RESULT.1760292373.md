```json
{
  "id": "c69ca4630bcbbe1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292373,
  "host_pid": "9e6742732c60:1",
  "hash": "c4efb0aba9e98812c149cb5b3a88248fda30d01a9f2edd9a4c28d8c6adb0dbf7",
  "cid": "QmV1c4efb0aba9e98812c149cb5b3a88248fda30d01a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292373,
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
      "evaluated_at": 1760292373
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
  "sig": "7b171108f45f9d910dd46cd7791aad15e7071455eda10ef9f37b33199f90fe37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248509249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 32252976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285764, 'matching_hash': '3102d5e76c589166'}}}