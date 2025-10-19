```json
{
  "id": "d9062067d1b54620",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288986,
  "host_pid": "9e6742732c60:1",
  "hash": "816d950796d6293a7fb620b567eaa9d78995c4d749de79683de33eb76cab79ac",
  "cid": "QmV1816d950796d6293a7fb620b567eaa9d78995c4d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288986,
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
      "evaluated_at": 1760288986
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
  "sig": "3929ac1345f4cb73686cd66a94deaacc00f78565971601c82c12096a2bcec39a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464396323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 11292820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': 'e47699aa17e8c37e'}}}