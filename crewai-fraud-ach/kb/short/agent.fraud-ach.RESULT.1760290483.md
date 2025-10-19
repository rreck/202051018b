```json
{
  "id": "49a4cfae0f4b4fce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290483,
  "host_pid": "9e6742732c60:1",
  "hash": "38c7749d6ee956c30cab43366f43f434289c9cf7d118bcbb9fe256373310c678",
  "cid": "QmV138c7749d6ee956c30cab43366f43f434289c9cf7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290483,
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
      "evaluated_at": 1760290483
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
  "sig": "6581c0a4e87fe3eedc61abd5779c2747a4c4a760d1129f91a1c008e9911e2c5c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 68357549, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}