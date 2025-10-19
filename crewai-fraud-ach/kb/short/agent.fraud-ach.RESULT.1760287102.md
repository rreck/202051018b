```json
{
  "id": "5fb6e75266461bbc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287102,
  "host_pid": "9e6742732c60:1",
  "hash": "bbb82b886caa18bdb0b71e7fffca8c508b91a4f4651694dc332b624d00dc6dd1",
  "cid": "QmV1bbb82b886caa18bdb0b71e7fffca8c508b91a4f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287102,
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
      "evaluated_at": 1760287102
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
  "sig": "fcd4f0281c6b7641c1bc6afc8a632bb4ee124cacb3c304917a7f022d1439724b"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 031201462455734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 24000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}