```json
{
  "id": "ffd1ef4112300a82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288248,
  "host_pid": "9e6742732c60:1",
  "hash": "bc199ac5c4d0032b56a10fbf2b05b057f3ac4ade9441691c3110b7a49a77576d",
  "cid": "QmV1bc199ac5c4d0032b56a10fbf2b05b057f3ac4ade",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288248,
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
      "evaluated_at": 1760288248
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
  "sig": "0d2290d4050a6eecf6ecdc94130bae4e3ef4e151e2f88d50d118215f7d9a5bb5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 26196570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}