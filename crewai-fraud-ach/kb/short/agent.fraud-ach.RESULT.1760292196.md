```json
{
  "id": "f4d088fcdfc1c978",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292196,
  "host_pid": "9e6742732c60:1",
  "hash": "7d8c84614e9f53572751528cc5932e9190826f76b62a4937d03d512658eefceb",
  "cid": "QmV17d8c84614e9f53572751528cc5932e9190826f76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292196,
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
      "evaluated_at": 1760292196
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
  "sig": "9f7dc5d7151d352638a7dd8e55f87f130f7b8e9529986686f8d6e95f1e676693"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021328085
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 268, 'threshold': 50, 'total_amount': 18514244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 267, 'first_seen': 1760284979, 'matching_hash': 'f7c67db4baca4bf3'}}}