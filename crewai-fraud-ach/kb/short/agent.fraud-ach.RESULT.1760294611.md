```json
{
  "id": "f94e4484fe000319",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294611,
  "host_pid": "9e6742732c60:1",
  "hash": "99652f55f35f236ec8ef3bf753b5bb0ff77fddc85147cf579d29f66fee1b7b32",
  "cid": "QmV199652f55f35f236ec8ef3bf753b5bb0ff77fddc8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294611,
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
      "evaluated_at": 1760294611
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
  "sig": "371e7fa02695ab0ca4b4773480f74d1ba711ffce714ba4bc028c1679276fc03c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465603072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 14578813, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'e359f7b1cd5a9343'}}}