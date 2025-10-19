```json
{
  "id": "f29812353c22fa8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287686,
  "host_pid": "9e6742732c60:1",
  "hash": "5de7aff55453595a838443ee6c8237584c32bddfd5ef3c8d7a5a9e4e4ff592c8",
  "cid": "QmV15de7aff55453595a838443ee6c8237584c32bddf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287686,
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
      "evaluated_at": 1760287686
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
  "sig": "6d6dbc835281a8e2ef46f7ae96dac0a967d3b208b460f7570d74d87c8b41e2ae"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 121000249862639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 23733585, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': '8cd9f1a7b8ce269f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}