```json
{
  "id": "3e2374e25142520e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290810,
  "host_pid": "9e6742732c60:1",
  "hash": "15b00ed9f358f984ca50c45029a1a0c5cc3e4205e135a8d63c79ddef7ce5cfb2",
  "cid": "QmV115b00ed9f358f984ca50c45029a1a0c5cc3e4205",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290810,
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
      "evaluated_at": 1760290810
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
  "sig": "d494ef5c1505077f3da7fd3bc41a10083f597475c9c6be2da51c8984cf4f9b77"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271879965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 33935840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}