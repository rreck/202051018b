```json
{
  "id": "92082b90a142d3cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291977,
  "host_pid": "9e6742732c60:1",
  "hash": "90a2fac5c4f198f09265c400a56342fe2b1e04903c1dd3a6d46b00acba801ed3",
  "cid": "QmV190a2fac5c4f198f09265c400a56342fe2b1e0490",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291977,
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
      "evaluated_at": 1760291977
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
  "sig": "651187b3bc94a2f8e1ee5dbe921c1ccadb2864380c6a507f278da75ab4053476"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 82941793, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}