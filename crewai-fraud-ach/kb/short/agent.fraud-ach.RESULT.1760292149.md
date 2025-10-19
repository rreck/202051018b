```json
{
  "id": "0a731f375d65369c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292149,
  "host_pid": "9e6742732c60:1",
  "hash": "431ed912894d32c7223827dfa0fa011d0211443ccbba17d1ad83ba55105c0e07",
  "cid": "QmV1431ed912894d32c7223827dfa0fa011d0211443c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292149,
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
      "evaluated_at": 1760292149
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
  "sig": "5e1192e5278236de1b5b777385ea02e0169bfa6f5e7036360d20834844eb47f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154102308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 267, 'threshold': 50, 'total_amount': 98370009, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 266, 'first_seen': 1760284979, 'matching_hash': '687d8a253912c530'}}}