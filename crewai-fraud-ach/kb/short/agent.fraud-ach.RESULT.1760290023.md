```json
{
  "id": "1cc8b8f8c3ab8e5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290023,
  "host_pid": "9e6742732c60:1",
  "hash": "dc279a18b4e57bf387b41d96609e4f64addace8c631637c1aacf79b08cd9c8e9",
  "cid": "QmV1dc279a18b4e57bf387b41d96609e4f64addace8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290023,
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
      "evaluated_at": 1760290023
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
  "sig": "77b8d974bce37cacb0c6e7e619082932ee94fccfa7e7535ddb3d54b99a95f4be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 45628974, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}