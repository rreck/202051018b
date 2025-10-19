```json
{
  "id": "a3cb2c2fe637e47a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293862,
  "host_pid": "9e6742732c60:1",
  "hash": "61292e0ca85bf6f82507e157b61d4988750f1af8e43359d747e876ca4e883489",
  "cid": "QmV161292e0ca85bf6f82507e157b61d4988750f1af8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293862,
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
      "evaluated_at": 1760293862
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
  "sig": "1695fa0fe57ddcf21d1e2d668f4876b464adf3e892387a78eb0d8323c79aaa3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462755939
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 19879979, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': '0ef039381f9434ef'}}}