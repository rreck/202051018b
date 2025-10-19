```json
{
  "id": "37553f264aec0556",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294402,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce36ca523b4e756bd4b13aabea5d39c0627d9cf0b842b3588a7847422e208f7",
  "cid": "QmV18ce36ca523b4e756bd4b13aabea5d39c0627d9cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294402,
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
      "evaluated_at": 1760294402
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
  "sig": "65e61d4346d377646c84eb1852a86046be5cd278e7f1292f90a99c41e2e9b52d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035599822
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 36561279, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'a98e7fc79b0958d1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}