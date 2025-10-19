```json
{
  "id": "ad7fdb6e73bb9ff7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293336,
  "host_pid": "9e6742732c60:1",
  "hash": "163099a9993bb6c962d65cca965aa8b128b11caf36d2a2dba8c441fd4875d985",
  "cid": "QmV1163099a9993bb6c962d65cca965aa8b128b11caf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293336,
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
      "evaluated_at": 1760293336
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
  "sig": "cf9840e18914cf4b45c64945812fdffbc768045e4705b2edeeeb0cf71a5a703a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022785658
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 86901768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': 'fafce013233f49bd'}}}