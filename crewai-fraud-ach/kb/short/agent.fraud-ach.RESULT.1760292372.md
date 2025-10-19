```json
{
  "id": "009e25422b58d16e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292372,
  "host_pid": "9e6742732c60:1",
  "hash": "e54305fc0f3a24c6ac492f57985bf8476fdf3857738ac249ba68949ce3c1c3dc",
  "cid": "QmV1e54305fc0f3a24c6ac492f57985bf8476fdf3857",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292372,
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
      "evaluated_at": 1760292372
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
  "sig": "f889a3ce45c1b4688fdd325eb806f384916f4b3c02da193eb7236f170c272493"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467394934
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 66510836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '227a4380e23ca7de'}}}