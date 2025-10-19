```json
{
  "id": "8a58c8f3e6b7a98c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292666,
  "host_pid": "9e6742732c60:1",
  "hash": "49d1b3daa49f705ffc81cbbbf9d3c99126789474855647361beba991113fa409",
  "cid": "QmV149d1b3daa49f705ffc81cbbbf9d3c99126789474",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292666,
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
      "evaluated_at": 1760292666
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
  "sig": "be784252204f10c0b891a11ad993418d90d1f3d6e6e9cc80a6608f567705ffc3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242007664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 29239298, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': 'b61887453511199f'}}}