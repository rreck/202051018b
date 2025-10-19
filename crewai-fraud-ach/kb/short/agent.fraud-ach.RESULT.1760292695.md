```json
{
  "id": "71d937c4c91fa5cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292695,
  "host_pid": "9e6742732c60:1",
  "hash": "8a4a511faec138b6b9e23d46a19e8e3158ccd1017c32efb1be7c7a8a7b64ceeb",
  "cid": "QmV18a4a511faec138b6b9e23d46a19e8e3158ccd101",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292695,
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
      "evaluated_at": 1760292695
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
  "sig": "0cc76a662bda342b0f055c992b4a8e208bae49450a7d2e3c995ec2fe14f27882"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035326391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 75860694, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '7c05ec5f373172f0'}}}