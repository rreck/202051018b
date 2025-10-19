```json
{
  "id": "1aef929d9412a165",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287448,
  "host_pid": "9e6742732c60:1",
  "hash": "8dd119e659cbc85bedbafe9a4340504a3d90798c4e037b4b4b577165793d1575",
  "cid": "QmV18dd119e659cbc85bedbafe9a4340504a3d90798c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287448,
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
      "evaluated_at": 1760287448
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
  "sig": "46e431739e80dfaf8650726aaf1a935d4fc931d8ef28c3381dba586dd2df82aa"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 19094880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}