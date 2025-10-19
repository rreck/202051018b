```json
{
  "id": "9b88dff615d67b7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293816,
  "host_pid": "9e6742732c60:1",
  "hash": "7050db2c67c9dc2d843071c78fcd678adae809e802a118561a523e4bd982eb5c",
  "cid": "QmV17050db2c67c9dc2d843071c78fcd678adae809e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293816,
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
      "evaluated_at": 1760293816
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
  "sig": "883fb274c584215f4846f82acd2ee0ce51ffc4b78f5487a2f73efb9db9b2f0b3"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 886156735269080
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 43347026, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': 'bf20bb751245cb05'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}