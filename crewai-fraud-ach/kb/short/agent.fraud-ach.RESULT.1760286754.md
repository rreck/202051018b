```json
{
  "id": "662599e34095b725",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286754,
  "host_pid": "9e6742732c60:1",
  "hash": "b7e4e5ae7ad1382bc2120900ffd9395a270ef0babb12b0f5c2dc1dbfd5487879",
  "cid": "QmV1b7e4e5ae7ad1382bc2120900ffd9395a270ef0ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286754,
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
      "evaluated_at": 1760286754
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
  "sig": "c6639fa2e58fa33861dd7861aaf1ef57321092fa4fb0dd1ad9e729a75d4a88e2"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 111000022304560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '2db1b4b6a652c406'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}