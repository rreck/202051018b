```json
{
  "id": "17b598fad76cd87f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290268,
  "host_pid": "9e6742732c60:1",
  "hash": "f839e075a812d767d7caf5a90fd7b68ce69b284256bb16ddfcca920246592acc",
  "cid": "QmV1f839e075a812d767d7caf5a90fd7b68ce69b2842",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290268,
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
      "evaluated_at": 1760290268
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
  "sig": "74f0d193066d17ae33976f6f9b2f73532b945a996036eb040c3f1ea534655f31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 19494942, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}