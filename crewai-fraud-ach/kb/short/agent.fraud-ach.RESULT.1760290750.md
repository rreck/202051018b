```json
{
  "id": "a9b5dd5f52aa066e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290750,
  "host_pid": "9e6742732c60:1",
  "hash": "5dd78044491e1eb00a6460b5e64da21b16ee28840a614425fe76eff199a33729",
  "cid": "QmV15dd78044491e1eb00a6460b5e64da21b16ee2884",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290750,
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
      "evaluated_at": 1760290750
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
  "sig": "b9bf51e42329570701dcfab7f00fa281b455d4ddb095c885275f5be706802262"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279280277
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 69792550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '5e64cdd29eaed333'}}}