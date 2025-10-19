```json
{
  "id": "43578285927faf8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287814,
  "host_pid": "9e6742732c60:1",
  "hash": "ceaf438f1714c2a96c148603f44fa78fb3de836a0bde28c1d4d7c51aeb7d5407",
  "cid": "QmV1ceaf438f1714c2a96c148603f44fa78fb3de836a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287814,
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
      "evaluated_at": 1760287814
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
  "sig": "831276fdfdb3382cac45b179a663ba9768271b9f2a503e76009972d63322f61a"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 021000023360084
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 13058532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': 'bfec758d4b349e38'}}}