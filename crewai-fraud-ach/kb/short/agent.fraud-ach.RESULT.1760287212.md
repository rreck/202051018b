```json
{
  "id": "64ff80af5b67c1bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287212,
  "host_pid": "9e6742732c60:1",
  "hash": "5bcd8b919166cc00bf1abaa3f32b7dfcd11f06c2eee647d11a88cb3f2f72c843",
  "cid": "QmV15bcd8b919166cc00bf1abaa3f32b7dfcd11f06c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287212,
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
      "evaluated_at": 1760287212
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
  "sig": "75e7481144a3dbeebe07d715e5726b637012ba1c2fdf10ac8fd000babefb9458"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465949521
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 20275840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': '5db5b45722d53397'}}}