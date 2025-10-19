```json
{
  "id": "8e0b7faec0d757aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292067,
  "host_pid": "9e6742732c60:1",
  "hash": "e4f475dd037a7a27a2e7c3a45bcac4628a5b02dab3b9045737557aa58ca58a02",
  "cid": "QmV1e4f475dd037a7a27a2e7c3a45bcac4628a5b02da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292067,
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
      "evaluated_at": 1760292067
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
  "sig": "dd2846b7ac6b44d3eda046706362dc84f42717f67dcfab7c28929c73680efaa7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 60272289, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}