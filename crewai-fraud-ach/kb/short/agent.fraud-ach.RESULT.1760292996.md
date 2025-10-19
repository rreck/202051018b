```json
{
  "id": "dfc35c5ce9f831ef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292996,
  "host_pid": "9e6742732c60:1",
  "hash": "470fe87faf73a13378d7323fcfaa561c44e666aa61fb9dd387ab446fde74b0d8",
  "cid": "QmV1470fe87faf73a13378d7323fcfaa561c44e666aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292996,
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
      "evaluated_at": 1760292996
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
  "sig": "fbfa22f155700f600a81556494d6e8f4b5ee31e9a066ca0d53574a69df53e9c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 53184230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}