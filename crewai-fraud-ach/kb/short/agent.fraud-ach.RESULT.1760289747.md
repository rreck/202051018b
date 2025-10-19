```json
{
  "id": "43984a97f51f26ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289747,
  "host_pid": "9e6742732c60:1",
  "hash": "9b2fbe97e251324654a9c22da8265d1fb3b6f5bb4962760cccbbc98a73780854",
  "cid": "QmV19b2fbe97e251324654a9c22da8265d1fb3b6f5bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289747,
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
      "evaluated_at": 1760289747
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
  "sig": "e3c111fefc37de7e580f5dd578a76d7841db681ff6a97c88effd3d178fa333eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 21687600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}