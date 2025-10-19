```json
{
  "id": "7431571a81ff7640",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294466,
  "host_pid": "9e6742732c60:1",
  "hash": "8f22d528b170001be145d345aa9867de1c80a747a9c7956f65aeefff8ed1af72",
  "cid": "QmV18f22d528b170001be145d345aa9867de1c80a747",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294466,
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
      "evaluated_at": 1760294466
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
  "sig": "63288951fcb62a4acf90a67a17705e28b22a5e20abc6d518c925384c01ecbffd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 102271456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}