```json
{
  "id": "49fdfa37dc5f4751",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290784,
  "host_pid": "9e6742732c60:1",
  "hash": "3a4efaf931d704ae99d7affa9e49a253644f7c64e5f52ab5a0bbbfa452d32c5f",
  "cid": "QmV13a4efaf931d704ae99d7affa9e49a253644f7c64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290784,
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
      "evaluated_at": 1760290784
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
  "sig": "324044c7c880954514a86316961e421f68e46da0a5262b68c7044a47b90bddd3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150540393
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 35885346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '5c99a38661a1ddcd'}}}