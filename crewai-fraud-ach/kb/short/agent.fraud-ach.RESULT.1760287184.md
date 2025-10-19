```json
{
  "id": "50e2f1597411761c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287184,
  "host_pid": "9e6742732c60:1",
  "hash": "d2c96c847e11919dc338497e272bd2638fc8f05d5274017ee9da784ddd44a990",
  "cid": "QmV1d2c96c847e11919dc338497e272bd2638fc8f05d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287184,
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
      "evaluated_at": 1760287184
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
  "sig": "051145a58854c575ff96b083c69f5909c4e241894af937366e054706c92df195"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000022625380
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 18446241, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': 'f6638b44b9180b42'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5513113}}}