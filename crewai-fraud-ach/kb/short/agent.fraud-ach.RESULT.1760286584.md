```json
{
  "id": "4cd75f6c2a8dfee6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286584,
  "host_pid": "9e6742732c60:1",
  "hash": "47c0dfb32a0970e142083945931658d9cf7066178214a26cb23cb167f8dc079b",
  "cid": "QmV147c0dfb32a0970e142083945931658d9cf706617",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286584,
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
      "evaluated_at": 1760286584
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c18f93faa05d02a7a9d2c5a0d54a7ac007ab8aac89c4ca412342d5060e2cb9cd"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105158176118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11797350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': '15ef7d28467628fb'}}}