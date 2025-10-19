```json
{
  "id": "b037b4f15dbfadd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289656,
  "host_pid": "9e6742732c60:1",
  "hash": "eedcd1e68e6f6e7f52a1c39d98a3a61142c87a5337d7916fe78ff8406ea41486",
  "cid": "QmV1eedcd1e68e6f6e7f52a1c39d98a3a61142c87a53",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289656,
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
      "evaluated_at": 1760289656
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
  "sig": "247c1bc6f5ca426e44c6d9696e1f6ef67ba98efe2a6e0d7a32a8e2a33aa215b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029441717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 27453522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}