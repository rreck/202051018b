```json
{
  "id": "18e8d97697f1732d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289371,
  "host_pid": "9e6742732c60:1",
  "hash": "fe02ca41abbee4a9ad0d1067b6a3ab037b643a7e42d97083d705040117a01d6a",
  "cid": "QmV1fe02ca41abbee4a9ad0d1067b6a3ab037b643a7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289371,
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
      "evaluated_at": 1760289371
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
  "sig": "204b068ba96039b85b01716e3cd22e374b23be173477f8c039a0405cda9b95d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156760115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 38813412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}