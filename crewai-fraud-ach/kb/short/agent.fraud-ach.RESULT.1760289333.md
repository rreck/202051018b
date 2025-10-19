```json
{
  "id": "69d559b24ad31d31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289333,
  "host_pid": "9e6742732c60:1",
  "hash": "6a0bc56f94647a85a3daa3868b566d29d837903e319d56a64c4537adccf1840d",
  "cid": "QmV16a0bc56f94647a85a3daa3868b566d29d837903e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289333,
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
      "evaluated_at": 1760289333
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
  "sig": "a2f67a7e376f84d04579242e25df8757b6598ee7511648dc79aaf9578f680dd1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027064013
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 35716080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': '811cb7a859f68158'}}}