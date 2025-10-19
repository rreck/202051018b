```json
{
  "id": "3ed37f7cfbc863cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293464,
  "host_pid": "9e6742732c60:1",
  "hash": "6012a3d598d4efb3f701ced7fcf873767afa58c5c9ff8eb7e992812741f52e96",
  "cid": "QmV16012a3d598d4efb3f701ced7fcf873767afa58c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293464,
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
      "evaluated_at": 1760293464
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
  "sig": "ac2a22b8ea53034a29596c9e32ed72c9acfc60552c9e133eee8f5d50083fd846"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248255202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 88285689, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': 'c66fc0c5e7caab92'}}}}