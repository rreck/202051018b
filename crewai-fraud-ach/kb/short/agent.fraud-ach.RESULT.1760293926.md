```json
{
  "id": "69f1854f860bb0b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293926,
  "host_pid": "9e6742732c60:1",
  "hash": "8e18b995001aa787943ab3ca8fcd593052902f3e7136d6c9ad502a41272ab576",
  "cid": "QmV18e18b995001aa787943ab3ca8fcd593052902f3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293926,
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
      "evaluated_at": 1760293926
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
  "sig": "d8c0cc9203272fe84eb988513c113e26b16094f75e8996e36ba5f35080892d0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464346208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 22800000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'be0548ed0e4f6107'}}}}