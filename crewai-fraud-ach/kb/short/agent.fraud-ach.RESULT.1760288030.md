```json
{
  "id": "381029a48c19a583",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288030,
  "host_pid": "9e6742732c60:1",
  "hash": "4c61570bb29871acc35d7fe38d97dfd5802fa6695f7030fc1a7a7f23b6327c40",
  "cid": "QmV14c61570bb29871acc35d7fe38d97dfd5802fa669",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288030,
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
      "evaluated_at": 1760288030
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
  "sig": "36694f17e97bf9d545f2397b96daa10ce439507901a641807a873f25d193df1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279614717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 31687760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': '2481e4baa9b260b7'}}}