```json
{
  "id": "001a59e2a8cc9a21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291417,
  "host_pid": "9e6742732c60:1",
  "hash": "376eb3adcc5a2da55d1301b051c0fae1c8dc971f90719a8eb2ee38e914619254",
  "cid": "QmV1376eb3adcc5a2da55d1301b051c0fae1c8dc971f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291417,
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
      "evaluated_at": 1760291417
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
  "sig": "ddc2a47cde3cf114dde94ebb59f94edeff1fb3b1fcd218c09cbc52b7309e8240"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157659459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 63320514, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': 'b2c549e42e296c8f'}}}