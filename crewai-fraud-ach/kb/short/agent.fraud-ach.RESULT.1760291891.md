```json
{
  "id": "28746227babe1b5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291891,
  "host_pid": "9e6742732c60:1",
  "hash": "e11ac54631f89ab63b5903370fd3395df9bff0987ef9079de989851ba8daec2c",
  "cid": "QmV1e11ac54631f89ab63b5903370fd3395df9bff098",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291891,
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
      "evaluated_at": 1760291891
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "32a8dabd13a5b23a89a40a2c4c35e7d4f73415d0670e6ed94940a41fc0433cf7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 22941480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}