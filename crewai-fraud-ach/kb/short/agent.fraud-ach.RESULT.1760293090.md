```json
{
  "id": "ab2aac66ac54556e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293090,
  "host_pid": "9e6742732c60:1",
  "hash": "23c336d76dd9b5c688a744ee7311fe7cbb1465f6f455e40eb9e8afe9ca3402c8",
  "cid": "QmV123c336d76dd9b5c688a744ee7311fe7cbb1465f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293090,
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
      "evaluated_at": 1760293090
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
  "sig": "1843ad1d1dfe72d9faccff310da81463f0a359fce27e19f2a28e39b35a8f09b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 86812996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}