```json
{
  "id": "bba630a0b2a849c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288700,
  "host_pid": "9e6742732c60:1",
  "hash": "c9a1423e1e1dbf1b14457717e3457b123ad6ef99d599edfab42dcad8f9b3a5ae",
  "cid": "QmV1c9a1423e1e1dbf1b14457717e3457b123ad6ef99",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288700,
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
      "evaluated_at": 1760288700
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
  "sig": "a0c53cc723ac90d401a42d5154a4d71d9b620239258fcc3006c7d103d5548639"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 20609656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}