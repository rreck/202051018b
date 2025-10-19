```json
{
  "id": "203be6ab01168894",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290879,
  "host_pid": "9e6742732c60:1",
  "hash": "61f5b326c81c2556b4d08622e9aae0476957bde5b4ff532a851a16ceafb9fab7",
  "cid": "QmV161f5b326c81c2556b4d08622e9aae0476957bde5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290879,
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
      "evaluated_at": 1760290879
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
  "sig": "56f9ac4b4eae9ca1467e5e6498ee011003ec701954b6505f21b687e5a5a6392d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156006729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': 'e8898c854a66ef00'}}}