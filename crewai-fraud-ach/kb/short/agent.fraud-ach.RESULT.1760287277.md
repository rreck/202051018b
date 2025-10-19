```json
{
  "id": "069820c881dfa910",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287277,
  "host_pid": "9e6742732c60:1",
  "hash": "0a00e0f0ca2dcd23917bee8a9d1827bbc4cd942a174075390dc370e45abaae8f",
  "cid": "QmV10a00e0f0ca2dcd23917bee8a9d1827bbc4cd942a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287277,
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
      "evaluated_at": 1760287277
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "b708c3a5a23f940560260422b50367d213e66d6625dcfb0ee73069856860383c"
}
```

Fraud detected: duplicate_transaction (score: 71)
Transaction: 031201466702370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 58, 'details': {'transaction_count': 54, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}