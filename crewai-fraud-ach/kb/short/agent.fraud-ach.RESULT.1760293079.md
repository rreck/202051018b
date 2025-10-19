```json
{
  "id": "205da0068ef2e087",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293079,
  "host_pid": "9e6742732c60:1",
  "hash": "f059d80250f62941028fd64946409300e05cbaea038a3bb50c3c155a953d195e",
  "cid": "QmV1f059d80250f62941028fd64946409300e05cbaea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293079,
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
      "evaluated_at": 1760293079
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
  "sig": "56d9b230dddd475cd775faa0f03c4f0d20a883c396f157df00af5b79b46bf401"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246379487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 100983967, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': 'aafc2265b0403e69'}}}