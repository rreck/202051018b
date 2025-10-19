```json
{
  "id": "fff77e17d20291fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290466,
  "host_pid": "9e6742732c60:1",
  "hash": "c54ffc853e05663f4b11c4b29b4cdd59ca32239512c58db03f7c04a6d798eba6",
  "cid": "QmV1c54ffc853e05663f4b11c4b29b4cdd59ca322395",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290466,
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
      "evaluated_at": 1760290466
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
  "sig": "e3f231cd7035a96262fab05b2a7ece6aca37e934350f4ba6eda892891bf3887f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242854691
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 27916125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '6f29fe2a1ce5e88d'}}}