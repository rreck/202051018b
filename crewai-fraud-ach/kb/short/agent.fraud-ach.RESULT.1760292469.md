```json
{
  "id": "ea02255c45b24d59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292469,
  "host_pid": "9e6742732c60:1",
  "hash": "d704ac969f9f17581fd6a445ac6c7a1a2ff42579e2dc63ec2ef700905df39883",
  "cid": "QmV1d704ac969f9f17581fd6a445ac6c7a1a2ff42579",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292469,
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
      "evaluated_at": 1760292469
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
  "sig": "59c794f7a8f2b711143405487406baa11e981a0a70b3bb7a7fffba55e056a925"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467519914
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 24209460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': '8f358df1d478d699'}}}