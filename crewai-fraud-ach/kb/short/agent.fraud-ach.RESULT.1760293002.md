```json
{
  "id": "7b502764843e6878",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293002,
  "host_pid": "9e6742732c60:1",
  "hash": "6d5c04267f6891aee1696ea888965f22dc4d3b0263fd7b03857bc5ea95d8ce6d",
  "cid": "QmV16d5c04267f6891aee1696ea888965f22dc4d3b02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293002,
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
      "evaluated_at": 1760293002
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
  "sig": "02ad9e0828b9be73107132f762f2bddb062151e2c99e93dc9995e7514ae5a38f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 35917277, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}