```json
{
  "id": "81eeb1783ac6e689",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288309,
  "host_pid": "9e6742732c60:1",
  "hash": "3444c8eb4bd7e8a2b220612ff5f0c697f758dea41198e4d82b972d59b68b76ab",
  "cid": "QmV13444c8eb4bd7e8a2b220612ff5f0c697f758dea4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288309,
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
      "evaluated_at": 1760288309
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
  "sig": "e4b3270a8a2f6bcdac19e5483deaed47da53e5704215bc6b46422282630e3a43"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036177444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 15750241, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285764, 'matching_hash': '11850a408d1201a4'}}}