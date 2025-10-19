```json
{
  "id": "58f5b3a491e35b39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291532,
  "host_pid": "9e6742732c60:1",
  "hash": "efa79e4a2ee134183c715a74cf98635335beed8698a13a3d692a9ecbbc580185",
  "cid": "QmV1efa79e4a2ee134183c715a74cf98635335beed86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291532,
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
      "evaluated_at": 1760291532
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
  "sig": "c351d42cf950cfd75fa14fff270098ccea1ae0e5570b1ea2a08640361275d4a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460804941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 13045608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'e3b2eb0d41697d4a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}