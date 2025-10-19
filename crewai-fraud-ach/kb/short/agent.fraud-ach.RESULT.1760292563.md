```json
{
  "id": "a2687385159284aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292563,
  "host_pid": "9e6742732c60:1",
  "hash": "6147b5b06a08d72ba5ace1e40bae7409746fe31a379427a126bbfd91cf9bbb65",
  "cid": "QmV16147b5b06a08d72ba5ace1e40bae7409746fe31a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292563,
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
      "evaluated_at": 1760292563
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
  "sig": "9a602a6e65612f87e530a59d59c0f09ef8ca2d664dce6b5f3ad3b5830c61c889"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026451752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 276, 'threshold': 50, 'total_amount': 68084784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 275, 'first_seen': 1760284979, 'matching_hash': 'ed66d17e763eb837'}}}