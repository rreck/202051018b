```json
{
  "id": "a5977b6bb161a4b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289308,
  "host_pid": "9e6742732c60:1",
  "hash": "9a210980132a75d94554ac55046dddb7ec07baaaeeb4ea9ddd8a93ab510693e6",
  "cid": "QmV19a210980132a75d94554ac55046dddb7ec07baaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289308,
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
      "evaluated_at": 1760289308
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
  "sig": "03270481fc7c086027bcade847bd357223d1464c7f13ec676f538f792ba9ce8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462765128
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 35889567, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': 'e332841741f2145e'}}}