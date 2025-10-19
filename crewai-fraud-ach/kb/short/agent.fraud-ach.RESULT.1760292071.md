```json
{
  "id": "485a44467967fa4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292071,
  "host_pid": "9e6742732c60:1",
  "hash": "dd28f530ba5d56fab7b63e6cfaa9a194af6a757ae316ad7f70d78fad6cd58460",
  "cid": "QmV1dd28f530ba5d56fab7b63e6cfaa9a194af6a757a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292071,
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
      "evaluated_at": 1760292071
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
  "sig": "1d2efd294ea76b95848eafffe31281f0bf2945cd750f0eb4491651b502f81ff9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 39671856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}