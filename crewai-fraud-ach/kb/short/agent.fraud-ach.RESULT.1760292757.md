```json
{
  "id": "68f6b38ad1272d2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292757,
  "host_pid": "9e6742732c60:1",
  "hash": "7c9405c4de1218d6f504edcdf18d26b2201095a1b6f52b01d07e471bd3dc04d0",
  "cid": "QmV17c9405c4de1218d6f504edcdf18d26b2201095a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292757,
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
      "evaluated_at": 1760292757
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
  "sig": "52bc71273bebd9d9a9308052a74b97d2bfdedbfc81f413ae788c347b38c9aed7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022785658
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 82073892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': 'fafce013233f49bd'}}}