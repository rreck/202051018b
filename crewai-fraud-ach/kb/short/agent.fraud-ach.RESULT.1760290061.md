```json
{
  "id": "c73ef98abe7143d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290061,
  "host_pid": "9e6742732c60:1",
  "hash": "d365c05c120a924972be81cd2ff00f9879441558c3ac2e88a2e0fd236a4c2dd0",
  "cid": "QmV1d365c05c120a924972be81cd2ff00f9879441558",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290061,
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
      "evaluated_at": 1760290061
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "ea9e51ea8b191f0c9d3c17a8de0e20cf10c7b5dac8c549ad7e869dc9d3a496f8"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201465841026
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 70000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': 'e2a83dab91a99cc0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}