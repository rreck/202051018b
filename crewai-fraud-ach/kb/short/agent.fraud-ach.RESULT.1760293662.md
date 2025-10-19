```json
{
  "id": "a790f3845b25bdb3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293662,
  "host_pid": "9e6742732c60:1",
  "hash": "7d9049bc6923fde99a081e5dd68d654a04d5b65d56104167a8d8aaf05307ebec",
  "cid": "QmV17d9049bc6923fde99a081e5dd68d654a04d5b65d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293662,
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
      "evaluated_at": 1760293662
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
  "sig": "568e29ec615ab91db7220bf9a36862bd1c14f3fdeb0d0fcb6d14ea89ec50a459"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023914154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 106667144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': '45ff85674ff7fdbe'}}}