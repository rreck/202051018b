```json
{
  "id": "ec7cb9c0d3461d68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287876,
  "host_pid": "9e6742732c60:1",
  "hash": "9e9de28ccfef5ea2829080f71843b17544d4d7227c776833ae3ecdf3c2cdbb39",
  "cid": "QmV19e9de28ccfef5ea2829080f71843b17544d4d722",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287876,
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
      "evaluated_at": 1760287876
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
  "sig": "1511f46b6de686cce61ab3fa8ea9767d68b5b886e948225a6777bbf0134a8733"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246932907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 33898200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': 'b5767c7cd6e7c742'}}}