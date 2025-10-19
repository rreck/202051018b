```json
{
  "id": "43f6c421c0112908",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287186,
  "host_pid": "9e6742732c60:1",
  "hash": "1164c5b945189905a533bf49d9b2a1e286311ea76cce591e62eafdef54d36770",
  "cid": "QmV11164c5b945189905a533bf49d9b2a1e286311ea7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287186,
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
      "evaluated_at": 1760287186
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "543f340f2a48cfc38b03b459750085b4a70069ade396a8cd98dde3f2a491d5c5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009597735648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 12844503, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': '529f1dc61ac58982'}}}