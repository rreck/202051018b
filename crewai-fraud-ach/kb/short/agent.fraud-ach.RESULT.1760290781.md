```json
{
  "id": "8cfa3286a2f58a68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290781,
  "host_pid": "9e6742732c60:1",
  "hash": "6771d7c55c352dfd23d2c84add65f86bce1ee5d6b749c2833deb15d42fc007c4",
  "cid": "QmV16771d7c55c352dfd23d2c84add65f86bce1ee5d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290781,
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
      "evaluated_at": 1760290781
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
  "sig": "6f8bdb9d86852221599d143e42ca3c2289739d4538f7684831ac6a1f4dba035d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026876887
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 42429468, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': 'ac27634a0ee0b6ee'}}}