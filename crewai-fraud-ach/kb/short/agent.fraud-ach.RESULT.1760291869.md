```json
{
  "id": "5f276fee975e6f70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291869,
  "host_pid": "9e6742732c60:1",
  "hash": "5b283483f6ab531fe3374bf5bad51cbe7f819796817429f5fa6c35620e2e6d05",
  "cid": "QmV15b283483f6ab531fe3374bf5bad51cbe7f819796",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291869,
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
      "evaluated_at": 1760291869
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
  "sig": "b8f7b1f01baba7d2c431a4f5738d67b4b161a9b2e621b7862ac82099f6452436"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158076407
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 27480825, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'bd01239b3993ff64'}}}