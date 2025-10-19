```json
{
  "id": "230b23cef2a238df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292331,
  "host_pid": "9e6742732c60:1",
  "hash": "d7d4c468ad576f38151acf638fc272f4c3555a3cbcb9bac17b9e1fabf3580975",
  "cid": "QmV1d7d4c468ad576f38151acf638fc272f4c3555a3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292331,
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
      "evaluated_at": 1760292331
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
  "sig": "57fbb09fc5d49ae575a658773c6e3669caac4d058e0bea34d46cf67e104f11c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270009801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 94361085, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '0a6cdd943232be17'}}}}