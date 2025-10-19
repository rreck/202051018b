```json
{
  "id": "3c1d272dc8831f99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289192,
  "host_pid": "9e6742732c60:1",
  "hash": "0ae8fe7ac56b2ab55e6192b0f06335f034d978107b40fd778ca2e9d73a809e9d",
  "cid": "QmV10ae8fe7ac56b2ab55e6192b0f06335f034d97810",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289192,
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
      "evaluated_at": 1760289192
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
  "sig": "4a32522afa4ad66feab49e13b4f90f1da22ca7d8115d3508fefb795aab4e1cff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277826130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285764, 'matching_hash': '6123129413abd06e'}}}een': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}