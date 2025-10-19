```json
{
  "id": "a3dcacc445a0dcd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294351,
  "host_pid": "9e6742732c60:1",
  "hash": "7e769f0ed4d8a781d3e828177ff08d7b61a8181ab7d16950eaab2c8bd22a2f79",
  "cid": "QmV17e769f0ed4d8a781d3e828177ff08d7b61a8181a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294351,
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
      "evaluated_at": 1760294351
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
  "sig": "1bc298424aff58a8fa939f20704d4956bfe6d7b751fdde462877ed35b2ed6811"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027745016
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 112784636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '88a158c93e7cc45f'}}}