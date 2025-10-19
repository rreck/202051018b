```json
{
  "id": "a8752452da64bab3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293320,
  "host_pid": "9e6742732c60:1",
  "hash": "7be58753eaddaff1fc8319ac35d8666d51b727f3e09b2c8992a10c480aa3daa1",
  "cid": "QmV17be58753eaddaff1fc8319ac35d8666d51b727f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293320,
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
      "evaluated_at": 1760293320
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
  "sig": "052b717bde05655b7f9ea425fc1fc050604516a08238fd3004990f7c4bbaf638"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 691661796885470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 22216032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': 'c2d09785100b76ca'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '691661790', 'validation_error': 'Invalid routing number checksum'}}}