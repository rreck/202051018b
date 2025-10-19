```json
{
  "id": "91b00346cd80b61c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292315,
  "host_pid": "9e6742732c60:1",
  "hash": "ee88776458d66b04053873821601db38ce7dc1a6fbb418e33d8c3bfc05f29cf2",
  "cid": "QmV1ee88776458d66b04053873821601db38ce7dc1a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292315,
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
      "evaluated_at": 1760292315
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
  "sig": "c468bc38382dabecaff8f46fb5c9fa52796a02a50f566e5bed5f01ce5662c3c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159848459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 40176240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'f6f76290fac8b474'}}}