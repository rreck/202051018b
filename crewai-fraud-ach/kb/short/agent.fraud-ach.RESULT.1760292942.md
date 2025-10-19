```json
{
  "id": "d3cfc67983757afe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292942,
  "host_pid": "9e6742732c60:1",
  "hash": "993cb01e9c88fccd4c0c5df7cea4eb9be6715e4c035dfb0340f2a85cc41b4b06",
  "cid": "QmV1993cb01e9c88fccd4c0c5df7cea4eb9be6715e4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292942,
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
      "evaluated_at": 1760292942
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
  "sig": "084ac3a538c0de6bbcef57d979cd1a2257ad2c5383dffad871ba059e6ae1ce2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154887163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 284, 'threshold': 50, 'total_amount': 99910916, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 283, 'first_seen': 1760284979, 'matching_hash': '445784114b53d57b'}}}