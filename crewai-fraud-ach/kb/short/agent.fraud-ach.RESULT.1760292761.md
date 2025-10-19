```json
{
  "id": "f893e0f5095c2e52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292761,
  "host_pid": "9e6742732c60:1",
  "hash": "6993bfc6b8c86abbe3960af62b461ff21c4052e1cda107162cdfae0bef5f3dcb",
  "cid": "QmV16993bfc6b8c86abbe3960af62b461ff21c4052e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292761,
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
      "evaluated_at": 1760292761
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
  "sig": "99457d6a24a7b9d1b007c8378b35b212eea9b37949466fc08311ec54bd14d86b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242007664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 29528796, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': 'b61887453511199f'}}}