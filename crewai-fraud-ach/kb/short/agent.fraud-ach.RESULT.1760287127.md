```json
{
  "id": "527151433395ec03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287127,
  "host_pid": "9e6742732c60:1",
  "hash": "1159e7d0df367e74514b43c57791fb2c203c7073251df35f318cb9943445c15a",
  "cid": "QmV11159e7d0df367e74514b43c57791fb2c203c7073",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287127,
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
      "evaluated_at": 1760287127
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
  "sig": "ee5ff00bbe3277ccef48e6d71e0662dbef0c457e7e5949ee765b18b6fddc350b"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 021000022964635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 49000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '99d3229e22856917'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}