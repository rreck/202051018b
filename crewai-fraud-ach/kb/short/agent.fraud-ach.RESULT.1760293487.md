```json
{
  "id": "e807751ba57e3353",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293487,
  "host_pid": "9e6742732c60:1",
  "hash": "0e1e499c9c43e96dc023a1aa3df67ae636fc623dc97c0f1c8fbeb5d870b2ca90",
  "cid": "QmV10e1e499c9c43e96dc023a1aa3df67ae636fc623d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293487,
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
      "evaluated_at": 1760293487
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
  "sig": "5116abe6aa724a6cfe47e1456fe54c63c1142adcead59c8e7a8b02602455bbcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466702370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 29278986, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}