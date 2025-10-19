```json
{
  "id": "5b4c3f9615e656a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293046,
  "host_pid": "9e6742732c60:1",
  "hash": "690aadfc522ba9db94882a626d792fc513b0e64ccbd658290de6625fb6374a5b",
  "cid": "QmV1690aadfc522ba9db94882a626d792fc513b0e64c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293046,
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
      "evaluated_at": 1760293046
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
  "sig": "1d91015e5acbee30c5c6022b7a628ce0c90b04e4589e5b3c36336f7bfd7996c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032369849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 87669960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '11b86d7f8733bf3d'}}}