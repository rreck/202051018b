```json
{
  "id": "27df16330fe403c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289030,
  "host_pid": "9e6742732c60:1",
  "hash": "5bdb60c0e7340e37524270e40ae6e45981182de665253ae88f22852b783782a4",
  "cid": "QmV15bdb60c0e7340e37524270e40ae6e45981182de6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289030,
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
      "evaluated_at": 1760289030
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
  "sig": "36a39da0d4a6a1e9abaa1e8e62a932a93032fcd32139d91175b9a7733dbf2ef1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 18826821, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}