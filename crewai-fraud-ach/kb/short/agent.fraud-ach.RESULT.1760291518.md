```json
{
  "id": "e42ae455e25ef644",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291518,
  "host_pid": "9e6742732c60:1",
  "hash": "779fb39a58971bbbf3aa3d794438f35300828ea817ea8f2474f472ed5d36b992",
  "cid": "QmV1779fb39a58971bbbf3aa3d794438f35300828ea8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291518,
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
      "evaluated_at": 1760291518
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "d65fddb8f8c403e01ba5b652d4cc4d08d80f9b6d1af7afcb00cae662714e36a9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 408733730305741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 71857044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '77eebc6eb9f79eeb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}ds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018549}}}