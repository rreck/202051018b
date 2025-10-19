```json
{
  "id": "02033745997c605a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292792,
  "host_pid": "9e6742732c60:1",
  "hash": "b7beeae51c2387f59fddcec88a0c9756fcb023b25172814da62a857e98a1aab0",
  "cid": "QmV1b7beeae51c2387f59fddcec88a0c9756fcb023b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292792,
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
      "evaluated_at": 1760292792
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
  "sig": "1c1285aed2652f2dfbb20b1035dd5fa9e8c1a23d837579db5b5ce374fcdb2464"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248764263
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 74455590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}