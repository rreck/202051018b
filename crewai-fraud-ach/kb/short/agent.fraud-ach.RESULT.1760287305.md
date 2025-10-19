```json
{
  "id": "9f8016dff49286e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287305,
  "host_pid": "9e6742732c60:1",
  "hash": "4704564bd7f980992fd63347802fa30443893f6093a727f64b77015fcd5b7cc2",
  "cid": "QmV14704564bd7f980992fd63347802fa30443893f60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287305,
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
      "evaluated_at": 1760287305
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
  "sig": "97b739a68f0d4a6d236d6598e808293c7790bfdf52fbdc8e184bcc254380fec5"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 044000038480332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '8289eea4583ef54f'}}}