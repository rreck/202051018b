```json
{
  "id": "38ca4fca2a31e2e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287262,
  "host_pid": "9e6742732c60:1",
  "hash": "8037d9acadd7033159de274b643151702fdac83ca607bc63645bd211b8bd513c",
  "cid": "QmV18037d9acadd7033159de274b643151702fdac83c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287262,
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
      "evaluated_at": 1760287262
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2f0348ec404bc05358b741435af86d98c8308713b93cd32d994313f621dd4f64"
}
```

Fraud detected: duplicate_transaction (score: 71)
Transaction: 031201465006650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 58, 'details': {'transaction_count': 54, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': 'ac98f3afdd973e27'}}}60285763, 'matching_hash': '74f25dd839f89a8f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}