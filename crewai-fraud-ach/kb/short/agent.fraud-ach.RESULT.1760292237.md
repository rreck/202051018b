```json
{
  "id": "be86f0a68b5176ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292237,
  "host_pid": "9e6742732c60:1",
  "hash": "750b2e49eb197dc8378174c323ceb1ce3857ca0fcf3b71298e770cbbdeefad99",
  "cid": "QmV1750b2e49eb197dc8378174c323ceb1ce3857ca0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292237,
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
      "evaluated_at": 1760292237
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
  "sig": "00e5d1e9e3d27fa25c3c7370456ee1709134f898780c75733a6474902ace73af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465280061
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 25668614, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '24e243e35a5cb5f6'}}}