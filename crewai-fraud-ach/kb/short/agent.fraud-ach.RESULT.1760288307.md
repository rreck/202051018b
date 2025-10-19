```json
{
  "id": "46594498950961bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288307,
  "host_pid": "9e6742732c60:1",
  "hash": "4adefa8067d4507000117de1e38c70ba3d1a8a3ffdc7975208137c314d41ae8e",
  "cid": "QmV14adefa8067d4507000117de1e38c70ba3d1a8a3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288307,
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
      "evaluated_at": 1760288307
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
  "sig": "2923059e6ceddf10d352c740634251f38facea8406eeef0a7b181de69324c0c2"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 89000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}