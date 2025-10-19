```json
{
  "id": "c07f3214cc3bf539",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287870,
  "host_pid": "9e6742732c60:1",
  "hash": "601027fb24ef9fb90237f9548f89750c4a29478e0dd11eedaa37e8725fadfa59",
  "cid": "QmV1601027fb24ef9fb90237f9548f89750c4a29478e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287870,
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
      "evaluated_at": 1760287870
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
  "sig": "b4311b648a04da611b0ad0d0779de7711219058279d340ca6eccb1c539a0c4f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 20132925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}