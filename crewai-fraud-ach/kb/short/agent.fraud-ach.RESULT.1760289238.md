```json
{
  "id": "4b0a830cfb4e7972",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289238,
  "host_pid": "9e6742732c60:1",
  "hash": "95fa3db1db10379a08ebc17e88cd99182b3d595da4dcc1ef5f2d0858174a1c99",
  "cid": "QmV195fa3db1db10379a08ebc17e88cd99182b3d595d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289238,
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
      "evaluated_at": 1760289238
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
  "sig": "04005d4af05da400d361a6dca2616831f72561653daffd5a23d3999db6552e94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592096226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 57753774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}