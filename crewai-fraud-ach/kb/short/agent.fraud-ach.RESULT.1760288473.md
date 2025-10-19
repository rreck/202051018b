```json
{
  "id": "3d9adf20e3331f19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288473,
  "host_pid": "9e6742732c60:1",
  "hash": "1e4dcd2b971a1bcf1c6d9cdcfcf93ea47bbbaea3a14d52a02f6fea6557f49e49",
  "cid": "QmV11e4dcd2b971a1bcf1c6d9cdcfcf93ea47bbbaea3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288473,
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
      "evaluated_at": 1760288473
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
  "sig": "493415f7227e705f49b1cd21a9b2d6380ae29fe2bd9a93c5fde4406a9441e73e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 23381372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}