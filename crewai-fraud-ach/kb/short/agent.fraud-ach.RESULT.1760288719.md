```json
{
  "id": "2162baed85da1c2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288719,
  "host_pid": "9e6742732c60:1",
  "hash": "0a4632014c49ae15614439b538e56a5e3f27b4675ecb442cd95c91a0bab2f9cd",
  "cid": "QmV10a4632014c49ae15614439b538e56a5e3f27b467",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288719,
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
      "evaluated_at": 1760288719
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
  "sig": "dce704319c22a6154f2855c5304f6dd7174be862b6509cb37728c3aca482c283"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 349235110674099
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 16990344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': '882aaca4d63a604c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}