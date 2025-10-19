```json
{
  "id": "d14c497ddc92c9be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286549,
  "host_pid": "9e6742732c60:1",
  "hash": "32149d0bbb438b8e2110bae68d848d82a274c86cce47c07c29c53dcf9760e9e5",
  "cid": "QmV132149d0bbb438b8e2110bae68d848d82a274c86c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286549,
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
      "evaluated_at": 1760286549
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
  "sig": "13acea43c6cb8e16a4248fcd4026adb938f2b40b1f5d4b32fd2237ed6cab3349"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 372851334846795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14265622, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': 'e24b6b5408d67f01'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}