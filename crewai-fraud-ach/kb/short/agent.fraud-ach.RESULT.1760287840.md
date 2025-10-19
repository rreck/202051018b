```json
{
  "id": "cdae5520527bab6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287840,
  "host_pid": "9e6742732c60:1",
  "hash": "2cca2a7a404f793c2d9fc087ac7b54c24b2950cb9b8e612f2df15d1f828f0676",
  "cid": "QmV12cca2a7a404f793c2d9fc087ac7b54c24b2950cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287840,
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
      "evaluated_at": 1760287840
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
  "sig": "8519ea27d2367337449cb5f7f630f0634f12718cfd1bb8c88fd79f44b25808bc"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 111000024392225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 32736268, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': 'c2833deea8e214b7'}}}