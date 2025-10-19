```json
{
  "id": "5e051f8d82574c8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290480,
  "host_pid": "9e6742732c60:1",
  "hash": "fd117372489ed50adac881f372bb255c69dbf0a56bbff4c438b7e445a0975937",
  "cid": "QmV1fd117372489ed50adac881f372bb255c69dbf0a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290480,
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
      "evaluated_at": 1760290480
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
  "sig": "e258eee77d2ea97c6f6b9c90339c442e48c445552a32dc0c2cff0817b4ccfe73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 28869237, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}