```json
{
  "id": "fffb48a066e5774d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287238,
  "host_pid": "9e6742732c60:1",
  "hash": "c50c1a9e43f97386c610a4a03baf01bac9e21faf93c1c066c51b7d9ddeaae611",
  "cid": "QmV1c50c1a9e43f97386c610a4a03baf01bac9e21faf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287238,
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
      "evaluated_at": 1760287238
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c4a190a1ebe98d5af455c5f44a9cffbebbc0e6dcde29e1784a577d0e014e8cee"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 026009591790243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285763, 'matching_hash': '8c245acd6e70ddc0'}}}n': 1760285763, 'matching_hash': '2db1b4b6a652c406'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}