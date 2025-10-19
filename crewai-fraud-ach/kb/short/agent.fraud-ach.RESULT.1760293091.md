```json
{
  "id": "10beafb93a4ddd8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293091,
  "host_pid": "9e6742732c60:1",
  "hash": "84d01e70ac095ab1355a8324e4d5e89023fa7a212d951df23d15a7ba8d3b621f",
  "cid": "QmV184d01e70ac095ab1355a8324e4d5e89023fa7a21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293091,
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
      "evaluated_at": 1760293091
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
  "sig": "58a06cbbf25cbe7e387fe595b1d21fef07f45d9871e5f330af6f8bac0e158272"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037157781
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 43239386, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': '7a7c344feaffaca5'}}}