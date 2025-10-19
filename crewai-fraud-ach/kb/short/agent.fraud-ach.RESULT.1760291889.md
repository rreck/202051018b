```json
{
  "id": "915a0b5d7bd9586d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291889,
  "host_pid": "9e6742732c60:1",
  "hash": "9928c6e5064d02aa7ec66a2b9bbc96aa35062d7ef8befa5882f4bb724d37b2f0",
  "cid": "QmV19928c6e5064d02aa7ec66a2b9bbc96aa35062d7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291889,
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
      "evaluated_at": 1760291889
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
  "sig": "85752d428f9c8c72d52e954b9dbfc2c8669333fe7e2bbced8b8d4ba140ebd985"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029441717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 39371330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}