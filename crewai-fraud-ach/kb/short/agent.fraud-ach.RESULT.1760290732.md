```json
{
  "id": "e2376b9e9b7ff368",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290732,
  "host_pid": "9e6742732c60:1",
  "hash": "a24439b795b21d8c0118f604b6abd316d536f40da6c51bbbfb23efddbf6c016d",
  "cid": "QmV1a24439b795b21d8c0118f604b6abd316d536f40d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290732,
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
      "evaluated_at": 1760290732
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
  "sig": "f4808b8bf7be2deaab57f299dabf35ac1763ee1ade70e74fb9e7a3d820c6fead"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029518652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 12015900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': 'e772ab4f6c2a0903'}}}