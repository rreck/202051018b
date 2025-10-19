```json
{
  "id": "fb983dc92fb39cdb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294606,
  "host_pid": "9e6742732c60:1",
  "hash": "559a54db172c0c01650f4a6655729a7392e044745f1d40f4d1de083387d13e51",
  "cid": "QmV1559a54db172c0c01650f4a6655729a7392e04474",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294606,
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
      "evaluated_at": 1760294606
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
  "sig": "83505379928a17efb2386b41cd1f3d46b344e1faf06d71b4e64471565dd1a71d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247259111
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 95000031, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': '0fd27855d157b4f6'}}}