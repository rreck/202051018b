```json
{
  "id": "2babe8fa0883ee90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293243,
  "host_pid": "9e6742732c60:1",
  "hash": "1430129887195e359db8a0c3e1cfaf6e57303f3441eef06b08a7579330253e3e",
  "cid": "QmV11430129887195e359db8a0c3e1cfaf6e57303f34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293243,
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
      "evaluated_at": 1760293243
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
  "sig": "1a8c15ad89f50087526c4be2e0cff4b5d6e53d666cc4c7cb9bc517d50c270048"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 67113396, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}