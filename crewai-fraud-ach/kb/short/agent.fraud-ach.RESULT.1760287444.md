```json
{
  "id": "181a1b2bd2cc1abf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287444,
  "host_pid": "9e6742732c60:1",
  "hash": "c51b5bde83c652276a84efc96df30d97a6fbe7a79f5596aafe536f0797b41a3e",
  "cid": "QmV1c51b5bde83c652276a84efc96df30d97a6fbe7a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287444,
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
      "evaluated_at": 1760287444
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
  "sig": "eb40799f58a31f1fb0719fcfe152e439226e933c2eed9a0d1f2432632da39643"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 121000248309566
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 60000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': '25ac79dd28618198'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}