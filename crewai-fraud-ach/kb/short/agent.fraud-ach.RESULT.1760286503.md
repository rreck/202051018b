```json
{
  "id": "2c3cf7d9163ab68b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286503,
  "host_pid": "9e6742732c60:1",
  "hash": "a527cb76f5a23a898bf8d01b5f11b3204809bc79cc94ba2c61fcc3e4dfe57fbc",
  "cid": "QmV1a527cb76f5a23a898bf8d01b5f11b3204809bc79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286503,
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
      "evaluated_at": 1760286503
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
  "sig": "76832b55a9485e111df417ad1f64f3ecd55b1348312dc514b7e58912043f0d9d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467961793
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}