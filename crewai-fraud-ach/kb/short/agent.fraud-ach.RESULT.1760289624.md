```json
{
  "id": "73b8fd4afb2db209",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289624,
  "host_pid": "9e6742732c60:1",
  "hash": "f7bb571aaed7a988c4262ade8aec639b3ce8e57d5bf49b44543f09049faefff2",
  "cid": "QmV1f7bb571aaed7a988c4262ade8aec639b3ce8e57d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289624,
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
      "evaluated_at": 1760289624
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
  "sig": "9dc7619ede98b79afd69b6f8833dfc8f8c300aa063d47708fd2e17199560fb5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 40006528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}