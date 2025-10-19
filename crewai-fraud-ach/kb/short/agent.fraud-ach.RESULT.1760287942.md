```json
{
  "id": "aa4de1e7ad6699f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287942,
  "host_pid": "9e6742732c60:1",
  "hash": "f3dad47a311c03fa87cb14123720b7a34f67b1c5a1b6cce32c946f25cd63e8bb",
  "cid": "QmV1f3dad47a311c03fa87cb14123720b7a34f67b1c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287942,
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
      "evaluated_at": 1760287942
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
  "sig": "e5ed90647436480d254bcfe53e446056f23712ffb9496c8f5d676308030938be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039834912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 26808012, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': '21095e194860d742'}}}