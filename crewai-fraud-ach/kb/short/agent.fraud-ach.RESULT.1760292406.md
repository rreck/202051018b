```json
{
  "id": "ba39d537a12a6689",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292406,
  "host_pid": "9e6742732c60:1",
  "hash": "8d5e4a63c02ca01be68d98fc0ae61c726e9e955cf16541a7ef06e8b5f82b0d85",
  "cid": "QmV18d5e4a63c02ca01be68d98fc0ae61c726e9e955c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292406,
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
      "evaluated_at": 1760292406
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
  "sig": "b57bd79f57c3e109ef72997f5d1a1028766d7fded4617407ddecb0a1cf35b5d9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 013419647478508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 49901676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': 'f6be81dddddc1883'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}