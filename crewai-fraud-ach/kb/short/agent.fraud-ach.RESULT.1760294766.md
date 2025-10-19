```json
{
  "id": "191832959653d5e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294766,
  "host_pid": "9e6742732c60:1",
  "hash": "f8804d221669420893ecbc0a09c9fb94b06874968d4c5ad48bcaf659e15cb24f",
  "cid": "QmV1f8804d221669420893ecbc0a09c9fb94b0687496",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294766,
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
      "evaluated_at": 1760294766
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
  "sig": "f762f33fa10b960b208b320ee23f5877b856400f39cce00193abc7f0a4c9e5bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246379487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 116777668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': 'aafc2265b0403e69'}}}