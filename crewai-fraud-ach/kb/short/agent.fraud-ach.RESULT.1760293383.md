```json
{
  "id": "dea40303b395df37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293383,
  "host_pid": "9e6742732c60:1",
  "hash": "271973c84575d2afe517efaf6a6266e7588f834f91cb13698a112d71ec488660",
  "cid": "QmV1271973c84575d2afe517efaf6a6266e7588f834f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293383,
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
      "evaluated_at": 1760293383
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
  "sig": "de2dcf444ff28c0edd69de51149f74b8cb797c0f9d94223ffe75e314f014efc6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460191060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 75623632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '1d882c6abf3447ef'}}}