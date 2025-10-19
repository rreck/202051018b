```json
{
  "id": "e6864839213f8f8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294121,
  "host_pid": "9e6742732c60:1",
  "hash": "b1d09bef381ed6b189fb1e1fb246b68f81fc151f3917ec3849dc1ecedf9ab710",
  "cid": "QmV1b1d09bef381ed6b189fb1e1fb246b68f81fc151f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294121,
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
      "evaluated_at": 1760294121
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
  "sig": "ceb9721e786dd8d62f9e97bd494ad80007f34d58cac55b864af804f03302eb2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249232395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 84688352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': '83f71011b8a0f970'}}}