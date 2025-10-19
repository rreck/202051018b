```json
{
  "id": "31261d21f5727749",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291504,
  "host_pid": "9e6742732c60:1",
  "hash": "cf1754ad898f85b9253cb9aa3d6c7ea2af41f79e137a1f58a346718e8d83a9a4",
  "cid": "QmV1cf1754ad898f85b9253cb9aa3d6c7ea2af41f79e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291504,
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
      "evaluated_at": 1760291504
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
  "sig": "230ab468317b155ce060a1a8c643fa8912c1729b0cc77e33a726a909e21bfacf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 36943104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}