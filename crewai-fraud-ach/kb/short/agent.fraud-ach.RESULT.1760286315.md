```json
{
  "id": "01f7543f86f3d4e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286315,
  "host_pid": "9e6742732c60:1",
  "hash": "d7a2342785b2947c650785923916370be7239450038e29aa7a1b08cc8e9f79af",
  "cid": "QmV1d7a2342785b2947c650785923916370be7239450",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286315,
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
      "evaluated_at": 1760286315
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
  "sig": "fba5ac603ccb36194cd8599f0a704e8d0c5a5e972e0b686fc9180506b58a7532"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 121000248309566
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': '25ac79dd28618198'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}