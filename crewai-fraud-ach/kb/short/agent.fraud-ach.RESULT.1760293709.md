```json
{
  "id": "bf11274856f174d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293709,
  "host_pid": "9e6742732c60:1",
  "hash": "f709a042630e4bdd41919f06c674c9f9ed2de0a8d223e446b5232c31ba209001",
  "cid": "QmV1f709a042630e4bdd41919f06c674c9f9ed2de0a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293709,
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
      "evaluated_at": 1760293709
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
  "sig": "6661e9b3a865a9078cce8730154289c0c2a30b6fcbe70e7af3c0ead7c35a9bb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465236749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 54175968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': '3442ebeb280b968f'}}}