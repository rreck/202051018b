```json
{
  "id": "f27eeeb7bac5d2a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289753,
  "host_pid": "9e6742732c60:1",
  "hash": "b993456a7eb7683458c99fc9ce49175d26cb7af184c6d71471c0bcc04a428600",
  "cid": "QmV1b993456a7eb7683458c99fc9ce49175d26cb7af1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289753,
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
      "evaluated_at": 1760289753
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
  "sig": "5388bdbd3f22aed58cf2e371d8e769d2d8b592253650ae2e39f388d32c3d2e44"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272056474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': 'eb54a2a49d3a706d'}}}