```json
{
  "id": "88f628c44a7160f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288209,
  "host_pid": "9e6742732c60:1",
  "hash": "58ef6fc72d7ac6c2163684be62e84fb23b7c7a48ed088c5919804693349a869b",
  "cid": "QmV158ef6fc72d7ac6c2163684be62e84fb23b7c7a48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288209,
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
      "evaluated_at": 1760288209
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
  "sig": "f0f089732c718a80e7017e56473f42a230998f0d95ee04c6bcb655cf94b3f7e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021576375
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 20386902, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '97ab95dbcdf49b98'}}}