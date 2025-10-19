```json
{
  "id": "735d767ec67d98e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288060,
  "host_pid": "9e6742732c60:1",
  "hash": "b75e5512e3356e1b293179ca0af225993194266c629febc02639793da2602bd3",
  "cid": "QmV1b75e5512e3356e1b293179ca0af225993194266c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288060,
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
      "evaluated_at": 1760288060
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
  "sig": "1ab963870da3ea2ff9574e194cd090a05eec4833f15612f73c5085b5143a2572"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025832040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 36319023, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285764, 'matching_hash': '02af8ad93f509b45'}}}