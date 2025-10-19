```json
{
  "id": "3b4625baf974fa05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287052,
  "host_pid": "9e6742732c60:1",
  "hash": "9cb7e8117ae403ddf3e131e15cee7e33d91ae5f22814f116dd72e433659a5c4c",
  "cid": "QmV19cb7e8117ae403ddf3e131e15cee7e33d91ae5f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287052,
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
      "evaluated_at": 1760287052
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
  "sig": "2a59654ac173cfbb92a3f22ba1c92f5600850d0e4af66e7f7c0abccbde4b4cb1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100276932154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16933060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '117d4b1b88487dad'}}}