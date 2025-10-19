```json
{
  "id": "25c4c79ed87d28f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286756,
  "host_pid": "9e6742732c60:1",
  "hash": "c9bbd06ace0435b6b2943694d8e4cb5febb01b12001245762fa4a1d2baebb538",
  "cid": "QmV1c9bbd06ace0435b6b2943694d8e4cb5febb01b12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286756,
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
      "evaluated_at": 1760286756
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
  "sig": "5a36fa04c79976fcb6db530fd8aa2505d8caa2d43774e09480f5af9ebf2c172d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100271259155
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14241564, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '525a45536127a4d2'}}}