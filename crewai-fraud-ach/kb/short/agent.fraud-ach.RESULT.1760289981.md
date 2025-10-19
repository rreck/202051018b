```json
{
  "id": "8df4de9ec8410c14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289981,
  "host_pid": "9e6742732c60:1",
  "hash": "249562bc09c46ad6d9c868d4e1f802441df13a8ca42281d42f289dff84d7bd31",
  "cid": "QmV1249562bc09c46ad6d9c868d4e1f802441df13a8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289981,
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
      "evaluated_at": 1760289981
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
  "sig": "8926b1cc21f14e32a4d73418556551e4bcd8b1d9e61db31b3550d3b216e9a2b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 54645516, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}