```json
{
  "id": "072512d7ffcb1e38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292359,
  "host_pid": "9e6742732c60:1",
  "hash": "3a68349a1e58125ae5c94ff69f846da9ad0c9cb97773269dae8100f54d026e30",
  "cid": "QmV13a68349a1e58125ae5c94ff69f846da9ad0c9cb9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292359,
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
      "evaluated_at": 1760292359
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
  "sig": "1c9b0cbcfb6d64d3dd1acca11264b2c9fdd58ea21612d370fa10a09a58d5aebd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 730896563459202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 70365372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'b6a475fea2d998c5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '730896563', 'validation_error': 'Invalid routing number checksum'}}}