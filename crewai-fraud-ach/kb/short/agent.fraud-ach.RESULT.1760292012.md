```json
{
  "id": "4a77f22733207364",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292012,
  "host_pid": "9e6742732c60:1",
  "hash": "6f947929ab5ec29fe082a7723edbcb6993cfafafb6f764d903113b1f68b2b3d4",
  "cid": "QmV16f947929ab5ec29fe082a7723edbcb6993cfafaf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292012,
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
      "evaluated_at": 1760292012
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
  "sig": "20c108e81cf560bf89043a908769e817bfb9aa9d052fe0260a4b81e1e0e24145"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 264, 'threshold': 50, 'total_amount': 49731000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 263, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}